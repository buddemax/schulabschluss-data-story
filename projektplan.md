# Projektplan – Data Story „Schulabschluss ist nicht nur Ländersache"

> Stand 2026-06-29 · Abgabe **09.07.2026** (10 Kalendertage) · Scope: **Sauberer Kern** · Tool: **Power BI Desktop** · Build: vollständig & übergabe-bereit · Leitfragen: nur die 9 (S03).
> Nachweistypen (§7c): **A** = ausführbare Assertion · **Q** = Quellenbeleg (Tabelle+URL+Datum) · **B** = begründetes Argument (schwächster, nur wenn A/Q unmöglich).
> Akzeptanzkriterien sind **binär**. Gate öffnet nur bei Zwei-Schlüssel-Abnahme (Soll-Ist-Prüfer + Qualitätsprüfer, je eigener Beleg).

## Scope-Fixierung (aus Check-in 1)
- **Datenkern:** Bundesland 2022/23→2023/24 (`21111-0013`) + Kreis-Drilldown 2023 (`21111-02-06-4`, `21111-01-03-4`, `21121-02-02-4`, `13211-02-05-4`, `12411-02-03-4`).
- **LF1–LF6** voll (Befund + Struktur). **LF7/LF8** auf Landesebene (Bildungsausgaben je Schüler). **LF9** im Kern als Kreis-Risiko aus vorhandenen Größen (Quote ohne HSA + Jugend-ALQ); Einkommen/Wanderung = nice-to-have (nur wenn zeitlich drin, sonst dokumentierte Lücke).
- **Out-of-Scope:** Zensus-DB-Online, BA-API, echte Kreis-Zeitreihen, Lag-Analysen, Zusatzdimensionen (ESK-01/02/03).
- **Priorisierungsrahmen (REQ-096):** Bewertet werden Data-Story 25 % + Dokumentation 30 % = **55 % der Modulnote** → Doku-tragende Phasen (P3-Modelldoku, P4-Abfragen, P7) werden ab P1 mitgeführt und nicht ans Ende geschoben.
- **REQ-004:** Datenbasis ausschließlich offene Daten (Destatis/Regionalstatistik) – verankert in P1-1..P1-6 + Gate 1.

## Zeitplan rückwärts (kritischer Pfad **fett**)
| Tag | Datum | Phase |
|---|---|---|
| Mo | 29.06 | **P0 fertig** · Setup (Umgebung, MCP) · **P1 Beschaffung** |
| Di | 30.06 | **P1 Ende** · **P2 Aufbereitung/DQ** |
| Mi | 01.07 | **P2** |
| Do | 02.07 | **P2 Ende** · **P3 Modell** |
| Fr | 03.07 | **P3 Ende** · **P4 KPIs/DAX** |
| Sa | 04.07 | **P4 Ende** · **P5 Visuals** |
| So | 05.07 | **P5** |
| Mo | 06.07 | **P5 Ende** · **P6 Story/Präsentation** |
| Di | 07.07 | P7 Doku (Finalisierung) · P6 Probe |
| Mi | 08.07 | **Puffer** · Voll-Audit · Generalprobe |
| Do | 09.07 | **Abgabe & Präsentation** |

> **Kritischer Pfad:** Beschaffung → Aufbereitung/DQ → Modell → KPIs → Visuals → Präsentation. **Dokumentation läuft ab P1 mit** (Artefakte sauber mitführen) und wird in P7 finalisiert.

---

## Phase 0 – Materialaufnahme (ABGESCHLOSSEN)
**Inhalt/Ziel:** Quellen erfasst, Pflichtenheft + Anforderungs-Rückgrat angelegt.
- Artefakte: `primaerquelle_praesentation.md`, `aufgabe_und_bewertung.md`, `datenspec.md`, `anforderungen.md` (65 REQ), `traceability.csv`, `anforderungsanalyse.md`, `werkzeuge_skills.md`.
- **Quality Gate 0:** unabhängiger Coverage-Prüfer (FAIL→Fix→Abdeckung vollständig). „P0 fertig" = diese 7 Artefakte vorhanden + Gate-0-Prüfung dokumentiert (A).

