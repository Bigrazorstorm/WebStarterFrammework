# Vertrag für Medienbausteine

Gilt für Bild, Bildfolge, Vergleich, Illustration, Diagramm, Karte, Audio, Video und 3D. Die konkrete Umsetzung folgt nach Technikentscheidung.

## Pflichtangaben einer Bausteinart

- Stabile Art-ID, Zweck, Version und zugelassene Inhaltsreferenzen.
- Erlaubte Breiten und Seitenverhältnisse; mobile Anordnung.
- Gewichtsklasse und expliziter Ladeauslöser.
- Alternativdarstellung und Verhalten bei fehlendem Medium.
- Zugänglicher Name, Tastaturbedienung, Fokusverhalten und sichtbare wichtige Aktionen.
- Unterschrift, Herkunft und Rechte aus dem zentralen Assetdatensatz.
- Aufräumen von Listenern, Beobachtern, Audio, Standortabfragen und Grafikressourcen.
- Testfälle und benötigte Ressourcen nach Aktivierung.

## Gewicht und Laden

Leicht: Text und kleine lokale Symbole. Mittel: Bilder und einfache Grafiken, außerhalb des Einstiegsbereichs nahe Sichtbarkeit laden. Schwer: Video, interaktive Karte oder 3D; zunächst ruhende Vorschau, anschließend bewusste Aktivierung. Ein wesentliches Einstiegsbild nicht pauschal verzögert laden. Die Gewichtsklasse ersetzt keine Messung.

## Bilder

Asset-ID, Originalmaße, Varianten, Alt-Text gemäß Verwendung, Unterschrift, Herkunft, Rechte und optional Fokuspunkt in Prozent erfassen. Unterschiedliche Verwendungen dürfen unterschiedliche Alt-Texte benötigen. Dekorative Bilder haben leeren Alternativtext.

Fokuspunkt steuert den Ausschnitt, verändert nicht das Original. Mobile und breite Vorschau prüfen; wichtige Personen, Werkstücke oder Beschriftungen dürfen nicht abgeschnitten werden. Ein Fokuspunkt genügt nicht immer: bei Bedarf alternative Zuschnitte/Medien für das Seitenverhältnis vorsehen.

Bildvarianten mit `srcset`/`sizes`, korrekten Abmessungen und kontrolliertem Format. Beim Ladefehler verständliche Ersatzdarstellung; keine endlos leere Fläche. Bildnachweise konsistent und lesbar.

## Icons, Motive und Datenvisualisierung

Bedien-Icons und Erklärmotive sind getrennte Kataloge. Icons bedienen; Motive erklären. Ein komplexes Motiv wird nicht automatisch zum kleinen Icon. Beispielzahlen eines Motivs werden ersetzt oder eindeutig als Beispiel markiert.

Diagramme referenzieren strukturierte Werte mit Einheit, Zeitraum und Beleg. Datentabelle oder andere geeignete Textfassung bereitstellen. Wichtige SVG-Beschriftungen nicht auf unlesbare Größen verkleinern: Darstellung vereinfachen, umbrechen oder Beschriftung außerhalb der Grafik anordnen.

## Fehler und Interaktion

Unbekannte Bausteinarten sind im Build/Editor ein sichtbarer Validierungsfehler; sie dürfen nicht stillschweigend wesentliche Inhalte entfernen. Zur Laufzeit sichere Textalternative und protokollierter Fehler. Bei fehlenden Nutzungsrechten wird das Medium nicht ausgeliefert.

Karten und 3D fangen das normale Seitenscrollen nicht ab. Bedienung erst nach bewusster Aktivierung, mit erkennbarem Rückweg. Wichtige Aktionen wie Textalternative und Aktivierung sind verständlich beschriftet.
