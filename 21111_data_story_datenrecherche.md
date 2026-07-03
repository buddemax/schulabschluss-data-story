# Datenrecherche fuer eine Data Story zu Schulabschluessen

Stand: 04.06.2026

## Ausgangsdaten

Die vorhandene Datei `21111-0013_de.csv` ist die Destatis/GENESIS-Tabelle `21111-0013`: Absolventen und Abgaenger allgemeinbildender Schulen nach Bundesland, Schuljahr, Geschlecht, Schulart und Abschluss. In der lokal vorliegenden Datei sind 16 Bundeslaender, 14 Schularten, 6 Abschlusskategorien und die Schuljahre 2022/23 sowie 2023/24 enthalten.

Staerke: sehr gute Bundesland- und Schulartperspektive.

Schwaeche: keine Kreise, keine Kontextfaktoren, keine direkten Sozial-/Arbeitsmarktvariablen.

## Bessere bzw. granularere Datenquellen

### 1. Regionaldatenbank Deutschland: allgemeinbildende Schulabgaenge auf Kreisebene

Empfohlene Kerntabelle:

- `21111-02-06-4`: Absolvierende/Abgehende allgemeinbildender Schulen nach Geschlecht und Abschlussarten, regionale Tiefe bis Kreise und kreisfreie Staedte.
- Stabile Metadaten/GovData: https://www.govdata.de/suche/daten/absolventen-abganger-allgemeinbildender-schulen-nachgeschlecht-und-abschlussarten-schuljahr-reg?ids=2de020de-1669-47ab-be72-d1e13d53622b
- Stabile Datensatzseite/Mirror: https://opendata.hessen.de/de/dataset/absolventen-abganger-allgemeinbildender-schulen-nachgeschlecht-und-abschlussarten-schuljahr-reg
- Kontext/Einordnung: https://www.bildungsserver.de/onlineressource.html?onlineressourcen_id=12916
- CSV: https://www.regionalstatistik.de/genesisws/downloader/00/tables/21111-02-06-4_00.csv
- Nutzbare Felder: Jahr, AGS/Regionalschluessel, Region, Abschlussart, Geschlecht, Anzahl.
- Granularitaet: Deutschland, Bundeslaender, Regierungsbezirke, Kreise/kreisfreie Staedte.
- Nutzen: ersetzt/ergaenzt die Bundesland-Tabelle fuer Karten und regionale Streuung innerhalb der Bundeslaender.

Wichtiger Unterschied zur Ausgangstabelle: Diese Tabelle hat Kreise und Abschlussarten, aber keine detaillierte Schulart wie Gymnasium G8/G9, Hauptschule usw. Fuer Schulartanalysen bleibt `21111-0013` auf Bundeslandebene relevant.

### 2. Regionaldatenbank Deutschland: Schulen und Schueler nach Schularten

Empfohlene Kontexttabelle:

- `21111-01-03-4`: Schulen, Schuelerinnen und Schueler nach Schularten, Schuljahresbeginn, regionale Tiefe bis Kreise und kreisfreie Staedte.
- Stabile Datensatzseite/Mirror: https://opendata.hessen.de/dataset/schulen-schuler-nach-schularten-stichtag-schuljahresbeginn-regionale-tiefe-kreise-und-krfr-stad
- Kontext/Einordnung: https://statistik.nrw/gesellschaft-und-staat/bildung-und-kultur/schulen
- CSV: https://www.regionalstatistik.de/genesisws/downloader/00/tables/21111-01-03-4_00.csv
- Nutzbare Felder: Jahr, AGS, Region, Schulart, Schulen, Schueler/-innen insgesamt, weiblich, auslaendisch, 7. Klassenstufe, 11. Jahrgangsstufe/Einfuehrungsphase.
- Nutzen: Schulstruktur, Schulartmix, Anteil auslaendischer Schueler/-innen und Groesse der relevanten Jahrgaenge als Erklaerungsvariablen.

### 3. Regionaldatenbank Deutschland: berufliche Schulen

Empfohlene Ergaenzung fuer den Uebergang nach der allgemeinbildenden Schule:

- `21121-02-02-4`: Absolventen/Abgaenger beruflicher Schulen nach Geschlecht und Abschlussarten.
- Stabile Datensatzseite/Mirror: https://opendata.hessen.de/dataset/absolventen-abganger-beruflicher-schulen-nach-geschlecht-undabschlussarten-schuljahr-regionale-
- Metadaten/Beispielportal: https://www.transparenz.bremen.de/daten/absolvierende-abgehende-beruflicher-schulen-nach-geschlecht-und-abschlussarten-schuljahr-regionale-ebenen-274471
- CSV: https://www.regionalstatistik.de/genesisws/downloader/00/tables/21121-02-02-4_00.csv
- Nutzbare Felder: Jahr, AGS, Region, Abschlussart, Geschlecht, Anzahl.
- Nutzen: pruefen, ob Kreise mit schwachen allgemeinbildenden Abschluessen spaeter ueber berufliche Schulen Abschluesse nachholen.