## Phase Setup (S) – Umgebung herstellen
**Ziel:** Werkzeugkette einsatzbereit.
- **S-1** Analyseumgebung für die unabhängige Nachrechnung der Referenzwerte einrichten. REQ: Grundlage §7d. *(Irreversibel-leicht → autonom nach Freigabe.)*
- **S-2** Power-BI-Modeling-MCP (`microsoft/powerbi-modeling-mcp`) via Node einrichten + an laufendes Power BI Desktop koppeln. REQ-055/082.
- **S-3** Computer-Use-Zugriff für Power BI Desktop anfordern (erst zu P5).
- **Quality Gate S:** [ ] Nachrechnungs-Umgebung lauffähig (A) · [ ] MCP listet leeres/Test-Modell (A) · [ ] Power BI Desktop startet (A).
- **Risiko:** Store-(MSIX-)Power-BI ↔ MCP-Port-Discovery scheitert → *Gegenmaßnahme:* PBIP-Projektdatei-Modus des MCP statt Live-AS; Fallback Tabular Editor/manuell.

## Phase 1 – Datenbeschaffung & Rohdaten-Inventar
**Inhalt:** Die 6 KERN-Quellen real herunterladen. **Ziel:** vollständiges, belegtes Roh-Inventar.
- **P1-1** Download `21111-0013` (Bundesland) – REQ-020. *(Hinweis: Genesis braucht ggf. Login; Alternative regionalstatistik-Mirror prüfen → bei Sperre Eskalation.)*
- **P1-2** Download `21111-02-06-4` (Kreis-Abschlüsse) – REQ-021.
- **P1-3** Download `21111-01-03-4` (Schulen/Schüler) – REQ-022.
- **P1-4** Download `21121-02-02-4` (berufl. Abschlüsse) – REQ-023.
- **P1-5** Download `13211-02-05-4` + `12411-02-03-4` (Arbeitsmarkt/Bevölkerung) – REQ-024.
- **P1-6** Bildungsausgaben je Schüler (Land) – REQ-025/LF7/LF8 (Destatis Bildungsfinanzen; falls kein stabiler Direktlink → portalbasiert + Eskalationsvermerk).
- **P1-7** Je Download Zeile in `datenquellen_log.md`: Tabellen-ID, URL, Abrufdatum, Größe, Encoding, Zeilen/Spalten, Jahre – REQ-042/050/069/092.
- **P1-8** Portal-Zugänglichkeit/Nützlichkeit bewerten – REQ-068/069.
- **Meilenstein:** alle KERN-CSVs lokal + protokolliert.
- **Quality Gate 1 (binär):**
 - [ ] Jede KERN-Quelle als Datei vorhanden (A: Datei-Existenz + Bytegröße>0)
 - [ ] `datenquellen_log.md` enthält alle Pflichtfelder je Datei (A: Feldprüfung)
 - [ ] Erwartete Jahre je Datei stimmen mit datenspec §2 (A: Jahres-Set-Vergleich)
 - [ ] Encoding je Datei erkannt & dokumentiert (A) – REQ-066
- **Abhängigkeit:** Setup S. **Risiko:** Quelle nicht direkt ladbar (Login/403) → *Gegenmaßnahme:* dokumentierter Mirror (opendata.hessen.de) oder Eskalation; LF7/LF8-Ausgaben als größtes Risiko früh angehen.

