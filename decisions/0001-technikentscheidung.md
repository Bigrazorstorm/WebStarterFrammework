# ADR-001 · Websitegrundlage, CMS und Hosting

Status: offen · Entscheidung vor Gate G1 erforderlich

## Kontext

Statische Betriebswebsite, optionaler ausbaubarer Admin ohne GitHub-Wissen, klassischer Webspace, GitHub-Entwicklung, optional sofortige redaktionelle Überlagerung mit späterem Abgleich.

## Kandidaten

| Kandidat | Zu prüfen |
| --- | --- |
| Astro + Git-basiertes CMS | Login ohne GitHub-Konto, Medien, Rechte, Entwürfe, Erweiterung, Sofortmodus |
| Astro + eigenständige Redaktion | Aufwand, sichere Authentifizierung, Schema-Gleichstand, Hosting und Betrieb |
| Grav / PHP-CMS | vorhandene Modulmöglichkeiten, Updatefähigkeit, statische Ausgabe falls gewünscht, Abgleich und Konflikte |

Keine Entscheidung nur anhand einer Funktionsliste. Kandidaten am durchgängigen mobilen Projektworkflow prüfen.

## Nachweise

Hosterfähigkeiten; mobile Projektpflege; Erweiterung um zweiten Inhaltstyp; Konflikttest; Export/Import ohne Verlust; Zugriffsprüfung; Sofortmodus inklusive Rücknahme; Aufwand und laufende Kosten.

## Entscheidung

Noch offen. Ergebnis, gewählte Versionen, Alternativen, Konsequenzen und Verantwortlichen hier eintragen und `project/site.json` aktualisieren.
