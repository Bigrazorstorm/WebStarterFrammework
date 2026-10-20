# Betriebsweb-Framework · Start-Repository

Version 0.3.0 · 9. Oktober 2026 · Konzept und verbindlicher Projektstart

Dieses Repository ist eine technologieoffene Arbeitsgrundlage für schlanke Betriebswebseiten mit optionaler, modularer Redaktion. Es enthält Regeln, verknüpfte Vorlagen und einen ausführbaren Strukturprüfer. Es enthält noch keine Website, kein fertiges CMS und kein produktives Deployment.

## Hier beginnen

1. [Bauablauf](docs/01-bauablauf.md) lesen und Phase 0 beginnen.
2. [Projektprofil](project/site.json) ausfüllen; [offene Entscheidungen](decisions/0001-technikentscheidung.md) bearbeiten.
3. Die zwölf [Testpersonas](personas/personas.json) an den Betrieb anpassen; mindestens zehn bleiben Pflicht.
4. [Regelkatalog](rules/catalog.json) und [Architektur](docs/02-architektur.md) als Arbeitsgrundlage verwenden.
5. Erst nach Abschluss der Planungs-Gates die Website implementieren.

```bash
python3 scripts/check_repo.py
python3 scripts/check_repo.py --project-ready
```

Der erste Befehl prüft die Integrität dieses Starters. Der zweite blockiert absichtlich, solange Projektangaben, Verantwortliche und Technikentscheidungen offen sind. Ein grüner Strukturcheck bestätigt keine Sicherheit, Barrierefreiheit oder Produktionsreife.

## Wegweiser

| Pfad | Inhalt |
| --- | --- |
| `docs/01-bauablauf.md` | Phasen, Ergebnisse und Freigabepunkte |
| `docs/02-architektur.md` | Kern, Inhaltsmodule, Interaktion und Dienste |
| `docs/03-inhalte-und-sync.md` | Datenmodell, Sofortveröffentlichung und Git-Abgleich |
| `docs/04-designsystem.md` | Icons, SVGs, Animationen, Tokens und Varianten |
| `docs/05-ui-ux-barrierefreiheit.md` | Bedienung und Zugänglichkeit |
| `docs/06-sicherheit.md` | Sicherheitsmodell und Umsetzungsvorgaben |
| `docs/07-web-seo-performance.md` | Webstandards, SEO und Budgets |
| `docs/08-qualitaet-betrieb.md` | Prüfungen, Deployment, Backup und Betrieb |
| `docs/09-wissen-und-regeln.md` | Markdown, Referenzen und Regelverwaltung |
| `docs/10-erkenntnisse-leimbach.md` | Herleitung aus dem alten Projekt |
| `docs/12-seitengestaltung.md` | Hierarchie, Typografie, Breiten und Seitenrhythmus |
| `docs/13-medienvertrag.md` | Medienrahmen, Fokuspunkt und Alternativen |
| `docs/14-designabnahme.md` | Musterseite und Prüfung gegen Designabweichungen |
| `docs/15-compliance.md` | Verpflichtende Compliance und fachliche Freigabe |
| `project/compliance.json` | Anwendbarkeit, Verantwortung und Nachweise |
| `rules/catalog.json` | Maßgeblicher Regelkatalog mit IDs und Nachweisen |
| `project/` | Websiteprofil und offene Abnahmen |
| `personas/`, `tests/` | Personas, Szenarien und Prüfnachweise |
| `design/`, `modules/`, `content/` | Verknüpfte Beispiele für die Umsetzung |
| `templates/` | Vorlagen für Module, Entscheidungen, Releases und Ausnahmen |
| `.github/` | Strukturprüfung und Pull-Request-Vorlage |
| `.claude/` | Ausgewählte KI-Agents und Skills aus ECC, siehe `decisions/0002-ecc-agentenwerkzeuge.md` |

## Festgelegt und offen

Festgelegt: GitHub-Entwicklung, klassischer Webspace, mobile first, optionale erweiterbare Redaktion, zentrale Gestaltung, mindestens zehn Personas, nachvollziehbare Beziehungen und verbindliche Qualitätsprüfungen.

Astro ist ein bevorzugter Kandidat, noch keine verbindliche Auswahl. CMS, Authentifizierung, Hostingfähigkeit und Datenablage werden anhand eines Prototyps entschieden. Grav und ein Git-basiertes CMS werden als Alternativen bewertet.

Das Sofortmodell aus Leimbach ist ausdrücklich vorgesehen: veröffentlichte Redaktionsänderungen dürfen den statischen Stand bis zum bestätigten Abgleich überlagern. Die prüfbaren Anforderungen gelten schon vor dieser Sofortveröffentlichung.

## In GitHub verwenden

ZIP entpacken, den Inhalt in ein neues Repository übernehmen und einen initialen Commit erstellen. Anschließend erforderlichen Check `repository-integrity`, Branchschutz und Reviewzuständigkeiten konfigurieren. Diese Einstellungen werden durch das Kopieren der Dateien nicht automatisch aktiviert.

Das alte Leimbach-Repository wird nicht verändert. Es wurde kein neues Remote-Repository angelegt. Vor Weitergabe des Framework-Codes eine bewusste Lizenzentscheidung treffen; diese Vorlage vergibt keine pauschalen Rechte an später eingebundenen Fremdassets.

## Formale Releaseprüfung

`python3 scripts/check_repo.py --release-ready` blockiert, solange Projektfreigaben und Compliance-Nachweise fehlen. Dies ist eine Vollständigkeitsprüfung, keine rechtliche oder technische Zertifizierung.
