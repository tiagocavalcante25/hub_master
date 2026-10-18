# -*- coding: utf-8 -*-
import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

base_dir = r"c:\Users\Admin\Downloads\INTERNATO GO\hub_master"

print("=========================================================")
print("=== SANITIZAÇÃO DE CARACTERES '$' E MENÇÕES A DOCENTE ===")
print("=========================================================\n")

def clean_latex_and_dollars(text):
    # Fix broken \r ightarrow or \rightarrow
    text = re.sub(r'\$\s*\\?r?ightarrow\s*\$', ' &rarr; ', text)
    text = re.sub(r'\\rightarrow', ' &rarr; ', text)
    text = re.sub(r'\$\s*\\leftarrow\s*\$', ' &larr; ', text)
    text = re.sub(r'\$\s*\\uparrow\s*\$', ' &uarr; ', text)
    text = re.sub(r'\\uparrow', ' &uarr; ', text)
    text = re.sub(r'\$\s*\\downarrow\s*\$', ' &darr; ', text)
    text = re.sub(r'\\downarrow', ' &darr; ', text)

    # Fix \ge, \le with numbers or alone
    text = re.sub(r'\$\s*\\ge\s*(\d+(?:[,\.]\d+)?(?:-\d+)?)\s*\$', r'&ge; \1', text)
    text = re.sub(r'\$\s*\\ge\s*(\d+)\\%?\s*\$', r'&ge; \1%', text)
    text = re.sub(r'\$\s*\\ge\s*\$', '&ge;', text)
    text = re.sub(r'\\ge\b', '&ge;', text)

    text = re.sub(r'\$\s*\\le\s*(\d+(?:[,\.]\d+)?(?:-\d+)?)\s*\$', r'&le; \1', text)
    text = re.sub(r'\$\s*\\le\s*(\d+)\\%?\s*\$', r'&le; \1%', text)
    text = re.sub(r'\$\s*\\le\s*\$', '&le;', text)
    text = re.sub(r'\\le\b', '&le;', text)

    # Fix Delta t
    text = re.sub(r'\$\s*\\Delta\s*t\s*=\s*0\s*\$', 'Δt = 0', text)
    text = re.sub(r'\$\s*\\Delta\s*t\s*>\s*20\s*\\text\{\s*a\s*\}\s*30\s*\\text\{\s*s\s*\}\s*\$', 'Δt &gt; 20 a 30s', text)
    text = re.sub(r'\$\s*\\Delta\s*t\s*>\s*20-30\s*\\text\{\s*s\s*\}\s*\$', 'Δt &gt; 20-30s', text)
    text = re.sub(r'\$\\Delta\s*t\$', 'Δt', text)

    # Fix pH
    text = re.sub(r'\$\s*pH\s*<\s*7,20\s*\$', 'pH &lt; 7,20', text)
    text = re.sub(r'\$\s*pH\s*&lt;\s*7,20\s*\$', 'pH &lt; 7,20', text)
    text = re.sub(r'\$\s*pH\s*\\le\s*7,20\s*\$', 'pH &le; 7,20', text)

    # Fix specific mangled strings like "$ 2º Respiração $"
    text = re.sub(r'\$\s*(\d+º\s+[^\$]+?)\s*\$', r' \1 ', text)

    # Fix residual $ around comparisons or numbers like $( \ge 24-25 semanas)$
    text = re.sub(r'\(\s*\$\s*&ge;\s*([^\$]+?)\s*\$\s*\)', r'(&ge; \1)', text)
    text = re.sub(r'\(\s*\$\s*&le;\s*([^\$]+?)\s*\$\s*\)', r'(&le; \1)', text)
    text = re.sub(r'\$\s*&ge;\s*([^\$]+?)\s*\$', r'&ge; \1', text)
    text = re.sub(r'\$\s*&le;\s*([^\$]+?)\s*\$', r'&le; \1', text)

    # Replace any leftover isolated dollar signs in text that aren't valid currency
    # E.g. $ followed by space or preceding space in HTML text
    text = re.sub(r'(?<![a-zA-Z0-9_])\$(?![a-zA-Z0-9_{])', '', text)

    return text

