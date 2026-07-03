import fitz, os
ROOT=r"C:\Users\maxot\OneDrive\Desktop\datastory_school"
OUT=os.path.join(ROOT,"qa_slides"); os.makedirs(OUT,exist_ok=True)
doc=fitz.open(os.path.join(ROOT,"Schulabschluss_DataStory_Praesentation.pdf"))
for i,page in enumerate(doc,1):
    pix=page.get_pixmap(dpi=110)
    pix.save(os.path.join(OUT,f"slide-{i:02d}.jpg"))
print("Folien gerendert:",len(doc),"->",OUT)
