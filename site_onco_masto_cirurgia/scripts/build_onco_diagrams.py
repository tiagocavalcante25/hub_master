"""
build_onco_diagrams.py - Gerador de Infográficos Médicos de Alta Definição
Parte 7: Oncologia Ginecológica, Mastologia e Cirurgia Ginecológica
Padronizado para Internato GO / USMLE / FEBRASGO / INCA / FIGO / ACOG
"""

import os
from PIL import Image, ImageDraw, ImageFont

IMG_DIR = r"c:\Users\Admin\Downloads\INTERNATO GO\site_onco_masto_cirurgia\assets\img"
os.makedirs(IMG_DIR, exist_ok=True)

# Fontes do Windows
FONT_BOLD = r"C:\Windows\Fonts\segoeuib.ttf"
FONT_REG = r"C:\Windows\Fonts\segoeui.ttf"
FONT_ITALIC = r"C:\Windows\Fonts\segoeuii.ttf"

def get_font(size, bold=False, italic=False):
    path = FONT_BOLD if bold else (FONT_ITALIC if italic else FONT_REG)
    try:
        return ImageFont.truetype(path, size)
    except:
        return ImageFont.load_default()

def draw_header(draw, width, title, subtitle, badge_text="ONCOLOGIA • MASTOLOGIA • CIRURGIA"):
    draw.rectangle([0, 0, width, 110], fill="#0f172a")
    draw.rectangle([0, 106, width, 110], fill="#e11d48")
    
    # Badge
    f_badge = get_font(13, bold=True)
    draw.rounded_rectangle([30, 20, 310, 44], radius=6, fill="#e11d48")
    draw.text((42, 23), badge_text, fill="#ffffff", font=f_badge)
    
    # Título e Subtítulo
    f_title = get_font(26, bold=True)
    f_sub = get_font(15, italic=False)
    draw.text((30, 52), title, fill="#ffffff", font=f_title)
    draw.text((30, 84), subtitle, fill="#94a3b8", font=f_sub)

def draw_footer(draw, width, height, text="Guia Obstetrícia & Ginecologia Parte 7 — Portal Interativo de Decisão Clínica"):
    draw.rectangle([0, height - 35, width, height], fill="#0f172a")
    f = get_font(12, italic=True)
    draw.text((30, height - 25), text, fill="#94a3b8", font=f)

