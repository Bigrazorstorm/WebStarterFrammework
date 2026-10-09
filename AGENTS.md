# Arbeitsanweisungen für Entwickler und KI-Assistenten

1. Vor Änderungen README, Bauablauf, Projektprofil, Regelkatalog und betroffene Fachrichtlinien lesen.
2. Keine offene Architekturentscheidung stillschweigend als beschlossen behandeln. Entscheidung in `decisions/` mit Begründung dokumentieren.
3. Neue Funktion zuerst einem Persona-Ziel und einem Modultyp zuordnen. Kein vorsorglicher Funktionsausbau.
4. Vorhandene Komponenten, Icons, Tokens, Animationen und Inhaltsreferenzen verwenden. Keine lokalen Kopien gemeinsamer Regeln.
5. Inhalt, Entwurf, Freigabe und Veröffentlichung getrennt behandeln. Sofortveröffentlichung muss dieselben anwendbaren Regeln erfüllen wie der Build.
6. Zu jeder Änderung betroffene Regel-, Persona-, Modul- und Test-IDs benennen. Neue Regel erhält einen Nachweis und eine verantwortliche Rolle.
7. Sicherheitsprüfungen niemals in Warnungen umwandeln, um einen Build grün zu bekommen. Keine Geheimnisse ausgeben oder einchecken.
8. Datenmigrationen, bestehende IDs, Rücknahmen und parallele Bearbeitung berücksichtigen. Kein stiller Datenverlust.
9. Passende Prüfungen ausführen und ehrlich berichten: bestanden, fehlgeschlagen, nicht ausgeführt. Strukturprüfung ist kein Funktionstest.
10. Dokumentation und Beispiele im selben Änderungsumfang aktualisieren. Doppelte Werte vermeiden.
11. Keine Produktionsveröffentlichung aus einem nicht freigegebenen Stand. Richtlinienänderungen benötigen eigenes Review.
12. Mindestens zehn projektspezifische Personas vor der Implementierung festlegen. Keine tatsächlichen Nutzertests erfinden.

Geltungsrang: explizite Projektentscheidung im vereinbarten Freigabeverfahren; globale Muss-Regeln; Projektprofil; Modulregeln; Beispiele. Ein Projektprofil darf Muss-Regeln nicht still abschwächen. Ausnahmen müssen dokumentiert und genehmigt werden.


Design-Ergänzung: Vor Seitenbau `docs/12-seitengestaltung.md`, `docs/13-medienvertrag.md` und `docs/14-designabnahme.md` lesen. Die Marke gehört nicht in ein optionales Produktionsmodul. Pflichtprüfungen bei fehlenden Werkzeugen nicht als bestanden melden. Baselineänderungen begründen.

Compliance ist verpflichtend: `docs/15-compliance.md` und `project/compliance.json` bei relevanten Änderungen prüfen. Keine Rechtskonformität aus bestandenen technischen Tests ableiten. Offene Pflichtpunkte blockieren Release; gesetzliche Pflichten nicht über Ausnahmen abwählen.
