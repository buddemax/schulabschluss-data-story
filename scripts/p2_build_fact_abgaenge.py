# -*- coding: utf-8 -*-
"""Vereinheitlichte Fakt-Tabelle Abgaenge fuer Power BI:
- 2023: alle Ebenen (DE/BL/RB/KR) aus fact_abgaenge_kreis_2023 (Regio), Geschlecht insg/w/m
- 2022: Bundeslandebene aus fact_abgaenge_land (Statbericht), zur Zwei-Jahres-Analyse
Kanonischer abschluss_key (join zu dim_abschluss).
"""
import csv, os
CLEAN = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),"data","clean")

# Label -> kanonischer key
KEY = {
 "ohne_hauptschulabschluss":"ohne_hauptschulabschluss","ohne hauptschulabschluss":"ohne_hauptschulabschluss",
 "mit_hauptschulabschluss":"mit_hauptschulabschluss","hauptschulabschluss":"mit_hauptschulabschluss","mit hauptschulabschluss":"mit_hauptschulabschluss",
 "mittlerer_abschluss":"mittlerer_abschluss","mittlerer abschluss":"mittlerer_abschluss",
 "fachhochschulreife":"fachhochschulreife",
 "allgemeine_hochschulreife":"allgemeine_hochschulreife","allgemeine hochschulreife":"allgemeine_hochschulreife",
}
def keyof(lbl): return KEY.get(lbl.strip().lower())

def rd(fn):
    with open(os.path.join(CLEAN,fn),encoding="utf-8") as f:
        return list(csv.DictReader(f,delimiter=";"))
def num(v):
    v=(v or "").strip()
    return int(v) if v not in ("","None") and v.lstrip("-").isdigit() else None

out=[]  # region_code, jahr, abschluss_key, geschlecht, anzahl

# --- 2023 alle Ebenen aus Kreis-Tabelle ---
for r in rd("fact_abgaenge_kreis_2023.csv"):
    k=keyof(r["abschlussart"])
    if not k: continue
    insg=num(r["anzahl"]); w=num(r["anzahl_weiblich"])
    out.append([r["region_code"],2023,k,"insgesamt",insg if insg is not None else ""])
    out.append([r["region_code"],2023,k,"weiblich",w if w is not None else ""])
    m = (insg-w) if (insg is not None and w is not None) else None
    out.append([r["region_code"],2023,k,"maennlich",m if m is not None else ""])

# --- 2022 Bundeslandebene aus Statbericht (Name -> Code mappen) ---
# Name->Code aus dim_region (BL-Ebene)
name2code={}
for r in rd("dim_region.csv"):
    if r["ebene"]=="BL":
        name2code[r["region"].strip()]=r["region_code"]
name2code["Zusammen"]="DG"; name2code["Deutschland"]="DG"  # Statbericht-Bezeichnung fuer Deutschland

unmapped=set()
for r in rd("fact_abgaenge_land.csv"):
    if int(r["abgangsjahr"])!=2022: continue   # 2023 kommt aus Regio
    k=keyof(r["abschluss"])
    if not k: continue
    code=name2code.get(r["bundesland"].strip())
    if not code: unmapped.add(r["bundesland"]); continue
    a=num(r["anzahl"])
    g=r["geschlecht"].strip().lower().replace("ä","ae")  # "männlich" -> "maennlich" (einheitlich mit 2023)
    out.append([code,2022,k,g,a if a is not None else ""])

fp=os.path.join(CLEAN,"fact_abgaenge.csv")
with open(fp,"w",newline="",encoding="utf-8") as f:
    w=csv.writer(f,delimiter=";"); w.writerow(["region_code","jahr","abschluss_key","geschlecht","anzahl"]); w.writerows(out)
print(f"geschrieben fact_abgaenge.csv: {len(out)} Zeilen")
if unmapped: print("  WARN unmapped Bundeslaender:", unmapped)

# Sanity: SH ohne HSA je Jahr (geschlecht insgesamt)
def sh(jahr):
    return [o[4] for o in out if o[0]=="01" and o[1]==jahr and o[2]=="ohne_hauptschulabschluss" and o[3]=="insgesamt"]
print("  SH ohne_HSA insgesamt 2022:", sh(2022), " 2023:", sh(2023))
# Jahre + Ebenen-Abdeckung
jahre=sorted(set(o[1] for o in out)); print("  Jahre:", jahre)
bl2022=sorted(set(o[0] for o in out if o[1]==2022)); print("  #Regionen 2022:", len(bl2022))
