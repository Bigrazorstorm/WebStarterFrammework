#!/usr/bin/env python3
"""Dependency-free starter integrity check; not a product security/a11y test."""
import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
errors = []
def need(ok, message):
    if not ok: errors.append(message)
def read(path):
    try: return json.loads((ROOT / path).read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        errors.append(f"{path}: {exc}")
        return {}
def index(items, label):
    out = {}
    for item in items:
        key = item.get("id")
        need(isinstance(key, str) and bool(key), f"{label}: missing id")
        need(key not in out, f"{label}: duplicate id {key}")
        if key: out[key] = item
    return out

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--project-ready", action="store_true")
    p.add_argument("--release-ready", action="store_true")
    args = p.parse_args()
    rules = index(read("rules/catalog.json").get("rules", []), "rules")
    personas = index(read("personas/personas.json").get("personas", []), "personas")
    tests = index(read("tests/scenarios.json").get("scenarios", []), "tests")
    modules = index([read(str(f.relative_to(ROOT))) for f in (ROOT / "modules").glob("*.json")], "modules")
    comps = index(read("design/components.json").get("components", []), "components")
    icons = index(read("design/icons.json").get("icons", []), "icons")
    motions = index(read("design/motion.json").get("motions", []), "motions")
    tokens = read("design/tokens.json").get("tokens", {})
    site = read("project/site.json")
    gates = index(read("project/gates.json").get("gates", []), "gates")
    need(len(personas) >= 10, "At least ten personas required")
    targets = {"rule_refs":rules,"persona_refs":personas,"test_refs":tests,"component_refs":comps,"icon_refs":icons,"motion_refs":motions,"token_refs":tokens,"dependencies":modules}
    for group in (rules, personas, tests, modules, comps, icons, motions):
        for key, item in group.items():
            for field, target in targets.items():
                for ref in item.get(field, []): need(ref in target, f"{key}: unknown {field}: {ref}")
    for key, rule in rules.items():
        for field in ("level","requirement","owner_role","document","verification","rationale"):
            need(bool(rule.get(field)), f"{key}: missing {field}")
        need((ROOT / rule.get("document", "missing")).is_file(), f"{key}: document missing")
        need(rule.get("owner_role") in site.get("owners", {}), f"{key}: owner role missing")
    for key, persona in personas.items():
        for field in ("context","goal","success","test_refs"):
            need(bool(persona.get(field)), f"{key}: missing {field}")
    for key, motion in motions.items():
        for field in ("duration_token", "reduced_token"):
            need(motion.get(field) in tokens, f"{key}: missing token {field}")
    for ref in site.get("modules", []): need(ref in modules, f"site: unknown module {ref}")
    visited, active = set(), set()
    def walk(key):
        if key in active:
            errors.append(f"module dependency cycle: {key}"); return
        if key in visited or key not in modules: return
        active.add(key)
        for dep in modules[key].get("dependencies", []): walk(dep)
        active.remove(key); visited.add(key)
    for key in modules: walk(key)
    for f in ROOT.rglob("*.md"):
        text = f.read_text(encoding="utf-8")
        for link in re.findall(r"\]\(([^)]+)\)", text):
            if "://" in link or link.startswith("#") or link.startswith("mailto:"): continue
            target = link.split("#", 1)[0]
            if target: need((f.parent / target).exists(), f"{f.relative_to(ROOT)}: missing link {target}")
    for f in ROOT.rglob("*.json"): read(str(f.relative_to(ROOT)))
    if args.project_ready or args.release_ready:
        need(site.get("status") == "configured", "Set site status to configured after review")
        need(site.get("name") not in (None, "", "OFFEN"), "Set project name")
        for role, owner in site.get("owners", {}).items(): need(owner not in (None,"","OFFEN"), f"Assign owner: {role}")
        for key, value in site.get("stack", {}).items(): need(value not in (None,"","undecided"), f"Decide stack: {key}")
        need(site.get("stack", {}).get("publication_mode") in ("git-first", "overlay-sync"), "Choose git-first or overlay-sync")
        for key, persona in personas.items(): need(persona.get("status") == "reviewed", f"Adapt and review {key}")
        for key in ("G0", "G1", "G2"):
            gate = gates.get(key, {})
            need(gate.get("status") == "approved" and bool(gate.get("evidence")), f"Approve {key} with evidence")
        adr = (ROOT / "decisions/0001-technikentscheidung.md").read_text(encoding="utf-8")
        need("Status: beschlossen" in adr, "Record accepted ADR (Status: beschlossen)")
    if args.release_ready:
        compliance = read("project/compliance.json")
        for field in ("jurisdiction", "operator", "reviewed_at"):
            need(compliance.get(field) not in (None, "", "OFFEN"), f"Compliance: complete {field}")
        areas = index(compliance.get("areas", []), "compliance")
        expected_areas = {f"C{i:02}" for i in range(1, 9)}
        need(expected_areas.issubset(areas), "All eight compliance areas required")
        for key, area in areas.items():
            need(area.get("applicability") in ("applicable", "not_applicable"), f"{key}: determine applicability")
            need(bool(area.get("reason")) and bool(area.get("evidence")), f"{key}: reason and evidence required")
            need(area.get("owner") not in (None, "", "OFFEN"), f"{key}: assign owner")
            need(area.get("status") == "approved", f"{key}: approval required")
        for key in (f"G{i}" for i in range(8)):
            gate = gates.get(key, {})
            need(gate.get("status") == "approved" and bool(gate.get("evidence")) and gate.get("owner") not in (None, "", "OFFEN"), f"Release: approve {key} with owner and evidence")
    if errors:
        print("FAILED\n" + "\n".join("- " + e for e in errors)); return 1
    print(f"PASS: {len(rules)} rules, {len(personas)} personas, {len(modules)} module(s), references and local links valid.")
    print("No product, accessibility, security or deployment tests performed.")
    return 0
if __name__ == "__main__":
    raise SystemExit(main())