## Phase 2 – Datenaufbereitung & Datenqualität
**Inhalt:** Cleaning, Encoding→UTF-8, Missing, Long-Format, DQ-Kennzahlen. **Ziel:** saubere, geprüfte Tabellen + reproduzierbare DQ-Belege (Referenzwert = amtlicher Quellwert).
- **P2-1** Einlesen mit korrektem Encoding; Sonderzeichen `-`/`.`/`x` → Missing – REQ-067/066.
- **P2-2** Breit→Long (`region × jahr × merkmal × wert`) – REQ-051.
- **P2-3** AGS normalisieren, Bundesland-Code aus AGS[0:2]; Stadtstaaten/Berlin sauber – REQ-034/065.
- **P2-4** Schuljahr↔Kalenderjahr-Mapping (`schuljahr`, `abschluss_jahr`) – REQ-035.
- **P2-5** Abschlussart-Mapping allgemeinbildend↔beruflich in `dim_abschluss`-Vorform – REQ-036.
- **P2-6** DQ-Prüfungen mit Assertions: DQ1 Vollständigkeit, DQ2 Σ==Insgesamt, DQ3 Kreis-Aggregat==Land, DQ4 Jahre, DQ5 Gebiets-Stabilität, DQ6 Encoding, DQ7 Sonderzeichen – REQ-061..067.
- **P2-7** `qualitaetskennzahlen.md` + `dq_report` (Tabelle je Check, Pass/Fail, Werte) – REQ-060/073.
- **P2-8** S09-Beispielwerte (SH-Abschlüsse; Arbeitsmarkt Flensburg/Kiel/Lübeck/Neumünster) reproduzieren – REQ-026/027.
- **Meilenstein:** `clean/`-Tabellen + grüner DQ-Report.
- **Quality Gate 2 (binär):** „erklärt" = **dokumentierte Ursache + nicht-leere Beleg-Zeile in `dq_report`** (A: Feld nicht leer); andernfalls Fail.
 - [ ] Alle 7 DQ-Checks als Assertion ausgeführt, Ergebnis (Pass/Fail + Wert) je Check in `dq_report` (A)
 - [ ] DQ2 (Σ Abschlussarten==Insgesamt je Region/Jahr): exakte Gleichheit bei Zählwerten ODER „erklärt" wie oben (A)
 - [ ] DQ3 (Kreis-Aggregat==Land): exakte Gleichheit ODER „erklärt" wie oben (A)
 - [ ] S09-Beispielwerte reproduziert: |Abweichung| ≤ 0,1 %-Pkt (Quoten) bzw. exakt (Zählwerte) ODER „erklärt" (A) – REQ-027
 - [ ] Keine `-`/`.`/`x` als 0 fehlinterpretiert (A)
- **Abhängigkeit:** P1. **Risiko:** Kreis↔Land inkonsistent (Geheimhaltung) → *Gegenmaßnahme:* Missing-Bilanz dokumentieren, nicht glätten.

## Phase 3 – Dimensionale Modellierung (Sternschema S10)
**Inhalt:** Power-BI-Modell mit genau 4 Fakten + 4 Dimensionen. **Ziel:** valides Sternschema, MCP-dokumentiert.
- **P3-1** `dim_region`, `dim_zeit`, `dim_abschluss`, `dim_schulart` anlegen – REQ-034..037.
- **P3-2** Fakten `Abgänge`, `Schule`, `Arbeitsmarkt`, `Ausgaben` laden – REQ-030..033.
- **P3-3** Beziehungen (Stern; Region+Zeit zentral; Abschluss/Schulart an passende Fakten); Geschlecht/Alter als Attribut, nicht eigene Dim (ESK-01 vermeiden); damit Abschlüsse mit Schulstruktur/Arbeitsmarkt/Ausgaben verknüpft – REQ-038/028/003.
- **P3-4** PBIP-Backup unter Versionierung vor erster MCP-Schreiboperation (§5a) – REQ-041.
- **P3-5** MCP-Modelldoku (.md + Mermaid) erzeugen – REQ-052/055.
- **Meilenstein:** lauffähiges `.pbix`/PBIP mit Sternschema.
- **Quality Gate 3 (binär):**
 - [ ] Genau 4 Fakten + 4 Dimensionen, Namen == S10 (A: Modell-Introspektion via MCP)
 - [ ] Keine zusätzlichen Dimensionen ohne Eskalationsvermerk (A) – REQ-028
 - [ ] Alle Beziehungen aktiv & 1:n korrekt orientiert (A)
 - [ ] Datei `dimensionales_schema.md` existiert UND enthält Mermaid-Block mit genau 4 Fakten + 4 Dim (A: Pattern-Match)
 - [ ] `.pbix`/PBIP öffnet ohne Fehler, alle bisherigen Objekte laden (A: Öffnen + Screenshot) – REQ-041