def remove_docente_references(text):
    text = re.sub(r'IDOMED\s*\(\s*Prof\.?\s*Phelipe\s*Balbi\s*\)', 'IDOMED • Diretrizes Especializadas em Medicina Fetal e Obstetrícia', text, flags=re.IGNORECASE)
    text = re.sub(r'Prof\.?\s*Phelipe\s*Balbi', 'Especialista em Obstetrícia', text, flags=re.IGNORECASE)
    text = re.sub(r'Phelipe\s*Balbi', 'Especialista em Obstetrícia', text, flags=re.IGNORECASE)
    text = re.sub(r'Conferir Análise do Professor', 'Conferir Parecer Obstétrico Oficial', text, flags=re.IGNORECASE)
    text = re.sub(r'Justificativa do Prof\.?\s*Phelipe\s*Balbi:', 'Justificativa Clínica e Parecer Obstétrico:', text, flags=re.IGNORECASE)
    text = re.sub(r'Justificativa do Professor:', 'Justificativa Clínica e Parecer Obstétrico:', text, flags=re.IGNORECASE)
    text = re.sub(r'Ver Traçado Comentado pelo Professor', 'Ver Traçado com Parecer Clínico', text, flags=re.IGNORECASE)
    text = re.sub(r'pelo Prof\.?\s*Phelipe\s*Balbi', 'pelo especialista', text, flags=re.IGNORECASE)
    text = re.sub(r'anotado pelo professor', 'comentado clinicamente', text, flags=re.IGNORECASE)
    text = re.sub(r'baseados na aula do Prof\.?\s*Phelipe\s*Balbi:?', 'baseados nas diretrizes obstétricas oficiais:', text, flags=re.IGNORECASE)
    text = re.sub(r'Zugaib 2020\s*/\s*Prof\.?\s*Phelipe\s*Balbi', 'Zugaib 2020 / Diretrizes Obstétricas Oficiais', text, flags=re.IGNORECASE)
    return text

print("1. Processando arquivos de site_obstetricia e site_parto_puerperio...")

target_files = [
    # site_obstetricia
    os.path.join(base_dir, "site_obstetricia", "components", "modulo-6-ctg-doppler.html"),
    os.path.join(base_dir, "site_obstetricia", "components", "modulo-5-dmg-preeclampsia.html"),
    os.path.join(base_dir, "site_obstetricia", "assets", "js", "app.js"),
    os.path.join(base_dir, "site_obstetricia", "index.html"),
    # site_parto_puerperio
    os.path.join(base_dir, "site_parto_puerperio", "components", "high-yield-summary.html"),
    os.path.join(base_dir, "site_parto_puerperio", "components", "modulo-18-puerperio.html"),
    os.path.join(base_dir, "site_parto_puerperio", "index.html")
]

for tf in target_files:
    if not os.path.exists(tf):
        continue
    with open(tf, 'r', encoding='utf-8') as f:
        orig = f.read()

    # Apply docente clean
    cleaned = remove_docente_references(orig)
    # Apply dollar clean
    if tf.endswith('.html'):
        cleaned = clean_latex_and_dollars(cleaned)
    elif tf.endswith('.js'):
        # For JS, carefully replace only LaTeX patterns in strings, NOT ${...}
        cleaned = re.sub(r'\$\s*\\ge\s*(\d+(?:[,\.]\d+)?(?:-\d+)?)\s*\$', r'&ge; \1', cleaned)
        cleaned = re.sub(r'\$\s*\\le\s*(\d+(?:[,\.]\d+)?(?:-\d+)?)\s*\$', r'&le; \1', cleaned)
        cleaned = re.sub(r'\\ge\b', '&ge;', cleaned)
        cleaned = re.sub(r'\\le\b', '&le;', cleaned)
        cleaned = re.sub(r'\$\s*&ge;\s*([^\$]+?)\s*\$', r'&ge; \1', cleaned)
        cleaned = re.sub(r'\$\s*&le;\s*([^\$]+?)\s*\$', r'&le; \1', cleaned)
        cleaned = re.sub(r'\$\s*\\rightarrow\s*\$', ' &rarr; ', cleaned)
        cleaned = re.sub(r'\\rightarrow', ' &rarr; ', cleaned)

    if cleaned != orig:
        with open(tf, 'w', encoding='utf-8') as f:
            f.write(cleaned)
        print(f"[ATUALIZADO] {os.path.relpath(tf, base_dir)}")
    else:
        print(f"[SEM ALTERAÇÕES] {os.path.relpath(tf, base_dir)}")

print("\nProcessamento concluído com sucesso!")
