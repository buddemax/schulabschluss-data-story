# -*- coding: utf-8 -*-
"""Profiliert die Regionalstatistik-Roh-CSVs: Encoding, Trennzeichen, Struktur, Jahre, Sonderzeichen."""
import os, glob, chardet, re

RAW = r"C:\Users\maxot\OneDrive\Desktop\datastory_school\data\raw"

def sniff(path):
    with open(path, "rb") as f:
        head = f.read(40000)
    det = chardet.detect(head)
    enc = det["encoding"] or "unknown"
    # robustes Decoding zum Anzeigen
    for try_enc in [enc, "cp1252", "latin-1", "utf-8"]:
        try:
            text = head.decode(try_enc)
            used = try_enc
            break
        except Exception:
            continue
    lines = text.splitlines()
    # Trennzeichen schätzen
    sample = "\n".join(lines[:40])
    seps = {";": sample.count(";"), ",": sample.count(","), "\t": sample.count("\t")}
    sep = max(seps, key=seps.get)
    return enc, det["confidence"], used, lines, sep

print("="*90)
for path in sorted(glob.glob(os.path.join(RAW, "*.csv"))):
    name = os.path.basename(path)
    size = os.path.getsize(path)
    enc, conf, used, lines, sep = sniff(path)
    # Gesamtzeilen zählen
    with open(path, "rb") as f:
        total = sum(1 for _ in f)
    # Jahre suchen (4-stellige 19xx/20xx) in den ersten 60 Zeilen
    years = sorted(set(re.findall(r"\b(19\d{2}|20\d{2})\b", "\n".join(lines[:60]))))
    print(f"DATEI: {name}  ({size:,} Bytes, {total:,} Zeilen)")
    print(f"  chardet: {enc} (conf {conf:.2f}) | dekodiert mit: {used} | Trennzeichen: '{sep}'")
    print(f"  Jahre (erste 60 Zeilen): {years[:15]}")
    print(f"  --- erste 12 Zeilen ---")
    for i, ln in enumerate(lines[:12]):
        print(f"   {i:2d}| {ln[:160]}")
    print("="*90)