- **Abhängigkeit:** P2 + Setup S2. **Risiko:** MCP-Schreibzugriff/Confirm → *Gegenmaßnahme:* kein `--skipconfirmation`; Backup vorab.

## Phase 4 – KPIs & Analyseabfragen (DAX, verifiziert)
**Inhalt:** Measures je Leitfrage, DAX == Referenzwert. **Ziel:** korrekte, getestete KPIs.
- **P4-1** Measures: Quote ohne (Haupt-)Schulabschluss, Abschlussquoten je Art, Geschlechter-Gap, Kreis-Streuung (LF3), Schulartmix-Anteile (LF5), Ausgaben je Schüler & Effizienz (LF7/8), Kreis-Risiko (LF9) – REQ-010..018/053.
- **P4-2** Je Measure Referenzwert berechnen; Testfall „DAX == Referenzwert" – REQ-093/§7d.
- **P4-3** `analyseabfragen.md` (DAX + Erklärung + Referenzwert je KPI) – REQ-053/056.
- **Meilenstein:** alle KERN-KPIs grün getestet.
- **Quality Gate 4 (binär):**
 - [ ] Jede der 9 Leitfragen hat ≥1 Measure (A)
 - [ ] Jedes Measure: **exakte Gleichheit bei Zählwerten**, **|DAX − Referenzwert| ≤ 0,1 %-Pkt bei Quoten/Anteilen**, je Testfall dokumentiert (A) – REQ-093
 - [ ] Keine verwaisten Measures ohne Leitfrage-Bezug (A)
- **Abhängigkeit:** P3. **Risiko:** Filterkontext-Fehler in DAX → *Gegenmaßnahme:* Referenzwert-Vergleich ist Pflicht-Gate.

## Phase 5 – Visualisierung / Dashboards
**Inhalt:** Report-Seiten je Story-Stufe; Gestaltungsregeln. **Ziel:** je Leitfrage ein klares, korrektes Visual.
- **P5-1** Visual-Spezifikation je Leitfrage (Visualtyp, Felder, Measure, Filter, Kernbotschaft) – REQ-072/057.
- **P5-2** Bau in Power BI Desktop via Computer Use: Ranking-Balken (LF1/LF2), Kreis-Choropleth (LF2/LF3), Streuungs-/Box (LF3), Geschlechter-Vergleich (LF4), Schulartmix-Stacked (LF5), absolut↔relativ-Toggle (LF6), Ausgaben-Treemap/Bar (LF7), Scatter Ausgaben↔Quote (LF8), Risiko-Matrix/Karte (LF9) – REQ-010..018.
- **P5-3** Nach jedem Visual Screenshot → Soll-Ist-Prüfer gegen Spec (richtiges Measure/Achse/Filter) – §5c.
- **P5-4** Gestaltungsregeln (Lerninhalt LI2): klare Kernbotschaft, korrekte Skalen (Null-Linie), keine irreführenden Achsen, barrierearme Farben – REQ-072/081.
- **Meilenstein:** vollständiger Report.
- **Quality Gate 5 (binär):**
 - [ ] Jede Leitfrage hat ≥1 Visual mit korrektem Measure (A: Screenshot vs. Spec)
 - [ ] Achsen-Checkliste alle erfüllt: Y-Achse aller Mengen-Balken startet bei 0; keine abgeschnittenen/doppelten Achsen; Achsentitel+Einheit vorhanden (A je Item)
 - [ ] Farbkontrast WCAG AA: ≥ 4,5:1 für Text, ≥ 3:1 für grafische Elemente, gemessen (A)
 - [ ] Interaktivität (Drilldown Land→Kreis) funktioniert (A: Screenshot) – REQ-002
- **Abhängigkeit:** P4. **Risiko:** GUI-Automation fehleranfällig → *Gegenmaßnahme:* Screenshot-Abgleich je Visual; Spec ist Primärartefakt.

