"""
verify_site.py - Verificador de Integridade e Responsividade do Portal
"""

import os
import re
import sys

# Garante codificação UTF-8 no stdout do Windows
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

SITE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INDEX_PATH = os.path.join(SITE_DIR, "index.html")
CSS_PATH = os.path.join(SITE_DIR, "assets", "css", "custom.css")
IMG_DIR = os.path.join(SITE_DIR, "assets", "img")
NOJEKYLL = os.path.join(SITE_DIR, ".nojekyll")

def run_checks():
    print("=== VERIFICAÇÃO DO PORTAL SITE_ONCO_MASTO_CIRURGIA ===")
    
    # 1. Checa existência dos arquivos básicos
    assert os.path.exists(INDEX_PATH), "index.html não encontrado!"
    assert os.path.exists(CSS_PATH), "custom.css não encontrado!"
    assert os.path.exists(NOJEKYLL), ".nojekyll não encontrado!"
    print("OK: Arquivos base presentes (index.html, custom.css, .nojekyll).")
    
    # 2. Checa regras essenciais de CSS
    with open(CSS_PATH, 'r', encoding='utf-8') as f:
        css = f.read()
    assert "overflow-x: hidden" in css, "Falta overflow-x: hidden no CSS!"
    assert "word-wrap: break-word" in css, "Falta word-wrap: break-word no CSS!"
    print("OK: Regras críticas de overflow-x e word-wrap presentes no CSS.")
    
    # 3. Checa tags de imagem no index.html e valida caminhos no disco
    with open(INDEX_PATH, 'r', encoding='utf-8') as f:
        html = f.read()
        
    imgs = re.findall(r'src=["\'](assets/img/[^"\']+)["\']', html)
    print(f"Total de referências a imagens no index.html: {len(imgs)}")
    
    missing = []
    for img_rel in imgs:
        full_path = os.path.join(SITE_DIR, img_rel.replace("/", os.sep))
        if not os.path.exists(full_path):
            missing.append(img_rel)
            
    if missing:
        print("ERRO: Imagens ausentes:", missing)
        raise FileNotFoundError(f"Imagens ausentes encontradas: {missing}")
    else:
        print("OK: 100% das imagens e infográficos referenciados existem no disco!")
        
    # 4. Checa navbar fixa
    assert "fixed top-0" in html, "Navbar fixa top-0 não encontrada no HTML!"
    print("OK: Navbar superior fixa com position: fixed confirmada.")
    
    print("\nTODOS OS TESTES PASSARAM COM SUCESSO! O site está pronto para deploy no GitHub Pages.")

if __name__ == "__main__":
    run_checks()
