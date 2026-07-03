# -*- coding: utf-8 -*-
"""Verifiziert csv-21111-14: Bundesland x Abschluss (Schulart=Insgesamt, Geschlecht=Insgesamt) über beide Schuljahre."""
import openpyxl, os, warnings
warnings.filterwarnings("ignore")
RAW = r"C:\Users\maxot\OneDrive\Desktop\datastory_school\data\raw"
files = ["statbericht_allgbild_2022-23.xlsx", "statbericht_allgbild_2023-24.xlsx"]

def load(fn):
    wb = openpyxl.load_workbook(os.path.join(RAW, fn), read_only=True, data_only=True)
    ws = wb["csv-21111-14"]
    rows = [[("" if c is None else str(c)) for c in r] for r in ws.iter_rows(values_only=True)]
    return rows[0], rows[1:]

for fn in files:
    header, data = load(fn)
    H = {c.strip(): i for i, c in enumerate(header)}
    def col(*names):
        for n in names:
            for k, i in H.items():
                if n.lower() in k.lower():
                    return i
        return None
    iJ, iBL, iSA, iAB, iFO, iGE = col("Abgangsjahr"), col("Bundesland"), col("Schulart"), col("Abschluss"), col("Foerder"), col("Geschlecht")
    iVAL = len(header) - 1  # Anzahl ist letzte Spalte
    print("="*95); print(f"DATEI: {fn}")
    print("  Header:", [c for c in header if c])
    def uniq(i): return sorted(set(r[i] for r in data if i is not None and i < len(r) and r[i] != ""))
    print("  Schularten:", uniq(iSA))
    print("  Foerderschwerpunkt:", uniq(iFO))
    print("  Geschlecht:", uniq(iGE))
    print("  Abschlussarten:", uniq(iAB))
    # Filter: Schulart=Insgesamt, Foerder=Insgesamt, Geschlecht=Insgesamt
    def isins(v): return v.strip().lower() == "insgesamt"
    tab = {}
    for r in data:
        if iSA is not None and not isins(r[iSA]): continue
        if iFO is not None and not isins(r[iFO]): continue
        if iGE is not None and not isins(r[iGE]): continue
        bl, ab = r[iBL], r[iAB]
        val = r[iVAL]
        tab.setdefault(bl, {})[ab] = val
    print(f"  #Bundesländer (Schulart=Insg, Foerder=Insg, Geschl=Insg): {len(tab)}")
    print(f"  Bundesländer: {sorted(tab.keys())}")
    # Beispiel Schleswig-Holstein
    for key in ["Schleswig-Holstein", "Zusammen"]:
        if key in tab:
            print(f"  >>> {key}: {tab[key]}")