### 4. Regionaldatenbank Deutschland: Bevoelkerung nach Altersgruppen

Empfohlene Denominator-Tabelle:

- `12411-02-03-4`: Bevoelkerung nach Geschlecht und Altersgruppen, Stichtag 31.12., Kreise und kreisfreie Staedte.
- Stabile Datensatzseite/Mirror: https://opendata.hessen.de/de/dataset/bevolkerung-nach-geschlecht-und-altersgruppen-17-stichtag-31-12-regionale-tiefe-kreise-und-krfr
- Metadaten/Synopse: https://opendata.hessen.de/de/dataset/metadata/bevolkerung-nach-geschlecht-und-altersgruppen-17-stichtag-31-12-regionale-tiefe-kreise-und-krfr
- CSV: https://www.regionalstatistik.de/genesisws/downloader/00/tables/12411-02-03-4_00.csv
- Nutzbare Felder: Jahr/Stichtag, AGS, Region, Altersgruppe, Geschlecht, Bevoelkerungsstand.
- Nutzen: Abschlussquoten je Alterskohorte, z. B. ohne Abschluss je 15- bis unter 18-Jaehrige oder je relevante Abschlusskohorte.

### 5. Regionaldatenbank Deutschland: Arbeitslosigkeit und Jugendarbeitslosigkeit

Empfohlene Kontexttabelle:

- `13211-02-05-4`: Arbeitslose nach ausgewaehlten Personengruppen sowie Arbeitslosenquoten, Jahresdurchschnitt, ab 2009.
- Stabile Metadaten/Beispielportal: https://www.transparenz.bremen.de/daten/arbeitslose-nach-ausgewaehlten-personengruppen-sowie-arbeitslosenquoten-jahresdurchschnitt-ab-2009-regionale-tiefe-kreise-und-krfr-staedte-274390
- Kontext/Statistikportal: https://statistik.nrw/wirtschaft-und-umwelt/arbeit/arbeitslose
- CSV: https://www.regionalstatistik.de/genesisws/downloader/00/tables/13211-02-05-4_00.csv
- Nutzbare Felder: Jahr, AGS, Region, Arbeitslose 15 bis unter 20, 15 bis unter 25, Arbeitslosenquote 15 bis unter 25, auslaendische Arbeitslose.
- Nutzen: Zusammenhang zwischen Schulabschlussprofil und regionalem Arbeitsmarktrisiko fuer Jugendliche.

### 6. Bundesagentur fuer Arbeit: Ausbildungsmarkt

Empfohlene Quelle fuer den Uebergang Schule-Beruf:

- Dashboard/API: https://statistik.arbeitsagentur.de/DE/Statischer-Content/Service/API/API-BB.html
- Interaktives Dashboard: https://statistik.arbeitsagentur.de/DE/Navigation/Statistiken/Interaktive-Statistiken/Ausbildungsmarkt/Ausbildungsmarkt-Nav.html
- Beispiel CSV fuer Bayern: https://statistik-dr.arbeitsagentur.de/bifrontend/bids-api/ct/v1/tableFetch/csv/EckwerteTabelleBB?Bundesland=Bayern
- Parameter laut BA: `Bundesland=...`, `Kreis=...`, `Agentur fuer Arbeit=...`, `Arbeitsmarktregion=...`.
- Nutzbare Felder: Bewerber/-innen, Berufsausbildungsstellen, unversorgte Bewerber/-innen, unbesetzte Stellen, Berufe, teils Merkmale wie Schulabschluss.
- Nutzen: zeigt, ob Regionen mit vielen Abgaengen ohne Abschluss auch einen schwierigeren Ausbildungsmarkt haben.

### 7. Regionaldatenbank Deutschland: fruehkindliche Betreuung

Moegliche Langfrist-Kontextvariable:

- `22543-03-01-4`: Betreute Kinder unter 3 Jahren und Betreuungsquoten nach Art der Kindertagesbetreuung.
- Stabile Datensatzseite/Mirror: https://opendata.hessen.de/dataset/betreute-kinder-von-unter-3-jahren-und-betreuungsquoten-nachart-der-kindertagesbetreuung-sticht
- Kontext/Statistikportal: https://www.statistikportal.de/de/kindertagesbetreuung-deutschland
- CSV: https://www.regionalstatistik.de/genesisws/downloader/00/tables/22543-03-01-4_00.csv
- Nutzbare Felder: Stichtag, AGS, Region, Betreuungsart, Altersgruppe, Betreuungsquote, Anteil auslaendische Herkunft mindestens eines Elternteils, Betreuungszeit.
- Nutzen: eher fuer eine explorative Langzeit-Story, z. B. ob fruehkindliche Betreuung und spaetere Abschlussquoten regional zusammenhaengen. Wegen Zeitversatz nur vorsichtig interpretieren.

