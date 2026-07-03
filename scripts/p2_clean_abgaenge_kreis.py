# -*- coding: utf-8 -*-
"""Phase 2 - Fakt Abgaenge Kreis/Land 2023 aus Regio 21111-02-06-4 (Wide->Long).
DQ2: Summe Abschlussarten == Insgesamt je Region.  DQ3: Kreis-Aggregat == Bundeslandwert.
"""
import csv, os
_R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW = os.path.join(_R,"data","raw")
CLEAN = os.path.join(_R,"data","clean")
os.makedirs(CLEAN, exist_ok=True)
SRC = os.path.join(RAW, "21111-02-06-4.csv")

# Spaltenindizes (0-basiert) der Wertspalten, verifiziert an Deutschland-Zeile
COLS = {  # name: (Insgesamt-idx, weiblich-idx, additiv?)
 "insgesamt":(3,4,False),
 "ohne_hauptschulabschluss":(5,6,True),
 "mit_hauptschulabschluss":(7,8,True),
 "mittlerer_abschluss":(9,10,True),
 "dar_schul_teil_fhr":(11,12,False),  # darunter -> NICHT additiv
 "fachhochschulreife":(13,14,True),
 "allgemeine_hochschulreife":(15,16,True),
}
ADDITIV = [k for k,(_,_,a) in COLS.items() if a]

def to_num(v):
    v=(v or "").strip()
    if v in {"-","x",".","...","/",""}: return None
    return int(v.replace(".","").replace(" ",""))

def ebene(code):
    code=code.strip()
    if code=="DG": return "DE"
    if code.isdigit():
        return {2:"BL",3:"RB",5:"KR"}.get(len(code),"?")
    return "?"

rows=[]
with open(SRC, encoding="cp1252") as f:
    for line in f:
        p=line.rstrip("\n").split(";")
        if len(p)<17: continue
        if p[0].strip()!="2023": continue          # nur Datenzeilen 2023
        code=p[1].strip()
        if ebene(code)=="?": continue
        rec={"jahr":2023,"region_code":code,"region":p[2].strip(),"ebene":ebene(code),
             "bundesland_code":("DG" if code=="DG" else code[:2])}
        for name,(iI,iW,_) in COLS.items():
            rec[name]=to_num(p[iI]); rec[name+"_w"]=to_num(p[iW])
        rows.append(rec)

# Schreiben (Long je Abschlussart)
long_out=os.path.join(CLEAN,"fact_abgaenge_kreis_2023.csv")
with open(long_out,"w",newline="",encoding="utf-8") as f:
    w=csv.writer(f,delimiter=";")
    w.writerow(["jahr","region_code","region","ebene","bundesland_code","abschlussart","anzahl","anzahl_weiblich"])
    for r in rows:
        for name in COLS:
            if name in ("dar_schul_teil_fhr",): continue
            w.writerow([r["jahr"],r["region_code"],r["region"],r["ebene"],r["bundesland_code"],name,r[name],r[name+"_w"]])
print(f"geschrieben: {long_out}  ({len(rows)} Regionen)")
print(f"  Ebenen: " + ", ".join(f"{e}={sum(1 for r in rows if r['ebene']==e)}" for e in ["DE","BL","RB","KR"]))

# ---- DQ2: Summe additiver Arten == Insgesamt je Region ----
print("\n=== DQ2 (Summe Abschlussarten == Insgesamt) ===")
f2=0; c2=0; miss=0
for r in rows:
    tot=r["insgesamt"]
    if tot is None: continue
    parts=[r[a] for a in ADDITIV]
    if any(p is None for p in parts): miss+=1; continue
    c2+=1
    if sum(parts)!=tot:
        f2+=1
        if f2<=8: print(f"  FAIL {r['region']}({r['region_code']}): Summe={sum(parts)} != {tot}")
print(f"  geprueft={c2}, FAILS={f2}, uebersprungen(Missing)={miss}")
print("  DQ2:", "GRUEN" if f2==0 else f"{f2} Abweichungen")

# ---- DQ3: Summe Kreise je Bundesland == Bundesland-Insgesamt ----
print("\n=== DQ3 (Kreis-Aggregat == Bundeslandwert) ===")
bl_val={r["region_code"]:r["insgesamt"] for r in rows if r["ebene"]=="BL"}
kreis_sum={}
for r in rows:
    if r["ebene"]=="KR" and r["insgesamt"] is not None:
        kreis_sum[r["bundesland_code"]]=kreis_sum.get(r["bundesland_code"],0)+r["insgesamt"]
f3=0;c3=0
for blc,blv in sorted(bl_val.items()):
    if blv is None or blc not in kreis_sum: continue
    c3+=1; ks=kreis_sum[blc]; diff=ks-blv
    status="OK" if diff==0 else f"DIFF {diff}"
    if diff!=0: f3+=1
    print(f"  BL {blc}: Kreissumme={ks} vs BL-Insgesamt={blv} -> {status}")
print(f"  geprueft={c3}, Abweichungen={f3}")
print("  DQ3:", "GRUEN" if f3==0 else f"{f3} Abweichungen (Stadtstaaten/Geheimhaltung pruefen)")