## Phase 6 – Story-Dramaturgie & Präsentation
**Inhalt:** Narrativ entlang INPUT→OUTPUT→ÜBERGANG→ERGEBNIS, 3×5 Min. **Ziel:** überzeugende Präsentation.
- **P6-1** Story-Bogen + Rollenaufteilung (3 Mitglieder) – REQ-006/090.
- **P6-2** Foliensatz (pptx) mit Visuals + Kernaussagen je Leitfrage – REQ-040.
- **P6-3** Kernthese „lokal entschieden" mit Streuungs-/Kreisbefund belegt – REQ-001.
- **Quality Gate 6 (binär):**
 - [ ] Jede der 4 Flow-Stufen im Narrativ vertreten (A: Folien-Checkliste) – REQ-005/006
 - [ ] Alle 9 Leitfragen in der Story beantwortet (A) – REQ-010..018
 - [ ] 3 Sprecherteile à ~5 Min strukturiert (A) – REQ-090
- **Abhängigkeit:** P5. **Risiko:** Zeitüberschreitung → *Gegenmaßnahme:* Probelauf 08.07.

## Phase 7 – Dokumentation (Finalisierung)
**Inhalt:** Pflicht-Doku zusammenführen (ab P1 mitgeführt). **Ziel:** vollständige Abgabe-Doku.
- **P7-1** Format der Datenquellen + Beispiele + Transformationen – REQ-050/051.
- **P7-2** Dimensionales Schema (MCP-Doku + Mermaid) – REQ-052.
- **P7-3** Analyseabfragen (DAX) – REQ-053.
- **P7-4** Tool-Auswertung Power BI: Datenbeschaffung/Modellierung/Abfragesprache/Visualisierung – REQ-054..057.
- **P7-5** Lerninhalte sichtbar: Berichte (LI1), Gestaltungsregeln (LI2), Architektur/Modellierungsmuster (LI3), **Data-Vault-Einordnung** (LI4: warum Stern statt Vault hier), SSBI (LI5) – REQ-080..084.
- **P7-6** Qualitätskennzahlen-Kapitel – REQ-060.
- **P7-7** Moodle-Abgabepaket schnüren – REQ-095.
- **P7-8** Projekt-Chronik dokumentieren: Zwischenpräsentation der Vision (5–10 Min) zum 11.06.2026 als erbrachten Meilenstein vermerken – REQ-094.
- **Quality Gate 7 (binär):**
 - [ ] Jeder Abgabe-Punkt B1/B2/B3a-d vorhanden (A: Checkliste) – REQ-050..057
 - [ ] Alle 5 Lerninhalte mit Fundstelle adressiert (Q) – REQ-080..084
 - [ ] Fixierte Liste der Qualitätsaussagen: jede hat ≥2 Citations (Kriterium+Artefaktstelle) (A: Zählung) – §7b
 - [ ] Zwischenpräsentations-Meilenstein 11.06. dokumentiert (A) – REQ-094
- **Abhängigkeit:** P3–P6.

---

## Schluss-Gate (vor Abgabe 08.07.)
- [ ] **Voll-Audit:** alle Assertions erneut grün (A) – §7i
- [ ] **Traceability-Coverage = 100 %** grün (A) – REQ-093
- [ ] Zwei-Schlüssel-Abnahme je Phase dokumentiert
- [ ] Alle 4 Bewertungsdimensionen (Detailgrad/Ausführung/Visualisierung/Datenaufbereitung) mit Belegen grün – REQ-070..073

## Top-Risiken (projektweit)
| Risiko | Wirkung | Gegenmaßnahme |
|---|---|---|
| Bildungsausgaben (LF7/8) nicht direkt ladbar | LF7/8 schwach | früh in P1; Mirror/portalbasiert; sonst dokumentierte Lücke + Eskalation |
| Store-Power-BI ↔ MCP-Kopplung | Modellbau blockiert | PBIP-Modus; manueller Fallback |
| 10-Tage-Frist | Abgabe gefährdet | Kern-Scope; Doku ab P1 mitführen; Puffer 08.07 |
| GUI-Automation Visuals | Falsche Visuals | Screenshot-Abgleich je Visual gegen Spec |
| Geheimhaltung/Missing in Kreisdaten | DQ3 rot | Missing-Bilanz dokumentieren, nicht glätten |