### 8. Zensus 2022: Bildungsstand, Erwerb, Migration und Haushalts-/Wohnkontext

Empfohlene Kontextquelle:

- Zensusdatenbank: https://ergebnisse.zensus2022.de/datenbank/online
- Destatis-Hinweis zu Bildung und Erwerbstaetigkeit im Zensus 2022: https://www.destatis.de/DE/Presse/Pressemitteilungen/Zensus2022-Pressemitteilungen/PM_zensus2022_50.html
- Beispieltabellen: `2000S-3070` Personen ab 15 Jahren nach ISCED-Bildung, Geschlecht und hoechstem Schulabschluss; `2000S-3071` nach Staatsangehoerigkeit; weitere Tabellen zu Erwerb und Haushalten.
- Regionalebenen: Bund, Laender, Kreise, Gemeinden/Gemeindeverbaende je nach Tabelle.
- Nutzen: Punktuelle Strukturvariablen fuer 2022, z. B. Bildungsstand der Erwachsenen, Erwerbsstatus, Einwanderungsgeschichte, Wohn-/Haushaltsstruktur.

### 9. Kommunale Bildungsdatenbank

Empfohlene Recherchequelle, wenn ihr eine kommunale Bildungsmonitoring-Story bauen wollt:

- Zugang: https://www.bildungsmonitoring.de/bildung/online
- Beschreibung: https://www.bildungsserver.de/onlineressource.html?onlineressourcen_id=50535
- Beschreibung: Daten der Kinder- und Jugendhilfestatistik, Schulstatistik, Berufsbildungsstatistik, Hochschulstatistik und Rahmenbedingungen auf Ebene der Landkreise und kreisfreien Staedte.
- Nutzen: guter thematischer Einstieg und oft passend zugeschnittene Bildungsindikatoren.

### 10. Regionalatlas Deutschland

Empfohlene Visualisierungs-/Validierungsquelle:

- Regionalatlas Deutschland: https://www.statistikportal.de/de/karten/regionalatlas-deutschland
- Bildung und Kultur: https://www.statistikportal.de/de/bildung-und-kultur
- Beispiele: Anteil Schulabgaenger/-innen ohne Hauptschulabschluss, Anteil mit allgemeiner Hochschulreife.
- Nutzen: fertige Indikatoren fuer Karten und Plausibilitaetscheck eigener Berechnungen aus `21111-02-06`.

### 11. Bildungsausgaben als Investitionsinput

Empfohlene Quelle fuer die Wirtschaftlichkeitsfrage:

- Destatis Ausgaben fuer oeffentliche Schulen je Schuelerin und Schueler 2024: https://www.destatis.de/DE/Themen/Gesellschaft-Umwelt/Bildung-Forschung-Kultur/Bildungsfinanzen-Ausbildungsfoerderung/Publikationen/Downloads-Bildungsfinanzen/statistischer-bericht-ausgaben-schueler-5217109247005.html
- Destatis Themenseite Bildungsfinanzen mit GENESIS-Codes, u. a. `21711-0002` und `21711-0010`: https://www.destatis.de/DE/Themen/Gesellschaft-Umwelt/Bildung-Forschung-Kultur/Bildungsfinanzen-Ausbildungsfoerderung/_inhalt.html
- BMFTR Datenportal Tabelle 2.1.13, oeffentliche Bildungsausgaben nach Laendern und Koerperschaftsgruppen: https://www.datenportal.bmftr.bund.de/portal/de/Tabelle-2.1.13.html
- Nutzbare Felder: Bundesland, Jahr, Ausgaben je Schueler/-in, oeffentliche Bildungsausgaben in Mrd. Euro, Koerperschaftsgruppe, Aufgabenbereich.
- Nutzen: Input-Seite fuer ROI-/Effizienzfragen, z. B. Abschlussquote je Bildungs-Euro oder Ausgabenentwicklung vs. spaetere Outcomes.

### 12. Einkommen als wirtschaftliches Outcome

Empfohlene Quelle fuer spaetere Wirkung:

- VGRdL Einkommen auf Kreisebene: https://www.statistikportal.de/de/vgrdl/ergebnisse-kreisebene/einkommen-kreise
- VGRdL Methoden und Informationen: https://www.statistikportal.de/de/vgrdl/methoden-und-informationen
- GovData verfuegbares Einkommen privater Haushalte nach Bundeslaendern und Jahren: https://www.govdata.de/suche/daten/vgr-der-lander-umverteilungsrechnung-verfugbareseinkommen-der-privaten-haushalte-bundeslander-j?ids=e37b439f-1e6a-4fb3-abfe-4afc9e1362e4
- Nutzbare Felder: Bundesland/Kreis, Jahr, verfuegbares Einkommen je Einwohner/-in, Primaereinkommen, Arbeitnehmerentgelt.
- Nutzen: pruefen, ob Regionen mit besseren Abschlussprofilen und/oder hoeheren Bildungsausgaben spaeter hoehere Einkommen erreichen.

