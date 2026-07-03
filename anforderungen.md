# Anforderungen – Single Source of Truth

> Jede Anforderung mit Quelle (Folien-ID Primärquelle `Sxx`, PDF-Seite Aufgabe `DS-Sxx`, Organisation `ORG-Sx`, Datenrecherche `DR`).
> Quellenregel: Primärquelle (Präsentation) definiert den Scope. `[KERN]` = aus Präsentation/Aufgabe verbindlich. `[ESK]` = Scope-Erweiterung aus Sekundärquelle → Freigabe nötig.
> Status-Legende: offen offen · teilweise in Arbeit · OK verifiziert (mit Nachweis).

## A. Vision & Story (Primärquelle)
| REQ | Anforderung | Quelle | Scope |
|---|---|---|---|
| REQ-001 | Story belegt: Bildungserfolg ist lokal, nicht nur Ländersache (Kernthese) | S02-Vision | KERN |
| REQ-002 | Schulabschlüsse von Bundesland- bis Kreisebene verfolgen | S02-Vision, S08 | KERN |
| REQ-003 | Abschlüsse mit Schulstruktur, Bildungsausgaben, Arbeitsmarkt verknüpfen | S02-Vision | KERN |
| REQ-004 | Datenbasis ausschließlich offene Daten (Destatis/Regionalstatistik) | S02, DS-S42 | KERN |
| REQ-005 | Daten-Flow INPUT→OUTPUT→ÜBERGANG→ERGEBNIS in Modell & Story abbilden | S04–S07 | KERN |
| REQ-006 | Kausalkette INPUT→OUTPUT→ÜBERGANG→ERGEBNIS (Ausgaben/Schulstruktur → Abschlüsse/Abgänge → Berufsschule/Ausbildung → Einkommen) als durchgehendes Story-Narrativ argumentieren | S04–S07 | KERN |

## B. Leitfragen (Primärquelle S03) – jede Leitfrage muss beantwortet & visualisiert sein
| REQ | Leitfrage | Quelle | Scope |
|---|---|---|---|
| REQ-010 | LF1: Welche Bundesländer führen 22/23 & 23/24 bei Abgängern ohne Abschluss? | S03 (Befund) | KERN |
| REQ-011 | LF2: Wo ist der Anteil ohne Hauptschulabschluss am höchsten? | S03 (Befund) | KERN |
| REQ-012 | LF3: Länder- oder Kreisproblem – wie stark streuen die Kreise? | S03 (Befund) | KERN |
| REQ-013 | LF4: Schneiden Jungen und Mädchen unterschiedlich ab? | S03 (Struktur) | KERN |
| REQ-014 | LF5: Wie prägt der Schulartmix die Abschlussverteilung? | S03 (Struktur) | KERN |
| REQ-015 | LF6: Ändert sich die Wertung relativ statt absolut? | S03 (Struktur) | KERN |
| REQ-016 | LF7: Wie verteilen sich die Bildungsausgaben nach Bereich? | S03 (Ökonomisch) | KERN |
| REQ-017 | LF8: Mehr Ausgaben je Schüler → bessere Abschlüsse? | S03 (Ökonomisch) | KERN |
| REQ-018 | LF9: Welche Kreise verbinden Bildungsrisiko, Arbeitslosigkeit & niedriges Einkommen? | S03 (Ökonomisch) | KERN |

