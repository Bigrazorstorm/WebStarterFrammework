# Wissen, Regeln und Verknüpfungen

`rules/catalog.json` ist die maßgebliche Liste der Regel-IDs. Die zugeordneten Fachdateien erläutern ihre Umsetzung. Zahlen werden nur in ihrer maßgeblichen Konfiguration gepflegt. Beispiele sind als Beispiele markiert.

Eine Regel besitzt ID, Muss/Soll, Geltungsbereich, Begründung, verantwortliche Rolle, Dokument und Prüfverfahren. Rollen werden im Projektprofil konkreten Verantwortlichen zugeordnet. Jede Änderung nennt betroffene Regeln und Personas; Ausnahmen verwenden `templates/exception.md`.

Wissensarten trennen: verbindliche Regeln; entschiedene ADRs; Projektkonfiguration; Inhalte; Ideen/Backlog; Testnachweise. Nicht alle Arbeitsnotizen sind verbindlich. Entscheidungen behalten Datum und Begründung, ersetzte Entscheidungen werden markiert und verlinkt.

Verknüpfungen verbinden Inhalte untereinander, Inhaltstypen mit Komponenten, Komponenten mit Tokens/Icons/Animationen, Module mit Regeln und Personas mit Testfällen. Rückverweise werden aus Referenzen erzeugt. Keine manuell gepflegten zweiten Listen als konkurrierende Wahrheit.

Geänderte Grundlagen können Folgeartefakte als prüfbedürftig markieren. Prüfsummen melden Änderung, ersetzen aber keine fachliche Bewertung. Markdown-Dateien mit privaten Notizen gehören nicht automatisch in öffentliche Exporte.

Die mitgelieferte Strukturprüfung prüft lokale Markdown-Dateilinks, JSON-Referenzen, Mindestanzahl Personas und Modulkreise. Sie prüft keine externen URLs, Normkonformität, Bildkontraste, produktiven Code oder Authentifizierung. Ergänzungen gehören in die echte Produktteststrecke.
