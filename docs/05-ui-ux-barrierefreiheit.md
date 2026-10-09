# UI, UX und Barrierefreiheit

Projektziel: WCAG 2.2, Stufe AA, für öffentliche Website und Redaktion. Anwendbare Erfolgskriterien werden in der Projektprüfung erfasst. Das ist ein technisches Qualitätsziel und keine pauschale Erklärung rechtlicher Konformität. Automatische Tests allein reichen nicht.

## Nutzerführung

Jede Seite beantwortet: Wo bin ich? Was kann ich hier tun? Was passiert danach? Eine Hauptaktion je Aufgabenschritt, konsistente Begriffe, vorhersehbares Zurück/Abbrechen. Keine leeren Sackgassen oder ausschließlich ikonischen wichtigen Aktionen.

Redaktion beginnt mit Aufgaben: „Projekt vorstellen“, „Entwurf weiterbearbeiten“, „Öffnungszeiten ändern“. Technische IDs, Git, Builds und Tokens bleiben hinter verständlichen Statusmeldungen. Einfache Aufgaben auf einer Seite; geführte Schritte nur bei tatsächlichem Nutzen.

## Bedienung

Semantische HTML-Elemente vor eigenen Rollen. Alle Funktionen per Tastatur, sichtbarer und nicht verdeckter Fokus. Dialoge führen Fokus hinein und zurück; Escape schließt, sofern dadurch kein unbemerkter Datenverlust entsteht. Keine Tastaturfallen. Sprunglink zum Hauptinhalt.

Formulare mit sichtbaren Labels, passendem Autocomplete, Hilfen und Fehlerübersicht. Fehler am Feld zuordnen. Eingaben bleiben erhalten. Statusmeldungen für Screenreader dosiert ankündigen. Login erlaubt Passwortmanager und Einfügen, ohne unnötige Gedächtnisaufgaben.

Projektstandard: interaktive Hauptziele möglichst mindestens 44 × 44 CSS-Pixel; Ausnahmen prüfen. Das ist ein eigener Komfortstandard und nicht mit der Mindestgröße aus WCAG AA gleichzusetzen. Normaler Text mindestens 4,5:1 Kontrast, großer Text mindestens 3:1; relevante UI-Grenzen und Zustände prüfen. Farbe nie allein.

Bei 200 % Textvergrößerung keine verlorenen Funktionen. Reflow bei 320 CSS-Pixel Breite beziehungsweise entsprechender 400-%-Vergrößerung prüfen; fachlich notwendige zweidimensionale Darstellungen erhalten zugängliche Alternative. Keine erzwungene Geräteausrichtung.

Videos mit gesprochenem Inhalt erhalten geprüfte Untertitel; weitere notwendige Medienalternativen gemäß Inhalt und WCAG-Prüfung vorsehen. Audio erhält Transkript. Reduzierte Bewegung respektieren. Wischen, Ziehen und Hover brauchen Alternativen.

## Personas und Nachweise

Vor Implementierung mindestens zehn angepasste Personas. `personas/personas.json` enthält zwölf Ausgangsprofile. Ziele und Situationen zählen, keine stereotypen Annahmen allein aufgrund Alter oder Behinderung.

Kernwege manuell per Tastatur, mit mindestens einem dokumentierten Screenreader-/Browserpaar, auf realem Smartphone und bei Vergrößerung testen. Repräsentative nicht technische Nutzer erledigen Aufgaben ohne Vorführung. Aufzeichnen: Abschluss, Hilfebedarf, Fehler, Verständnis des Status. Keine erfundenen Nutzerbeobachtungen.

Ein automatischer Scan ohne Fehler ist kein Barrierefreiheitsnachweis. Befunde erhalten Verantwortliche und Wiederholungsprüfung. Einfach-Modus ergänzt eine bereits zugängliche Standardansicht.
