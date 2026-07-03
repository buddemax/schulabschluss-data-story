# Bewertungskonzept – Data Story „Schulabschluss ist nicht nur Ländersache"
### Bewertung aus Sicht eines *strengen* Dozenten (Prof. Dr. Kempa, W2-AA), evidenzbasiert und gegen Gefälligkeitsnoten abgesichert

> Zweck: Eine ehrliche, nachvollziehbare Note ableiten, die nur dann 1,0 ist, wenn jede Anforderung, die Zielstellung und die Lerninhalte **nachweislich** erfüllt sind. Das Konzept ist so gebaut, dass weder ein Mensch noch ein LLM „wohlwollend durchwinken" kann.

---

## 0. Warum dieses Konzept (Problem, das es löst)
Eine naive (LLM-)Bewertung neigt zu drei Fehlern: (1) sie liest die Selbstauskunft der Autoren (README/Traceability) als Beleg, (2) sie belohnt Aufwand/Absicht statt erbrachter Leistung, (3) sie defaultet auf die Bestnote, weil „alles ganz gut aussieht". Dieses Konzept unterbindet das durch **Belegpflicht, Lückenlogik, K.O.-Gates, verankerte Notendeskriptoren und einen adversarialen Zweitprüfer**.

---

## 1. Grundprinzipien (verbindlich für jede Bewertung)

