# Qualität, Veröffentlichung und Betrieb

## Drei Prüfebenen

1. Struktur: IDs, Referenzen, Vollständigkeit und gültige Konfiguration. Der mitgelieferte Prüfer deckt ausschließlich diese Ebene teilweise ab.
2. Produkt: Schemas, Rechte, Komponenten, Barrierefreiheit, Browserabläufe, Performance und SEO. Implementierung folgt nach Stackentscheidung.
3. Betrieb: reale Hostingeinstellungen, Zugriffsschutz, Transport, Wiederherstellung, Rollback und Monitoring.

Fehler blockieren; Warnungen informieren; Ausnahmen sind dokumentierte Entscheidungen mit Verantwortlichem und Ablaufdatum. Sicherheits- und Datenschutzprobleme dürfen nicht pauschal über Ausnahmefelder ignoriert werden.

## Erforderliche Tests

Referenzprojekt anlegen, Medienfehler, Autosave ohne Veröffentlichung, Vorschau, Freigabe, Rücknahme, Wiederherstellung, parallele Bearbeitung, unberechtigter Zugriff, abgelaufene Sitzung, langsame Verbindung und Abbruch.

Für Sofortmodus zusätzlich: Git nicht erreichbar, wiederholter Abgleich, Konflikt, teilweise übernommene Medien, Git-Commit ohne Deployment, fehlgeschlagenes Deployment, neue Bearbeitung während Bestätigung, Rücknahme bei Feed-Ausfall und wiederhergestelltes Backup.

Personas werden mit Testfällen und Regel-IDs verknüpft. Tests gegen echten Datenbestand verwenden anonymisierte/projektgeeignete Daten. Visuelle Vergleichsbilder sind gezielte Nachweise, kein Ersatz für Bedienprüfung.

## Deployment

Prüfen → unveränderliches Artefakt bauen → Freigabe → geschützte Umgebung → Upload → Aktivierung → Smoke-Test → Versionsbestätigung. Codecommit, Datenrevision, Frameworkversion und Artefakt-Prüfsumme festhalten.

Wenn der Hoster atomaren Releasewechsel erlaubt: neues Verzeichnis hochladen und kontrolliert umschalten. Sonst sichere Uploadreihenfolge, Wartungsstrategie und gemischte Versionen explizit behandeln. Geheimnisse und Laufzeitdaten niemals überschreiben. Deploy-Allowlist statt gesamtes Repo veröffentlichen.

Rollback von Code und Daten unterscheiden: eine alte Anwendung kann eine migrierte DB nicht automatisch lesen. Rückwärtskompatibilität oder getesteten Wiederherstellungsplan verlangen. Rücknahmen dürfen durch Rollback nicht rückgängig werden.

## Backup und Monitoring

Projekt setzt RPO (maximal akzeptierter Datenverlust) und RTO (Wiederherstellungszeit). Git, Laufzeit-DB, nicht synchronisierte Änderungen, Medien und Schlüsselkonfiguration separat erfassen. Backups verschlüsseln, Zugriff beschränken und unabhängig speichern. Wiederherstellung in Testumgebung praktisch nachweisen.

Überwachen: Website erreichbar, Redaktion erreichbar, Veröffentlichung erfolgreich, Sync-Rückstand, Backupalter, Speicher und Jobfehler. Ausfall einer externen Quelle darf Kernseiten nicht blockieren. Veraltete Daten sichtbar kennzeichnen oder verbergen gemäß Fachregel.

Kostenbudgets für CI-Minuten, Medien, APIs und Speicher festlegen. Kritische Sicherung darf nicht unbemerkt wegen Kostenlimit ausfallen. Fehlgeschlagene oder pausierte Sicherung wird gemeldet.

## Übergabe

Kurze Redaktionsanleitung, Zuständigkeiten, Zugangswiederherstellung, Updateplan und Incidentkontakt übergeben. Releasebericht in `templates/release.md` ausfüllen. Keine Produktion ohne konkrete Betriebsverantwortung.