# ==============================================================================
# 1. HPV & ONCOGÊNESE MOLECULAR (E6/p53, E7/Rb, p16)
# ==============================================================================
def create_diagram_hpv_oncogenese():
    W, H = 1300, 860
    im = Image.new("RGB", (W, H), "#f8fafc")
    draw = ImageDraw.Draw(im)
    
    draw_header(draw, W, "ONCOGÊNESE MOLECULAR DO HPV & ZONA DE TRANSFORMAÇÃO", 
                "Mecanismos E6/p53 e E7/pRb • Superexpressão de p16INK4a • Histologia LAST/Bethesda")
    
    # Card 1: Oncoproteína E6
    draw.rounded_rectangle([30, 130, 420, 800], radius=12, fill="#ffffff", outline="#cbd5e1", width=2)
    draw.rounded_rectangle([30, 130, 420, 175], radius=10, fill="#be123c")
    draw.text((45, 142), "1. ONCOPROTEÍNA E6 (p53)", fill="#ffffff", font=get_font(17, bold=True))
    
    y = 195
    itens_e6 = [
        ("Alvo Molecular:", "Proteína supressora de tumor p53"),
        ("Mecanismo:", "Liga-se à ubiquitina-ligase E6AP"),
        ("Consequência:", "Degradação proteassomal da p53"),
        ("Efeito Biológico:", "Perda da apoptose e do reparo do DNA"),
        ("Ativação Adicional:", "Superexpressão da telomerase (hTERT)"),
        ("🎈 Didática (5 anos):", "A mãozinha E6 rouba o freio que\nmanda consertar estragos na célula!"),
        ("Marcador Clínico:", "Células com dano genético acumulam\nmutações sem sofrer morte celular.")
    ]
    for tit, desc in itens_e6:
        draw.text((45, y), tit, fill="#881337", font=get_font(14, bold=True))
        y += 20
        draw.text((45, y), desc, fill="#334155", font=get_font(13))
        y += 45

    # Card 2: Oncoproteína E7
    draw.rounded_rectangle([450, 130, 840, 800], radius=12, fill="#ffffff", outline="#cbd5e1", width=2)
    draw.rounded_rectangle([450, 130, 840, 175], radius=10, fill="#1e293b")
    draw.text((465, 142), "2. ONCOPROTEÍNA E7 (Rb / p16)", fill="#ffffff", font=get_font(17, bold=True))
    
    y = 195
    itens_e7 = [
        ("Alvo Molecular:", "Proteína do retinoblastoma fosforilada (pRb)"),
        ("Mecanismo:", "Liga-se à pRb e desloca o fator E2F livre"),
        ("Consequência:", "Entrada contínua na Fase S do ciclo celular"),
        ("Superexpressão p16:", "Perda do Rb gera acúmulo difuso de p16"),
        ("Imuno-histoquímica:", "p16 em bloco = infecção transformante"),
        ("🎈 Didática (5 anos):", "A mãozinha E7 rouba o pedal de freio\nque diz 'espere, não se divida agora!'"),
        ("Integração Viral:", "Perda do gene E2 desreprime E6 e E7.")
    ]
    for tit, desc in itens_e7:
        draw.text((465, y), tit, fill="#0f172a", font=get_font(14, bold=True))
        y += 20
        draw.text((465, y), desc, fill="#334155", font=get_font(13))
        y += 45

    # Card 3: Histologia & Evolução Clínica
    draw.rounded_rectangle([870, 130, 1270, 800], radius=12, fill="#ffffff", outline="#cbd5e1", width=2)
    draw.rounded_rectangle([870, 130, 1270, 175], radius=10, fill="#047857")
    draw.text((885, 142), "3. HISTOLOGIA & LAST (NIC 1, 2, 3)", fill="#ffffff", font=get_font(17, bold=True))
    
    y = 195
    itens_hist = [
        ("NIC 1 (LSIL):", "Atipias no terço inferior do epitélio.\nRegressão espontânea em ~60% dos casos."),
        ("NIC 2 (HSIL):", "Atipias nos dois terços inferiores.\nSe p16 positivo = lesão precursora verdadeira."),
        ("NIC 3 (HSIL):", "Atipias em toda a espessura do epitélio.\nMembrana basal intacta. Risco invasor >12%."),
        ("Carcinoma Invasor:", "Rompimento da membrana basal.\nDisseminação para o estroma cervical."),
        ("Zona de Transformação:", "Metaplasia escamosa ativa entre ecto\ne endocérvice: o campo de entrada do vírus."),
        ("Pegadinha de Prova:", "Preservativo reduz mas não elimina HPV!")
    ]
    for tit, desc in itens_hist:
        draw.text((885, y), tit, fill="#065f46", font=get_font(14, bold=True))
        y += 20
        draw.text((885, y), desc, fill="#334155", font=get_font(13))
        y += 45
        
    draw_footer(draw, W, H)
    im.save(os.path.join(IMG_DIR, "hpv_oncogenese_molecular_e6_e7.jpg"), quality=95)

