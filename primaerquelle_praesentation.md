# Primärquelle – Präsentation „Schulabschluss ist nicht nur Ländersache"

> **Status:** Maßgebliches Pflichtenheft (Quellenhierarchie Stufe 1, 100 %).
> Bei jedem Konflikt mit anderen Quellen **gewinnt diese Präsentation**.
> Quelle: `Schulabschluss ist nicht nur Ländersache (1).pdf` (11 Folien), Autoren: Max Budde, John Kanto & Aaron Ziegler, HTW Berlin.
> Konvertiert Folie-für-Folie, verlustfrei. Jede Folie hat eine stabile ID.

---

## S01-Titel
**Titel:** Schulabschluss ist nicht nur Ländersache
**Autoren:** Max Budde, John Kanto & Aaron Ziegler
**Institution:** HTW Berlin – Hochschule für Technik und Wirtschaft Berlin (University of Applied Sciences)

---

## S02-Vision
**Überschrift:** VISION

> „Bildungserfolg in Deutschland ist kein reines Länderphänomen. Er wird lokal entschieden. Mit offenen Daten von Destatis und der Regionalstatistik verfolgen wir Schulabschlüsse von der Bundesland- bis auf die Kreisebene und verknüpfen sie mit Schulstruktur, Bildungsausgaben und Arbeitsmarkt."

**Verbindliche Aussagen:**
- Bildungserfolg wird **lokal** (nicht nur auf Länderebene) entschieden.
- Datenbasis: **offene Daten von Destatis und Regionalstatistik**.
- Granularität: **Bundesland- bis Kreisebene**.
- Verknüpfungsdimensionen: **Schulstruktur, Bildungsausgaben, Arbeitsmarkt**.

---

## S03-Leitfragen
**Überschrift:** LEITFRAGEN – gegliedert in drei Blöcke.

### Block „DER BEFUND"
- LF1: Welche Bundesländer führen 22/23 und 23/24 bei Abgängern **ohne Abschluss**?
- LF2: Wo ist der Anteil **ohne Hauptschulabschluss** am höchsten?
- LF3: Länder- oder Kreisproblem: Wie stark **streuen die Kreise**?

### Block „DIE STRUKTUR"
- LF4: Schneiden **Jungen und Mädchen** unterschiedlich ab?
- LF5: Wie prägt der **Schulartmix** die Abschlussverteilung?
- LF6: Ändert sich die Wertung, wenn man **relativ statt absolut** zählt?

### Block „DAS ÖKONOMISCHE"
- LF7: Wie verteilen sich die **Bildungsausgaben nach Bereich**?
- LF8: **Mehr Ausgaben je Schüler, bessere Abschlüsse**?
- LF9: Welche Kreise verbinden **Bildungsrisiko, Arbeitslosigkeit und niedriges Einkommen**?

---

## S04-Dateninhalt-Input
**Überschrift:** DATENINHALT – Schrittweiser Aufbau eines Fluss-Diagramms.
**Knoten 1 – INPUT:** AUSGABEN, SCHULSTRUKTUR

## S05-Dateninhalt-Output
**Fluss:** INPUT → **OUTPUT**
**Knoten 2 – OUTPUT:** ABSCHLÜSSE, ABGÄNGE
(Pfeil von INPUT nach OUTPUT)

## S06-Dateninhalt-Uebergang
**Fluss:** INPUT → OUTPUT → **ÜBERGANG**
**Knoten 3 – ÜBERGANG:** BERUFSSCHULE, AUSBILDUNG
(Pfeil von OUTPUT nach ÜBERGANG)

## S07-Dateninhalt-Ergebnis
**Fluss vollständig:** INPUT → OUTPUT → ÜBERGANG → **ERGEBNIS**
**Knoten 4 – ERGEBNIS:** EINKOMMEN, … (auf der Folie abgeschnitten/unvollständig; im Daten-Flow am Ende „Einkommen" als Ergebnisgröße; vgl. S08 „Einkommen, Wanderung")

> **Verbindlicher Daten-Flow (Kausalkette der Story):**
> INPUT (Ausgaben, Schulstruktur) → OUTPUT (Abschlüsse, Abgänge) → ÜBERGANG (Berufsschule, Ausbildung) → ERGEBNIS (Einkommen).

---

## S08-Datenquellen
**Überschrift:** DATEN – Tabelle Datenquelle × Ebene.

| Datenquelle | Ebene |
|---|---|
| Abschlüsse allgemeinbildender Schulen | Bundesland, Schuljahr |
| Regionale Abschlüsse | Kreis, Schuljahr |
| Schulen und Schüler nach Schulart | Kreis, Jahr |
| Berufliche Schulabschlüsse | Kreis, Jahr |
| Bevölkerung und Arbeitsmarkt | Kreis, Jahr |
| Ausgaben, Einkommen, Wanderung | Land, Kreis, Jahr |

> **Verbindlich:** Genau diese 6 Datenquellen-Kategorien auf den genannten Ebenen definieren den Datenscope.

---

## S09-Datensaetze-Beispiele
**Überschrift:** DATENSÄTZE – zwei Beispieltabellen (Belege für reale Datenwerte).

**Tabelle A – Abschlüsse Schleswig-Holstein (Beispiel):**
| Bundesland | Abschluss | Anzahl | Anteil |
|---|---|---|---|
| Schleswig-Holstein | Ohne Ersten Schulabschluss | 7.531 | 7,4 % |
| Schleswig-Holstein | Erster Schulabschluss | 16.207 | 15,9 % |
| Schleswig-Holstein | Mittlerer Schulabschluss | 48.966 | 48,1 % |
| Schleswig-Holstein | Fachhochschulreife | 367 | 0,4 % |

**Tabelle B – Arbeitsmarkt nach Region (Beispiel):**
| Region | Jugend-ALQ | Arbeitslose 15–25 | Bev. 15–20 |
|---|---|---|---|
| Flensburg | 6,7 % | 492 | 4560 |
| Kiel | 6,0 % | 1091 | 11354 |
| Lübeck | 7,6 % | 982 | 9873 |
| Neumünster | 8,5 % | 430 | 4108 |

> Diese Beispielwerte sind im Reproduktions-/Plausibilitäts-Check (§7d) gegen die Rohdaten zu verifizieren.

---

## S10-Dimensionales-Modell
**Überschrift:** DATEN – verbindliches dimensionales Schema (Sternschema).

**Faktentabellen (4):**
| Tabelle (Typ) | Inhalt |
|---|---|
| Abgänge (Fakt) | Abgänge und Abschlüsse |
| Schule (Fakt) | Schulen, Schulart, Schüler |
| Arbeitsmarkt (Fakt) | Ausbildungsmarkt, Arbeitslosenquote |
| Ausgaben (Fakt) | Ausgaben, Einkommen |

**Dimensionen (4):**
| Dimension | Inhalt |
|---|---|
| Region (Dimension) | Bundesland, Kreis, Stadt |
| Zeit (Dimension) | Schuljahr, Jahr |
| Abschluss (Dimension) | (Abschlussarten – auf Folie ohne Detailspalte) |
| Schulart (Dimension) | (Schularten – auf Folie ohne Detailspalte) |

> **Verbindlich:** Das umzusetzende Sternschema hat **genau diese 4 Fakten und 4 Dimensionen**. Erweiterungen (z. B. dim_geschlecht, dim_alter aus der Datenrecherche) sind Vorschläge und müssen eskaliert werden (Quellenregel).

---

## S11-Danke
**Überschrift:** DANKE!
**Autoren:** Max Budde, John Kanto & Aaron Ziegler
