# Bauablauf mit Freigabepunkten

Jede Phase endet mit einem nachvollziehbaren Ergebnis. Kleine Projekte dürfen Schritte zusammen bearbeiten, aber keinen anwendbaren Freigabepunkt überspringen. Abnahmen werden in `project/gates.json` mit Verantwortlichem, Datum und Nachweis erfasst.

| Phase | Arbeit | Ergebnis / Gate |
| --- | --- | --- |
| 0 · Auftrag | Ziel, Betrieb, Zielgruppen, Inhalte, Funktionen, Nicht-Ziele, Verantwortung, Budget, Webspace erfassen | G0: Projektprofil vollständig; mindestens zehn angepasste Personas und Kernaufgaben |
| 1 · Architektur | Bedrohungsmodell, Inhaltsmodell, Veröffentlichungsmodus, Hostingfähigkeiten und CMS-Kandidaten bewerten | G1: Technik-ADR entschieden; Rollen und Datenzuständigkeiten klar |
| 2 · Gestaltung | Mobile Informationsstruktur, Sprachprofil, Tokens und Komponenten definieren | G2: Navigationsentwurf und zentrale Komponenten für Kernaufgaben freigegeben |
| 3 · Durchgängiger Prototyp | Anmeldung → Projekt mit drei Fotos → Entwurf → Vorschau → Freigabe → Webspace; bei Sofortmodus zusätzlich Git-Abgleich | G3: Ablauf auf Smartphone funktioniert; Konflikt, Rücknahme und Ausfall nachgestellt |
| 4 · Minimalwebsite | Nur vereinbarte Seitentypen und Referenzmodul implementieren; reale Beispielinhalte integrieren | G4: öffentliche Kerninhalte als HTML; aktive Module halten Budgets ein |
| 5 · Qualität | Persona-Szenarien, Sicherheit, Barrierefreiheit, SEO, Medienrechte und Performance prüfen | G5: Muss-Regeln erfüllt; Ausnahmen bewertet; keine offenen kritischen Blocker |
| 6 · Betrieb | Deployment, Überwachung, Backup, Wiederherstellung und Rollback einrichten | G6: Wiederherstellung praktisch erfolgreich; Hosting-Sicherheitschecks erfolgreich |
| 7 · Veröffentlichung | Exakten geprüften Stand freigeben, veröffentlichen, Smoke-Test, Anleitung und Übergabe | G7: Releaseprotokoll mit Commit, Inhaltsstand, Artefakt-ID und Verantwortlichem |
| 8 · Weiterentwicklung | Feedback prüfen, Priorität und Kosten bewerten, neue Module separat abnehmen | Je Erweiterung relevante Gates erneut durchlaufen |

## Die ersten Arbeitsaufträge

1. Projektprofil kopieren und auf einen konkreten Betrieb zuschneiden.
2. Personas gemeinsam mit Auftraggeber prüfen; nicht relevante Beispiele ersetzen.
3. Webspace testen: TLS, PHP-Version falls benötigt, SSH/SFTP/FTPS, Schreibrechte, Cron, Speicher außerhalb Webroot, Header, Rewrite, atomarer Wechsel.
4. CMS-Kandidaten an vier Fällen prüfen: mobile Bildpflege; neuer Inhaltstyp; gleichzeitige Bearbeitung; Ausbau ohne Belastung anderer Seiten.
5. Einen Technikentscheid treffen, dann erst Anwendungsgerüst und Buildsystem anlegen.
6. Acht bis zwölf tatsächlich benötigte Komponenten definieren, z. B. Navigation, Button, Formularfeld, Projektkarte, Galerie, Statusmeldung, Dialog und Footer.
7. Eine reale Projektvorstellung Ende zu Ende bauen. Keine Karten-, Video- oder KI-Pipeline ohne konkreten Bedarf.

## Definition of Ready für eine Aufgabe

Nutzerziel, betroffene Personas, Umfang, Datenbeziehungen, Regel-IDs, Abnahmekriterien und Prüfverfahren stehen fest. Risiken und offene Entscheidungen sind benannt.

## Definition of Done

Implementierung und Inhalte erfüllen die anwendbaren Regeln; betroffene Tests bestanden; manuelle Nachweise erfasst; Dokumentation aktuell; Migration und Rücknahme bedacht; Ressourcenbudget eingehalten; keine unbestätigte Erfolgsbehauptung. Eine nicht ausgeführte Prüfung bleibt offen.

## Änderungen nach Projektstart

Pull Request beschreibt Zweck und Auswirkungen statt nur Dateien. Zentrale Navigation, Authentifizierung, Tokens oder Schemas lösen breitere Regressionstests aus. Eine reine Textkorrektur benötigt keine vollständige Browsermatrix, aber Inhalts-, Link- und Freigabeprüfung bleiben anwendbar.

## Konkretisierung der Design-Gates ab Version 0.2.0

G2 enthält die [Seitentypregeln](12-seitengestaltung.md) und den [Medienvertrag](13-medienvertrag.md). Vor G3 entsteht die [Musterseite](14-designabnahme.md) für die Prototypkomponenten. G5 fordert die vollständige Abdeckung aller tatsächlich ausgelieferten Varianten. Kein zusätzlicher Medienumfang ist dadurch automatisch beauftragt.

## Compliance-Gates

[Compliance](15-compliance.md) gilt verpflichtend. G0 benennt Betreiber und Complianceverantwortung; G1 klärt Anwendbarkeit; G5 erfasst Umsetzung und Nachweise; G7 setzt dokumentierte Freigabe voraus. `python3 scripts/check_repo.py --release-ready` prüft die formale Vollständigkeit aller Gates und des Compliance-Registers. Er ersetzt keine fachliche Freigabe.