# ==============================================================================
# 2. RASTREAMENTO DO COLO: ASCCP 2019 vs INCA 2024-2025
# ==============================================================================
def create_diagram_rastreamento_colo():
    W, H = 1300, 860
    im = Image.new("RGB", (W, H), "#f8fafc")
    draw = ImageDraw.Draw(im)
    
    draw_header(draw, W, "ALGORITMOS DE RASTREAMENTO DO CÂNCER DE COLO UTERINO", 
                "Diretrizes INCA 2024–2025 (DNA-HPV Primário) vs ASCCP 2019 (Manejo Baseado em Risco)")
    
    # Coluna 1: Brasil / SUS
    draw.rounded_rectangle([30, 130, 630, 800], radius=12, fill="#ffffff", outline="#cbd5e1", width=2)
    draw.rounded_rectangle([30, 130, 630, 175], radius=10, fill="#0369a1")
    draw.text((45, 142), "DIRETRIZES BRASIL (INCA / SUS)", fill="#ffffff", font=get_font(17, bold=True))
    
    y = 195
    itens_br = [
        ("Faixa Etária de Rastreamento:", "25 aos 64 anos de idade após início da atividade sexual."),
        ("Transição DNA-HPV (2024-2025):", "Teste de DNA-HPV primário a cada 5 anos no SUS."),
        ("Citologia Convencional (Papanicolau):", "Anual nos 2 primeiros anos; se normais, a cada 3 anos."),
        ("Conduta em ASC-US:", "< 25 anos: repetir em 3 anos.\n25 a 29 anos: repetir em 12 meses.\n≥ 30 anos: repetir em 6 meses (ou colposcopia se 2º alterado)."),
        ("Conduta em LSIL:", "< 25 anos: repetir em 3 anos.\n≥ 25 anos: repetir em 6 meses."),
        ("Conduta em HSIL / ASC-H / AGC:", "Colposcopia imediata em qualquer idade (≥ 25 anos)."),
        ("Populações Especiais (HIV/Imunossuprimidas):", "Citologia semestral no 1º ano; após, anual se CD4 > 200.")
    ]
    for tit, desc in itens_br:
        draw.text((45, y), tit, fill="#075985", font=get_font(14, bold=True))
        y += 20
        draw.text((45, y), desc, fill="#334155", font=get_font(13))
        y += 45

    # Coluna 2: EUA / ASCCP / USPSTF
    draw.rounded_rectangle([660, 130, 1270, 800], radius=12, fill="#ffffff", outline="#cbd5e1", width=2)
    draw.rounded_rectangle([660, 130, 1270, 175], radius=10, fill="#475569")
    draw.text((675, 142), "DIRETRIZES INTERNACIONAIS (USPSTF / ASCCP)", fill="#ffffff", font=get_font(17, bold=True))
    
    y = 195
    itens_us = [
        ("21 a 29 anos (USPSTF):", "Citologia isolada a cada 3 anos (HPV não recomendado)."),
        ("30 a 65 anos (USPSTF):", "Três opções válidas:\n1. DNA-HPV primário a cada 5 anos (preferencial ACS)\n2. Co-teste (Citologia + HPV) a cada 5 anos\n3. Citologia isolada a cada 3 anos"),
        ("Manejo ASCCP Baseado em Risco:", "Calcula o risco estimado imediato de NIC 3+:\n• Risco ≥ 4%: Colposcopia imediata.\n• Risco 25 a 59%: Tratamento excisional ou colposcopia.\n• Risco ≥ 60%: Tratamento excisional direto (Ver e Tratar)."),
        ("HPV 16 ou 18 Positivos:", "Encaminhamento direto para Colposcopia imediata."),
        ("Parada do Rastreamento:", "Aos 65 anos se rastreamento prévio adequado nos últimos 10 anos.")
    ]
    for tit, desc in itens_us:
        draw.text((675, y), tit, fill="#1e293b", font=get_font(14, bold=True))
        y += 20
        draw.text((675, y), desc, fill="#334155", font=get_font(13))
        y += 45
        
    draw_footer(draw, W, H)
    im.save(os.path.join(IMG_DIR, "algoritmo_rastreamento_colo_asccp_inca.jpg"), quality=95)

