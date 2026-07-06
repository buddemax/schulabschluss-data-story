# Agenten-Team-Review (Runde 3): Data Story „Schulabschluss ist nicht nur Ländersache"

> **Verwendung:** Diesen Prompt in einer Power-BI-fähigen Claude-Session einsetzen (die 4 Plugins der Marketplace `power-bi-agentic-development` müssen installiert sein → 17 Skills). Ein **Orchestrator-Agent** koordiniert, spawnt die Fach-Agenten, konsolidiert und **setzt um**.
>
> **Diese Runde ist die ABSCHLUSS-Runde.** Korrektheit (Runde 1) und Entschlackung/Bedienung (Runde 2) sind erledigt und live verifiziert. **Fokus jetzt: (1) LF9 sichtbar & erklärbar machen (neuer Team-Wunsch, Priorität 1), (2) die verbliebenen Kompositions-/Stil-Punkte, (3) die Kür-Punkte tatsächlich umsetzen** – nicht mehr nur vorschlagen. Bereits Erledigtes nicht erneut anfassen.

---

## 0. Rolle & Auftrag

Du bist **Lead-Orchestrator** eines Review-Teams für eine Self-Service-BI-Data-Story (Power BI, Modul „Analytische Anwendungen", HTW Berlin, Abgabe **09.07.2026**, Zielnote 1,0). Dein Auftrag: die offenen Punkte aus §11 **umsetzen** – mit dem Fokus:

> **Jede Kernaussage muss auf Präsentations-Distanz sichtbar sein (ohne Hovern), jede Kennzahl muss für den Betrachter nachvollziehbar sein (Methodik sichtbar), und die gesamte Ausarbeitung wirkt aus einem Guss.**

Arbeite **adversarial**: Wer etwas baut, prüft es nicht selbst – ein zweiter Agent verifiziert am **live gerenderten Bericht** (Screenshot), nicht nur am JSON. **Ground Truth** sind die unabhängig nachgerechneten Referenzwerte (`data/kpi_referenzwerte.json`, `scripts/verify_all.py` – aktuell **96/96 grün**). Grundsatz: **„nicht verifizierbar = FAIL".**

---

## 1. Kontext (Ist-Stand)

**Projekt:** 9 Leitfragen (LF1–LF9) entlang INPUT → OUTPUT → ÜBERGANG → ERGEBNIS. Sternschema (Kimball): 8 Fakttabellen + 4 Dimensionen, konforme `dim_region` über `region_code` (AGS), **18 analytische Measures + 1 Formatierungs-Measure** (`Farbe Führung LF1`). Okabe-Ito-Theme, nur offene Daten (Destatis/Regionalstatistik, BA, VGRdL).

**Technischer Zustand (sauber):** `.pbip` = `.pbix` synchron (**45 Visuals**), `verify_all` **96/96 grün**, Bilder/DOCX/PPTX aus dem aktuellen Bericht erzeugt. `.pbip` ist Single Source of Truth.

### Bereits erledigt (NICHT erneut anfassen) ✅
- **Korrektheit (Runde 1):** jahr=2023 pro Visual (12×), ebene-Filter (LF3=KR, LF4/LF5=DE), LF6-Faktor-2 behoben (relativ 41,6), LF3-Scatter repariert, LF1-Stadtstaat-Default entfernt; Werte == Ground Truth.
- **Entschlackung (Runde 2):** 6 redundante Slicer entfernt (LF1 stadtstaat+Land, LF2 stadt_land, LF5 schulart, LF8 stadtstaat, LF9 stadt_land); verbleibende Land-Slicer (LF4/5/6/7/9) Single-Select + Titel „Bundesland"; LF7-Schulart-Chart per NoFilter-Interaktion fest auf Deutschland (W5).
- **Inhalt (Runde 2):** LF5-Zweitsicht „ohne Grundschule" (Gymnasien ~40 % führen); LF9-Tabelle mit Treiberspalten (Quote ohne HSA, Jugend-ALQ, Einkommen); LF8-Datenpunkt-Labels an (W10); LF3-Seitentitel angeglichen; LF6/LF7-Achsentitel mit Einheit (W4).
- **W8 belegt statt entschärft:** r(Einkommen, ohne HSA)=−0,489, r(Einkommen, Jugend-ALQ)=−0,590 (n=398), Bayern 5,36 % → als Guards in verify_all (daher 96 Tests).
- **Stil:** Seitentitel + Erkenntnis-Boxen auf x=24 (S1/S2); LF1-Leader Sachsen-Anhalt vermillion `#D55E00` via Formatierungs-Measure + fx „nach Feldwert"; K3 (LF3-Geister-Interaktion) entfernt.
- **Repo/Doku:** sensible/fremde PDFs raus (History-Rewrite), Duplikate gelöscht, Slicer-Bugs dokumentiert, `LF3_Boxplot_Anleitung.md` liegt bereit.

### ⚠️ Bekannte Fallen (aus Runde 1/2 – unbedingt beachten)
1. **Bedingte Farbe „nach Feldwert" per JSON braucht den `selector`:** `objects.dataPoint`-Eintrag ohne `"selector": {"data":[{"dataViewWildcard":{"matchingOption":1}}]}` wird still ignoriert. Zuverlässig: Measure im Modell anlegen, Farbe in der **GUI** binden (Format → Farbe → **fx** → Formatstil „Feldwert") – das schreibt den Selector korrekt.
2. **Visual per Ordner-Löschung entfernt → verwaiste `visualInteractions` prüfen!** Ein page.json-Eintrag mit der toten Visual-ID lässt den Bericht normal rendern, aber **„Speichern unter → .pbix" scheitert STILL** (springt ohne Fehlermeldung zur Backstage zurück). Diagnose: `grep -rl "<visual-id>" …/Report/`. Fix: Eintrag aus der page.json entfernen, PBI neu öffnen.
3. **Workflow je Bearbeitungszyklus:** alte `PBIDesktop`/`msmdsrv`-Prozesse killen → JSON-Edits auf die `.pbip` → PBI **frisch** öffnen → refreshen → live verifizieren (Screenshots) → ggf. GUI-Edits (fx-Farben) → **Ctrl+S** (schreibt .pbip) → *Speichern unter → .pbix* (kanonisch überschreiben). Nie aus einer alten In-Memory-Instanz speichern. OneDrive: `rmtree` scheitert oft → Dateien einzeln löschen, Ordner per PowerShell.
4. **PDF-Export** stempelt oben mittig „Power BI Desktop" (y≈25–37 pt) → beim Croppen den Textblock **weiß übermalen**, dann Auto-Bounding-Box (Skript-Muster existiert; PDF liegt unter `AppData/Local/Temp/Power BI Desktop/print-job-*/`).
5. **Guard-Konventionen in `verify_all.py`:** Formatierungs-Measures MÜSSEN mit **`Farbe `** beginnen (werden getrennt gezählt: „18 analytisch + N Formatierung"). Neue **analytische** Measures oder neue **Seiten** erfordern bewusste Guard-Updates (Measure-Zahl, Visual-Zahl .pbix==.pbip, „9 Seiten"-Bild-Guards, crop-Skript `assert len(d)==9` → Seiten-Mapping anpassen). Guards nachziehen = Teil der Aufgabe, still rot lassen = FAIL.

