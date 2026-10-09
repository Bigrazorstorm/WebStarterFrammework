# Musterseite und Designabnahme

Vor der ersten vollständigen Website wird eine nicht öffentliche Komponenten-Musterseite implementiert. Sie wird aus dem Komponentenregister aufgebaut. Eine einzelne schöne Demoseite genügt nicht.

## Abdeckungsmatrix

Jede verwendete Komponente: Standard, Fokus, deaktiviert falls relevant, Laden, leer, Fehler und Erfolg. Zusätzlich kurze/lange Texte, fehlendes Bild, schmaler Bildschirm, Vergrößerung und reduzierte Bewegung. Helles/dunkles Theme prüfen, falls beide angeboten werden.

Mindestens 360 px Touch, 320 CSS-Pixel Reflow, mittlere und breite Ansicht; zusätzlich reales Smartphone für Kernwege. Browser, Schriftladezustand und Testdaten für Bildvergleiche festlegen.

Automatisch prüfbar: Überlauf, erlaubte Breiten, Tokenverweise, fehlende Assetreferenzen, Fokusziel nach Dialogen, Kontrast geeigneter statischer Zustände, generierte Dateien aktuell. Manuell: Lesbarkeit, verständliche Hierarchie, Bildausschnitt, Bedienbarkeit und sinnvolle Alternativen.

## Keine still übersprungenen Pflichtprüfungen

Fehlender Browser, fehlendes Testwerkzeug oder fehlende Testdaten lässt einen erforderlichen Releasecheck scheitern. Lokale optionale Tests dürfen ausdrücklich als nicht ausgeführt gemeldet werden. Übersprungen ist nicht bestanden.

## Neue Designabweichungen verhindern

Für neue Projekte keine lokalen Kopien zentraler Bedien-Icons, keine unregistrierten gemeinsamen Farb-/Abstandswerte. Fachwerte wie eine geographische Koordinate oder historische Materialfarbe bleiben erlaubt und werden nicht künstlich zu globalen Tokens.

Bei Übernahme alten Codes darf eine überprüfte Ausnahmeliste den Bestand festhalten. Neue Abweichungen sind verboten; die Liste darf beim Umbau schrumpfen. Jede Bestandsausnahme hat Ort, Grund und Rückbauaufgabe. Ein pauschales Erhöhen der Grenze benötigt Architekturreview.

Prüfung syntaktisch geeigneter Quellen (AST/CSS-Analyse nach Stackwahl), ergänzt durch Review. Eine bloße Textsuche ist kein vollständiger Nachweis. Änderungen an Baselines, Tokenprüfungen und Screenshotreferenzen brauchen begründetes Review; Referenzbilder nicht automatisch akzeptieren.

## Abnahme

G2: Rollen, Breiten und Komponentenverträge festgelegt. G3: Musterseite für Prototypkomponenten geprüft. G5: alle ausgelieferten Varianten abgedeckt, Fehler behoben, manuelle Nachweise vorhanden. Registereinträge mit `planned` sind keine fertigen Komponenten.