# ==============================================================================
# 3. SISTEMA BI-RADS 6ª EDIÇÃO & CONDUTAS
# ==============================================================================
def create_diagram_birads():
    W, H = 1300, 880
    im = Image.new("RGB", (W, H), "#f8fafc")
    draw = ImageDraw.Draw(im)
    
    draw_header(draw, W, "SISTEMA BI-RADS (6ª EDIÇÃO ACR) & CONDUTAS CLÍNICAS", 
                "Classificação Radiológica • Risco de Malignidade • Recomendações e Condutas Propedêuticas")
    
    categorias = [
        ("BI-RADS 0", "Incompleto", "Exame adicional (USG, compressão, magnificação ou exames anteriores)", "N/A", "#64748b"),
        ("BI-RADS 1", "Negativo / Normal", "Rastreamento habitual por faixa etária", "0%", "#10b981"),
        ("BI-RADS 2", "Achado Benigno", "Rastreamento habitual (cisto simples, fibroadenoma calcificado)", "0%", "#059669"),
        ("BI-RADS 3", "Provavelmente Benigno", "Controle radiológico precoce semestral por 2 a 3 anos", "< 2%", "#eab308"),
        ("BI-RADS 4", "Suspeito de Malignidade", "Biópsia por agulha grossa (Core Biopsy ou Mamotomia)", "2% a 95%", "#f97316"),
        ("• 4A", "Baixa suspeita", "Biópsia percutânea", "2% a 10%", "#fb923c"),
        ("• 4B", "Média suspeita", "Biópsia percutânea", "10% a 50%", "#f97316"),
        ("• 4C", "Alta suspeita", "Biópsia percutânea", "50% a 95%", "#ea580c"),
        ("BI-RADS 5", "Altamente Suspeito", "Biópsia imediata (massa espiculada, microcalcificações pleomórficas)", "> 95%", "#dc2626"),
        ("BI-RADS 6", "Malignidade Confirmada", "Estadiamento, planejamento cirúrgico e oncológico sistêmico", "100%", "#7f1d1d")
    ]
    
    y = 140
    # Header da tabela
    draw.rectangle([30, y, 1270, y + 40], fill="#0f172a")
    draw.text((45, y + 10), "CATEGORIA", fill="#ffffff", font=get_font(14, bold=True))
    draw.text((230, y + 10), "INTERPRETAÇÃO", fill="#ffffff", font=get_font(14, bold=True))
    draw.text((480, y + 10), "CONDUTA RECOMENDADA", fill="#ffffff", font=get_font(14, bold=True))
    draw.text((1100, y + 10), "RISCO DE CÂNCER", fill="#ffffff", font=get_font(14, bold=True))
    y += 45
    
    for cat, inter, cond, risco, cor in categorias:
        h_row = 48 if not cat.startswith("•") else 38
        draw.rounded_rectangle([30, y, 1270, y + h_row], radius=6, fill="#ffffff", outline="#e2e8f0", width=1)
        draw.rectangle([30, y, 40, y + h_row], fill=cor)
        
        f_cat = get_font(14, bold=True)
        f_txt = get_font(13)
        draw.text((50, y + 12), cat, fill="#0f172a", font=f_cat)
        draw.text((230, y + 12), inter, fill="#334155", font=f_txt)
        draw.text((480, y + 12), cond, fill="#334155", font=f_txt)
        draw.text((1110, y + 12), risco, fill=cor, font=get_font(14, bold=True))
        y += h_row + 8

    # Nota USPSTF 2024
    draw.rounded_rectangle([30, y + 10, 1270, H - 50], radius=10, fill="#f1f5f9", outline="#cbd5e1", width=1)
    draw.text((45, y + 20), "⚠️ ATUALIZAÇÃO DE RASTREAMENTO USPSTF 2024 vs BRASIL:", fill="#b91c1c", font=get_font(14, bold=True))
    draw.text((45, y + 45), "• USPSTF 2024 (EUA): Mamografia bienal dos 40 aos 74 anos para todas as mulheres de risco habitual.", fill="#1e293b", font=get_font(13))
    draw.text((45, y + 68), "• MS / INCA (Brasil): Mamografia bienal dos 50 aos 69 anos. SBM / FEBRASGO / CBR recomendam anual a partir dos 40 anos.", fill="#1e293b", font=get_font(13))

    draw_footer(draw, W, H)
    im.save(os.path.join(IMG_DIR, "birads_classificacao_condutas.jpg"), quality=95)

