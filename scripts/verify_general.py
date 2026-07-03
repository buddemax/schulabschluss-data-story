# -*- coding: utf-8 -*-
"""Sucht das allgemeine Bundesland x Abschluss Blatt (alle Schulen, 17 BL)."""
import openpyxl, os, warnings
warnings.filterwarnings("ignore")
RAW = r"C:\Users\maxot\OneDrive\Desktop\datastory_school\data\raw"
fn = "statbericht_allgbild_2023-24.xlsx"
wb = openpyxl.load_workbook(os.path.join(RAW, fn), read_only=True, data_only=True)

for sheet in ["csv-21111-12", "csv-21111-15", "csv-21111-17"]:
    ws = wb[sheet]
    rows = [[("" if c is None else str(c)) for c in r] for r in ws.iter_rows(values_only=True)]
    header = [c.strip() for c in rows[0]]; data = rows[1:]
    print("="*95); print(f"BLATT: {sheet}  Wertspalte: '{header[-1]}'  Zeilen: {len(data)}")
    H = {c: i for i, c in enumerate(header)}
    def col(name):
        return next((i for c, i in H.items() if name.lower() in c.lower()), None)
    iBL, iSA, iAB, iGE, iAL = col("Bundesland"), col("Schulart"), col("Abschluss"), col("Geschlecht"), col("Alter")
    def uniq(i): return sorted(set(r[i] for r in data if i is not None and i < len(r) and r[i] != "")) if i is not None else None
    print("  Spalten:", header)
    print("  Schularten:", uniq(iSA))
    print("  Abschlussarten:", uniq(iAB))
    if iAL is not None: print("  Alter:", uniq(iAL))
    # Versuch: Bundesland x Abschluss mit Insgesamt-Filtern
    def isins(v): return v.strip().lower() == "insgesamt"
    tab = {}
    for r in data:
        if iSA is not None and not isins(r[iSA]): continue
        if iGE is not None and not isins(r[iGE]): continue
        if iAL is not None and not isins(r[iAL]): continue
        tab.setdefault(r[iBL], {})[r[iAB]] = r[-1]
    print(f"  -> #Bundeslaender bei (Schulart/Geschl/Alter=Insgesamt): {len(tab)}")
    if "Schleswig-Holstein" in tab:
        print("     SH:", tab["Schleswig-Holstein"])
