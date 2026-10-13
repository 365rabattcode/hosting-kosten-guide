![365Rabattcode — Hosting verstehen. Gesamtkosten vergleichen.](cover.svg)

<div align="center">

### 365RABATTCODE · WISSEN & WERKZEUGE

# Hosting verstehen. Gesamtkosten vergleichen.

**Ein deutscher Leitfaden mit einem kostenlosen, anbieterneutralen Kostenrechner.**

Einführungspreis · Verlängerung · Domains · Zusatzleistungen

[Kostenrechner](#kostenrechner) · [Hosting auswählen](#welches-hosting-passt) · [Checkliste](checkliste.md)

</div>

---

## Wofür dieses Projekt da ist

Ein niedriger Monatspreis beantwortet noch nicht, was eine Website über mehrere Jahre kostet. Dieses Projekt hilft dir, Angebote verschiedener Hosting-Anbieter mit denselben Annahmen zu vergleichen. Der Rechner funktioniert unabhängig von einem Kauf und unabhängig von Affiliate-Links.

Du erhältst einen transparenten Rechenweg, eine technische Entscheidungshilfe und eine Checkliste vor dem Vertragsabschluss. Es werden keine aktuellen Tarifpreise oder funktionierenden Gutscheine behauptet.

## Welches Hosting passt?

| Dein Projekt | Mögliche Lösung | Was du vorher prüfen solltest |
|---|---|---|
| Portfolio oder einfache statische Website | Statisches Hosting | Eigene Domain, HTTPS, Build-Prozess und zulässige Nutzung |
| Blog oder Unternehmensseite mit WordPress | Webhosting / verwaltetes WordPress-Hosting | PHP-Version, Datenbanken, Backups, Wiederherstellung und Ressourcenlimits |
| Anwendung mit eigener Serverkonfiguration | VPS | Betriebssystempflege, Firewall, Monitoring und eigener Administrationsaufwand |
| Mehrere Kundenprojekte | Mehrere getrennte Hosting-Konten oder Agenturlösung | Zugriffstrennung, Übergabe, Backups und Verantwortlichkeiten |
| Größeres Projekt mit Lastspitzen | Passend dimensioniertes verwaltetes Hosting oder Cloud-Lösung | Messbarer Ressourcenbedarf, Skalierungskosten und Ausfallsicherheit |
| Eigene E-Mail-Adressen | Separater E-Mail-Dienst oder enthaltene Postfächer | Speicher, Zustellbarkeit, SPF, DKIM, DMARC und Verlängerungskosten |

Ein VPS ist nicht automatisch die beste Wahl: Die Verantwortung für Updates und Sicherheit kann zusätzliche Zeit und Kosten verursachen. Vergleiche den tatsächlich benötigten Leistungsumfang.

## Kostenrechner

Der mitgelieferte Rechner benötigt Python 3 und keine zusätzlichen Pakete. Alle Eingaben sind deine eigenen Vergleichswerte. Verwende Preise mit derselben Steuerbasis.

```bash
python kostenrechner.py --intro-monat 3 --intro-monate 12 --verlaengerung-monat 9 --horizont-monate 24 --domain-jahr 15 --domain-gratis-jahre 1 --extras-monat 2
```

**Fiktives Rechenbeispiel, kein Angebot eines Anbieters:**

| Kostenpunkt | Rechnung | Betrag |
|---|---|---:|
| Hosting im ersten Jahr | 12 × 3 € | 36 € |
| Hosting im zweiten Jahr | 12 × 9 € | 108 € |
| Domain ab dem zweiten Jahr | 1 × 15 € | 15 € |
| Zusatzleistungen | 24 × 2 € | 48 € |
| **Gesamt über 24 Monate** | | **207 €** |
| **Durchschnitt pro Monat** | 207 € ÷ 24 | **8,63 €** |

Der Vergleichswert verteilt Kosten über den gewählten Zeitraum. Er ist kein Zahlungsplan. Ein Vertrag kann eine längere Vorauszahlung verlangen als dein Vergleichszeitraum. Bei Domains wird jedes angefangene Vertragsjahr als volles Jahr gerechnet. Tatsächliche Abrechnung, Rundung, Steuern und Tarifwechsel können abweichen.

Weitere Optionen: `python kostenrechner.py --help`. Mit `--einmalig` kannst du beispielsweise eine einmalige Einrichtung berücksichtigen.

## Vor dem Kauf: fünf Entscheidungen

1. **Bedarf festlegen:** Websites, Anwendungen, Datenbanken, Speicher und Postfächer aufschreiben.
2. **Vertrag verstehen:** Laufzeit, Vorauszahlung, Kündigung und automatische Verlängerung prüfen.
3. **Folgekosten erfassen:** Verlängerung, Domains, E-Mail, Backups und kostenpflichtige Erweiterungen berücksichtigen.
4. **Technik prüfen:** Dokumentierte Limits, Support, Datenverarbeitung und Wiederherstellungsprozess vergleichen.
5. **Endbetrag kontrollieren:** Der Checkout und die Vertragsbedingungen des Anbieters sind maßgeblich. Ein angezeigter Prozentwert ersetzt keine Gesamtkostenrechnung.

Die ausführliche [Projekt-Checkliste](checkliste.md) kannst du für jeden Anbieter verwenden.

## Hostinger als Anbieter recherchieren

Hostinger ist ein möglicher Anbieter für die oben beschriebenen Anwendungsfälle. Prüfe den konkreten Tarif direkt beim Anbieter; Produktumfang und Bedingungen können sich ändern. Dieses Projekt ist unabhängig und kein offizielles Hostinger-Angebot.

## Hostinger-Links nach Projektbedarf

**Werbung / Affiliate-Links:** Diese sieben Links wurden aus der Hostinger-Storeseite von 365Rabattcode übernommen. Sie verwenden die dort hinterlegten Weiterleitungen über 365rabattcode.de. Bei einem qualifizierten Kauf kann 365Rabattcode eine Provision erhalten. Rabattwirkung, aktuelle Gültigkeit und Provisionszuordnung wurden nicht durch einen Testkauf überprüft. Es wird kein bestimmter Rabatt zugesichert.

### Webhosting

Für Blogs, Portfolios und Unternehmenswebsites. Prüfe Speicher, Datenbanken und Verlängerungskosten.

[![Webhosting ansehen — Werbung / Affiliate-Link](button-webhosting.svg)](https://365rabattcode.de/?cout=57445)

### VPS-Hosting

Für Projekte mit eigener Serverkonfiguration. Plane Administration, Updates und Backups ein.

[![VPS-Hosting ansehen — Werbung / Affiliate-Link](button-vps.svg)](https://365rabattcode.de/?cout=57454)

### Agency-Hosting

Für Agenturen und mehrere Kundenprojekte. Prüfe Zugriffstrennung, Übergabe und Ressourcenlimits.

[![Agency-Hosting ansehen — Werbung / Affiliate-Link](button-agency.svg)](https://365rabattcode.de/?cout=57450)

### Cloud-Hosting

Für Projekte mit höherem Ressourcenbedarf. Vergleiche Leistung, Skalierung und Gesamtkosten.

[![Cloud-Hosting ansehen — Werbung / Affiliate-Link](button-cloud.svg)](https://365rabattcode.de/?cout=57451)

### E-Mail-Lösungen

Für professionelle Postfächer mit eigener Domain. Prüfe Speicher, enthaltene Leistungen und Verlängerung.

[![E-Mail-Lösungen ansehen — Werbung / Affiliate-Link](button-email.svg)](https://365rabattcode.de/?cout=57458)

### Reach E-Mail-Marketing

Für Newsletter und E-Mail-Kampagnen. Prüfe Kontaktlimits, Versandumfang und die benötigten Funktionen.

[![Reach E-Mail-Marketing ansehen — Werbung / Affiliate-Link](button-reach.svg)](https://365rabattcode.de/?cout=57460)

### Business Email

Für geschäftliche E-Mail-Adressen. Vergleiche Postfachgrößen, Teamverwaltung und Abrechnung.

[![Business Email ansehen — Werbung / Affiliate-Link](button-business-email.svg)](https://365rabattcode.de/?cout=57463)

Alle Buttons führen über 365rabattcode.de und können zum Anbieter weiterleiten. Preis, Tarifumfang und Bedingungen des jeweiligen Angebots sind vor dem Kauf zu prüfen. Ein Besuch dieser GitHub-Seite allein löst keine Affiliate-Zuordnung aus.

## Quellen und Transparenz

- [GitHub: Werbung und zulässige Nutzung](https://docs.github.com/en/site-policy/acceptable-use-policies/github-acceptable-use-policies#advertising-on-github)
- [Hostinger: Affiliate-Programm-Bedingungen](https://www.hostinger.com/legal/affiliate-program-agreement)
- [Hostinger: Erstattungsbedingungen](https://www.hostinger.com/legal/refund-policy)

**Stand der Projektredaktion: 13. Oktober 2026.** Das ist kein Nachweis einer Gutscheinprüfung im Checkout. Es wurden keine Testkäufe vorgenommen und keine eigenen Leistungstests von Hostinger behauptet.

## Mitmachen

Verbesserungen am Rechner, nachvollziehbare Korrekturen und zusätzliche technische Checklisten sind willkommen. Bitte keine Affiliate-Links, Werbung oder persönlichen Zugangsdaten in Issues oder Pull Requests veröffentlichen. Konkrete Rabattfragen gehören zum jeweiligen Anbieter beziehungsweise zur Angebotswebsite.

## Herausgeber und Kontakt

365Rabattcode · [Impressum](https://365rabattcode.de/impressum/) · [Datenschutzerklärung der Website](https://365rabattcode.de/datenschutzerklaerung/)

Die Datenschutzerklärung der verlinkten Website ersetzt nicht die [Datenschutzerklärung von GitHub](https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement). Für die Verarbeitung beim Besuch von GitHub gelten auch GitHubs eigene Hinweise.
