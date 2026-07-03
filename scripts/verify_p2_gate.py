# -*- coding: utf-8 -*-
import pandas as pd, codecs, sys
io = sys.stdout
def p(*a): print(*a)

RAW = 'data/raw/21111-02-06-4.csv'
CLEAN = 'data/clean/'

def to_num(x):
    if x is None: return None
    x=str(x).strip()
    if x in ('-','.','x','...','/',''): return None
    return int(x.replace('.',''))

# ---- load raw 21111-02-06-4 ----
with codecs.open(RAW,'r','cp1252') as f:
    lines=[l.rstrip('\n') for l in f]
data={}
for ln in lines[9:]:
    parts=ln.split(';')
    if len(parts)<16: continue
    jahr,code,name=parts[0],parts[1],parts[2].strip()
    data[code]=parts

p('================ PUNKT 1: DQ2-Stichprobe DG ================')
dg=data['DG']
ins=to_num(dg[3]); ohne=to_num(dg[5]); mit=to_num(dg[7]); mitt=to_num(dg[9]); fhr=to_num(dg[13]); ahr=to_num(dg[15])
s=ohne+mit+mitt+fhr+ahr
p('Insgesamt(sp3)=',ins,' ohneHSA(5)=',ohne,' mitHSA(7)=',mit,' mittlerer(9)=',mitt,' FHR(13)=',fhr,' allgHR(15)=',ahr)
p('Summe 5+7+9+13+15 =',s,' == Insgesamt?',s==ins,' erwartet 782423:',s==782423 and ins==782423)

p('\n================ PUNKT 2: Clean-Konsistenz Kreis ================')
k=pd.read_csv(CLEAN+'fact_abgaenge_kreis_2023.csv',sep=';',encoding='utf-8')
dgrow=k[(k.region_code=='DG')&(k.abschlussart=='insgesamt')]
p('Clean DG insgesamt=',int(dgrow.anzahl.iloc[0]),' Rohwert=',ins,' match?',int(dgrow.anzahl.iloc[0])==ins)
ebenen=k.drop_duplicates('region_code').ebene.value_counts().to_dict()
p('Ebenen-Zaehlung (unique region_code):',ebenen)
p('erwartet DE=1,BL=16,RB=35,KR=471')

p('\n================ PUNKT 3: Zwei-Jahres-Beleg Land ================')
land=pd.read_csv(CLEAN+'fact_abgaenge_land.csv',sep=';',encoding='utf-8')
# bundesland col has mojibake; match by startswith
def land_val(bl_prefix, jahr, abschluss='ohne Hauptschulabschluss', g='Insgesamt'):
    sub=land[(land.abgangsjahr==jahr)&(land.abschluss==abschluss)&(land.geschlecht==g)]
    sub=sub[sub.bundesland.str.startswith(bl_prefix)]
    return None if sub.empty else int(sub.anzahl.iloc[0]), sub.bundesland.tolist()
for (name,pref) in [('SH','Schleswig'),('Bayern','Bayern')]:
    for yr,exp in ( [('2022', 2333 if name=='SH' else 6205),('2023', 2499 if name=='SH' else 6474)] ):
        v=land_val(pref,yr)
        val=v[0] if v else None
        p(f'{name} {yr} ohne_HSA = {val}  erwartet {exp}  match? {val==exp}  (bl={v[1] if v else None})')

p('\n================ PUNKT 4: Cross-Source SH 2023 ohne_HSA ================')
# from raw kreis-table BL zeile 01
sh_raw=to_num(data['01'][5])
sh_land=land_val('Schleswig','2023')[0]
p('Regio (BL 01, sp5)=',sh_raw,' fact_abgaenge_land=',sh_land,' beide 2499?',sh_raw==2499 and sh_land==2499)

p('\n================ PUNKT 5: DQ3 Konsistenz Kreis-Summe==BL ================')
# build from raw: for given BL 2-digit, sum 5-stellige codes insgesamt(sp3) vs BL row sp3
def bl_check(bl):
    blrow=to_num(data[bl][3])
    kr=[to_num(v[3]) for c,v in data.items() if len(c)==5 and c[:2]==bl and v[1]==c]
    kr=[x for x in kr if x is not None]
    return blrow, sum(kr), len(kr)
for bl in ['01','05','09','06']:
    blv,ksum,n=bl_check(bl)
    p(f'BL {bl}: Land(sp3)={blv}  Sum Kreise(insg)={ksum}  n={n}  Delta={ksum-blv if blv else None}')

p('\n================ PUNKT 6: DQ7 Missing != 0 ================')
# SH (01) FHR-darunter col 11? Actually check raw "-" -> clean. Use FHR/dar columns which had "-"
# In raw, SH col 13 (mit FHR)?? SH row: ...1176;627;-;-;9192 -> col11=1176,col13=- ? recheck
sh=data['01']
p('SH raw cols 11,12,13,14,15:',sh[11],sh[12],sh[13],sh[14],sh[15])
# find an abschlussart that is "-" in raw and check clean value
# clean kreis abschlussart values:
p('clean abschlussart unique:',k.abschlussart.unique().tolist())
# check fachhochschulreife for SH region 01 in clean
fhr_sh=k[(k.region_code=='01')&(k.abschlussart.str.contains('fachhochschul',case=False))]
p('clean SH fachhochschulreife rows:')
p(fhr_sh[['abschlussart','anzahl','anzahl_weiblich']].to_string())
# any zeros where raw was '-'? sample across kreis FHR
fhrall=k[k.abschlussart.str.contains('fachhochschul',case=False)]
p('count clean FHR anzahl==0:', (fhrall.anzahl==0).sum(), ' isna:', fhrall.anzahl.isna().sum(),' total:',len(fhrall))

p('\n================ PUNKT 7: Dimensionen ================')
da=pd.read_csv(CLEAN+'dim_abschluss.csv',sep=';',encoding='utf-8')
p('dim_abschluss rows=',len(da),' cols=',list(da.columns))
dr=pd.read_csv(CLEAN+'dim_region.csv',sep=';',encoding='utf-8')
p('dim_region rows=',len(dr),' has stadt_land/ost_west?', 'stadt_land' in dr.columns and 'ost_west' in dr.columns)
ds=pd.read_csv(CLEAN+'dim_schulart.csv',sep=';',encoding='utf-8')
p('dim_schulart rows=',len(ds),' cols=',list(ds.columns))

p('\n================ PUNKT 8: Encoding UTF-8 + Umlaute ================')
import glob, os
for fp in sorted(glob.glob(CLEAN+'*.csv')):
    try:
        with open(fp,'rb') as fh: raw=fh.read()
        raw.decode('utf-8')  # strict
        # search for replacement char or mojibake marker 0xEF 0xBF 0xBD or raw 0x81/0x9d? check '�'
        txt=raw.decode('utf-8')
        bad = ('�' in txt)
        p(os.path.basename(fp),'valid-utf8=True  replacement-char(mojibake)?',bad)
    except UnicodeDecodeError as e:
        p(os.path.basename(fp),'NOT valid utf-8:',e)
# explicit umlaut probes
p('--- Umlaut-Proben ---')
p('land bundesland sample:', land.bundesland.unique()[:6].tolist())
p('Wuerttemberg literal present in land?', land.bundesland.str.contains('Württemberg').any())
p('Thueringen literal present in dim_region?', dr.region.str.contains('Thüringen').any())
