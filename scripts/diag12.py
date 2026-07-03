# -*- coding: utf-8 -*-
import openpyxl, os, warnings
warnings.filterwarnings("ignore")
RAW = r"C:\Users\maxot\OneDrive\Desktop\datastory_school\data\raw"
wb = openpyxl.load_workbook(os.path.join(RAW,"statbericht_allgbild_2023-24.xlsx"), read_only=True, data_only=True)
ws = wb["csv-21111-12"]
data = list(ws.iter_rows(values_only=True))
header=[("" if c is None else str(c)).strip() for c in data[0]]
H={c:i for i,c in enumerate(header)}
def col(n,ex=None):
    for c,i in H.items():
        if n.lower() in c.lower() and (ex is None or ex.lower() not in c.lower()): return i
iBL,iSA,iST,iKL,iAB,iA2,iGE=col("Bundesland"),col("Schulart"),col("Status"),col("Klassenstufe"),col("Abschluss"),col("Abschluss2"),col("Geschlecht")
iVAL=col("Absolvierende_und_Abgehende_Anzahl",ex="auslaend")
print("cols:",header)
n=0
for r in data[1:]:
    r=[("" if c is None else str(c)).strip() for c in r]
    if r[iBL]=="Schleswig-Holstein" and r[iSA]=="Insgesamt" and r[iGE]=="Insgesamt":
        print(f"  Status={r[iST]!r:14} Klassenst={r[iKL]!r:18} Abschluss={r[iAB]!r:28} Abschluss2={r[iA2]!r:50} val={r[iVAL]!r}")
        n+=1
        if n>=25: break