1. **Belegpflicht (Zeigen statt Behaupten).** Jede positive Bewertungszeile muss einen **konkreten Nachweis** zitieren: `Datei:Stelle` + nachgeprüfter Inhalt. **Ohne Beleg = „nicht erfüllt"** – nicht „vermutlich erfüllt".
2. **Selbstauskunft ≠ Nachweis.** Aussagen in `traceability.csv`, `ABGABE_README.md`, Folien oder Doku sind **Behauptungen der Autoren**. Sie zählen erst, wenn sie **unabhängig gegen das Artefakt** geprüft wurden (Daten neu rechnen, Datei öffnen, Modell inspizieren).
3. **Lückenlogik statt Wohlwollen.** Bewertung startet bei der Anforderung und sucht **aktiv, was fehlt oder falsch ist** (Red-Team-Haltung), nicht bei „wirkt vollständig".
4. **Kein Bonus für Absicht.** „geplant", „optional", „ausstehend", „könnte man noch" = **nicht erfüllt**. Nur tatsächlich Erbrachtes zählt.
5. **Gates vor Skala.** Pflicht-Bestandteile, Formalia und Lerninhalte sind **K.O.-Kriterien**: Fehlt eines, ist die Bestnote gesperrt (Deckelung), unabhängig von der Qualität des Rests.
6. **Verankerte Deskriptoren.** Pro Dimension gibt es **ausformulierte Notenstufen** (1,0/1,3–1,7/2,0–2,7/3,0–3,7/4,0/5,0). Der Prüfer muss den **am besten passenden Text** wählen und zitieren – das verhindert den 1,0-Default.
7. **Forcierte Kritik.** Bevor in einer Dimension eine 1,0 vergeben werden darf, müssen **mindestens 2 konkrete, ernsthaft gesuchte Schwachstellen** benannt und begründet als unkritisch eingestuft werden. Findet der Prüfer keine zwei, hat er nicht streng genug gesucht.
8. **Zwei-Augen-/Advocatus-Diaboli-Prinzip.** Eine zweite, **unabhängige** Bewertung sucht gezielt Abwertungsgründe. Bei Dissens gilt die **strengere** Note. (Methodik „der Ersteller ist nie sein eigener Prüfer".)
9. **Trennung bewertbar / nicht vorab bewertbar.** Der **Live-Vortrag (09.07.)** kann schriftlich nicht final bewertet werden → separat als **Risiko/Prognose** ausweisen, **nie** in die schriftliche Note „hineinraten".
10. **Wissenschaftliche Redlichkeit als Deckel.** Sachliche Fehler, Kausal-Übertreibung bei Korrelation, Schema-Doku ≠ reales Modell, nicht reproduzierbare Werte → **deckeln die Gesamtnote**, egal wie schön der Rest ist.

---

## 2. Bewertungsarchitektur (aus den Quellen abgeleitet)

**Gewichte (01_anan_organisation, S5):** Data-Story **25 %** + Dokumentation **30 %** der Modulnote (Übungsaufgaben 45 % separat). Diese Aufgabe = **55 % der Modulnote**, aufgeteilt in *Präsentation* und *Dokumentation*.

Die Bewertung läuft in **vier Stufen**:

```
Stufe 1: GATES (K.O.) → erfüllt? sonst Deckel
Stufe 2: 4 BW-DIMENSIONEN → Detailgrad, Ausführung, Visualisierung, Datenaufbereitung
Stufe 3: QUERSCHNITT-DECKEL → Redlichkeit, Reproduzierbarkeit, Lerninhalte-Tiefe
Stufe 4: AGGREGATION → getrennt: Doku-Note (30%) & Präsentations-Note (25%) → Gesamt
```

### Stufe 1 – K.O.-Gates (binär, müssen ALLE „ja" sein)
| Gate | Quelle | Kriterium | Beleg-Anforderung |
|---|---|---|---|
| G1 | S42 | Nur **öffentlich zugängliche** Daten, kein Login | Quellen-Log mit URLs + „kein Login"-Nachweis |
| G2 | S43 | **3 Personen**, jede:r erzählt einen Teil | Folien-Teilung + Namen; Live nur prüfbar am 09.07. |
| G3 | S43 | Zwischenpräsentation (Vision) gehalten | Chronik-Nachweis |
| G4 | S44-A | **A1 Präsentation, A2 SSBI-Projekt, A3 Quellen-Doku** vorhanden | je Artefakt geöffnet/geprüft |
| G5 | S44-B | **B1** Formate/Beispiele/Transformationen · **B2** dim. Schema + Analyseabfragen · **B3a–d** Tool-Auswertung | je Kapitel inhaltlich vorhanden |
| G6 | Org-S6 | **LI1–LI5** sichtbar adressiert (inkl. **LI4 Data-Vault als bewusste Einordnung**) | je Lerninhalt benannt + fachlich korrekt |
| G7 | S42 | **Qualitätskennzahlen berechnet** | DQ-Report mit echten Werten |

> Fehlt ein Gate → **keine 1,x möglich**; je nach Schwere Deckel auf 2,0–5,0.

### Stufe 2 – Die 4 Bewertungsdimensionen (S44)
> **Transparente Annahme:** Die Quelle nennt vier Dimensionen ohne Untergewichte → **Gleichgewichtung (je 25 % der Qualitätsnote)**. Diese Annahme ist im Bogen kenntlich zu machen und ggf. mit dem Dozenten zu verifizieren.

Für jede Dimension gelten die **verankerten Deskriptoren** aus Abschnitt 4.

### Stufe 3 – Querschnitt-Deckel (mindern, addieren nie)
- **Redlichkeit:** keine unbelegten/überzogenen Aussagen; Korrelation ≠ Kausalität explizit.
- **Konsistenz Doku ↔ Artefakt:** Schema-Doku == reales Modell; Zahlen in Folien == pandas-Referenz.
- **Reproduzierbarkeit:** Skripte laufen; Werte nachrechenbar; Testsuite grün.
- **Lerninhalte-Tiefe:** LI1–LI5 nicht nur erwähnt, sondern fachlich korrekt eingeordnet (v. a. LI4: *warum kein* Data-Vault).

### Stufe 4 – Aggregation
- **Doku-Note** = Mittel der für die Doku relevanten Dimensionen (BW1/BW2/BW4 stark) × Querschnitt-Deckel, nur belegte Zeilen.
- **Präsentations-Note** = Deck-Qualität (jetzt) + Vortrags-Prognose (Risiko, 09.07.).
- **Gesamtprognose** = gewichtetes Mittel (25/30 normalisiert), mit getrennter Ausweisung „jetzt sicher bewertbar" vs. „hängt am Vortrag".

---

## 3. Persona „strenger Dozent" (Kalibrierung)
Ein BI-/DWH-Professor (Kimball/Ross, Kohlhammer, Olson) prüft fachlich tief und gibt **keine Punkte für Selbstverständlichkeiten**. Typische **Abwertungsgründe**, auf die er gezielt schaut (Negativ-Checkliste):

- **Modellierung:** falscher/unklarer **Grain**; „Sternschema" behauptet, real Schneeflocke/Chaos; **bidirektionale m:n** ohne Begründung; Fakt-an-Fakt; Dimensionen unsauber.
- **Data-Vault (LI4):** nur Schlagwort statt **begründeter Einordnung** (wann Vault sinnvoll wäre vs. warum hier Stern).
- **Datenqualität (BW4):** Kennzahlen ohne Methodik; Missing als 0 interpretiert; Encoding-/Locale-Fehler unbemerkt; keine Cross-Source-Prüfung.
- **Visualisierung (BW3):** Achse nicht bei 0; irreführende Aggregation; keine Kernbotschaft; fehlende Quellen; nicht barrierearm; Diagrammtyp unpassend.
- **Wissenschaft:** **Kausalität aus Korrelation**; Stichjahr-Vermischung; nicht ausgewiesene Annahmen; runde Behauptungen ohne Zahl.
- **Vollständigkeit:** Pflicht-Bestandteil fehlt/oberflächlich; Lerninhalt nur genannt.
- **Reproduzierbarkeit:** Zahlen nicht nachrechenbar; „es funktioniert bei uns".

Grundhaltung: **„Im Zweifel gegen die Arbeit."** Unklarheit = nicht erfüllt, bis bewiesen.

---

## 4. Verankerte Notendeskriptoren je Dimension
> Der Prüfer wählt **pro Dimension genau eine Stufe** und **zitiert den Beleg**. Eine höhere Stufe ist nur erreichbar, wenn **alle** Merkmale der niedrigeren erfüllt sind.

### BW1 – Detailgrad
- **1,0:** Alle 9 Leitfragen tief beantwortet; mehrere Analyseebenen (Land→Kreis); Kennzahlen quantifiziert und **unabhängig verifiziert**; über das Geforderte hinaus (z. B. selbst gefundene & **behobene** Datenfehler, Testsuite). Keine inhaltliche Lücke.
- **1,3–1,7:** Alle Leitfragen beantwortet, gute Tiefe, aber 1–2 Aspekte oberflächlich oder eine Ebene fehlt.
- **2,0–2,7:** Kernfragen beantwortet, aber spürbare Lücken/oberflächliche Stellen.
- **3,0–3,7:** Nur Teil der Fragen substanziell; vieles deskriptiv.
- **4,0/5,0:** Wesentliche Fragen unbeantwortet / nur Datenschau.

### BW2 – Ausführung
- **1,0:** Saubere, reproduzierbare Pipeline; Modell **live & korrekt**; Werte == pandas-Referenz; sauberer roter Faden; Doku konsistent zum Artefakt; keine sachlichen Fehler.
- **1,3–1,7:** Solide, kleine Inkonsistenz Doku↔Artefakt oder 1 kleiner Fehler.
- **2,0–2,7:** Funktioniert, aber mehrere Inkonsistenzen / teilweise nicht reproduzierbar.
- **3,0+:** Brüchige Umsetzung, nicht durchgängig nachvollziehbar.

### BW3 – Visualisierung (Kohlhammer-Regeln, LI2)
- **1,0:** Jede Grafik mit **einer Kernbotschaft**, **Achse ab 0**, barrierearme Farben, Quellen; passender Diagrammtyp je Frage; interaktiver Bericht + statische Belege; keine irreführende Darstellung.
- **1,3–1,7:** Überwiegend regelkonform, 1–2 kleinere Verstöße (z. B. ein fehlendes Label).
- **2,0–2,7:** Brauchbar, aber mehrere Regelverstöße oder schwache Aussagekraft.
- **3,0+:** Irreführend / Regeln missachtet / Rohdatenschau.

### BW4 – Datenaufbereitung (Olson, LI5/DQ)
- **1,0:** Transformationen dokumentiert & reproduzierbar; **Qualitätskennzahlen mit Methodik**; Missing≠0; Encoding/Locale beherrscht; Cross-Source-Konsistenz; Auffälligkeiten transparent erklärt/behoben.
- **1,3–1,7:** Saubere Aufbereitung, kleine Lücke in Methodik/Doku.
- **2,0–2,7:** Aufbereitet, aber DQ oberflächlich / Auffälligkeiten unkommentiert.
- **3,0+:** Unsaubere/oberflächliche Aufbereitung; DQ fehlt.

### Notenanker – was 1,0 von 1,3 trennt
**1,0 = makellos UND überdurchschnittlich tief, ohne einen einzigen belegten Sachmangel.** Schon **eine** unbelegte Kernaussage, **eine** Doku-Artefakt-Abweichung oder **ein** ungeklärter Fehler ⇒ höchstens **1,3**.

---

## 5. Bewertungsbogen (operationalisiert)
Pro Kriterium **eine Zeile**; ohne Belegspalte keine Wertung:

| Krit.-ID | Anforderung (Quelle) | Geforderter Nachweis | **Gefundener Nachweis (Datei:Stelle)** | Erfüllt (ja/teilw/nein) | Strenge Anmerkung / Abwertung | Teilbewertung |
|---|---|---|---|---|---|---|

**Regeln für den Bogen**
- Jede „ja"-Zeile **ohne** geprüften Beleg wird automatisch zu **„nein"**.
- Pro BW-Dimension **≥2 ernsthafte Kritikpunkte** dokumentieren (forcierte Kritik), bevor 1,0 zulässig ist.
- Gesamtnote nur gültig, wenn **≥95 % der Pflicht-Zeilen belegt** geprüft wurden; sonst „nicht abschließend bewertbar".

---

## 6. So führt man eine *ehrliche LLM-gestützte* Bewertung durch (Anti-Gefälligkeits-Protokoll)
Gegen „LLM bewertet wahllos":

1. **Rollentrennung in getrennten Durchläufen:**
 - **(a) Evidenz-Sammler** (read-only): zitiert nur Fakten/Belege, **vergibt keine Note**.
 - **(b) Strenger Bewerter:** darf **nur** die von (a) belegten Fakten verwenden; jede Note braucht Zitat + Deskriptor-Stufe.
 - **(c) Advocatus Diaboli:** sucht ausschließlich Abwertungsgründe und Gegenbelege.
 - **(d) Schlichtung:** bei Dissens gilt die **strengere** Bewertung.
2. **Unabhängige Nachrechnung:** KPIs aus den Rohdaten **neu** berechnen, nicht aus der Doku übernehmen.
3. **Verbotene Formulierungen:** „wirkt", „sieht gut aus", „wahrscheinlich erfüllt", Note ohne Zitat → ungültig.
4. **Pflicht-Output:** (i) ausgefüllter Bogen, (ii) Liste **konkreter Schwächen** mit Schweregrad, (iii) Note **pro Dimension** mit zitiertem Deskriptor, (iv) Gesamtnote **getrennt** in „jetzt sicher" vs. „vortragsabhängig", (v) explizite **Annahmen** (z. B. Gleichgewichtung BW1–4).
5. **Ehrlichkeits-Test:** Wenn die Bewertung **keine** echten Schwächen findet, ist sie **nicht streng genug** und muss wiederholt werden.

---

## 7. Anwendung auf dieses Projekt (nächster Schritt)
Dieses Konzept ist direkt anwendbar. Empfohlener Lauf:
1. Evidenz-Sammler + Advocatus-Diaboli als getrennte (Sub-)Prüfungen über die echten Artefakte (`.pbix`, `.docx`, `.pptx`, `data/clean`, `scripts/verify_all.py`).
2. Strenger Bewerter füllt den Bogen, wählt Deskriptor-Stufen, benennt je Dimension ≥2 Schwächen.
3. Ausgabe: ehrliche Notenprognose **getrennt** für Dokumentation (jetzt bewertbar) und Präsentation (Deck jetzt, Vortrag = Risiko 09.07.), inkl. priorisierter „So kommt ihr sicher auf 1,0"-Liste.

> Hinweis zur Erwartungssteuerung: Eine seriöse 1,0-Prognose für die **Gesamtleistung** ist **vor** dem Live-Vortrag **nicht** möglich – bewertbar ist vorab nur der schriftlich/technische Teil. Das Konzept weist diese Grenze bewusst aus, statt sie wegzurunden.
