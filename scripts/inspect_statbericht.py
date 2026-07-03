# -*- coding: utf-8 -*-
"""Prüft Blatt csv-21111-13 (GENESIS 21111-0013 Spiegel): findet Header dynamisch."""
import openpyxl, os, warnings
warnings.filterwarnings("ignore")
RAW = r"C:\Users\maxot\OneDrive\Desktop\datastory_school\data\raw"
files = ["statbericht_allgbild_2022-23.xlsx", "statbericht_allgbild_2023-24.xlsx"]

for fn in files:
    p = os.path.join(RAW, fn)
    wb = openpyxl.load_workbook(p, read_only=True, data_only=True)
    ws = wb["csv-21111-13"]
    rows = [[("" if c is None else str(c)) for c in r] for r in ws.iter_rows(values_only=True)]
    print("="*95)
    print(f"DATEI: {fn}  Blatt csv-21111-13  ({len(rows)} Zeilen)")
    print("  --- erste 6 Zeilen roh ---")
    for i in range(min(6,len(rows))):
        print(f"   {i}| " + " | ".join(rows[i][:9]))
    # Header = Zeile mit 'Bundesland'
    h = next((i for i,r in enumerate(rows) if any("bundesland" in c.lower() for c in r)), None)
    if h is None:
        print("  Kein Header mit 'Bundesland' gefunden."); continue
    header = rows[h]
    print(f"  HEADER in Zeile {h}: {[c for c in header if c]}")
    def idx(name):
        return next((i for i,c in enumerate(header) if name.lower() in c.lower()), None)
    iL, iJ, iA, iS = idx("Bundesland"), idx("Abgangsjahr") or idx("jahr"), idx("Abschluss"), idx("Schulart")
    data = rows[h+1:]
    def uniq(i): return sorted(set(r[i] for r in data if i is not None and i < len(r) and r[i] != "")) if i is not None else []
    laender = uniq(iL)
    print(f"  Abgangsjahre: {uniq(iJ)}")
    print(f"  #Bundesländer: {len(laender)} -> {laender}")
    print(f"  Abschlussarten: {uniq(iA)}")
    sa = uniq(iS); print(f"  Schularten ({len(sa)}): {sa}")