# ==============================================================================
# 4. SUBTIPOS MOLECULARES DO CÂNCER DE MAMA & TERAPIA
# ==============================================================================
def create_diagram_subtipos_mama():
    W, H = 1300, 860
    im = Image.new("RGB", (W, H), "#f8fafc")
    draw = ImageDraw.Draw(im)
    
    draw_header(draw, W, "SUBTIPOS MOLECULARES DO CÂNCER DE MAMA & TERAPIA SISTÊMICA", 
                "Receptores Hormonais (RE/RP) • HER2 • Ki-67 • Ensaio ACOSOG Z0011 & Terapias-Alvo")
    
    cards = [
        ("LUMINAL A", "RE+, RP+, HER2-, Ki-67 baixo (<20%)", "Melhor prognóstico global", 
         "Hormonoterapia (Tamoxifeno / Anastrozol)", "Quimioterapia geralmente dispensável", "#0284c7"),
        ("LUMINAL B", "RE+, RP baixo ou HER2+ ou Ki-67 alto (≥20%)", "Mais agressivo que Luminal A", 
         "Hormonoterapia + Quimioterapia frequente", "Se HER2+, associar Trastuzumabe", "#0d9488"),
        ("HER2 ENRIQUECIDO", "RE-, RP-, HER2 superexpresso (3+ ou FISH+)", "Crescimento rápido e invasivo", 
         "Terapia anti-HER2 dupla (Trastuzumabe + Pertuzumabe)", "Excelente resposta patológica completa (pCR)", "#d97706"),
        ("TRIPLO-NEGATIVO", "RE-, RP-, HER2- (Basal-like)", "Mais frequente em jovens e BRCA1", 
         "Quimioterapia neoadjuvante + Pembrolizumabe", "Sem terapia-alvo hormonal ou anti-HER2", "#dc2626")
    ]
    
    x = 30
    w_card = 295
    for tit, biom, prog, trat1, trat2, cor in cards:
        draw.rounded_rectangle([x, 130, x + w_card, 680], radius=12, fill="#ffffff", outline="#cbd5e1", width=2)
        draw.rounded_rectangle([x, 130, x + w_card, 185], radius=10, fill=cor)
        draw.text((x + 15, 145), tit, fill="#ffffff", font=get_font(18, bold=True))
        
        y = 205
        draw.text((x + 15, y), "Perfil Imuno-histoquímico:", fill="#0f172a", font=get_font(13, bold=True))
        y += 22
        draw.text((x + 15, y), biom, fill="#475569", font=get_font(12))
        y += 50
        
        draw.text((x + 15, y), "Prognóstico:", fill="#0f172a", font=get_font(13, bold=True))
        y += 22
        draw.text((x + 15, y), prog, fill="#475569", font=get_font(12))
        y += 50
        
        draw.text((x + 15, y), "Tratamento Sistêmico:", fill="#0f172a", font=get_font(13, bold=True))
        y += 22
        draw.text((x + 15, y), trat1, fill="#047857", font=get_font(12, bold=True))
        y += 35
        draw.text((x + 15, y), trat2, fill="#334155", font=get_font(12))
        
        x += w_card + 20

    # Banner ACOSOG Z0011
    draw.rounded_rectangle([30, 705, 1270, 805], radius=10, fill="#f8fafc", outline="#0284c7", width=2)
    draw.text((45, 718), "📌 ENSAIO ACOSOG Z0011 (PÉROLA DA RESIDÊNCIA E USMLE):", fill="#0369a1", font=get_font(14, bold=True))
    draw.text((45, 745), "Em pacientes com tumores T1-T2 submetidas a Cirurgia Conservadora + Radioterapia de campo total, com 1 a 2 linfonodos sentinela", fill="#1e293b", font=get_font(13))
    draw.text((45, 768), "comprometidos e sem invasão extracapsular macroscópica: O ESVAZIAMENTO AXILAR COMPLETO PODE SER DISPENSADO com segurança!", fill="#b91c1c", font=get_font(13, bold=True))

    draw_footer(draw, W, H)
    im.save(os.path.join(IMG_DIR, "cancer_mama_subtipos_moleculares.jpg"), quality=95)

