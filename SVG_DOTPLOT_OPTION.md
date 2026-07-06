# SVG-Dot-Plot mit Bundesland-Kürzeln (login-freie Option, getestet)

Neben dem Deneb-Weg (`DENEB_DOTPLOT_ANLEITUNG.md`, braucht AppSource-Login) haben wir eine
**dritte Variante** gebaut und live gerendert: Ein **DAX-Measure zeichnet den kompletten Dot-Plot
als SVG-Bild** – mit echten **Bundesland-Kürzeln (SH…TH) auf der X-Achse**, einem Punkt je Kreis
(deterministischer Jitter aus dem AGS), Kontextgrau + Vermillion-Akzent nach Farbvertrag und
Gitterlinien. **Kein Custom Visual, kein Login** – nur ein Measure (Datenkategorie *Bild-URL*)
in einem Tabellen-/Bild-Visual.

**Trade-off (Grund, warum es nicht eingebaut ist):** Das SVG ist ein statisches Bild – keine
Kreisnamen-Tooltips beim Hover und kein Cross-Filtering. Der eingebaute native Dot-Plot
(X = Position 01–16, Land im Tooltip) bleibt deshalb die interaktive Standardlösung; dieses SVG
ist die dokumentierte Alternative, falls die Namen auf der Achse wichtiger sind als Interaktivität.

