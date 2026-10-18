import fitz
import os

pdf_path = r"C:\Users\Admin\.gemini\antigravity\brain\c8a7917c-8cbc-4119-b7c7-b6bf1409ed34\.user_uploaded\media_1792074989961_5a014125.pdf"
img_dir = r"C:\Users\Admin\Downloads\INTERNATO GO\hub_master\site_obstetricia\assets\img"
os.makedirs(img_dir, exist_ok=True)

doc = fitz.open(pdf_path)
print(f"Total pages: {len(doc)}")

# Pages to export (0-indexed):
# 12 (DIP I - slide 13)
# 13 (DIP II - slide 14)
# 14 (DIP III - slide 15)
# 17 (Adaptacao hipoxia FEBRASGO - slide 18)
# 26 (Centralizacao - slide 27)
# 27 (Ducto venoso - slide 28)
# 28 (Delphi RCIU - slide 29)
# 35, 36 (Treino 1: DIP III desfavoravel - slides 36, 37)
# 37, 38 (Treino 2: DIP I precoce - slides 38, 39)
# 39, 40 (Treino 3: Categoria 1 normal - slides 40, 41)

pages_to_extract = {
    12: "ctg_dip1_fisiologico.jpg",
    13: "ctg_dip2_tardio.jpg",
    14: "ctg_dip3_variavel.jpg",
    17: "adaptacao_hipoxia_febrasgo.jpg",
    26: "centralizacao_fetal_rezende.jpg",
    27: "ducto_venoso_rezende.jpg",
    28: "criterios_delphi_rciu.jpg",
    35: "ctg_treino1_desafio.jpg",
    36: "ctg_treino1_gabarito.jpg",
    37: "ctg_treino2_desafio.jpg",
    38: "ctg_treino2_gabarito.jpg",
    39: "ctg_treino3_desafio.jpg",
    40: "ctg_treino3_gabarito.jpg",
}

for page_idx, filename in pages_to_extract.items():
    if page_idx < len(doc):
        page = doc[page_idx]
        pix = page.get_pixmap(dpi=150)
        dest = os.path.join(img_dir, filename)
        pix.save(dest)
        print(f"Salvo: {filename} ({pix.width}x{pix.height})")
    else:
        print(f"Pagina {page_idx} fora dos limites!")

print("Extracao concluida com sucesso!")
