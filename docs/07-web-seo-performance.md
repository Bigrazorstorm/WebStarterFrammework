# Webstandards, SEO, Performance und Text

## Öffentliche Website

Semantisches HTML, echte Links und Buttons, progressive Verbesserung. Kerninhalte und Navigation ohne JavaScript. Stabile URLs pro Inhalt, korrekte HTTP-Statuscodes, Weiterleitungen bei URL-Änderung. Routing darf nicht nur aus Hash-Ansichten bestehen, wenn eigenständige indexierbare Inhaltsseiten benötigt werden.

Komponenten trennen Darstellung, Fachlogik und Datenzugriff. Modul-CSS nicht global einbinden. Keine globale Bibliothek für eine einzelne Unterseite. Browser-/Gerätematrix im Projekt festlegen; Standardsfunktionen bevorzugen.

## SEO

Seitentypen erzeugen eindeutige Titel, Beschreibungen, Hauptüberschrift, Canonical und Social-Vorschau. Sitemap enthält nur öffentliche kanonische URLs. Robotsregeln und noindex gezielt setzen; private Inhalte benötigen echten Zugriffsschutz. Interne Links aus geprüften Beziehungen erzeugen. Strukturierte Daten müssen sichtbaren tatsächlichen Angaben entsprechen, ohne erfundene Bewertungen.

Betriebsname, Adresse, Kontakt und Öffnungszeiten einmal pflegen. Neue Seiten im Sofortmodus erhalten eine bewusste URL-/Renderingentscheidung; bloße Clientanzeige ist keine bestätigte Indexierbarkeit. Rücknahmen müssen Dateien, Sitemap und Caches berücksichtigen. Auffindbarkeit ist ein Qualitätsziel, keine Rankinggarantie.

## Startbudgets

Maßgebliche Zahlen in `project/site.json`. Öffentliche Standardseiten starten mit maximal 30 KB gzip JavaScript, 40 KB gzip CSS und 500 KB initialer Übertragung einschließlich Bildern und Schriften. Dies sind Projektbudgets, keine Normwerte und keine Aussage über die Größe des Adminbereichs.

Messprofil vor Umsetzung festlegen: 360 × 800 CSS-Pixel, leerer Cache, keine Interaktion, initiale Ressourcen bis Netzruhe; Browser, Drosselung und CPU-Profil im Prüfbericht exakt festhalten. Dynamische Module erhalten zusätzlich Budgets nach Aktivierung für Bytes, Speicher und Rechenlast. Wiederholte Messungen unter identischem Profil; keine beliebig günstige Einzelmessung auswählen.

Bilder im Build oder beim Upload optimieren, Abmessungen setzen, responsive Größen erzeugen, nachgelagerte Bilder verzögert laden. Wesentliches Einstiegsbild nicht unnötig verzögern. Schriften möglichst lokal oder Systemschriften. Animationen bei Unsichtbarkeit pausieren. Caches begrenzen und Ressourcen aufräumen.

## Sprachprofil

Jeder Betrieb legt Du/Sie, Zielgruppe, Ton, Fachbegriffe, Schreibweisen, Handlungsaufforderungen und Beispiele fest. Klare Alltagssprache; keine unbelegten Superlative. CMS-Felder erklären die Aufgabe statt technische Formate.

Automatische Wort-/Pflichtfeldprüfungen unterstützen. Sachlichkeit, Verständlichkeit und Markenwirkung benötigen redaktionelles Review. KI-Vorschläge bleiben Entwürfe bis zur Freigabe.