## C. Datenquellen (Primärquelle S08)
| REQ | Anforderung | Quelle | Scope |
|---|---|---|---|
| REQ-020 | Abschlüsse allgemeinbildender Schulen (Bundesland, Schuljahr) – `21111-0013` | S08, DR | KERN |
| REQ-021 | Regionale Abschlüsse (Kreis, Schuljahr) – `21111-02-06-4` | S08, DR | KERN |
| REQ-022 | Schulen & Schüler nach Schulart (Kreis, Jahr) – `21111-01-03-4` | S08, DR | KERN |
| REQ-023 | Berufliche Schulabschlüsse (Kreis, Jahr) – `21121-02-02-4` | S08, DR | KERN |
| REQ-024 | Bevölkerung & Arbeitsmarkt (Kreis, Jahr) – `12411-02-03-4`, `13211-02-05-4` | S08, DR | KERN |
| REQ-025 | Ausgaben, Einkommen, Wanderung (Land, Kreis, Jahr) | S08 | KERN (Beschaffung teils ESK) |
| REQ-026 | Beispieldatensätze S09 (Tab. A Abschlüsse SH; Tab. B Arbeitsmarkt Flensburg/Kiel/Lübeck/Neumünster) als reale Belegwerte im Projekt nachweisen | S09 | KERN |
| REQ-027 | S09-Beispielwerte reproduzierbar gegen Rohdaten verifizieren (Plausibilitäts-Check §7d) | S09/§7d | KERN |
| REQ-028 | Datenscope auf die 6 S08-Quellenkategorien begrenzt; weitere Quellen nur via Eskalation | S08 | KERN |
| REQ-069 | Mind. ein Open-Data-Portal (Destatis/Regionalstatistik) systematisch erkunden, Zugänglichkeit/Nützlichkeit dokumentieren | DS-S42 | KERN |

## D. Dimensionales Modell (Primärquelle S10) – verbindliches Sternschema
| REQ | Anforderung | Quelle | Scope |
|---|---|---|---|
| REQ-030 | Fakt **Abgänge** (Abgänge & Abschlüsse) | S10 | KERN |
| REQ-031 | Fakt **Schule** (Schulen, Schulart, Schüler) | S10 | KERN |
| REQ-032 | Fakt **Arbeitsmarkt** (Ausbildungsmarkt, Arbeitslosenquote) | S10 | KERN |
| REQ-033 | Fakt **Ausgaben** (Ausgaben, Einkommen) | S10 | KERN |
| REQ-034 | Dimension **Region** (Bundesland, Kreis, Stadt) | S10 | KERN |
| REQ-035 | Dimension **Zeit** (Schuljahr, Jahr) | S10 | KERN |
| REQ-036 | Dimension **Abschluss** | S10 | KERN |
| REQ-037 | Dimension **Schulart** | S10 | KERN |
| REQ-038 | Beziehungen Stern (Fakten↔Dimensionen über Region+Zeit, Abschluss, Schulart) | S10, DR | KERN |

## E. Abgabe-Bestandteile (Aufgabe DS-S44)
| REQ | Anforderung | Quelle | Scope |
|---|---|---|---|
| REQ-040 | Präsentation: Live-Vorstellung der Data-Story | DS-S44 A1 | KERN |
| REQ-041 | Self-Service-BI-Projekt (lauffähiges Artefakt) | DS-S44 A2 | KERN |
| REQ-042 | Dokumentation der Datenquellen | DS-S44 A3 | KERN |

## F. Dokumentation (Aufgabe DS-S44 B)
| REQ | Anforderung | Quelle | Scope |
|---|---|---|---|
| REQ-050 | Format der Datenquellen + Beispiele | DS-S44 B1 | KERN |
| REQ-051 | Transformationen dokumentiert | DS-S44 B1 | KERN |
| REQ-052 | **Dimensionales Schema** dokumentiert (hervorgehoben) | DS-S44 B2 | KERN |
| REQ-053 | Analyseabfragen dokumentiert | DS-S44 B2 | KERN |
| REQ-054 | Tool-Auswertung: Datenbeschaffung | DS-S44 B3a | KERN |
| REQ-055 | Tool-Auswertung: Modellierung | DS-S44 B3b | KERN |
| REQ-056 | Tool-Auswertung: Abfragesprache | DS-S44 B3c | KERN |
| REQ-057 | Tool-Auswertung: Visualisierung | DS-S44 B3d | KERN |

