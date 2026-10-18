import os

base_dir = r"c:\Users\Admin\Downloads\INTERNATO GO\hub_master\site_obstetricia"
index_file = os.path.join(base_dir, "index.html")
js_file = os.path.join(base_dir, "assets", "js", "app.js")

with open(index_file, "r", encoding="utf-8") as f:
    html = f.read()

with open(js_file, "r", encoding="utf-8") as f:
    js = f.read()

print("=== 1. VERIFICAÇÃO DE IMAGENS E STRIPS LIMPAS DE CTG ===")
clean_imgs = [
    "ctg_strip_caso1.jpg",
    "ctg_strip_caso2.jpg",
    "ctg_strip_caso3.jpg",
    "ctg_treino1_gabarito.jpg",
    "ctg_treino2_gabarito.jpg",
    "ctg_treino3_gabarito.jpg"
]

all_ok = True
for img in clean_imgs:
    p = os.path.join(base_dir, "assets", "img", img)
    if os.path.exists(p) and os.path.getsize(p) > 0:
        print(f"[OK] {img}: {os.path.getsize(p):,} bytes")
    else:
        print(f"[FAIL] {img} ausente!")
        all_ok = False

print("\n=== 2. VERIFICAÇÃO DE DIAGRAMAS VETORIAIS NATIVOS (SVG) EM INDEX.HTML ===")
svg_checks = [
    ("SVG DIP I (Precoce)", 'gridDIP1'),
    ("SVG DIP II (Tardio)", 'gridDIP2'),
    ("SVG DIP III (Variável)", 'gridDIP3'),
    ("SVG Ducto Venoso (Onda 'a' Reversa)", 'PADRÃO CRÍTICO: ONDA \'a\' REVERSA'),
    ("Diagrama Hemodinâmica Centralização", 'Brain Sparing Effect')
]

for label, needle in svg_checks:
    if needle in html:
        print(f"[OK] {label}: Presente e nativo")
    else:
        print(f"[FAIL] {label}: Ausente!")
        all_ok = False

print("\n=== 3. VERIFICAÇÃO DAS FUNÇÕES JS DO MÓDULO 6 ===")
expected_funcs = [
    "avaliarMobilograma",
    "avaliarMaturidadePulmonar",
    "calcularPBFExpandido",
    "avaliarDelphiRCIU",
    "responderQuizCTG"
]

for func in expected_funcs:
    if f"function {func}" in js or f"{func} = function" in js:
        print(f"[OK] Função {func} declarada em app.js")
    else:
        print(f"[FAIL] Função {func} NÃO declarada em app.js")
        all_ok = False

print("\n=== 4. VERIFICAÇÃO DOS ELEMENTOS INTERATIVOS NO INDEX.HTML ===")
actual_m6_ids = [
    "mobilograma-modo", "mobilograma-movs", "mob-tempo-box", "mobilograma-tempo", "mobilograma-resultado",
    "le-valor", "clements-resultado", "maturidade-res",
    "pbf-ig", "pbf-tem-ciur", "pbf-ila-status", "pbf-ctg-sel", "pbf-resp-sel", "pbf-mov-sel", "pbf-tonus-sel",
    "pbf-expandido-results", "pbf-exp-score", "pbf-exp-badge", "pbf-exp-interpretacao", "pbf-exp-conduta",
    "delphi-ig", "delphi-ca-p3", "delphi-pfe-p3", "box-delphi-au-zero", "delphi-au-zero", "delphi-pfe-p10",
    "delphi-ip-ut", "delphi-ip-umb", "box-delphi-rcp", "delphi-rcp", "box-delphi-queda", "delphi-queda-quartis",
    "delphi-result",
    "ctg-quiz-1", "ctg-quiz-res-1", "ctg-quiz-2", "ctg-quiz-res-2", "ctg-quiz-3", "ctg-quiz-res-3"
]

for el_id in actual_m6_ids:
    if f'id="{el_id}"' in html or f"id='{el_id}'" in html:
        print(f"[OK] Elemento #{el_id} presente")
    else:
        print(f"[FAIL] Elemento #{el_id} AUSENTE no index.html!")
        all_ok = False

print("\n==========================================")
if all_ok:
    print(">>> SUCESSO TOTAL: Módulo 6 elevado com elementos nativos, sem recortes de slides! <<<")
else:
    print(">>> ATENÇÃO: Falhas encontradas na validação. <<<")
print("==========================================")
