# -*- coding: utf-8 -*-
"""Finale Bestätigung csv-21111-12: Bundesland x Abschluss (alle Insgesamt-Filter), korrekte Wertspalte."""
import openpyxl, os, warnings
warnings.filterwarnings("ignore")
RAW = r"C:\Users\maxot\OneDrive\Desktop\datastory_school\data\raw"

for fn in ["statbericht_allgbild_2022-23.xlsx", "statbericht_allgbild_2023-24.xlsx"]:
    wb = openpyxl.load_workbook(os.path.join(RAW, fn), read_only=True, data_only=True)
    ws = wb["csv-21111-12"]
    rows = [[("" if c is None else str(c)) for c in r] for r in ws.iter_rows(values_only=True)]
    header = [c.strip() for c in rows[0]]; data = rows[1:]
    H = {c: i for i, c in enumerate(header)}
    def col(name, exclude=None):
        for c, i in H.items():
            if name.lower() in c.lower() and (exclude is None or exclude.lower() not in c.lower()):
                return i
        return None
    iJ=col("Abgangsjahr"); iBL=col("Bundesland"); iSA=col("Schulart"); iST=col("Status")
    iKL=col("Klassenstufe"); iAB=col("Abschluss"); iA2=col("Abschluss2"); iGE=col("Geschlecht")
    iVAL=col("Absolvierende_und_Abgehende_Anzahl", exclude="auslaend")
    print("="*90); print(f"DATEI: {fn}  Wertspalte idx={iVAL} ('{header[iVAL]}')")
    for c in ["Status","Klassenstufe","Abschluss2"]:
        i=col(c);
        if i is not None: print(f"  {c}:", sorted(set(r[i] for r in data if r[i]!=""))[:8])
    def isins(v): return v.strip().lower()=="insgesamt"
    tab={}
    for r in data:
        if not isins(r[iSA]): continue
        if iST is not None and not isins(r[iST]): continue
        if iKL is not None and not isins(r[iKL]): continue
        if iA2 is not None and not isins(r[iA2]): continue
        if not isins(r[iGE]): continue
        ab=r[iAB];
        if isins(ab): continue
        tab.setdefault(r[iBL],{})[ab]=r[iVAL]
    print(f"  #Bundeslaender: {len(tab)}")
    for k in ["Schleswig-Holstein","Bayern","Berlin","Zusammen"]:
        if k in tab: print(f"  {k}: {tab[k]}")
