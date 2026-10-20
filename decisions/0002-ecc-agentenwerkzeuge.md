# ADR-002 · KI-Agentenwerkzeuge aus ECC

Status: vorgeschlagen · 20. Oktober 2026 · Review durch `engineering` und `security` erforderlich (Richtlinienänderung, AGENTS.md Nr. 11)

## Kontext

Für die Programmierung der Anwendung sollen KI-Assistenten (Claude Code) wiederverwendbare Arbeitsabläufe für Planung, testgetriebene Umsetzung, Review, Sicherheit, Barrierefreiheit, SEO und Performance nutzen. Quelle ist [ECC](https://github.com/affaan-m/ECC), MIT-Lizenz.

ECC umfasst 71 Agents, 311 Skills, Hooks und immer geladene Regeln. Der Installer `--target claude-project` würde selbst für sieben Skills über 680 Dateien schreiben, darunter Regeln für Angular, C++ und andere fremde Stacks.

## Entscheidung (Vorschlag)

Eine kleine, technologieneutrale Auswahl wird unverändert nach `.claude/` übernommen und mit dem Repository versioniert:

| Art | Auswahl | Bezug |
| --- | --- | --- |
| Agents | `planner`, `architect`, `code-reviewer`, `tdd-guide`, `silent-failure-hunter` | GOV-02, ARCH-01, QA-01 |
| Agents | `security-reviewer` | SEC-01 bis SEC-04 |
| Agents | `a11y-architect` | A11Y-01, A11Y-02 |
| Agents | `seo-specialist` | WEB-01, SEO-01 |
| Agents | `performance-optimizer` | PERF-01, PERF-02 |
| Skills | `search-first`, `tdd-workflow`, `verification-loop`, `coding-standards` | GOV-02, QA-01 |
| Skills | `security-review` | SEC-01 bis SEC-04 |
| Skills | `accessibility` | A11Y-01, A11Y-02 |
| Skills | `seo` | WEB-01, SEO-01 |

Herkunft: ECC 2.2.3, Commit `6f1881aeafa3c48f7b603cc4be4b2e4e70daad59`. Lizenztext: `.claude/ECC-LICENSE`.

Nicht übernommen:

- **ECC-Regeln (`rules/`)**: werden immer geladen und konkurrieren mit `rules/catalog.json`, z. B. Commit-Format und feste 80-%-Testabdeckung. Maßgeblich bleibt der Regelkatalog.
- **Hooks**: führen automatisch Code aus. Nur nach eigener Sicherheitsprüfung (SEC-04).
- **Plugin `ecc@ecc`**: lädt alle 311 Skills, ist nicht an einen Commit gebunden und benötigt Netzzugriff zum Marketplace.
- **Stackspezifisches** (React, Next.js, TypeScript-Reviewer, Build-Resolver, Playwright): erst nach Entscheidung in [ADR-001](0001-technikentscheidung.md) gezielt ergänzen.
- **ADR-Skill von ECC**: schreibt nach `docs/adr/`; dieses Projekt verwendet `decisions/`.

## Konsequenzen

- ECC-Inhalte sind Arbeitshilfen, keine Projektregeln. Bei Widerspruch gelten `AGENTS.md`, Regelkatalog und Projektprofil (Geltungsrang in `AGENTS.md`).
- Ergebnisse von Agents ersetzen keine Pflichtprüfung und keinen Nachweis nach `templates/test-evidence.md`.
- Bekannte Abweichung: `tdd-workflow` verweist auf `scripts/setup-package-manager.js` aus ECC; das Skript ist nicht enthalten. Testbefehle werden aus dem gewählten Stack abgeleitet.
- Dateien werden nicht lokal angepasst. Aktualisierung: ECC-Commit prüfen, dieselbe Auswahl erneut kopieren, Diff reviewen, Commit in diesem ADR nachtragen.
- Rücknahme: `.claude/agents/`, `.claude/skills/` und `.claude/ECC-LICENSE` entfernen; keine Daten betroffen.

## Prüfung

`python3 scripts/check_repo.py` bestanden. Wirksamkeit der Agents in einer echten Implementierung ist noch nicht nachgewiesen.