### 13. Migration und regionale Bindung der Bildungsinvestition

Empfohlene Kontrollquellen:

- Kreiswanderungsmatrix: https://www.statistikportal.de/de/veroeffentlichungen/kreiswanderungsmatrix
- Destatis Wanderungen nach Bundeslaendern: https://www.destatis.de/DE/Themen/Gesellschaft-Umwelt/Bevoelkerung/Wanderungen/Tabellen/gesamtwanderung_Jahr-01.html
- Statistik.NRW Kontext zu Zu- und Fortzuegen und EVAS 12711: https://statistik.nrw/gesellschaft-und-staat/gebiet-und-bevoelkerung/zu-und-fortzuege
- Nutzbare Felder: Herkunftskreis, Zielkreis, Jahr, Altersgruppe, Geschlecht, Nationalitaet, Wanderungssaldo.
- Nutzen: pruefen, ob Bildungsinvestitionen lokal wirken oder ob die gebildeten Kohorten spaeter abwandern bzw. andere Regionen von Zuzug profitieren.

### 14. Zensus-Regionaltabellen fuer Bildungsstand und Erwerb

Empfohlene Strukturquelle:

- Zensus-Regionaltabellen: https://www.destatis.de/DE/Themen/Gesellschaft-Umwelt/Bevoelkerung/Zensus2022/Publikationen/publikationen-akkordeon-regionaltabellen.html
- Zensusdatenbank: https://ergebnisse.zensus2022.de/datenbank/online
- Nutzbare Felder: hoechster Schul-/Berufsabschluss, Erwerbsstatus, Demografie, Haushalte, Migration/Einwanderungsgeschichte je nach Tabelle.
- Nutzen: Kontrollvariablen fuer Erwachsenenbildungsstand, Erwerbstaetigkeit, Altersstruktur und Haushaltskontext.

## Portal- und Methodiklinks gesammelt

- Destatis-Ausgangstabelle `21111-0013`: https://genesis.destatis.de/datenbank/online/statistic/21111/table/21111-0013
- Destatis-Bildungsindikator Absolventen/Abgaenger: https://www.destatis.de/DE/Themen/Gesellschaft-Umwelt/Bildung-Forschung-Kultur/Bildungsindikatoren/absolventen.html
- Hinweis: Regionaldatenbank-Tabellen wie `21111-02-06-4` muessen ueber `regionalstatistik.de` aufgerufen werden, nicht ueber `genesis.destatis.de`. Fuer Quellenangaben nennen wir Portal-/Tabellenseite und, fuer Power BI, den stabilen `genesisws/downloader`-Direktdownload.
- Statistikportal Open Data: https://www.statistikportal.de/de/open-data
- Destatis Regio-Stat-Katalog: https://www.destatis.de/DE/Themen/Laender-Regionen/Regionales/Publikationen/regiostatkatalog-artikel.html
- Statistik.NRW Schulen mit Regionaldatenbank-/EVAS-Kontext: https://statistik.nrw/gesellschaft-und-staat/bildung-und-kultur/schulen
- Deutscher Bildungsserver zur Regionaldatenbank/Schulstatistik: https://www.bildungsserver.de/onlineressource.html?onlineressourcen_id=12916
- Bundesagentur fuer Arbeit, Ausbildungsmarkt-Dashboard: https://statistik.arbeitsagentur.de/DE/Navigation/Statistiken/Interaktive-Statistiken/Ausbildungsmarkt/Ausbildungsmarkt-Nav.html
- Bundesagentur fuer Arbeit, Ausbildungsmarkt-API: https://statistik.arbeitsagentur.de/DE/Statischer-Content/Service/API/API-BB.html
- Zensusdatenbank 2022: https://ergebnisse.zensus2022.de/datenbank/online
- Kommunale Bildungsdatenbank: https://www.bildungsmonitoring.de/bildung/online
- Statistikportal Bildung und Kultur/Regionalatlas: https://www.statistikportal.de/de/bildung-und-kultur
- Destatis Ausgaben je Schueler/-in: https://www.destatis.de/DE/Themen/Gesellschaft-Umwelt/Bildung-Forschung-Kultur/Bildungsfinanzen-Ausbildungsfoerderung/Publikationen/Downloads-Bildungsfinanzen/statistischer-bericht-ausgaben-schueler-5217109247005.html
- Destatis Bildungsfinanzen: https://www.destatis.de/DE/Themen/Gesellschaft-Umwelt/Bildung-Forschung-Kultur/Bildungsfinanzen-Ausbildungsfoerderung/_inhalt.html
- BMFTR Bildungsausgaben nach Laendern: https://www.datenportal.bmftr.bund.de/portal/de/Tabelle-2.1.13.html
- VGRdL Einkommen auf Kreisebene: https://www.statistikportal.de/de/vgrdl/ergebnisse-kreisebene/einkommen-kreise
- VGRdL Methoden: https://www.statistikportal.de/de/vgrdl/methoden-und-informationen
- Kreiswanderungsmatrix: https://www.statistikportal.de/de/veroeffentlichungen/kreiswanderungsmatrix
- Zensus-Regionaltabellen: https://www.destatis.de/DE/Themen/Gesellschaft-Umwelt/Bevoelkerung/Zensus2022/Publikationen/publikationen-akkordeon-regionaltabellen.html