**Einbau in 3 Schritten:**
1. Measure(s) unten in `dim_abschluss` anlegen (Measure-Guard in `scripts/verify_all.py` Z. „23 analytische" um +2 anheben und begründen).
2. Measure markieren → *Measuretools → Datenkategorie = Bild-URL*.
3. Tabellen-Visual (nur dieses eine Feld) auf die Seite, Kopfzeile aus, Bildgröße im Format-Pane maximieren.

## Measure LF3 (Quote ohne HSA je Kreis, gruppiert nach Bundesland)

```DAX
SVG Dot LF3 =
VAR L=48 VAR R=692 VAR B=318 VAR T=14 VAR BW=DIVIDE(R-L,16) VAR YMAX=18 VAR YS=DIVIDE(B-T,YMAX)
VAR KR=CALCULATETABLE(VALUES(dim_region[region_code]),dim_region[ebene]="KR")
VAR D=ADDCOLUMNS(KR,"@bc",CALCULATE(SELECTEDVALUE(dim_region[bundesland_code])),"@v",[Quote ohne HSA %])
VAR D2=ADDCOLUMNS(FILTER(D,NOT ISBLANK([@v])&&NOT ISBLANK([@bc])),
  "@x",ROUND(L+(VALUE([@bc])-0.5)*BW+(MOD(VALUE(dim_region[region_code]),21)-10),0),
  "@y",ROUND(B-[@v]*YS,0))
VAR Grey="<g fill='#8C8C8C'>"&CONCATENATEX(D2,"<circle cx='"&[@x]&"' cy='"&[@y]&"' r='3'/>")&"</g>"
VAR Acc=CONCATENATEX(FILTER(D2,[@bc]="07"),"<circle cx='"&[@x]&"' cy='"&[@y]&"' r='3.8' fill='#D55E00'/>")
VAR XL=CONCATENATEX(CALCULATETABLE(VALUES(dim_region[bundesland_code]),dim_region[ebene]="KR"),
  "<text x='"&ROUND(L+(VALUE(dim_region[bundesland_code])-0.5)*BW,0)&"' y='334' font-size='11' fill='#555' text-anchor='middle'>"&CALCULATE(SELECTEDVALUE(dim_region[Land-Kürzel]))&"</text>")
VAR Grid=CONCATENATEX({0,5,10,15},
  "<line x1='"&L&"' y1='"&ROUND(B-[Value]*YS,0)&"' x2='"&R&"' y2='"&ROUND(B-[Value]*YS,0)&"' stroke='#eee'/><text x='42' y='"&(ROUND(B-[Value]*YS,0)+4)&"' font-size='10' fill='#999' text-anchor='end'>"&[Value]&"</text>")
RETURN "data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 700 360' preserveAspectRatio='xMidYMid meet' font-family='Segoe UI'>"&Grid&Grey&Acc&XL&"</svg>"
```

## Measure LF9 (Risiko-Score je Kreis, gruppiert nach Bundesland, Top-10 vermillion)

```DAX
SVG Dot LF9 =
VAR L=48 VAR R=692 VAR B=318 VAR T=14 VAR BW=DIVIDE(R-L,16) VAR YMIN=-6 VAR YMAX=9 VAR YS=DIVIDE(B-T,YMAX-YMIN)
VAR pop=CALCULATETABLE(ADDCOLUMNS(FILTER(VALUES(dim_region[region_code]),
    NOT ISBLANK([Quote ohne HSA %])&&NOT ISBLANK([Jugend-ALQ Ø])&&NOT ISBLANK([Verf. Einkommen je EW Ø])),
    "@q",[Quote ohne HSA %],"@a",[Jugend-ALQ Ø],"@e",[Verf. Einkommen je EW Ø]),
  REMOVEFILTERS(dim_region),REMOVEFILTERS(fact_einkommen_kreis),dim_region[ebene]="KR")
VAR muQ=AVERAGEX(pop,[@q]) VAR sdQ=STDEVX.S(pop,[@q])
VAR muA=AVERAGEX(pop,[@a]) VAR sdA=STDEVX.S(pop,[@a])
VAR muE=AVERAGEX(pop,[@e]) VAR sdE=STDEVX.S(pop,[@e])
VAR KR=CALCULATETABLE(VALUES(dim_region[region_code]),dim_region[ebene]="KR")
VAR D=ADDCOLUMNS(KR,"@bc",CALCULATE(SELECTEDVALUE(dim_region[bundesland_code])),
  "@q",[Quote ohne HSA %],"@a",[Jugend-ALQ Ø],"@e",[Verf. Einkommen je EW Ø])
VAR D2=ADDCOLUMNS(FILTER(D,NOT ISBLANK([@q])&&NOT ISBLANK([@a])&&NOT ISBLANK([@e])&&NOT ISBLANK([@bc])),
  "@x",ROUND(L+(VALUE([@bc])-0.5)*BW+(MOD(VALUE(dim_region[region_code]),21)-10),0),
  "@v",DIVIDE([@q]-muQ,sdQ)+DIVIDE([@a]-muA,sdA)+DIVIDE(muE-[@e],sdE))
VAR D3=ADDCOLUMNS(D2,"@y",ROUND(B-([@v]-YMIN)*YS,0))
VAR Grey="<g fill='#8C8C8C'>"&CONCATENATEX(D3,"<circle cx='"&[@x]&"' cy='"&[@y]&"' r='3'/>")&"</g>"
VAR Acc=CONCATENATEX(FILTER(D3,[@v]>=5.5),"<circle cx='"&[@x]&"' cy='"&[@y]&"' r='3.8' fill='#D55E00'/>")
VAR XL=CONCATENATEX(CALCULATETABLE(VALUES(dim_region[bundesland_code]),dim_region[ebene]="KR"),
  "<text x='"&ROUND(L+(VALUE(dim_region[bundesland_code])-0.5)*BW,0)&"' y='334' font-size='11' fill='#555' text-anchor='middle'>"&CALCULATE(SELECTEDVALUE(dim_region[Land-Kürzel]))&"</text>")
VAR Grid=CONCATENATEX({-5,0,5},
  "<line x1='"&L&"' y1='"&ROUND(B-([Value]-YMIN)*YS,0)&"' x2='"&R&"' y2='"&ROUND(B-([Value]-YMIN)*YS,0)&"' stroke='#eee'/><text x='42' y='"&(ROUND(B-([Value]-YMIN)*YS,0)+4)&"' font-size='10' fill='#999' text-anchor='end'>"&[Value]&"</text>")
RETURN "data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 700 360' preserveAspectRatio='xMidYMid meet' font-family='Segoe UI'>"&Grid&Grey&Acc&XL&"</svg>"
```

*(Beide Measures wurden am 06.07.2026 live in Power BI Desktop gerendert und geprüft: Kürzel-Achse,
ein Punkt je Kreis, Akzent korrekt. Sie sind bewusst nicht im Modell, damit die Measure-Guards und
der interaktive Standard-Dot-Plot unverändert bleiben.)*
