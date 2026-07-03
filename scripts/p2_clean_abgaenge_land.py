# -*- coding: utf-8 -*-
"""Phase 2 - Fakt Abgaenge (Bundeslandebene, 2 Schuljahre) aus csv-21111-12.
Erzeugt clean/fact_abgaenge_land.csv und prueft DQ2 (Summe Abschlussarten == Insgesamt).
Plus S09-Reproduktion (REQ-027).
"""
import openpyxl, os, csv, warnings
warnings.filterwarnings("ignore")
_R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW = os.path.join(_R,"data","raw")
CLEAN = os.path.join(_R,"data","clean")
os.makedirs(CLEAN, exist_ok=True)

FILES = {2022: "statbericht_allgbild_2022-23.xlsx", 2023: "statbericht_allgbild_2023-24.xlsx"}
ABSCHLUSS_ARTEN = {"ohne Hauptschulabschluss","Hauptschulabschluss","mittlerer Abschluss",
                   "Mittlerer Abschluss","Fachhochschulreife","allgemeine Hochschulreife"}

def norm(s): return ("" if s is None else str(s)).strip()
def isins(v): return norm(v).lower() == "insgesamt"

def to_num(v):
    v = norm(v)
    if v in {"-","x",".","...","/"} or v == "": return None  # Sonderzeichen = Missing
    return int(v.replace(".","").replace(" ",""))

rows_out = []
for jahr, fn in FILES.items():
    wb = openpyxl.load_workbook(os.path.join(RAW, fn), read_only=True, data_only=True)
    ws = wb["csv-21111-12"]
    data = list(ws.iter_rows(values_only=True))
    header = [norm(c) for c in data[0]]
    H = {c:i for i,c in enumerate(header)}
    def col(name, exclude=None):
        for c,i in H.items():
            if name.lower() in c.lower() and (exclude is None or exclude.lower() not in c.lower()): return i
        return None
    iBL,iSA,iST,iKL,iAB,iA2,iGE = col("Bundesland"),col("Schulart"),col("Status"),col("Klassenstufe"),col("Abschluss"),col("Abschluss2"),col("Geschlecht")
    iVAL = col("Absolvierende_und_Abgehende_Anzahl", exclude="auslaend")
    for r in data[1:]:
        r = [norm(c) if c is not None else "" for c in r]
        if not (isins(r[iSA]) and isins(r[iST]) and isins(r[iKL]) and isins(r[iA2])): continue
        if not (isins(r[iGE]) or r[iGE] in ("männlich","weiblich")): continue
        ab = r[iAB]
        rows_out.append({"abgangsjahr":jahr,"bundesland":r[iBL],"abschluss":ab,
                         "geschlecht":r[iGE],"anzahl":to_num(r[iVAL])})

# Schreiben
out = os.path.join(CLEAN, "fact_abgaenge_land.csv")
with open(out,"w",newline="",encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=["abgangsjahr","bundesland","abschluss","geschlecht","anzahl"], delimiter=";")
    w.writeheader(); w.writerows(rows_out)
print(f"geschrieben: {out}  ({len(rows_out)} Zeilen)")

# ---- DQ2: Summe der Abschlussarten == Insgesamt (je BL/Jahr/Geschlecht) ----
print("\n=== DQ2 Plausibilitaet (Summe Abschlussarten == Insgesamt) ===")
agg = {}
for r in rows_out:
    key = (r["abgangsjahr"], r["bundesland"], r["geschlecht"])
    d = agg.setdefault(key, {})
    # nicht mit None ueberschreiben (Duplikate/suppressed)
    if r["abschluss"] not in d or d[r["abschluss"]] is None:
        d[r["abschluss"]] = r["anzahl"]
fails = 0; checks = 0
for key, d in sorted(agg.items()):
    if "Insgesamt" not in d or d["Insgesamt"] is None: continue
    total = d["Insgesamt"]
    s = sum(v for a,v in d.items() if a in ABSCHLUSS_ARTEN and v is not None)
    checks += 1
    if s != total:
        fails += 1
        if fails <= 8:
            print(f"  FAIL {key}: Summe={s} != Insgesamt={total} (Diff {s-total})  parts={ {a:v for a,v in d.items() if a in ABSCHLUSS_ARTEN} }")
print(f"  Checks: {checks}, FAILS: {fails}")
print("  DQ2-ERGEBNIS:", "GRUEN" if fails==0 else f"{fails} Abweichungen (zu erklaeren)")

# ---- S09-Reproduktion (REQ-027): SH-Werte der Praesentation ----
print("\n=== S09 Tabelle A Reproduktion (Schleswig-Holstein) ===")
for jahr in (2022,2023):
    d = agg.get((jahr,"Schleswig-Holstein","Insgesamt"),{})
    tot = d.get("Insgesamt")
    print(f"  SH {jahr}: Insgesamt={tot}", {a:d.get(a) for a in ["ohne Hauptschulabschluss","Hauptschulabschluss","mittlerer Abschluss","Mittlerer Abschluss","allgemeine Hochschulreife","Fachhochschulreife"] if d.get(a) is not None})
print("  Praesentation S09 nennt: ohne Ersten 7531 (7,4%), Erster 16207 (15,9%), Mittlerer 48966 (48,1%), FHR 367 (0,4%)")
