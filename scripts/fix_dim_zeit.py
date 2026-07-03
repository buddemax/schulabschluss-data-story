# -*- coding: utf-8 -*-
import os
CLEAN=r"C:\Users\maxot\OneDrive\Desktop\datastory_school\data\clean"
TAB=r"C:\Users\maxot\OneDrive\Desktop\datastory_school\powerbi\SchulabschlussDataStory.SemanticModel\definition\tables"
# 1) dim_zeit.csv mit Schluessel 'jahr'
with open(os.path.join(CLEAN,"dim_zeit.csv"),"w",encoding="utf-8",newline="") as f:
    f.write("jahr;schuljahr;kalenderjahr\n2022;2022/23;2022\n2023;2023/24;2023\n2024;2024/25;2024\n2025;-;2025\n")
# 2) dim_zeit.tmdl
tmdl = """table dim_zeit

\tcolumn jahr
\t\tdataType: int64
\t\tsummarizeBy: none
\t\tsourceColumn: jahr

\tcolumn schuljahr
\t\tdataType: string
\t\tsummarizeBy: none
\t\tsourceColumn: schuljahr

\tcolumn kalenderjahr
\t\tdataType: int64
\t\tsummarizeBy: none
\t\tsourceColumn: kalenderjahr

\tpartition dim_zeit = m
\t\tmode: import
\t\tsource =
\t\t\t\tlet
\t\t\t\t    Quelle = Csv.Document(File.Contents(DataFolder & "dim_zeit.csv"), [Delimiter=";", Encoding=65001, QuoteStyle=QuoteStyle.Csv]),
\t\t\t\t    Headers = Table.PromoteHeaders(Quelle, [PromoteAllScalars=true]),
\t\t\t\t    Typed = Table.TransformColumnTypes(Headers, {{"jahr", Int64.Type}, {"schuljahr", type text}, {"kalenderjahr", Int64.Type}})
\t\t\t\tin
\t\t\t\t    Typed
"""
with open(os.path.join(TAB,"dim_zeit.tmdl"),"w",encoding="utf-8") as f:
    f.write(tmdl)
print("dim_zeit.csv und dim_zeit.tmdl korrigiert")
print(open(os.path.join(CLEAN,"dim_zeit.csv"),encoding="utf-8").read())