**Team-Leitplanken (nicht zurückdrehen):** LF1-Balken bewusst auf 2023 gepinnt (Balken=Ranking, Linie=Trend); LF6 absolut+relativ nebeneinander; Okabe-Ito; Korrelation ≠ Kausalität + ökologischer-Fehlschluss-Vorbehalt bleiben.

**Kernartefakte:** `powerbi/…SemanticModel` (TMDL), `powerbi/…Report` (PBIR), `powerbi/SchulabschlussDataStory.pbix`, `charts/pbi/pbi_lf*.png`, `Schulabschluss_DataStory_Dokumentation.docx`, `…_Praesentation.pptx`, `scripts/verify_all.py`, `REVIEW_BEFUND.md`, `LF3_Boxplot_Anleitung.md`.

---

## 2. Ziele dieser Runde

1. **LF9 präsentationstauglich (Priorität 1, neuer Team-Wunsch):** Unterschiede zwischen den Kreisen müssen **ohne Hovern** sichtbar sein; die **Berechnung des Risiko-Scores muss für den Betrachter direkt auf der Seite nachvollziehbar** sein (Details §6/LF9 + §11a).
2. **Verbliebene Komposition** umsetzen: LF4 Card-Wall → Delta-Karten, LF2-Karte umkodieren oder streichen, LF1-Charttyp entscheiden, LF7-Achse auf konforme Dimension (W3/W9).
3. **Stil-Rest** umsetzen: Akzentfarbe je Visual für die Kernaussage (S3), Slicer-Spalte vereinheitlichen (S4), Abstände/Fluchten (K1), leere Filter-Stubs (K2), Inline-Font → Theme (K5).
4. **Kür umsetzen** (nicht nur vorschlagen): Einstiegsseite, Quellenzeile je Seite, Slicer-Sync, Drillthrough „Kreissteckbrief" – soweit ohne Login machbar (§11d).
5. **Konsistenz halten:** `.pbip` = `.pbix` = Bilder = DOCX/PPTX; `verify_all` **grün** (Guards bewusst nachgezogen, nie still rot).