## Empfohlenes Datenmodell

## Zeitliche Abdeckung im aktuellen Datenstand

Wichtig: Die folgende Abdeckung bezieht sich auf die aktuell heruntergeladenen Direktdownloads bzw. die lokal vorliegende Ausgangsdatei, nicht zwingend auf alles, was theoretisch ueber eine registrierte GENESIS-/Regionaldatenbank-Abfrage rekonstruierbar waere.

| Quelle | Tabelle | Im aktuellen Datenstand enthaltene Jahre | Anzahl Jahre | Story-Konsequenz |
|---|---:|---:|---:|---|
| Destatis-Ausgangstabelle | `21111-0013` | Schuljahre `2022/23`, `2023/24` | 2 | Bundeslandvergleich ueber zwei Schuljahre moeglich. |
| Allgemeinbildende Schulabgaenge, Kreise | `21111-02-06-4` | `2023` | 1 | Lokale Hotspots/Kreisvergleich moeglich, aber keine echte Kreis-Zeitreihe im aktuellen Download. |
| Schulen und Schueler, Kreise | `21111-01-03-4` | `2023` | 1 | Kontextjoin zur Schulstruktur fuer 2023 moeglich. |
| Berufliche Schulabgaenge, Kreise | `21121-02-02-4` | `2023` | 1 | Zweite-Chance-/Uebergangsperspektive fuer 2023 moeglich. |
| Bevoelkerung nach Altersgruppen, Kreise | `12411-02-03-4` | `1995` bis `2024` | 30 | Sehr gute Zeitreihe fuer Nenner, Alterskohorten und demografischen Kontext. |
| Arbeitsmarkt/Arbeitslosenquoten, Kreise | `13211-02-05-4` | `2025` | 1 | Im aktuellen Download nur aktueller Arbeitsmarkt-Kontext; die Tabellenbeschreibung nennt aber Jahresdurchschnittsdaten ab 2009. |

Fuer eine starke Data Story ist damit der sauberste Kern: Bundeslandentwicklung 2022/23 bis 2023/24 plus lokaler Drilldown fuer 2023. Eine echte mehrjaehrige Kreis-Zeitreihe fuer Schulabgaenge muesste separat ueber eine parameterisierte GENESIS-/Regionaldatenbank-Abfrage oder eine weitere stabile Datenquelle nachgezogen werden.

### Faktenmodell

| Faktentabelle | Grain | Wichtige Metriken | Quelle | Join |
|---|---|---|---|---|
| `fact_abgaenge_allgemeinbildend` | Region x Jahr x Geschlecht x Abschluss | Abgaenge insgesamt, ohne HSA, HSA, mittlerer Abschluss, FHR, Abitur | `21111-02-06-4`, plus Bundeslandtabelle `21111-0013` | `ags`, `bundesland_code`, Abschlussjahr/Schuljahr |
| `fact_schueler_schulen` | Region x Jahr x Schulart | Schueler/-innen, Schulen, auslaendische Schueler/-innen, Klasse 7, Jahrgang 11 | `21111-01-03-4` | `ags` + Jahr; Schulart ueber `dim_schulart` |
| `fact_abgaenge_beruflich` | Region x Jahr x Geschlecht x Abschluss | nachgeholte/erworbene Abschluesse an beruflichen Schulen | `21121-02-02-4` | `ags` + Jahr + Abschluss |
| `fact_arbeitsmarkt` | Region x Jahr | Jugend-ALQ 15-25, Arbeitslose 15-25, auslaendische Arbeitslose | `13211-02-05-4`, BA-Ausbildungsmarkt | `ags` + Jahr, optional Lag zum Abschlussjahr |
| `fact_bevoelkerung` | Region x Stichtag x Altersgruppe x Geschlecht | Bevoelkerung, Alterskohorte, Nenner fuer Quoten | `12411-02-03-4` | `ags` + Stichtag/Jahr + Altersgruppe |
| `fact_bildungsausgaben_land` | Bundesland x Jahr x Aufgabenbereich x Koerperschaftsgruppe | Ausgaben je Schueler/-in, Grundmittel, Ausgabenwachstum, Anteil am Haushalt | Destatis/BMFTR Bildungsfinanzen | `bundesland_code` + Jahr; als Landesinput an lokale Outcomes anhaengen |
| `fact_einkommen_region` | Bundesland/Kreis x Jahr | verfuegbares Einkommen je Einwohner/-in, Primaereinkommen, Arbeitnehmerentgelt | VGRdL | `ags` oder `bundesland_code` + Jahr; mit Lag zu Bildung |
| `fact_wanderungen_region` | Herkunftsregion x Zielregion x Jahr x Altersgruppe | Zuzuege, Fortzuege, Wanderungssaldo, Saldo junge Erwachsene | Kreiswanderungsmatrix / Wanderungsstatistik | Herkunfts-AGS, Ziel-AGS, Jahr, Altersgruppe |
| `fact_zensus_struktur` | Region x Stichtag x Merkmal | Erwachsenenbildungsstand, Erwerbsstatus, Haushalts- und Demografiemerkmale | Zensus 2022 Regionaltabellen | `ags` + Stichtag + Merkmal |