# ==============================================================================
# 5. CÂNCER DE ENDOMÉTRIO & CLASSIFICAÇÃO MOLECULAR FIGO 2023
# ==============================================================================
def create_diagram_endometrio_molecular():
    W, H = 1300, 860
    im = Image.new("RGB", (W, H), "#f8fafc")
    draw = ImageDraw.Draw(im)
    
    draw_header(draw, W, "CÂNCER DE ENDOMÉTRIO & CLASSIFICAÇÃO MOLECULAR (TCGA / FIGO 2023)", 
                "Investigação do Sangramento Pós-Menopausa • 4 Subtipos Moleculares • Imunoterapia")
    
    # Coluna 1: Investigação Inicial
    draw.rounded_rectangle([30, 130, 420, 800], radius=12, fill="#ffffff", outline="#cbd5e1", width=2)
    draw.rounded_rectangle([30, 130, 420, 175], radius=10, fill="#1e293b")
    draw.text((45, 142), "INVESTIGAÇÃO DO SANGRAMENTO", fill="#ffffff", font=get_font(16, bold=True))
    
    y = 195
    itens_inv = [
        ("Regra de Ouro:", "Sangramento na pós-menopausa é\ncâncer até que se prove o contrário!"),
        ("Exame Inicial:", "USG Transvaginal para eco endometrial."),
        ("Ponto de Corte USG:", "Espessura endometrial > 4 mm sem THM\n(ou > 8 mm com THM) = Biópsia!"),
        ("Método de Biópsia:", "Ambulaorial com cânula de Pipelle.\nSe inconclusivo: Histeroscopia com biópsia."),
        ("Tipos de Bokhman:", "• Tipo I: Endometrioide, estrogênio-dependente, obesas, bom prognóstico.\n• Tipo II: Seroso/células claras, idosas, p53-mutado, alto risco."),
        ("🎈 Didática (5 anos):", "Na vovó, o forrinho da casinha não pode\nsangrar. Se sangrar, tem que olhar!")
    ]
    for tit, desc in itens_inv:
        draw.text((45, y), tit, fill="#be123c", font=get_font(14, bold=True))
        y += 20
        draw.text((45, y), desc, fill="#334155", font=get_font(13))
        y += 50

    # Coluna 2: Classificação Molecular TCGA / FIGO 2023
    draw.rounded_rectangle([450, 130, 1270, 800], radius=12, fill="#ffffff", outline="#cbd5e1", width=2)
    draw.rounded_rectangle([450, 130, 1270, 175], radius=10, fill="#be123c")
    draw.text((465, 142), "CLASSIFICAÇÃO MOLECULAR DO TCGA & ESTADIAMENTO FIGO 2023", fill="#ffffff", font=get_font(16, bold=True))
    
    subtipos = [
        ("1. POLE ultramutado (POLEmut)", "Excelente prognóstico", 
         "Mutações no domínio exonuclease da DNA-polimerase epsilon. Hipermutação e resposta imune massiva. Raras recidivas mesmo em alto grau histológico.", "#059669"),
        ("2. Instabilidade de Microssatélites (MMRd / MSI-H)", "Prognóstico Intermediário", 
         "Perda de proteínas de reparo do DNA (MLH1, MSH2, MSH6, PMS2). Associado à Síndrome de Lynch. Alta sensibilidade à Imunoterapia (Anti-PD-1 / Pembrolizumabe - Ensaios RUBY e NRG-GY018).", "#0284c7"),
        ("3. Sem Perfil Molecular Específico (NSMP)", "Prognóstico Intermediário", 
         "Cânceres endometrioides clássicos com receptores hormonais preservados e sem mutações de POLE ou p53. Terapia hormonal adjuvante eficaz.", "#d97706"),
        ("4. p53 Anômalo (p53abn)", "Pior Prognóstico (Alto Risco)", 
         "Mutações em TP53 (superexpressão difusa ou perda nula completa). Tumores serosos e carcinossarcomas. Alta taxa de disseminação à distância e recidiva precoce.", "#dc2626")
    ]
    
    y = 195
    for tit, prog, desc, cor in subtipos:
        draw.rounded_rectangle([470, y, 1250, y + 130], radius=8, fill="#f8fafc", outline=cor, width=2)
        draw.rectangle([470, y, 480, y + 130], fill=cor)
        draw.text((495, y + 12), tit, fill="#0f172a", font=get_font(15, bold=True))
        draw.text((850, y + 12), f"[{prog}]", fill=cor, font=get_font(13, bold=True))
        draw.text((495, y + 40), desc, fill="#334155", font=get_font(12))
        y += 145
        
    draw_footer(draw, W, H)
    im.save(os.path.join(IMG_DIR, "endometrio_classificacao_molecular_figo2023.jpg"), quality=95)