---

## 3. Nicht-Ziele & Stop-Bedingungen

- **Bereits Erledigtes (§1 ✅) nicht zurückdrehen** – insb. Korrektheits-Filter, Slicer-Entschlackung, LF1-Farbe, gepinnte Jahre.
- **Keine neuen Leitfragen/Analysen/Datenquellen**; inhaltliche Kernaussagen bleiben (Zahlen sind belegt).
- **Kein Redesign um des Redesigns willen**; sobald eine LF „grün" ist (§8): weiter zur nächsten. Keine kosmetischen Endlosschleifen.
- **Login-pflichtige Schritte** (AppSource/Deneb, Shape-Map-Aktivierung falls kontogebunden) NICHT versuchen zu automatisieren → als klar beschriebene User-Aktion ausweisen und weiterarbeiten.
- **Nichts löschen/überschreiben ohne Beleg**; keine Credentials; öffentliches Repo sauber; kein Push halbfertiger Stände.
- **Deadline 09.07.2026:** Reihenfolge strikt nach §11-Priorität – „muss" (LF9, W3, S3) vor Kür.

---

## 4. Team & Skill-Zuordnung

| Agent | Fokus | Skills / Agenten |
|---|---|---|
| **Orchestrator (du)** | Plan, Fan-out, Umsetzung, Abschluss | alle, `pbir-cli`, `semantic-model` |
| **Modell-Auditor** | neue Measures (Deltas, Farb-Helfer) korrekt? Grain, Filterkontext | `semantic-models:semantic-model` (+ `semantic-model-auditor`), `dax` |
| **Report-/Design-Kritiker** | Kodierung, Farben, Layout/Raster, Data-Ink, Barrierefreiheit | `reports:pbir-cli`, `pbi-report-design`, `review-report`, `modifying-theme-json` |
| **Visual-Spezialist** | LF9-Einfärbung, LF2-Karte, Delta-Karten, ggf. SVG-KPIs | `custom-visuals:deneb-visuals`, `svg-visuals`, `python-visuals` (+ Reviewer) |
| **PBI-Desktop-Operator** | Live laden, fx-Farben in der GUI binden, jede berührte Seite screenshotten, exportieren | `pbi-desktop:connect-pbid`, `pbir-cli` (+ `query-listener`) |
| **Daten-/QA-Wächter** | Werte == Ground Truth, Guards nachziehen (bewusst, dokumentiert) | `verify_all.py`, `kpi_referenzwerte.json` |
| **Story-/Konsistenz-Editor** | Methodik-Texte (LF9!), Titel=Aussage, DOCX/PPTX-Abgleich | `review-report`, DOCX/PPTX |

**Adversarial-Regel:** Ersteller ≠ Prüfer; ein Umsetzungs-Schritt gilt erst als fertig, wenn ein zweiter Agent ihn am **gerenderten Bericht** (Screenshot) bestätigt hat – nicht nur im JSON (Lektion: JSON-Farb-Edits können still wirkungslos sein, Falle 1).

---

## 5. Bewertungs- & Umsetzungsrahmen (je berührter Seite)

Vor jeder Änderung kurz prüfen, nach jeder Änderung verifizieren:
**1** Kernaussage in 1 Satz · **2** Ist die Aussage **auf Distanz sichtbar** (Farbe/Sortierung/Beschriftung, ohne Hover/Tooltip)? · **3** Ist jede gezeigte Kennzahl **nachvollziehbar** (Einheit, Bezugsgröße, Methodik erkennbar)? · **4** Filter nötig & korrekt · **5** Wert == Ground Truth · **6** Text deckt sich mit Bild · **7** kein Ballast · **8** Okabe-Ito, Kontrast ≥ 4,5:1, Achse ab 0, Titel = Aussage, Quelle.

