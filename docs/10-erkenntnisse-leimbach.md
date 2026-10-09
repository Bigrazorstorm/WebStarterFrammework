# Erkenntnisse aus Leimbach

Grundlage: lesende Architekturprüfung von Bigrazorstorm/Leimbach am 9. Oktober 2026. Main damals `6f3f36947e1c08a766dfb6fce7284c12d6f5a6e8`. Der über Touren-PRs zugeordnete Branch `ccr-fa98c744-dpq5s1` war bereits enthalten. Keine umfassende Live- oder Sicherheitsprüfung.

Übernehmen: geführte Redaktion, getrennte Entwürfe und Veröffentlichung, Rücknahme/Wiederherstellung, Revisionskonflikte, kontrollierter Git-Abgleich, Quellbeziehungen, alternative Darstellungen, nachgeladenes 3D und Freigaben entlang von Produktionsschritten.

Bewusst beibehalten: Redaktion überlagert den statischen Bestand bis zum bestätigten Sync. Dies ist fachlicher Bedarf, kein Architekturfehler. Sicherheits- und Inhaltsregeln müssen schon vor der sofortigen Veröffentlichung greifen.

Verbessern: zentrale Dateisammlung ist keine bedarfsgerechte Auslieferung; Modulressourcen pro Seite laden. Große zentrale Dateien in klar verantwortete Komponenten aufteilen. Eigene SVGs und Farben in Spezialmodulen an das Designsystem anbinden. Warnungen von blockierenden Datenfehlern trennen. Produktionswerkzeuge vom normalen Seitenbuild entkoppeln.

Mehrfachdarstellungen brauchen dieselbe Faktenbasis, aber eigene Fassungen und Freigaben für Text, Audio und Video. Änderungen der Grundlage markieren Folgeprodukte als prüfbedürftig. Synchronisierte Texte allein sichern keine Laufzeitmedien oder Redaktionseinstellungen.

## Interne Referenzen (privates Repository)

- https://github.com/Bigrazorstorm/Leimbach/blob/main/Admin/docs/DATENSCHICHTEN.md
- https://github.com/Bigrazorstorm/Leimbach/blob/main/Admin/docs/NEUAUFBAU.md
- https://github.com/Bigrazorstorm/Leimbach/blob/main/Homepage/src/index.html
- https://github.com/Bigrazorstorm/Leimbach/blob/main/.github/workflows/homepage.yml
- https://github.com/Bigrazorstorm/Leimbach/blob/main/Video/DATENMODELL.md
- https://github.com/Bigrazorstorm/Leimbach/pull/255

Diese Links können sich ändern; die Beobachtungen sind dem oben genannten Prüfstand zugeordnet. Keine privaten Daten oder Quellcodekopien werden mitgeliefert.

## Designbranch `ccr-82e14370-ysr2i3`

Bei der ergänzenden lesenden Prüfung am 9. Oktober 2026 lag dieser Branch 41 Commits vor dem genannten Main-Stand. Herangezogen: `Homepage/konzept/themenseiten.md`, `Homepage/src/marke.css`, `bausteine.js`, `bild.js`, `motive.js`, `Homepage/tests/icons.cjs` und `themenseite.cjs`.

Übertragen werden gemeinsame Tokengenerierung, typografische Rollen, Raster/Breiten, Medienvertrag, Fokuspunkt, getrennte Bedien-Icons und Erklärmotive sowie überprüfbare Designabnahme. Keine Übernahme der konkreten Leimbach-Schriften, der historischen Inhalte oder eines pauschalen Vollbild-Storylayouts.

Verbesserungen für das neue Framework: zentrale Marke unabhängig vom optionalen Video; Pflichtprüfungen scheitern bei fehlender Testumgebung; unbekannte Bausteine nicht still verwerfen; wichtige Beschriftungen nicht auf 10 px verkleinern. Die Browserprüfungen des Branches wurden gelesen, nicht ausgeführt.

Quelle: https://github.com/Bigrazorstorm/Leimbach/tree/ccr-82e14370-ysr2i3
