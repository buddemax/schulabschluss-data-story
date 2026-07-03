# Werkzeuge & Skills – Inventar und Gap-Analyse (§5)

> Stand 2026-06-29. Welcher Skill/welches Werkzeug wird in welcher Phase warum eingesetzt.

## 1. Verfügbares Inventar (relevant)
| Werkzeug/Skill | Zweck | Status |
|---|---|---|
| Read (PDF/Bild/Notebook) | Quellen lesen | vorhanden |
| Bash / PowerShell | Skripte, Downloads, pandas | vorhanden |
| `data:explore-data`, `data:analyze`, `data:validate-data` | Datenprofiling, Analyse, QA | vorhanden |
| `data:create-viz` / `data:data-visualization` | Visualisierungen (Python) | vorhanden |
| `data:sql-queries` / `data:write-query` | Abfragen | vorhanden |
| `anthropic-skills:xlsx` | Excel-Artefakte | vorhanden |
| `anthropic-skills:pptx` | Präsentation | vorhanden |
| `anthropic-skills:docx` | Dokumentation (Word) | vorhanden |
| `anthropic-skills:pdf` | PDF-Handling | vorhanden |
| Computer Use (`mcp__computer-use__*`) | Power BI Desktop GUI / Visuals (§5c) | verfügbar (Zugriff anzufordern) |
| WebFetch / WebSearch | Quellen-/Portalzugriff | vorhanden |

## 2. Gap-Analyse – was fehlt
| Lücke | Benötigt für | Maßnahme | Phase |
|---|---|---|---|
| **Power-BI-Modeling-MCP** (`microsoft/powerbi-modeling-mcp`) nicht eingebunden | Semantische Schicht (Tabellen/Measures/DAX-Validierung) §5a | Einbinden (Node 18+, Entra-ID, laufendes Power BI Desktop). **Eskalation:** Voraussetzungen bestätigen lassen. | 3–4 |
| **Power BI Desktop** lokal lauffähig? | SSBI-Projekt + Visuals | Bestätigung des Nutzers nötig | 3 |
| **pandas-Umgebung** | pandas-Referenz (§7d) | erledigt: Python 3.12 + pandas installiert (anfänglich nur Windows-Store-Stub); alle Referenzwerte und `verify_all.py` laufen darauf. | 1–2 |
| Rohdaten-CSVs | Alles | Download §5b nach Scope-Freigabe | 1 |

## 3. Skill-Einsatz je Phase (geplant)
- **Phase 1 Datenbeschaffung:** Bash/PowerShell (Download), `data:explore-data` (Profiling), `datenquellen_log.md`.
- **Phase 2 Aufbereitung/DQ:** pandas (Bash), `data:validate-data`, Assertions.
- **Phase 3 Modellierung:** Power-BI-MCP (Modell/Measures), `data:sql-queries`.
- **Phase 4 KPIs:** Power-BI-MCP (DAX) + pandas-Referenz.
- **Phase 5 Visualisierung:** Computer Use (Power BI GUI) + `data:data-visualization` (Mockups/Gestaltungsregeln-Belege).
- **Phase 6 Story/Präsentation:** `anthropic-skills:pptx`.
- **Phase 7 Dokumentation:** `anthropic-skills:docx`, MCP-Modelldoku.

## 4. Offene Werkzeug-Entscheidungen (Check-in 1)
- Power BI Desktop + Power-BI-MCP einsatzbereit? Falls nein: Alternative (z. B. reines pandas+Mockup-Modell, oder anderes SSBI-Tool).
- Computer-Use-Zugriff für Power BI Desktop wird zur Visualisierungsphase angefordert.