**Stil-Norm (Kurzfassung, gilt weiter):** 8/16-px-Raster, Abstände ≥16 px, Ränder 24–32 px, gefluchtete Kanten; Segoe UI, max. 2 Größen je Visual; **eine Akzentfarbe je Visual** für die Kernaussage, Rest gedämpft; Farben aus Theme statt Inline-Hex; ≤3 Slicer je Seite; Anti-Patterns verboten (KPI-Wände, monochrome Balken ohne Akzent, fehlende Sortierung, Roh-Feldnamen als Titel, Off-Grid, 3D, Doppel-Y, Riesen-Torten).

---

## 6. Die 9 Leitfragen – Ist-Stand & Aufträge dieser Runde

> ✅ = erledigt (nicht anfassen) · 🟠 = Auftrag Runde 3.

- **LF1 – Führende Bundesländer ohne Abschluss.**
  ✅ Balken 2023 + Sachsen-Anhalt vermillion; Jahr-Slicer sauber; Linie zweijährig.
  🟠 **Charttyp-Entscheidung (W3b):** Linie über 16 diskrete BL → **Dumbbell/Slope** (Deneb, falls ohne Login importierbar per `.pbiviz`-Datei; sonst native Alternative: gruppierte Balken 22/23 vs. 23/24) ODER begründet BEHALTEN („zwei Jahrgänge als Verlauf lesbar") – Entscheidung dokumentieren, nicht endlos iterieren.

- **LF2 – Höchster Anteil ohne HSA (Kreise).**
  ✅ 2023 gepinnt, tote Slicer weg.
  🟠 **W3c:** Bubble-Map (Größe=Rate = Anti-Pattern) → **(a)** native **Shape Map/Choropleth** mit AGS-`region_code` prüfen (wenn ohne Login aktivierbar: umsetzen, sequentielle Füllfarbe, Anhalt-Bitterfeld als dunkelster Wert), **(b)** sonst Karte **streichen** (Top-15-Balken trägt die Aussage allein) und die Bubble-Grenze als **Werkzeug-Grenze** in die Tool-Bewertung schreiben. **S3:** im Top-15-Balken den Spitzenreiter **Anhalt-Bitterfeld** akzentuieren (`Farbe Hotspot LF2`-Measure + GUI-fx, Falle 1 beachten).

- **LF3 – Streuung ohne HSA je Kreis.**
  ✅ Scatter repariert, Titel angeglichen, K3 raus.
  🟠 **Boxplot bleibt User-Aktion** (AppSource-Login; `LF3_Boxplot_Anleitung.md`). Falls das Team Deneb inzwischen importiert hat: Boxplot gemäß Anleitung einbauen. Sonst: nichts tun.

- **LF4 – Unterschied Jungen/Mädchen?**
  ✅ ebene=DE + jahr=2023.
  🟠 **W3a – Card-Wall ersetzen:** die 4–5 Einzel-KPIs durch **≤2 Delta-Karten**: `Gap ohne HSA (pp)` (Jungen−Mädchen) und `Gap Abitur (pp)` (Mädchen−Jungen), als neue **analytische** Measures (DAX aus den vorhandenen `(Geschlecht)`-Measures; Werte gegen GT: ~8,4−5,8=**2,6 pp** bzw. ~37,1−29,3=**7,8 pp** – exakt nachrechnen!). Karten mit Kontext-Untertitel („Jungen 8,4 % vs. Mädchen 5,8 %"). **Guards bewusst nachziehen:** Measure-Zahl 18→20 analytisch (verify_all + powerbi/README konsistent).

- **LF5 – Schulartmix.**
  ✅ Zweitsicht „ohne Grundschule", ebene=DE, Slicer sauber.
  🟠 **S3:** in beiden Säulencharts den tragenden Balken akzentuieren (links **Grundschulen**, rechts **Gymnasien**) via `Farbe Schulart LF5`-/`Farbe Schulart LF5 oG`-Measures + GUI-fx.

- **LF6 – Absolut vs. relativ.**
  ✅ Faktor-2 behoben, Achsentitel mit Einheit.
  🟠 **S3:** Rangwechsel farblich erzählen: **Sachsen-Anhalt** in beiden Charts vermillion, **NRW** in beiden petrol/blau (`Farbe Rangwechsel LF6`), Rest grau – der Blicksprung zeigt den Kipp-Effekt ohne Lesen. **K2:** leere Filter-Stubs (Advanced ohne Where) aus beiden Chart-JSONs entfernen.

- **LF7 – Bildungsausgaben.**
  ✅ Werte GT-konform, NoFilter-Interaktion (W5), €-Achsentitel.
  🟠 **W9:** Category des BL-Charts von `fact_ausgaben_je_schueler[bundesland]` auf **`dim_region[Land]`** umstellen (konforme Dimension). VORSICHT: danach live prüfen, dass alle 16 Balken + identische Werte erscheinen (Beziehung fact→dim_region muss greifen); bei Wertabweichung → zurück und als „bewusst nicht geändert" dokumentieren. **K2:** leere Filter-Platzhalter entfernen (den wirksamen `NOT IN ('Deutschland')`-Filter BEHALTEN).

- **LF8 – Mehr Geld = mehr Abitur?**
  ✅ 2023 auf Y, Labels an, Slicer weg.
  🟠 nur S4/K1-Feinschliff (Layout), sonst nichts.

- **LF9 – Risiko-Kreise (NEUER TEAM-WUNSCH, Priorität 1).**
  ✅ Treiberspalten, Summenzeile aus, Slicer-Titel, Achsen korrekt.
  🟠 **Problem laut Team:** Im Streudiagramm sehen alle ~400 Punkte gleich aus – Unterschiede erst beim Hovern erkennbar (präsentationsuntauglich); außerdem ist **nicht ersichtlich, wie der Risiko-Score berechnet wird**. Auftrag (Details §11a):
  **(a) Punkte nach Risiko-Score einfärben** – Formatierungs-Measure `Farbe Risiko LF9` (z. B. Top-10-Risiko-Kreise vermillion `#D55E00`, Rest gedämpft grau/blau; RANKX über den Score) und in der **GUI** via fx binden (Falle 1!). Alternativ/zusätzlich prüfen: Farbverlauf (Gradient) nach Score – entscheiden, was auf Distanz klarer ist (Panel-Urteil).
  **(b) Score-Spalte sichtbar machen:** **Datenbalken** auf der Risiko-Score-Spalte der Tabelle (Conditional Formatting → Data bars) – Ranking ohne Lesen erfassbar.
  **(c) Methodik erklären:** kompakte **Methodik-Textbox** auf der Seite (oder Untertitel der Tabelle): „Risiko-Score = Summe der z-standardisierten Werte aus (1) Quote ohne HSA 2023, (2) Jugend-ALQ 2025, (3) verfügbarem Einkommen 2021 (invertiert). 0 = Bundesschnitt der 398 Kreise; höher = höheres strukturelles Risiko. Kein Individualmaß (ökologischer Fehlschluss)." Zusätzlich die drei Treiber + Score in den **Tooltip** des Scatters legen.
  **(d) Visual-Frage:** prüfen, ob der Scatter mit (a)–(c) die Frage jetzt trägt; falls das Panel ihn weiterhin für zu unleserlich hält, Alternative: **Top-15-Balken nach Risiko-Score** (gefärbt) als Haupt-Visual + Scatter als Kontext daneben. Entscheidung dokumentieren.
  Erkenntnistext ggf. anpassen (Gelsenkirchen 8,1; die r-Werte sind belegt und bleiben).

---

## 7. Phasen & Meilensteine

**Phase 0 – Setup.** Alte PBI-Instanzen beenden, `.pbip` frisch öffnen, refresh; `verify_all` = 96/96 grün bestätigen.
**Phase 1 – Kurz-Inventur** nur der berührten Seiten (LF9-Scatter/-Tabelle, LF4-Karten, LF2-Karte, LF6/LF7-Filter-Stubs, Slicer-Positionen aller Seiten) + Screenshots.
**Phase 2 – Panel-Entscheidungen (adversarial, kurz):** LF9 (a) Top-N vs. Gradient, (d) Scatter vs. Balken; LF1 Charttyp; LF2 Choropleth vs. streichen. Je 2 Bewerter, Entscheidung + Begründung festhalten – dann NICHT mehr aufmachen.
**Phase 3 – Umsetzung Zyklus A („muss"):** LF9 (a–d) → LF4 Delta-Karten (+ Guard-Update 18→20) → LF2-Entscheidung umsetzen → W9 LF7-Achse → S3-Akzentfarben (LF2/LF5/LF6; alle via Modell-Measure `Farbe …` + GUI-fx) → K2-Stubs. Live verifizieren, **Ctrl+S + .pbix-Export**, `verify_all` grün.
**Phase 4 – Umsetzung Zyklus B (Stil + Kür):** S4 Slicer-Spalte (rechts bündig, gleiche Breite/x, ein Typ), K1 Abstände/Fluchten (≥16 px, Unterkanten), K5 Font→Theme; dann Kür §11d: **Quellenzeile** je Seite, **Einstiegsseite** (⚠️ Guards + crop-Mapping anpassen: 10 PDF-Seiten, Intro überspringen), **Slicer-Sync** (syncGroup), **Drillthrough Kreissteckbrief** (falls Zeit). Live verifizieren, Export.
**Phase 5 – Abschluss:** Berichts-PDF exportieren → `charts/pbi/pbi_lf*.png` neu croppen (Falle 4; Seiten-Mapping!) → DOCX (p7) + PPTX (p6) + Präsentations-PDF (LibreOffice headless) neu → `verify_all` **komplett grün** (alle Guard-Änderungen im Commit begründet) → Commit(s) mit klaren Messages → Push → Kurzbericht „vorher → nachher" je berührter LF.

**Meilenstein-Regel:** Nach jedem Zyklus committen (kein Riesen-Commit am Ende); an jedem Meilenstein kurz berichten.

---

## 8. Akzeptanzkriterien / Definition of Done (binär)

Eine berührte LF ist **grün**, wenn: Kernaussage **ohne Hover** auf Distanz erkennbar · Methodik/Einheiten für Betrachter nachvollziehbar · Wert == Ground Truth · Text == Bild · kein Ballast · Akzentfarbe genau EINE je Visual · Layout on-grid/gefluchtet · Screenshot-verifiziert durch zweiten Agenten.

**Gesamt fertig, wenn:** §11a–c vollständig umgesetzt oder je Punkt begründet „bewusst nicht" · §11d so weit wie ohne Login möglich · `.pbip`=`.pbix`=Bilder=DOCX/PPTX · `verify_all` grün (Guard-Änderungen dokumentiert) · gepusht. *(LF3-Boxplot + ggf. LF2-Shape-Map-Login als User-Aktionen ausgewiesen.)*

---

## 9. Guardrails & Constraints

- **Single Source of Truth = `.pbip`**; jede Änderung landet in der Textquelle.
- **Ground Truth = unabhängige Nachrechnung**; „nicht verifizierbar = FAIL".
- **Adversarial:** Ersteller ≠ Prüfer; Verifikation am gerenderten Bericht.
- **Formatierungs-Measures heißen `Farbe …`** (Guard-Konvention); analytische Measure-/Seiten-Änderungen → Guards bewusst nachziehen (Falle 5).
- **Nur offene Daten**; keine Credentials/Logins automatisieren; Repo sauber.
- **Okabe-Ito bleibt**; Achsen ab 0; Korrelation ≠ Kausalität; ökologischer-Fehlschluss-Vorbehalt bleibt (gehört jetzt sogar sichtbar auf die LF9-Seite).
- **Minimal-invasiv & Deadline 09.07.:** §11-Prioritätsreihenfolge einhalten.

---

## 10. Output-Format (Deliverables)

1. **Entscheidungsprotokoll** der Panel-Fragen (LF9 a/d, LF1, LF2) mit Begründung.
2. **Umsetzungsprotokoll** je Punkt (was, wo, Vorher/Nachher-Screenshot).
3. **Guard-Änderungsliste** (welcher Test, alt→neu, warum).
4. **Abschlussbericht:** verify_all-Resultat, Konsistenz-Nachweis, Commit-Hashes, verbleibende User-Aktionen (Logins).

**Starte mit Phase 0.**

---

## 11. Aufgabenliste (Stand: Runde 2 abgeschlossen; Reihenfolge = Priorität)

### 11a. LF9 sichtbar & erklärbar (NEU, Priorität 1)
1. **`Farbe Risiko LF9`**-Measure (Formatierungs-Helfer): Top-10 nach `[Risiko-Score]` (RANKX über die KR-Ebene) → `#D55E00`, Rest `#B0BEC8`-artig gedämpft; in der GUI via fx an die Scatter-Punktfarbe binden (Falle 1). Panel-Alternative Gradient prüfen.
2. **Datenbalken** auf der Risiko-Score-Spalte der LF9-Tabelle.
3. **Methodik-Textbox** (Formel in Worten, Bezugsgröße, „kein Individualmaß") + Treiber & Score in den Scatter-**Tooltip**.
4. **Visual-Urteil:** Scatter (aufgewertet) vs. Top-15-Risiko-Balken als Haupt-Visual – entscheiden, umsetzen, dokumentieren.

### 11b. Komposition (wichtig)
5. **W3a – LF4:** Card-Wall → 2 Delta-Karten (`Gap ohne HSA (pp)`, `Gap Abitur (pp)`; neue analytische Measures, GT-geprüft; Guards 18→20 nachziehen).
6. **W3c – LF2:** Shape-Map-Choropleth (AGS) ODER Karte streichen + Werkzeug-Grenze dokumentieren; Anhalt-Bitterfeld im Balken akzentuieren.
7. **W3b – LF1:** Dumbbell/Slope vs. Linie – entscheiden & umsetzen/dokumentieren.
8. **W9 – LF7:** Achse auf `dim_region[Land]`, live gegen GT verifizieren (bei Abweichung: revertieren + dokumentieren).

### 11c. Stil & Formalien
9. **S3 – Akzentfarben:** LF2 (Anhalt-Bitterfeld), LF5 (Grundschulen/Gymnasien), LF6 (Sachsen-Anhalt + NRW in beiden Charts) – alle via `Farbe …`-Measures + GUI-fx.
10. **S4 – Slicer-Spalte:** alle Slicer rechts bündig (x=980, w=300), gleiche Kopf-Formatierung, ein Slicer-Typ.
11. **K1 – Abstände/Fluchten:** ≥16 px zwischen Visuals, gefluchtete Unterkanten, Ränder 24–32 px (v. a. LF3/LF5/LF6/LF7/LF9-Leerbänder schließen).
12. **K2 – leere Filter-Stubs** (Advanced/Categorical ohne Where) aus LF6/LF7-Visuals entfernen.
13. **K5 – Inline-Fonts** in Theme-Textklassen überführen (`modifying-theme-json`).

### 11d. Kür (umsetzen, soweit ohne Login)
14. **Quellenzeile** unten auf jeder Seite (Destatis/Regionalstatistik 21111; BA-Statistik 2025; VGRdL 2021 – je Seite passend).
15. **Einstiegsseite** vor LF1: These, Fluss INPUT→OUTPUT→ÜBERGANG→ERGEBNIS, Navigations-Buttons zu den Blöcken. ⚠️ Danach: crop-Mapping (10 Seiten, Intro skippen) + „9 Seiten"-Guards bewusst anpassen.
16. **Land-Slicer synchronisieren** (syncGroup über LF4/5/6/7/9) + identische Position.
17. **Drillthrough „Kreissteckbrief"** (Kreis → Quote, Risiko-Score, Jugend-ALQ, Einkommen) – falls Zeit vor Deadline.
18. **Beruflich-Tabelle**: in einem Visual nutzen ODER Übergangs-Stufe im Deck streichen – entscheiden + konsistent machen (Doku/PPTX).

### 11e. User-Aktionen (Login – NICHT automatisieren)
- **LF3-Boxplot** via Deneb/AppSource (`LF3_Boxplot_Anleitung.md`).
- Falls native Shape Map ein kontogebundenes Feature-Flag verlangt: LF2-Choropleth ebenfalls als User-Aktion ausweisen und Alternative (Karte streichen) umsetzen.

### 11f. Abschluss (immer)
- Berichts-PDF → PNGs neu croppen → DOCX/PPTX/Präsentations-PDF neu bauen → `verify_all` grün → committen → pushen → Kurzbericht.