# ==============================================================================
# 6. ANATOMIA CIRÚRGICA & VIAS DE HISTERECTOMIA (ACOG)
# ==============================================================================
def create_diagram_vias_histerectomia():
    W, H = 1300, 860
    im = Image.new("RGB", (W, H), "#f8fafc")
    draw = ImageDraw.Draw(im)
    
    draw_header(draw, W, "VIAS DE HISTERECTOMIA & ANATOMIA CIRÚRGICA PÉLVICA", 
                "Hierarquia ACOG • Relações do Ureter ('Water Under the Bridge') • Salpingectomia Oportunista")
    
    # 3 Vias de Histerectomia
    vias = [
        ("1ª ESCOLHA: VAGINAL (HV)", "Sem incisões abdominais. Menor dor, menor taxa de infecção de ferida e retorno mais rápido às atividades.", 
         "Indicações: Úteros móveis, ausência de suspeita oncológica, prolapso uterino.", "#059669"),
        ("2ª ESCOLHA: LAPAROSCÓPICA (TLH / LAVH)", "Minimamente invasiva. Excelente visualização pélvica, menor perda sanguínea e recuperação rápida.", 
         "Indicações: Suspeita de aderências/endometriose, nulíparas, miomas maiores.", "#0284c7"),
        ("3ª ESCOLHA: ABDOMINAL ABERTA (HTA)", "Reservada para grandes volumes uterinos (> 14-16 semanas), contraindicações laparoscópicas ou câncer avançado.", 
         "Desvantagens: Maior dor pós-operatória, maior tempo de internação e risco infeccioso.", "#d97706")
    ]
    
    x = 30
    w_card = 400
    for tit, desc, ind, cor in vias:
        draw.rounded_rectangle([x, 130, x + w_card, 450], radius=12, fill="#ffffff", outline="#cbd5e1", width=2)
        draw.rounded_rectangle([x, 130, x + w_card, 180], radius=10, fill=cor)
        draw.text((x + 15, 142), tit, fill="#ffffff", font=get_font(15, bold=True))
        
        y = 195
        draw.text((x + 15, y), "Vantagens / Características:", fill="#0f172a", font=get_font(13, bold=True))
        y += 22
        draw.text((x + 15, y), desc, fill="#334155", font=get_font(12))
        y += 65
        draw.text((x + 15, y), "Indicações Principais:", fill="#0f172a", font=get_font(13, bold=True))
        y += 22
        draw.text((x + 15, y), ind, fill="#334155", font=get_font(12))
        
        x += w_card + 20

    # Banner Anatômico Ureter e Artéria Uterina
    draw.rounded_rectangle([30, 475, 1270, 800], radius=12, fill="#ffffff", outline="#e11d48", width=2)
    draw.rounded_rectangle([30, 475, 1270, 520], radius=10, fill="#be123c")
    draw.text((45, 487), "ANATOMIA DE RISCO CIRÚRGICO: 'WATER UNDER THE BRIDGE'", fill="#ffffff", font=get_font(16, bold=True))
    
    y = 535
    draw.text((45, y), "• Relação Ureter e Artéria Uterina:", fill="#881337", font=get_font(15, bold=True))
    draw.text((340, y), "O ureter (água) cruza por BAIXO da artéria uterina (ponte) a cerca de 1,5 a 2,0 cm lateralmente ao colo uterino.", fill="#1e293b", font=get_font(14))
    
    y += 35
    draw.text((45, y), "• Três Sítios Críticos de Lesão do Ureter:", fill="#881337", font=get_font(15, bold=True))
    y += 25
    draw.text((65, y), "1. No ligamento infundibulopélvico (durante ligadura dos vasos ovarianos).", fill="#334155", font=get_font(13))
    y += 22
    draw.text((65, y), "2. No ligamento cardeal / artéria uterina (ao pinçar os vasos uterinos na base do paramétrio).", fill="#334155", font=get_font(13))
    y += 22
    draw.text((65, y), "3. No ângulo da cúpula vaginal (ao fechar a cúpula vaginal após a retirada do útero).", fill="#334155", font=get_font(13))
    
    y += 35
    draw.text((45, y), "• Salpingectomia Oportunista Bilateral:", fill="#059669", font=get_font(15, bold=True))
    draw.text((390, y), "Recomendada universalmente em histerectomias benignas com preservação ovariana para prevenir carcinoma seroso de ovário (STIC fímbrico).", fill="#1e293b", font=get_font(13))

    draw_footer(draw, W, H)
    im.save(os.path.join(IMG_DIR, "vias_histerectomia_anatomia_cirurgica.jpg"), quality=95)

