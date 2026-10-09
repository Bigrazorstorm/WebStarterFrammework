# Sicherheitskonzept

Vor Implementierung Bedrohungsmodell mit Assets, Rollen, Eintrittspunkten, Vertrauensgrenzen und Missbrauchsfällen erstellen. OWASP ASVS 5.0 dient als versionierter Prüfkatalog; passende Anforderungen und angestrebtes Prüfniveau im Technikentscheid festlegen. Kein pauschales „ASVS-konform“ ohne Nachweis.

## Rollen und Zugriff

Besucher, Mitarbeit, Redaktion, Administration und Synchronisationsdienst getrennt betrachten. Serverseitige Rechte bei jeder Aktion, standardmäßig verweigern. Mitarbeit bearbeitet nur erlaubte Entwürfe; Veröffentlichung ist eigenes Recht. Adminzugänge mit MFA, Wiederherstellung und Widerruf. Keine geteilten Konten.

Cookies für Sitzungen mit Secure, HttpOnly und passendem SameSite; Sessionwechsel nach Anmeldung, Ablauf und Widerruf. CSRF-Schutz bei Cookie-authentifizierten Änderungen. Drosselung gegen parallele Login- und Uploadversuche; keine sensible Kontenauskunft. Setup nur mit einmaliger Berechtigung, niemals offene Administratoranlage.

## Daten und Medien

Schema-/Typ-/Längenvalidierung, kontextgerechte Ausgabe, sichere URL-Protokolle, vorbereitete DB-Abfragen. Markdown ohne ausführbare Templates. Uploads nach tatsächlichem Inhalt prüfen: Typ, Dateigröße, Pixelzahl, sichere Dateinamen und Speicherquote. Kein ausführbarer Upload; Metadaten einschließlich Standort nach festgelegter Medienrichtlinie entfernen. ZIPs gegen Pfadausbruch und Dekompressionsbomben schützen.

Externe Abrufe erhalten erlaubte Ziele/Protokolle, Timeout und Größenlimit; Zugriff auf interne Netze und Umgehungen über Redirects verhindern. Keine beliebigen URL-Abrufe aus Redaktionsfeldern.

## Hosting

Redaktion bevorzugt auf eigener Subdomain mit eng begrenzten Cookies. Private Dateien außerhalb Webroot; Zugriffsschutz zusätzlich testen. HTTPS, passende CSP, nosniff und Frame-Schutz. HSTS erst passend zur Domainstrategie einführen. Private Antworten no-store; Service Worker dürfen weder Redaktion noch private Vorschauen cachen.

Keine Geheimnisse in Git, Artefakten, Logs oder Browsercode. Schlüsselwechsel und Backup notwendiger Schlüssel getrennt dokumentieren. Fehlermeldungen veröffentlichen keine Interna.

## Lieferkette und CI

Abhängigkeiten festlegen, Lockfiles einchecken, Aktualisierungen prüfen. Actions auf vollständige geprüfte SHAs festlegen. Jobs standardmäßig lesend; Deploymentgeheimnisse nur im geschützten Veröffentlichungsjob. Kein untrusted PR-Code mit Produktionsrechten. Kein `pull_request_target` mit Ausführung untrusted Checkout.

Geschützte Hauptbranches, erforderliche Checks und Review für Workflow-/Regeländerungen im Repository konfigurieren. Inhaltssynchronisation darf nur freigegebene Inhaltspfade ändern. Transport via SFTP/SSH oder FTPS mit Zertifikatsprüfung; kein unverschlüsseltes FTP. SSH-Hostschlüssel prüfen.

## Betrieb

Updates, Vorfallmeldung, Zugriffswiderruf und Wiederherstellung haben Verantwortliche. Kritische Schwachstellen blockieren Release, bis behoben oder Funktion sicher deaktiviert ist. Protokolle enthalten Akteur, Aktion, Objekt und Ergebnis, aber keine Tokens oder unnötigen Inhalte. Aufbewahrung begrenzen.