### Dimensionen

| Dimension | Inhalt | Warum sie wichtig ist |
|---|---|---|
| `dim_region` | AGS, Name, Bundesland, Regionsebene, Kreistyp, Stadt/Land, Ost/West | Zentraler Join ueber alle regionalen Fakten; loest Bundesland-zu-Kreis-Rollups. |
| `dim_zeit` | Kalenderjahr, Schuljahr, Stichtag, Abschlussjahr, Lag-Jahr | Verbindet Schuljahrlogik mit Kalenderjahrdaten und wirtschaftlichen Verzoegerungen. |
| `dim_abschluss` | standardisierte Abschlussarten und Mapping zwischen Tabellen | Macht allgemeinbildende und berufliche Abschluesse vergleichbar. |
| `dim_schulart` | Gymnasium, Foerder-, Haupt-, Real-, Gesamt-/andere Schularten | Kontrolliert Strukturunterschiede, damit Effizienzvergleiche fairer werden. |
| `dim_geschlecht` | maennlich, weiblich, insgesamt | Ermoeglicht Zielgruppen- und Gap-Analysen. |
| `dim_alter` | Altersgruppen, besonders 15-18 und 18-30 | Wichtig fuer Nenner, Wanderung junger Erwachsener und Uebergang in Arbeit/Ausbildung. |
| `dim_investitionsbereich` | Kita, allgemeinbildende Schulen, berufliche Schulen, Hochschule, sonstige Bildung | Verhindert, dass alle Bildungsausgaben pauschal den Schulabschluessen zugerechnet werden. |
| `dim_outcome_typ` | Abschluss, Uebergang, Arbeitsmarkt, Einkommen, Migration | Ordnet kurzfristige Outputs und spaetere wirtschaftliche Outcomes sauber. |

Join-Keys:

- Primaer: `AGS`/Regionalschluessel + Jahr/Stichtag.
- Bundesland-Aggregation: aus AGS ableiten, z. B. erste zwei Stellen.
- Zeit-Mapping pruefen: Regionaldaten nutzen oft ein Kalender-/Abgangsjahr; die Destatis-Tabelle `21111-0013` nutzt Schuljahr-Labels wie `2023/24`. Fuer die Modellierung sauber dokumentieren, ob `2023` dem Schuljahr `2022/23` bzw. Abschlussjahr 2023 entspricht.
- Lag-Mapping fuer Wirtschaftlichkeit: Bildungsausgaben und Abschlussprofile muessen zeitversetzt gegen spaetere Arbeitsmarkt-/Einkommenswerte gelesen werden, z. B. Input Jahr t oder t-3 gegen Outcome t+3 bis t+10.
- Migration/Pendeln: Regionale Outcomes nicht nur am Schulort interpretieren. Wanderungssaldo junger Erwachsener und ggf. Pendlerdaten als Kontrollvariablen aufnehmen.

### Zusammenbau der Quellen

1. `dim_region` bauen: alle AGS normalisieren, Bundesland-Code aus den ersten zwei Stellen ableiten, Regionsebene markieren, Berliner Bezirke und Stadtstaaten sauber behandeln.
2. Tabellen in lange Fakten ueberfuehren: breite CSVs mit Spalten fuer Abschlussarten/Geschlecht in eine saubere Struktur `region x jahr x merkmal x wert` bringen.
3. Abschlussarten mappen: `Ohne Ersten Schulabschluss` aus `21111-0013` mit `ohne Hauptschulabschluss` aus `21111-02-06-4` in `dim_abschluss` zusammenfuehren und die Unterschiede dokumentieren.
4. Schuljahre auf Kalenderjahre mappen: `2023/24` nicht blind mit `2023` gleichsetzen; fuer Abschlussdaten ein Feld `abschluss_jahr` und ein Feld `schuljahr` fuehren.
5. Bildungsausgaben nur auf korrekter Ebene joinen: Landesausgaben per `bundesland_code + jahr` an Kreise anhaengen, aber als `input_grain = Bundesland` markieren.
6. Wirtschafts-Lags bilden: `input_jahr`, `abschluss_jahr`, `outcome_jahr` getrennt speichern, z. B. Ausgaben 2018-2021 gegen Abschluesse 2023 und Einkommen 2025+.
7. Kontrollen hinzufuegen: Altersstruktur, Schulartmix, Foerderschueleranteil, auslaendische Schueler/-innen, Zensus-Erwachsenenbildung, Migration und Arbeitsmarkt.
8. KPIs berechnen: Quote ohne HSA, Abschlussleistung je 1.000 Euro, Jugend-ALQ, verfuegbares Einkommen, Wanderungssaldo junger Erwachsener, Risiko-/Ausreisser-Score.
9. Sensitivitaet pruefen: Ergebnisse einmal mit und ohne Stadtstaaten, mit und ohne Migration sowie mit verschiedenen Lag-Fenstern rechnen.