## G. Datenqualität / Qualitätskennzahlen (Aufgabe DS-S42 + Datenrecherche)
| REQ | Anforderung | Quelle | Scope |
|---|---|---|---|
| REQ-060 | Qualitätskennzahlen berechnen (Pflicht) | DS-S42 | KERN |
| REQ-061 | DQ1 Vollständigkeit (Null-Raten) | DR | KERN |
| REQ-062 | DQ2 Plausibilität (Σ Abschlussarten == Insgesamt) | DR | KERN |
| REQ-063 | DQ3 Konsistenz (Kreis-Aggregat == Bundesland) | DR | KERN |
| REQ-064 | DQ4 Zeitliche Abdeckung dokumentiert | DR | KERN |
| REQ-065 | DQ5 Regionale Stabilität (Gebietsreformen/AGS) | DR | KERN |
| REQ-066 | DQ6 Encoding (Win-1252→UTF-8) geprüft & dokumentiert | DR | KERN |
| REQ-067 | DQ7 Sonderzeichen `-`/`.`/`x` als Missing behandelt | DR | KERN |
| REQ-068 | Bewertung Daten-Portal-Zugänglichkeit/Nützlichkeit | DS-S42 | KERN |

## H. Bewertungsdimensionen (Aufgabe DS-S44) – als Querschnitts-Qualitätsziele
| REQ | Anforderung | Quelle | Scope |
|---|---|---|---|
| REQ-070 | Detailgrad nachweislich hoch | DS-S44 BW1 | KERN |
| REQ-071 | Ausführung sauber/vollständig | DS-S44 BW2 | KERN |
| REQ-072 | Visualisierung exzellent (Gestaltungsregeln) | DS-S44 BW3 | KERN |
| REQ-073 | Datenaufbereitung exzellent | DS-S44 BW4 | KERN |

## I. Lerninhalte sichtbar adressieren (Organisation ORG-S6)
| REQ | Anforderung | Quelle | Scope |
|---|---|---|---|
| REQ-080 | LI1 Berichte & Berichtsgeneratoren | ORG-S6 | KERN |
| REQ-081 | LI2 Gestaltungsregeln (Visualisierung) | ORG-S6 | KERN |
| REQ-082 | LI3 Architekturkonzepte & Modellierungsmuster | ORG-S6 | KERN |
| REQ-083 | LI4 Data-Vault (mind. bewusste Einordnung) | ORG-S6 | KERN |
| REQ-084 | LI5 Self-Service Business Intelligence | ORG-S6 | KERN |

## J. Formalien & Randbedingungen
| REQ | Anforderung | Quelle | Scope |
|---|---|---|---|
| REQ-090 | 3 Teammitglieder, je 5 Min, jedes erzählt einen Teil | DS-S43 | KERN |
| REQ-091 | Termin Abschluss 09.07.2026 eingehalten | DS-S45 | KERN |
| REQ-092 | Nur öffentlich zugängliche Daten | DS-S42 | KERN |
| REQ-093 | Traceability-Coverage 100 % mit reproduzierbaren Nachweisen | Auftrag §9 (intern) | KERN |
| REQ-094 | Zwischenpräsentation der Vision (5–10 Min) zum 11.06.2026 als erbrachten/zu dokumentierenden Meilenstein behandeln | DS-S43/S45 | KERN (vergangen) |
| REQ-095 | Abgabe aller Bestandteile über Moodle | DS-S43/ORG-S5 | KERN |
| REQ-096 | Notengewicht Data-Story 25 % + Doku 30 % = 55 % als Priorisierungsrahmen vermerken | ORG-S5 | KERN |

---

## Eskalations-/Vorschlagspunkte (über Präsentations-Scope hinaus – NICHT ohne Freigabe)
| ID | Inhalt | Quelle | Empfehlung |
|---|---|---|---|
| ESK-01 | Zusätzliche Dimensionen `dim_geschlecht`, `dim_alter`, `dim_investitionsbereich`, `dim_outcome_typ` | DR | Geschlecht/Alter als Attribut statt eigener Dim; Rest weglassen |
| ESK-02 | Ökonomische Vertiefung: Einkommen, Wanderung, Lag-Analysen, Zensus, BA-API | DR (Fragen 4–9,16,17) | Optionaler Story-Teil 2; Beschaffung teils nur interaktiv |
| ESK-03 | Echte Kreis-Zeitreihe Schulabgänge (nur 2023 vorhanden) | DR | Out-of-Scope mangels Daten |
