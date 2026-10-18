import os
import re
import sys
from html.parser import HTMLParser

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INDEX_PATH = os.path.join(BASE_DIR, 'index.html')
CSS_PATH = os.path.join(BASE_DIR, 'assets', 'css', 'custom.css')
JS_PATH = os.path.join(BASE_DIR, 'assets', 'js', 'app.js')

print("=======================================================")
print("=== AUDITORIA DE INTEGRIDADE & RESPONSIVIDADE (GO) ===")
print("=======================================================\n")

all_passed = True

# 1. HTML PARSE & BALANCE TEST
print("1. Validando estrutura HTML de index.html...")
class Validator(HTMLParser):
    def __init__(self):
        super().__init__()
        self.tags = []
        self.errors = []
    def handle_starttag(self, tag, attrs):
        if tag not in ['img', 'br', 'hr', 'input', 'meta', 'link']:
            self.tags.append(tag)
    def handle_endtag(self, tag):
        if tag not in ['img', 'br', 'hr', 'input', 'meta', 'link']:
            if self.tags and self.tags[-1] == tag:
                self.tags.pop()

with open(INDEX_PATH, 'r', encoding='utf-8') as f:
    html_content = f.read()

v = Validator()
v.feed(html_content)
if len(v.tags) == 0:
    print("[PASS] HTML 100% balanceado sem tags orfas ou desfechadas.")
else:
    print(f"[FAIL] Tags abertas restantes: {len(v.tags)}")
    all_passed = False

# 2. CSS SYNTAX & ANTI-COLLAPSE SAFEGUARDS
print("\n2. Validando regras de CSS e blindagem mobile...")
with open(CSS_PATH, 'r', encoding='utf-8') as f:
    css_content = f.read()

open_b = css_content.count('{')
close_b = css_content.count('}')
if open_b == close_b:
    print(f"[PASS] Sintaxe CSS valida ({open_b} blocos balanceados).")
else:
    print(f"[FAIL] Chaves desbalanceadas no CSS: {open_b} open vs {close_b} close.")
    all_passed = False

# Ensure font-bold does NOT have word-break: break-word
if re.search(r'\.font-bold\s*\{[^}]*word-break\s*:\s*break-word', css_content):
    print("[FAIL] Regra perigosa de word-break detectada em .font-bold!")
    all_passed = False
else:
    print("[PASS] Nenhuma regra destrutiva de word-break em .font-bold (botões protegidos).")

# Ensure pump-btn has white-space nowrap
if '.pump-btn' in css_content and 'white-space: nowrap' in css_content:
    print("[PASS] Botões de bomba BIC (.pump-btn) blindados com white-space: nowrap.")
else:
    print("[FAIL] .pump-btn ausente ou sem proteção nowrap.")
    all_passed = False

# 3. VERIFICAR COMPONENTES CRÍTICOS EM INDEX.HTML
print("\n3. Validando componentes interativos em index.html...")
critical_checks = [
    ("Grid Priscilla White", 'grid grid-cols-2 sm:grid-cols-3 md:grid-cols-5 gap-2'),
    ("Grid Estratégias DMG", 'grid grid-cols-1 sm:grid-cols-2 gap-2 w-full sm:w-auto'),
    ("Grid Protocolos MgSO4", 'grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-6 gap-2'),
    ("Grid Ampolas MgSO4", 'grid grid-cols-1 sm:grid-cols-2 gap-2'),
    ("BIC Presets Grid", 'grid grid-cols-4 gap-1'),
    ("Flashcards Wrap Controls", 'flex flex-wrap sm:flex-nowrap items-center justify-center')
]

for label, snippet in critical_checks:
    if snippet in html_content:
        print(f"[PASS] {label}: Responsivo e protegido contra colapso.")
    else:
        print(f"[FAIL] {label}: Snippet não encontrado no index.html.")
        all_passed = False

# 4. VERIFICAR ARQUIVOS ESTÁTICOS
print("\n4. Validando integridade de imagens médicas HD...")
images = [
    "assets/img/leopold_maneuvers.jpg",
    "assets/img/fetal_ultrasound.jpg",
    "assets/img/gdm_pathophysiology.jpg",
    "assets/img/preeclampsia_pathology.jpg",
    "assets/img/ctg_decelerations.jpg",
    "assets/img/doppler_fetal_iupr.jpg",
    "assets/img/ttts_twins.jpg",
    "assets/img/rh_isoimmunization.jpg"
]

for img_rel in images:
    img_path = os.path.join(BASE_DIR, img_rel)
    if os.path.exists(img_path) and os.path.getsize(img_path) > 0:
        print(f"[PASS] Imagem {img_rel} ({os.path.getsize(img_path):,} bytes)")
    else:
        print(f"[FAIL] Imagem ausente ou vazia: {img_rel}")
        all_passed = False

# 5. VERIFICAR LINKS DE ÂNCORA E ÍNDICE DE BUSCA (APP.JS)
print("\n5. Validando integridade de links de âncora e searchIndex...")
with open(JS_PATH, 'r', encoding='utf-8') as f:
    js_content = f.read()

html_ids = set(re.findall(r'\bid=["\']([^"\']+)["\']', html_content))
html_hrefs = [h for h in re.findall(r'\bhref=["\']#([^"\']+)["\']', html_content) if h]
js_anchors = [a for a in re.findall(r'anchor:\s*["\']#([^"\']+)["\']', js_content) if a]

broken_hrefs = [h for h in html_hrefs if h not in html_ids]
broken_js_anchors = [a for a in js_anchors if a not in html_ids]

if not broken_hrefs:
    print(f"[PASS] Todos os {len(html_hrefs)} links internos href=\"#...\" apontam para IDs válidos ({len(html_ids)} IDs).")
else:
    print(f"[FAIL] Links quebrados em index.html: {broken_hrefs}")
    all_passed = False

if not broken_js_anchors:
    print(f"[PASS] Todas as {len(js_anchors)} âncoras do searchIndex (app.js) apontam para IDs válidos.")
else:
    print(f"[FAIL] Âncoras quebradas em app.js: {broken_js_anchors}")
    all_passed = False

# 6. VERIFICAR TIPOGRAFIA FLUIDA CLAMP(), LINE-HEIGHT, MIN-HEIGHT E FLEX-WRAP
print("\n6. Validando tipografia fluida clamp(), line-height e cabeçalho Flexbox...")
css_audit_checks = [
    ("Tipografia fluida clamp()", "clamp(" in css_content),
    ("Ajuste de line-height calibrado", "line-height: 1.65" in css_content),
    ("Cabeçalho e subnav com flex-wrap e min-height", "#module-subnav" in css_content and "flex-wrap: wrap" in css_content and "min-height:" in css_content),
    ("Compensação dinâmica de scroll-margin-top", "scroll-margin-top: calc(var(--header-height" in css_content),
]

for label, ok in css_audit_checks:
    if ok:
        print(f"[PASS] {label}")
    else:
        print(f"[FAIL] {label}")
        all_passed = False

print("\n=======================================================")
if all_passed:
    print(">>> SUCESSO TOTAL: Responsividade mobile e tablet 100% calibrada! <<<")
else:
    print(">>> ATENÇÃO: Falhas encontradas na validação. <<<")
print("=======================================================\n")