## Konkrete Operationalisierung der wirtschaftlichen Fragen

| Frage | Kennzahl / Rechnung | Quelle und Join | Lesart und Grenze |
|---|---|---|---|
| Bringen hoehere Bildungsausgaben bessere Abschluesse? | Ausgaben je Schueler/-in vs. Quote ohne HSA, mittlerer Abschluss, Abiturquote; optional Lag t-3 bis t-10 | `fact_bildungsausgaben_land` per Bundesland + Jahr an `fact_abgaenge_allgemeinbildend` | Nur Bundeslandebene belastbar; mehr Geld kann auch Strukturkosten oder Besoldung abbilden. |
| Wo ist viel Input, aber schwacher Output? | Output-Luecke = erwartete Abschlussquote bei aehnlichem Strukturmix minus beobachtete Abschlussquote | Bildungsausgaben + Schulstruktur + Abschlussdaten | Effizienzsignal, kein Schuldnachweis; Sozialstruktur und Migration kontrollieren. |
| Welche Region erzielt die beste Leistung je Euro? | Abschlussleistung je 1.000 Euro oder vermiedene Quote ohne HSA pro 1.000 Euro | Landesausgaben an Kreiswerte ueber Bundesland-Code anhaengen | Kreiswerte sind lokale Outcomes, nicht lokale Budgetwerte. |
| Senken Investitionen spaeter Jugendarbeitslosigkeit? | Jugend-ALQ 15-25 in Jahr t+n vs. Abschluss-/Ausgabenprofil in Jahr t | Arbeitsmarkt + Abschlussdaten per AGS; Ausgaben per Bundesland | Branchenstruktur, Konjunktur, Pendeln und Ausbildungsplaetze kontrollieren. |
| Steigern bessere Abschluesse spaeter Einkommen? | verfuegbares Einkommen je Einwohner/-in oder Arbeitnehmerentgelt vs. Abschlussprofil frueherer Kohorten | VGRdL Einkommen per AGS/Bundesland + Jahr, mit Lag | Schulort und spaeterer Wohn-/Arbeitsort koennen auseinanderfallen. |
| Verliert eine Region Bildungsinvestitionen durch Abwanderung? | Wanderungssaldo 18-30, Fortzuege junger Erwachsener | Kreiswanderungsmatrix/Wanderungsstatistik per AGS + Jahr | Wanderung zeigt Bewegung, aber nicht direkt individuellen Bildungsabschluss. |
| Profitiert eine Region durch Zuzug gut ausgebildeter Personen? | Zuzug 18-30, Zensus-Anteil hoher Bildungsabschluesse, Einkommensniveau | Wanderung + Zensus + VGRdL | Hohe Einkommen koennen importierte Qualifikation spiegeln. |
| Welche Kreise sind wirtschaftliche Risikoregionen? | Score aus hoher Quote ohne HSA, hoher Jugend-ALQ, niedrigem Einkommen, negativem Wanderungssaldo | Abschlussdaten + Arbeitsmarkt + Einkommen + Wanderung | Score transparent gewichten und Sensitivitaet zeigen. |
| Welche Regionen sind positive Ausreisser? | niedrige Quote ohne HSA und gute Outcomes trotz schwieriger Strukturindikatoren | Residualanalyse nach Schulstruktur, Altersstruktur, Migration und Arbeitsmarkt | Kandidaten fuer Fallstudien, keine automatischen Best-Practice-Beweise. |
| Welche Ausgabenbereiche sind relevant? | Anteile fuer allgemeinbildende Schulen, berufliche Bildung, Kita, Hochschule; Entwicklung ueber Jahre | Destatis/BMFTR nach Aufgabenbereich und Koerperschaftsgruppe | Nicht alle Bildungsausgaben wirken direkt auf Schulabschlussquoten. |

## Datenqualitaet, die ihr messen solltet