# ==============================================================================
# 7. COMPLICAÇÕES CIRÚRGICAS & PROTOCOLO ERAS / ACERTO
# ==============================================================================
def create_diagram_complicacoes_eras():
    W, H = 1300, 860
    im = Image.new("RGB", (W, H), "#f8fafc")
    draw = ImageDraw.Draw(im)
    
    draw_header(draw, W, "COMPLICAÇÕES CIRÚRGICAS EM GINECOLOGIA & PROTOCOLO ERAS", 
                "Lesão de Bexiga e Ureter • Febre dos 5 W's • Protocolo ERAS / ACERTO de Otimização Perioperatória")
    
    # Coluna 1: Complicações Urológicas
    draw.rounded_rectangle([30, 130, 630, 800], radius=12, fill="#ffffff", outline="#cbd5e1", width=2)
    draw.rounded_rectangle([30, 130, 630, 175], radius=10, fill="#be123c")
    draw.text((45, 142), "COMPLICAÇÕES UROLÓGICAS & DIAGNÓSTICO", fill="#ffffff", font=get_font(16, bold=True))
    
    y = 195
    itens_uro = [
        ("Lesão de Bexiga (Mais comum):", "Geralmente na cúpula durante dissecção do espaço vesicouterino.\n• Teste intraoperatório: Instilação de Soro com Azul de Metileno.\n• Reparo: Sutura em 2 planos com fio absorvível + sonda 7 a 14 dias."),
        ("Lesão Ureteral (Mais traiçoeira):", "Ligadura ou queimadura térmica inadvertida.\n• Clínica tardia: Dor em flanco, hidronefrose, urinoma ou fístula ureterovaginal.\n• Padrão-ouro diagnóstico: Urotomografia com fase excretora tardia.\n• Tratamento: Cateter duplo J retrógrado ou reimplante ureteroneocistostomia."),
        ("Febre Pós-Operatória (Os 5 W's):", "• Wind (D1-D2): Atelectasia pulmonar.\n• Water (D3): Infecção do trato urinário (Foley).\n• Wound (D5-D7): Infecção de ferida / sítio cirúrgico.\n• Walking (D7+): Trombose Venosa Profunda / TEP.\n• Wonder drugs: Febre medicamentosa (a qualquer momento)."),
        ("Evisceração de Cúpula Vaginal:", "Emergência ginecológica! Cobrir com compressa úmida morna,\nhidratar, prescrever antibióticos e retorno imediato ao CC!")
    ]
    for tit, desc in itens_uro:
        draw.text((45, y), tit, fill="#991b1b", font=get_font(14, bold=True))
        y += 20
        draw.text((45, y), desc, fill="#334155", font=get_font(13))
        y += 50

    # Coluna 2: Protocolo ERAS / ACERTO
    draw.rounded_rectangle([660, 130, 1270, 800], radius=12, fill="#ffffff", outline="#cbd5e1", width=2)
    draw.rounded_rectangle([660, 130, 1270, 175], radius=10, fill="#047857")
    draw.text((675, 142), "PROTOCOLO ERAS / ACERTO (BOAS PRÁTICAS)", fill="#ffffff", font=get_font(16, bold=True))
    
    y = 195
    itens_eras = [
        ("Jejum Pré-Operatório Abreviado:", "Líquidos claros contendo carboidratos até 2 horas antes da indução.\nSólidos leves até 6 horas antes."),
        ("Preparo Mecânico de Cólon:", "ABOLIDO de rotina! Causa desidratação e distúrbios hidroeletrolíticos sem reduzir infecção."),
        ("Antibioprofilaxia Cirúrgica:", "Cefazolina 2g IV em dose única 30 a 60 minutos antes da incisão da pele.\nRepetir se cirurgia > 3 horas ou perda volêmica > 1.500 mL."),
        ("Prevenção de TEV (Escore de Caprini):", "Deambulação precoce + meias compressivas/compressão pneumática intermitente.\nSe cirurgia oncológica de grande porte: Enoxaparina estendida por 28 dias pós-alta!"),
        ("Analgesia Multimodal Poupando Opioides:", "Associação de AINEs, paracetamol e infiltração anestésica local para reduzir íleo paralítico."),
        ("Realimentação & Deambulação:", "Início de dieta oral e caminhada no pós-operatório imediato (mesmo dia).")
    ]
    for tit, desc in itens_eras:
        draw.text((675, y), tit, fill="#065f46", font=get_font(14, bold=True))
        y += 20
        draw.text((675, y), desc, fill="#334155", font=get_font(13))
        y += 50

    draw_footer(draw, W, H)
    im.save(os.path.join(IMG_DIR, "complicacoes_cirurgicas_urologicas_eras.jpg"), quality=95)

if __name__ == "__main__":
    print("Gerando diagramas infográficos para Parte 7...")
    create_diagram_hpv_oncogenese()
    create_diagram_rastreamento_colo()
    create_diagram_birads()
    create_diagram_subtipos_mama()
    create_diagram_endometrio_molecular()
    create_diagram_vias_histerectomia()
    create_diagram_complicacoes_eras()
    print("Todos os 7 infográficos gerados com sucesso em:", IMG_DIR)
