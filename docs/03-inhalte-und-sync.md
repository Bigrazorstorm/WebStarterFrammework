# Inhalte, Beziehungen und Synchronisation

## Wissensformat

Markdown enthält längere Texte und Erläuterungen. Strukturierte Metadaten liegen im Dateikopf oder in JSON/YAML. Tokens, Schemas und technische Konfiguration sind maschinenlesbar. Redaktionelle Inhalte dürfen weder Templates ausführen noch beliebiges MDX/HTML einschleusen.

Jeder Inhalt besitzt stabile ID, Typ, Schemaversion, Revision und explizite Beziehungen. Titel und URLs können sich ändern; IDs bleiben. Medien werden über Asset-IDs referenziert. Ein erzeugter Index liefert Rückverweise und Verwendungsnachweise, wird aber nicht manuell gepflegt.

Löschen wird bei eingehenden Referenzen blockiert oder durch eine explizite Ersatz-/Archiventscheidung begleitet. Eine Quelle kann optional mit ihrer Revision/Prüfsumme referenziert werden: Änderungen lösen Prüfbedarf aus. Freigaben gelten für konkrete Fassungen; Nachfolgeprodukte wie Sprechertext und Video können veralten.

## Zwei ausdrücklich wählbare Veröffentlichungsmodi

A: Redaktion → geprüfter Git-Änderungsvorschlag → Freigabe → Build → Veröffentlichung.
B: Redaktion → Prüfung/Freigabe → sofortige öffentliche Überlagerung → späterer Git-Abgleich → Build → Bestätigung des ausgelieferten Stands.

Modus B ist beabsichtigt und gleichberechtigt. Kein Modul darf ihn durch einen unbeabsichtigten zweiten Schreibweg einführen. Projektprofil und ADR entscheiden den Modus. Bei B gelten Sicherheits-, Inhalts- und Komponentenregeln vor der sofortigen Freigabe; CI allein kommt zu spät. Nicht zur Laufzeit prüfbare Änderungen benötigen vorab eine geprüfte Vorschau beziehungsweise Buildfreigabe.

## Zustände

Entwurf → zur Prüfung → freigegeben → sofort sichtbar oder wartet auf Build → in Git übernommen → statisch ausgeliefert.

„Gespeichert“, „freigegeben“, „sofort sichtbar“ und „statisch ausgeliefert“ werden separat angezeigt. Autosave veröffentlicht nie. Neue Entwürfe ändern die bisher öffentliche Fassung nicht.

## Änderungsumschlag für Modus B

Jede Operation erhält change_id, content_id, base_revision, neue revision, operation (upsert/withdraw), payload_hash, actor_id, Zeitstempel und schema_version. Der Hash prüft Inhalt, keine Authentizität. Transport und Zugriff werden separat authentifiziert.

- Vergleich erfolgt anhand der Basisrevision, nicht allein nach Uhrzeit.
- Gleiche change_id wird idempotent verarbeitet: keine doppelten Inhalte oder Medien.
- Konflikte werden sichtbar; niemals automatisch „letzter Schreibzugriff gewinnt“.
- Git-Abgleich bestätigt Commit und übernommene Revision je Inhalt.
- Deployment bestätigt Artefakt und tatsächlich ausgelieferte Revision.
- Eine Überlagerung wird erst entfernt, wenn mindestens ihre Revision ausgeliefert wurde und keine neuere lokale Änderung vorliegt.
- Medien müssen vorhanden und revisionspassend sein, bevor die öffentliche Änderung aktiviert wird.
- Synchronisation bekommt beschränkte Pfade und Rechte; keine Code-/Workflowänderungen aus einem Inhaltsfeed.

## Rücknahmen und Ausfall

Rücknahme ist eine versionierte Operation mit dauerhaftem Rücknahmevermerk (Tombstone). Fällt die Redaktion aus, darf der alte statische Stand zurückgenommene Inhalte nicht erneut zeigen. Dafür braucht das Hosting eine unabhängige Sperre/Entfernung des statischen Artefakts oder eine sofortige bereinigte Veröffentlichung. Ist das nicht möglich, ist das eine Releaseblockade für Inhalte mit verbindlichem Rücknahmebedarf.

Normale Aktualisierungen dürfen bei Ausfall auf den letzten sicheren Stand zurückfallen, sofern das fachlich erlaubt ist. Entwürfe werden nie als Ersatz ausgeliefert. Fehler, leerer Feed und nicht veröffentlicht sind verschiedene Zustände.

Nicht synchronisierte Inhalte, Uploads und notwendige Schlüsselkonfiguration erhalten ein eigenes Backup. Git ersetzt dieses Backup nicht. API-Verträge sind versioniert; inkompatible Änderungen erhalten Migration und Rollbackplan.

## Inhaltsgrenzen

Anfragen, Bewerbungen, Buchungen, Zugangsdaten und persönliche Vorgangsdaten gehören in geeignete Laufzeitspeicher. Eine öffentliche Inhaltsdatei darf keine privaten Kontaktdaten aus Einsendungen übernehmen. Git-Löschung entfernt keine Historie; deshalb vor dem Import klassifizieren.
