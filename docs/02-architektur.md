# Architektur

## Bausteine

- Framework-Kern: Inhaltsschnittstellen, Designsystem, Validierung, gemeinsame Bedienmuster und Modulverträge.
- Websiteprofil: Identität, Sprache, Tokens, aktive Module, Seitentypen, Budgets und Hostingeinstellungen.
- Redaktion: optional; Anmeldung, Rechte, Medien, Entwürfe, Vorschau, Konflikte und Veröffentlichungsstatus.
- Inhaltsmodule: Referenzen, Leistungen, Team, Neuigkeiten, Stellenangebote.
- Interaktive Module: Galerie, Filter, Karte, Vergleich, Tour; laden nur auf verwendenden Seiten.
- Dienste: Einsendungen, Buchungen, externe Importe und Benachrichtigungen; eigene Datenhaltung und Betriebsverantwortung.
- Produktionswerkzeuge: Video, Audio, große Geodaten; erzeugen Artefakte außerhalb des normalen Seitenbuilds.

Ein gemeinsamer Login darf mehrere Bereiche zugänglich machen; er macht deren Speicher- und Berechtigungsmodelle nicht identisch.

## Repositorymodell

Framework und Betriebswebsite werden getrennt versioniert. Jede Website legt ihre Framework-Version fest und erhält Updates als geprüfte Pull Requests. Für den ersten Prototyp darf das Framework als lokales Paket liegen. Keine unkontrollierten Kopien in Kundenprojekten.

Code und Inhalte können zunächst in einem Betriebsrepository liegen. Ein gesondertes Inhaltsrepository ist erforderlich zu bewerten, wenn Redakteure sonst Schreibzugriff auf Workflows oder Code erhalten. CMS-Feldkonfiguration ist keine Sicherheitsgrenze.

## Modulvertrag

Jedes Modul nennt ID, Version, Typ, benötigte Module, Inhalte, Komponenten, Regeln, Personas, Tests, Ressourcen, Rechte, Migration, Datenlöschung und Ausfallverhalten. Abhängigkeiten müssen gerichtet und prüfbar sein; zyklische Abhängigkeiten zwischen Modulen sind verboten. Inhaltliche Beziehungen dürfen fachlich sinnvolle Kreise bilden.

Module verwenden öffentliche Schnittstellen. Sie greifen nicht auf private Tabellen anderer Module zu. Deaktivierung entfernt Jobs, Navigation und Endpunkte kontrolliert; Daten werden nur durch eine ausdrücklich angeforderte Löschung entfernt.

Interaktive Module haben Start-, Pause-, Fortsetzen- und Aufräumverhalten. Beim Verlassen enden Medien, Standortabfragen und Listener; ausstehende Antworten dürfen keine verlassene Ansicht überschreiben.

## Technologieentscheidung

Astro ist Kandidat für statische öffentliche HTML-Seiten. Ein CMS wird nach mobilem Redaktionsablauf, Ausbau, Authentifizierung ohne GitHub-Konto, Rechten, Migration, Export und Synchronisationsfähigkeit ausgewählt. Ein PHP-CMS oder eigenes Backend ist nur mit begründetem Bedarf einzusetzen. Versionswahl erfolgt zum Implementierungsbeginn mit Lockfiles.

Ein statischer Webspace kann neue vollständige serverseitige URLs nicht spontan aus einer Browserüberlagerung erzeugen. Sofortmodus benötigt deshalb entweder passende Backend-Routen, oder neue Seiten werden erst nach dem Build als vollständig veröffentlicht gemeldet. Diese Einschränkung wird im ADR entschieden, nicht verdeckt.
