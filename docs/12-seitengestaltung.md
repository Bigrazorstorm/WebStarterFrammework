# Seitengestaltung und Komposition

Die Marke definiert Werte, Komponenten definieren Verhalten und Seitentypen definieren Aufbau. Diese drei Ebenen werden gemeinsam geprüft. Ein Theme darf keine Zugänglichkeits- oder Sicherheitsregeln aushebeln.

## Regeln je Seitentyp

| Seitentyp | Inhaltliche Reihenfolge | Hauptaufgabe |
| --- | --- | --- |
| Startseite | Angebot, Vertrauensbelege, passende Leistungen/Referenzen, Kontakt | Betrieb und nächsten Schritt verstehen |
| Leistung | Nutzen, Umfang, Grenzen, passende Referenzen, Anfrage | Eignung des Angebots beurteilen |
| Projekt | Aufgabe, Umsetzung, Ergebnis, Medien, zugehörige Leistung | Tatsächliche Arbeit nachvollziehen |
| Kontakt | Kontaktwege, Erreichbarkeit, Standort, optional Formular | Betrieb direkt erreichen |
| Redaktion | Aufgabe, Eingabe, Vorschau, Freigabe, Ergebnis | Inhalt sicher bearbeiten |

Die Reihenfolge ist ein Ausgangsmuster und wird anhand der Personas geprüft. Optionale Abschnitte ohne Inhalt entfallen. Keine leeren Schmuckbereiche; Navigation und Hauptaktion bleiben erreichbar.

## Visuelle Hierarchie

Typografische Rollen für Titel, Lesetext, Metadaten und Bedienung festlegen. Rollen erfordern keine getrennten Schriftfamilien. Standard bleibt Systemschrift; zusätzliche Fonts brauchen Nutzen, Lizenz und Budget.

Zulässige Breiten als Tokens: Textspalte, mittlere Fläche, breite Medienfläche und volle Breite. Jede Komponente erklärt erlaubte Breiten. Textbreite nach Lesbarkeit wählen; Vollbreite nicht auf Fließtext übertragen. Abstände zwischen Absätzen, Abschnitten und Medien folgen einer gemeinsamen Skala.

Gliederung bevorzugt über Schrift, Abstand und klare Überschriften. Karten sind für auswählbare oder vergleichbare Einheiten vorgesehen, nicht als Pflichtumrandung jedes Absatzes. Farbe kennzeichnet Bedeutung; beliebige Akzente je Komponente vermeiden.

## Aufmacher und Rhythmus

Ein Betrieb braucht nicht grundsätzlich einen bildschirmfüllenden Aufmacher. Kernangebot und nächste Handlung müssen zur Aufgabe passen. Gute Bilder dürfen führen; ohne geeignetes Bild gibt es eine gleichwertige typografische Variante.

Text und Medien wechseln entsprechend dem Inhalt. Kein erzwungenes Bild nach einer bestimmten Wortzahl, keine allgemeine Mindestleselänge. Jeder Medienbaustein vermittelt eine benennbare Aussage. Zahl und Gewicht aufwendiger Bausteine werden im Seitentyp begrenzt.

Text auf Bildern wird über ungünstigen Bildausschnitten geprüft. Wenn ein kontraststabiler Hintergrund nicht sicher hergestellt werden kann, steht der Text außerhalb des Bildes. Ein Schatten allein ist kein Kontrastnachweis.

## Gemeinsame Marke

Die Quelle gemeinsamer Tokens liegt im Framework unter `design/`, nicht in einer optionalen Videopipeline. Aus ihr werden Web-CSS und gegebenenfalls Medienkonfigurationen erzeugt. Medien dürfen passende, nachvollziehbare Anpassungen besitzen: identische Farbe bedeutet nicht automatisch ausreichenden Kontrast auf hellem und dunklem Hintergrund.

Generierte Dateien erhalten Herkunftsangabe und werden nicht manuell geändert. CI erzeugt sie erneut und prüft auf unerwartete Unterschiede. Dieser Generator ist nach Wahl des Stacks zu implementieren.