- Vollstaendigkeit: Anteil fehlender Werte je Tabelle, Jahr, Bundesland und Kreis.
- Plausibilitaet: Summe der Abschlussarten gegen `Insgesamt` je Region/Jahr.
- Konsistenz: Kreiswerte zu Bundeslandwerten aggregieren und mit Bundeslandzeilen bzw. `21111-0013` vergleichen.
- Zeitliche Abdeckung: Welche Jahre sind je Quelle vorhanden?
- Regionale Stabilitaet: Gebietsreformen und AGS-Aenderungen dokumentieren.
- Zeichen/Encoding: Regionalstatistik-CSV ggf. mit Windows-1252/ISO-8859-1 pruefen.
- Geheimhaltung/Sonderzeichen: `-`, `.`, `x` als eigene Missing-/Nicht-zutreffend-Kategorien behandeln.

## Analysefragen fuer die Data Story

1. Wirtschaft: Steigen Bundeslaender mit hoeheren Ausgaben je Schueler/-in auch bei Abschlussquoten, Uebergangsindikatoren oder Abituranteilen besser aus?
2. Wirtschaft: Wo ist die Quote ohne Hauptschulabschluss trotz hoher Bildungsausgaben weiterhin hoch, also wo ist die Output-Wirkung schwach?
3. Wirtschaft: Welche Laender oder Kreise erzielen bei aehnlicher Schulstruktur die beste Abschlussleistung je eingesetztem Bildungs-Euro?
4. Wirtschaft: Haengen hoehere Bildungsausgaben zeitverzoegert mit niedrigerer Jugendarbeitslosigkeit zusammen?
5. Wirtschaft: Erhoehen bessere Abschlussprofile in einer Region spaeter das verfuegbare Einkommen je Einwohner/-in oder das Arbeitnehmerentgelt?
6. Wirtschaft: Wie veraendert Migration die Interpretation: wandern gut qualifizierte junge Menschen nach dem Schulabschluss ab oder zu?
7. Wirtschaft: Welche Regionen verlieren Bildungsinvestitionen durch Abwanderung junger Erwachsener, und welche profitieren durch Zuzug?
8. Wirtschaft: Gibt es Kreise mit hohem Bildungsrisiko, hoher Jugendarbeitslosigkeit und niedrigem Einkommen als kumulierte wirtschaftliche Risikoregionen?
9. Wirtschaft: Wo sind positive Ausreisser: niedrige Quote ohne Abschluss, gute Arbeitsmarktwerte und solides Einkommen trotz begrenzter Ressourcen?
10. Wirtschaft: Wie stark unterscheiden sich oeffentliche Bildungsausgaben nach Aufgabenbereich, z. B. Schule, berufliche Bildung, Kita oder Hochschule?
11. Welche Bundeslaender haben 2022/23 und 2023/24 den hoechsten Anteil an Abgaenger/-innen ohne ersten Schulabschluss?
12. In welchen Kreisen ist der Anteil ohne Hauptschulabschluss besonders hoch, und liegen diese Kreise konzentriert in bestimmten Bundeslaendern?
13. Wie stark unterscheiden sich die Kreise innerhalb desselben Bundeslandes, also ist das Problem eher ein Bundesland- oder ein lokales Kreisproblem?
14. Gibt es ein Geschlechtergefaelle bei Abschlussarten, besonders bei "ohne Hauptschulabschluss" und "allgemeine Hochschulreife"?
15. Welche Rolle spielt der Schulartmix eines Kreises, z. B. Anteil Gymnasien, Gesamtschulen oder Foerderschulen, fuer die Abschlussverteilung?
16. Haengen hohe Anteile auslaendischer Schueler/-innen regional mit bestimmten Abschlussprofilen zusammen, und wie stark veraendert sich das Bild, wenn man nach Bundesland kontrolliert?
17. Kompensieren berufliche Schulen schwache allgemeinbildende Abschluesse, indem in denselben Kreisen spaeter mittlere Abschluesse oder Fachhochschulreife erworben werden?
18. Wie veraendert sich die Bewertung der Bundeslaender, wenn man nicht absolute Zahlen, sondern Abschlussquoten pro relevanter Alterskohorte betrachtet?

## Story-Vorschlag

Arbeitstitel: "Schulabschluss ist nicht nur Laendersache: Wo Bildungsrisiken lokal sichtbar werden"

Moegliche Dramaturgie:

1. Einstieg mit Bundeslandvergleich aus `21111-0013`.
2. Aufbrechen des Durchschnitts: Kreiskarte aus `21111-02-06-4`.
3. Investitionsebene: Bildungsausgaben je Schueler/-in und oeffentliche Bildungsausgaben nach Land.
4. Erklaerungsebene: Schulartmix, Schuelerstruktur, Alterskohorte und Zensus-Kontext.
5. Folgenebene: berufliche Schulen, Ausbildungsmarkt, Jugendarbeitslosigkeit, Einkommen und Migration.
6. Fazit: Bundeslandpolitik ist wichtig, aber die wirtschaftliche Wirkung haengt davon ab, ob Bildungsinvestitionen lokal in Abschluesse, Uebergaenge und Einkommen uebersetzt werden.
