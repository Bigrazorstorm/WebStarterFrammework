# Zentrales Designsystem

Einmal definieren, referenzieren, nur bei Verwendung ausliefern. `design/tokens.json` ist die maßgebliche Quelle für Beispielwerte; CSS wird später daraus erzeugt. Die Werte sind Startwerte, keine bereits abgenommene Marke.

## Ebenen

1. Primitive Werte: Farbtöne, Maße, Schriftfamilien und Zeiten.
2. Semantische Tokens: Text, Hintergrund, Fehler, Fokus, ausgewählt, Abstand und Bewegung.
3. Komponenten: erlaubte Varianten mit dokumentiertem Verhalten.
4. Seitentypen: Kombinationen freigegebener Komponenten.

Betriebsspezifische Themes überschreiben erlaubte Tokens. Sie dürfen Kontrast, Fokus oder reduzierte Bewegung nicht abschalten. Jede Farbkombination und alle Zustände werden geprüft.

## Icons und SVG

Icons erhalten stabile Namen, Herkunft/Lizenz, viewBox und Größenregeln. Dekorative Icons sind für assistive Technik verborgen; bedeutungstragende erhalten eine verständliche Bezeichnung. Kritische Aktionen kombinieren Icon und Text. Keine kopierten SVG-Pfade in Fachmodulen. Markenlogos bleiben eigenständige Assets.

Redakteur-Uploads sind keine vertrauenswürdige Iconbibliothek. SVGs auf aktive Inhalte, Fremdreferenzen und unerlaubte Elemente prüfen oder in sichere Rasterdarstellung umwandeln. Keine ungeprüfte Einbettung als HTML.

## Animation

Zentrale Bewegungsrezepte besitzen Zweck, Dauer, Kurve, Auslöser und bewegungsarme Alternative. Keine notwendigen Informationen nur animiert zeigen. Automatische Bewegung muss bei Bedarf anhaltbar sein. Im Hintergrund pausieren; Audio nur nach bewusster Nutzeraktion. Fachliche Animationen verwenden denselben Einstellungsdienst.

## Darstellungen

Projektkarte, Liste, Galerie, Zeitleiste und Vergleich arbeiten mit demselben Inhaltsmodell. Jede Variante beschreibt Tastaturverhalten, Fokus, leeren Zustand, Ladezustand, Fehler und Textalternative. Für Karten/3D gibt es einen inhaltlich nutzbaren Listen-/Textzugang.

Eine Komponentenübersicht muss später alle Varianten und Zustände zeigen, einschließlich langem Text, fehlendem Bild, schmalem Bildschirm und Vergrößerung. Änderungen an zentralen Tokens lösen visuelle und zugänglichkeitsbezogene Regressionstests aus.

## Ergänzende Verträge

- [Seitengestaltung](12-seitengestaltung.md)
- [Medienbausteine](13-medienvertrag.md)
- [Musterseite und Designabnahme](14-designabnahme.md)
