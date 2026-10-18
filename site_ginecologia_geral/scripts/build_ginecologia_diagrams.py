"""
build_ginecologia_diagrams.py - Gerador de Infográficos Médicos de Alta Definição
Parte 5: Ginecologia Geral • FEBRASGO / SUS / ACOG / FIGO / ESHRE
"""

import os
from PIL import Image, ImageDraw, ImageFont

IMG_DIR = r"c:\Users\Admin\Downloads\INTERNATO GO\site_ginecologia_geral\assets\img"
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

def draw_header(draw, width, title, subtitle, badge_text="FEBRASGO • SUS • FIGO • ESHRE"):
    # Fundo do cabeçalho
    draw.rectangle([0, 0, width, 110], fill="#0f172a")
    # Barra de destaque
    draw.rectangle([0, 106, width, 110], fill="#e11d48")
    
    # Badge
    f_badge = get_font(13, bold=True)
    draw.rounded_rectangle([30, 20, 260, 44], radius=6, fill="#e11d48")
    draw.text((42, 23), badge_text, fill="#ffffff", font=f_badge)
    
    # Título e Subtítulo
    f_title = get_font(26, bold=True)
    f_sub = get_font(15, italic=False)
    draw.text((30, 52), title, fill="#ffffff", font=f_title)
    draw.text((30, 84), subtitle, fill="#94a3b8", font=f_sub)

def draw_footer(draw, width, height, text="Guia Obstetrícia & Ginecologia Parte 5 — Portal Interativo de Decisão Clínica"):
    draw.rectangle([0, height - 35, width, height], fill="#0f172a")
    f = get_font(12, italic=True)
    draw.text((30, height - 25), text, fill="#94a3b8", font=f)

# ==============================================================================
# 1. CICLO MENSTRUAL & EIXO HHO (M40)
# ==============================================================================
def create_diagram_ciclo_menstrual():
    W, H = 1300, 880
    im = Image.new("RGB", (W, H), "#f8fafc")
    draw = ImageDraw.Draw(im)
    
    draw_header(draw, W, "FISIOLOGIA DO CICLO MENSTRUAL & EIXO HHO", "Orquestra Hipotálamo-Hipófise-Ovário • Fases Folicular e Lútea • Parâmetros FIGO")
    
    # Coluna 1: O Eixo HHO
    draw.rounded_rectangle([30, 130, 420, 820], radius=12, fill="#ffffff", outline="#cbd5e1", width=2)
    draw.rounded_rectangle([30, 130, 420, 175], radius=10, fill="#1e293b")
    draw.text((45, 142), "1. O MAESTRO & O EIXO HHO", fill="#ffffff", font=get_font(17, bold=True))
    
    # Card Hipotálamo
    draw.rounded_rectangle([45, 190, 405, 300], radius=8, fill="#eff6ff", outline="#bfdbfe")
    draw.text((55, 198), "Hipotálamo (O Maestro)", fill="#1e3a8a", font=get_font(15, bold=True))
    draw.text((55, 222), "• Secreção pulsátil de GnRH\n• Pulsos rápidos: estimulam secreção de LH\n• Pulsos lentos: estimulam secreção de FSH", fill="#334155", font=get_font(13))
    
    # Seta
    draw.line([(225, 305), (225, 330)], fill="#3b82f6", width=3)
    
    # Card Hipófise
    draw.rounded_rectangle([45, 335, 405, 455], radius=8, fill="#eff6ff", outline="#bfdbfe")
    draw.text((55, 343), "Hipófise Anterior / Adenoipófise (O Spalla)", fill="#1e3a8a", font=get_font(15, bold=True))
    draw.text((55, 368), "• FSH: Recruta e amadurece coorte folicular\n• Pico de LH: Deflagra a ovulação (36h após início)\n• Feedback: Estrogênio elevado prolongado gera pico", fill="#334155", font=get_font(13))
    
    # Seta
    draw.line([(225, 460), (225, 485)], fill="#3b82f6", width=3)
    
    # Card Ovários & Endométrio
    draw.rounded_rectangle([45, 490, 405, 620], radius=8, fill="#fdf2f8", outline="#fbcfe8")
    draw.text((55, 498), "Ovários (Os Músicos) & Endométrio", fill="#831843", font=get_font(15, bold=True))
    draw.text((55, 523), "• Estrogênio = 'Adubo' (faz o endométrio crescer)\n• Progesterona = 'Cimento' (deixa firme e estável)\n• Sem gravidez: Queda hormonal desaba o endométrio\n  de forma organizada = Menstruação normal", fill="#334155", font=get_font(13))

    # Destaque de Regra de Ouro
    draw.rounded_rectangle([45, 635, 405, 805], radius=8, fill="#fef2f2", outline="#fecaca")
    draw.text((55, 645), "⚠️ REGRA DE OURO DA GINECOLOGIA", fill="#991b1b", font=get_font(14, bold=True))
    draw.text((55, 672), "Em qualquer mulher em idade reprodutiva com\nsangramento anormal, dor ou amenorreia:\nO PRIMEIRO EXAME É SEMPRE O beta-hCG!\nDescartar gestação é mandatória antes de\nqualquer investigação funcional ou anatômica.", fill="#7f1d1d", font=get_font(13, bold=True))

    # Coluna 2: Fases do Ciclo & Curvas
    draw.rounded_rectangle([440, 130, 860, 820], radius=12, fill="#ffffff", outline="#cbd5e1", width=2)
    draw.rounded_rectangle([440, 130, 860, 175], radius=10, fill="#1e293b")
    draw.text((455, 142), "2. FASES DO CICLO MENSTRUAL (28 DIAS)", fill="#ffffff", font=get_font(17, bold=True))

    # Fase Folicular
    draw.rounded_rectangle([455, 190, 845, 335], radius=8, fill="#f0fdf4", outline="#bbf7d0")
    draw.text((470, 200), "Fase Folicular (Variável: Dia 1 ao 14)", fill="#166534", font=get_font(15, bold=True))
    draw.text((470, 226), "• Recrutamento folicular dependente de FSH\n• Seleção do folículo dominante (maior expressão de receptores FSH)\n• Células da granulosa sintetizam Estradiol a partir de androgênios\n• Endométrio proliferativo: estrogênio faz as glândulas crescerem", fill="#334155", font=get_font(13))

    # Ovulação
    draw.rounded_rectangle([455, 350, 845, 475], radius=8, fill="#fefce8", outline="#fef08a")
    draw.text((470, 360), "Ovulação (Dia 14 — O Ponto Crítico)", fill="#854d0e", font=get_font(15, bold=True))
    draw.text((470, 386), "• Estrogênio atinge limiar de feedback positivo (> 200 pg/mL por > 48h)\n• Pico agudo de LH induz retomada da meiose I do ovócito\n• Ruptura da parede folicular: liberação do óvulo\n• 36 horas após início do pico de LH (ou 10-12h após o pico máximo)", fill="#334155", font=get_font(13))

    # Fase Lútea
    draw.rounded_rectangle([455, 490, 845, 635], radius=8, fill="#fdf4ff", outline="#f5d0fe")
    draw.text((470, 500), "Fase Lútea (Constante: 14 dias fixos)", fill="#86198f", font=get_font(15, bold=True))
    draw.text((470, 526), "• Formação do Corpo Lúteo: secreta grandes quantidades de Progesterona\n• Endométrio secretor: glândulas tortuosas, estroma edemaciado\n• Progesterona inibe novos pulsos de FSH/LH (impede nova ovulação)\n• Sem hCG (implantação), corpo lúteo involui em 14 dias (corpo albicans)", fill="#334155", font=get_font(13))

    # Anovulação fisiopatológica
    draw.rounded_rectangle([455, 650, 845, 805], radius=8, fill="#f8fafc", outline="#cbd5e1")
    draw.text((470, 660), "🧠 Ivy League: Fisiopatologia da Anovulação", fill="#0f172a", font=get_font(14, bold=True))
    draw.text((470, 686), "Sem ovulação, não há corpo lúteo e NÃO HÁ PROGESTERONA.\nO endométrio fica exposto ao estrogênio contínuo sem oposição,\nproliferando desordenadamente até sofrer isquemia focal e descamação\nirregular = Sangramento Uterino Anormal Ovulatório (SUA-O / SOP).", fill="#475569", font=get_font(13))

    # Coluna 3: Parâmetros Normais FIGO
    draw.rounded_rectangle([880, 130, 1270, 820], radius=12, fill="#ffffff", outline="#cbd5e1", width=2)
    draw.rounded_rectangle([880, 130, 1270, 175], radius=10, fill="#1e293b")
    draw.text((895, 142), "3. PARÂMETROS NORMAIS (FIGO)", fill="#ffffff", font=get_font(17, bold=True))

    params = [
        ("Frequência (Intervalo)", "24 a 38 dias", "Intervalo normal entre o 1º dia de cada fluxo"),
        ("Duração do Sangramento", "<= 8 dias", "Duração normal do período menstrual"),
        ("Variação de Regularidade", "<= 7 a 9 dias", "Variação aceitável entre ciclos no mesmo ano"),
        ("Volume Menstrual", "Normal subjetivo", "Que não interfira na qualidade de vida (< 80 mL)")
    ]
    
    y = 190
    for p_title, p_val, p_desc in params:
        draw.rounded_rectangle([895, y, 1255, y + 80], radius=8, fill="#f1f5f9", outline="#e2e8f0")
        draw.text((910, y + 8), p_title, fill="#334155", font=get_font(13, bold=True))
        draw.text((910, y + 28), p_val, fill="#0f172a", font=get_font(18, bold=True))
        draw.text((910, y + 54), p_desc, fill="#64748b", font=get_font(12))
        y += 92

    # Tabela de termos proscritos
    draw.rounded_rectangle([895, 570, 1255, 805], radius=8, fill="#fef2f2", outline="#fee2e2")
    draw.text((910, 582), "❌ Termos Antigos Proscritos pela FIGO", fill="#991b1b", font=get_font(14, bold=True))
    draw.text((910, 608), "• Menorragia / Metrorragia / Hipomenorreia\n• Menometrorragia / Sangramento Disfuncional\n\n✅ Terminologia Atual Recomendada:\n• Sangramento Menstrual Excessivo\n• Sangramento Intermenstrual\n• Sangramento Menstrual Prolongado\n• Sangramento Pós-Coital ou Pós-Menopausa", fill="#7f1d1d", font=get_font(12, bold=True))

    draw_footer(draw, W, H)
    out_path = os.path.join(IMG_DIR, "ciclo_menstrual_eixo_hho.jpg")
    im.save(out_path, quality=95)
    print(f"[OK] Gerado: {out_path}")

# ==============================================================================
# 2. SANGRAMENTO UTERINO ANORMAL & PALM-COEIN (M41)
# ==============================================================================
def create_diagram_palm_coein():
    W, H = 1350, 900
    im = Image.new("RGB", (W, H), "#f8fafc")
    draw = ImageDraw.Draw(im)
    
    draw_header(draw, W, "SANGRAMENTO UTERINO ANORMAL: CLASSIFICAÇÃO PALM-COEIN (FIGO)", "Etiologias Estruturais vs Não Estruturais • Roteiro Diagnóstico e Algoritmo de Biópsia")

    # Bloco PALM (Estruturais)
    draw.rounded_rectangle([30, 130, 660, 520], radius=12, fill="#ffffff", outline="#cbd5e1", width=2)
    draw.rounded_rectangle([30, 130, 660, 175], radius=10, fill="#be123c")
    draw.text((45, 142), "P A L M — ESTRUTURAIS (VISÍVEIS / PALPÁVEIS)", fill="#ffffff", font=get_font(17, bold=True))

    palm_items = [
        ("P", "Pólipo (Endometrial / Cervical)", "Sangramento intermenstrual, escape ou pós-menopausa. USG, histerossonografia e histeroscopia com polipectomia."),
        ("A", "Adenomiose", "Glândulas endometriais no miométrio. Dismenorreia progressiva + menorragia em multípara de 40-50 anos. Útero boggy globoso."),
        ("L", "Leiomioma (Miomatose Uterina)", "Submucosos (FIGO 0-2) causam sangramento grave. Intramurais e subserosos geram sintomas de compressão pélvica."),
        ("M", "Malignidade & Hiperplasia", "Hiperplasia com atipia (NIE) ou carcinoma de endométrio. Investigar em >= 45 anos ou sangramento pós-menopausa.")
    ]

    y = 190
    for ltr, title, desc in palm_items:
        draw.rounded_rectangle([45, y, 645, y + 72], radius=8, fill="#fff1f2", outline="#fecdd3")
        draw.rounded_rectangle([55, y + 12, 95, y + 60], radius=6, fill="#e11d48")
        draw.text((68, y + 20), ltr, fill="#ffffff", font=get_font(20, bold=True))
        draw.text((110, y + 10), title, fill="#881337", font=get_font(14, bold=True))
        draw.text((110, y + 32), desc, fill="#4c0519", font=get_font(11))
        y += 80

    # Bloco COEIN (Não Estruturais)
    draw.rounded_rectangle([690, 130, 1320, 520], radius=12, fill="#ffffff", outline="#cbd5e1", width=2)
    draw.rounded_rectangle([690, 130, 1320, 175], radius=10, fill="#1d4ed8")
    draw.text((705, 142), "C O E I N — NÃO ESTRUTURAIS (FUNCIONAIS / SISTÊMICAS)", fill="#ffffff", font=get_font(17, bold=True))

    coein_items = [
        ("C", "Coagulopatia (von Willebrand, etc.)", "Menorragia desde a menarca, epistaxe, hematomas. Triagem laboratorial com antígeno e atividade de vWF e Fator VIII."),
        ("O", "Ovulatória (Disfunção Ovulatória)", "Anovulação por SOP, puberdade, perimenopausa, tireoidopatias. Estrogênio sem progesterona desaba sem padrão."),
        ("E", "Endometrial (Hemostasia Local)", "Ciclos regulares e ovulatórios mas com fluxo volumoso sem lesão estrutural. Desbalanço de prostaglandinas/vasoconstritores."),
        ("I", "Iatrogênica", "Uso de anticoagulantes, tamoxifeno, escape de DIU ou implante, esquecimento de pílula anticoncepcional."),
        ("N", "Não Classificada", "Istmocele (nicho de cesárea prévia com sangue represado), malformações arteriovenosas (MAV uterina).")
    ]

    y = 190
    for ltr, title, desc in coein_items:
        draw.rounded_rectangle([705, y, 1305, y + 58], radius=8, fill="#eff6ff", outline="#bfdbfe")
        draw.rounded_rectangle([715, y + 8, 750, y + 50], radius=6, fill="#2563eb")
        draw.text((725, y + 14), ltr, fill="#ffffff", font=get_font(18, bold=True))
        draw.text((765, y + 8), title, fill="#1e3a8a", font=get_font(13, bold=True))
        draw.text((765, y + 28), desc, fill="#1e40af", font=get_font(10))
        y += 64

    # Painel Inferior: Investigação de Sangramento Pós-Menopausa e Biópsia
    draw.rounded_rectangle([30, 540, 1320, 850], radius=12, fill="#ffffff", outline="#cbd5e1", width=2)
    draw.rounded_rectangle([30, 540, 1320, 585], radius=10, fill="#0f172a")
    draw.text((45, 552), "ALGORITMO DECISÓRIO: SANGRAMENTO PÓS-MENOPAUSA & BIÓPSIA ENDOMETRIAL (ACOG)", fill="#ffffff", font=get_font(16, bold=True))

    # Box 1: Apresentação
    draw.rounded_rectangle([45, 600, 360, 830], radius=8, fill="#f8fafc", outline="#cbd5e1")
    draw.text((60, 612), "1. Paciente com Sangramento", fill="#0f172a", font=get_font(14, bold=True))
    draw.text((60, 638), "• Sangramento na pós-menopausa\n  é suspeito de CÂNCER DE\n  ENDOMÉTRIO até prova em contrário!\n• Causa mais comum: Atrofia (60-80%)\n• Causa mais grave: Câncer (~10%)\n• 1º Passo: USG transvaginal ou\n  biópsia direta com Pipelle", fill="#334155", font=get_font(12))

    # Box 2: USG Cutoffs
    draw.rounded_rectangle([380, 600, 840, 830], radius=8, fill="#fdf2f8", outline="#fbcfe8")
    draw.text((395, 612), "2. Espessura Endometrial ao USG Transvaginal", fill="#831843", font=get_font(14, bold=True))
    draw.text((395, 638), "Espessura <= 4 mm (Sem Terapia Hormonal):\n• Risco de câncer extremamente baixo (< 1%)\n• Conduta: Observação clínica; se o sangramento persistir ou recorrer = Biópsia!\n\nEspessura > 4 mm ou Eco Heterogêneo / Não Mensurável:\n• Risco de câncer ou hiperplasia atípica aumentado\n• Conduta: BIÓPSIA ENDOMETRIAL OBRIGATÓRIA (Cânula de Pipelle)\n• Se amostra insuficiente ou inconclusiva: Histeroscopia com biópsia dirigida\n\n⚠️ Em uso de Tamoxifeno: O ponto de corte de 4 mm NÃO se aplica!", fill="#831843", font=get_font(12))

    # Box 3: Hiperplasia Endometrial OMS
    draw.rounded_rectangle([860, 600, 1305, 830], radius=8, fill="#fef2f2", outline="#fecaca")
    draw.text((875, 612), "3. Conduta na Hiperplasia (OMS 2020)", fill="#991b1b", font=get_font(14, bold=True))
    draw.text((875, 638), "Hiperplasia Sem Atipia (Risco CA < 5%):\n• Tratamento Clínico Progestacional\n• 1ª Linha: DIU de Levonorgestrel 52 mg\n• Biópsia de controle em 3 a 6 meses\n\nHiperplasia Com Atipia / NIE (Até 40% já têm CA):\n• Tratamento de Escolha: Histerectomia Total\n  com Anexectomia Bilateral (sem morcelamento!)\n• Se desejo de fertilidade: Megestrol ou DIU-LNG\n  com biópsias a cada 3 meses e histerectomia pós-prole", fill="#7f1d1d", font=get_font(12))

    draw_footer(draw, W, H)
    out_path = os.path.join(IMG_DIR, "sangramento_uterino_palm_coein.jpg")
    im.save(out_path, quality=95)
    print(f"[OK] Gerado: {out_path}")

# ==============================================================================
# 3. SÍNDROME DOS OVÁRIOS POLICÍSTICOS (M41.8)
# ==============================================================================
def create_diagram_sop():
    W, H = 1300, 880
    im = Image.new("RGB", (W, H), "#f8fafc")
    draw = ImageDraw.Draw(im)
    
    draw_header(draw, W, "SÍNDROME DOS OVÁRIOS POLICÍSTICOS (SOP): ROTTERDAM 2023", "Fisiopatologia da Resistência à Insulina • Fenótipos Clínicos • Indução Ovulatória com Letrozol")

    # Coluna 1: Critérios de Rotterdam
    draw.rounded_rectangle([30, 130, 420, 820], radius=12, fill="#ffffff", outline="#cbd5e1", width=2)
    draw.rounded_rectangle([30, 130, 420, 175], radius=10, fill="#0f172a")
    draw.text((45, 142), "CRITÉRIOS DE ROTTERDAM (2 DE 3)", fill="#ffffff", font=get_font(16, bold=True))

    crit = [
        ("1. Oligo / Anovulação", "Ciclos menstruais com intervalos > 35 dias ou < 8 ciclos/ano. Endométrio instável e infertilidade anovulatória."),
        ("2. Hiperandrogenismo", "Clínico: Hirsutismo (Ferriman-Gallwey >= 4 a 6), acne inflamatória, alopecia androgenética.\nLaboratorial: Testosterona total/livre elevada."),
        ("3. Morfologia Ovariana Policística", "USG Transvaginal (Critério 2023):\n>= 20 folículos de 2 a 9 mm por ovário E/OU\nVolume ovariano aumentado >= 10 mL.\n* AMH elevado pode substituir USG em adultas.")
    ]
    y = 190
    for title, desc in crit:
        draw.rounded_rectangle([45, y, 405, y + 120], radius=8, fill="#eff6ff", outline="#bfdbfe")
        draw.text((55, y + 10), title, fill="#1e3a8a", font=get_font(14, bold=True))
        draw.text((55, y + 36), desc, fill="#1e40af", font=get_font(12))
        y += 130

    # Diagnósticos de exclusão obrigatórios
    draw.rounded_rectangle([45, 590, 405, 805], radius=8, fill="#fef2f2", outline="#fecaca")
    draw.text((55, 600), "⚠️ EXCLUSÃO OBRIGATÓRIA", fill="#991b1b", font=get_font(14, bold=True))
    draw.text((55, 626), "Antes de firmar o diagnóstico de SOP:\n• beta-hCG (excluir gestação)\n• TSH (hipotireoidismo primário)\n• Prolactina (hiperprolactinemia)\n• 17-OH-Progesterona (HAC não clássica)\n• Se virilização rápida / DHEA-S alto:\n  Excluir tumor de adrenal ou ovariano!", fill="#7f1d1d", font=get_font(12, bold=True))

    # Coluna 2: Fisiopatologia
    draw.rounded_rectangle([440, 130, 860, 820], radius=12, fill="#ffffff", outline="#cbd5e1", width=2)
    draw.rounded_rectangle([440, 130, 860, 175], radius=10, fill="#be123c")
    draw.text((455, 142), "FISIOPATOLOGIA & HIPERINSULINEMIA", fill="#ffffff", font=get_font(16, bold=True))

    draw.rounded_rectangle([455, 190, 845, 340], radius=8, fill="#fff1f2", outline="#fecdd3")
    draw.text((470, 200), "O Círculo Vicioso Central", fill="#881337", font=get_font(15, bold=True))
    draw.text((470, 226), "1. Resistência à Insulina periférica crônica\n2. Hiperinsulinemia compensatória pancreática\n3. Estimulação direta das Células da Teca Ovariana:\n   Aumento acentuado da síntese de andrógenos\n4. Redução da síntese hepática de SHBG:\n   Mais testosterona livre ativa circulante", fill="#4c0519", font=get_font(13))

    draw.rounded_rectangle([455, 360, 845, 510], radius=8, fill="#fdf2f8", outline="#fbcfe8")
    draw.text((470, 370), "Disfunção do Feedback Gonadotrófico", fill="#831843", font=get_font(15, bold=True))
    draw.text((470, 396), "• Pulsos acelerados de GnRH no hipotálamo\n• Aumento preferencial da liberação de LH sobre FSH\n• Relação LH / FSH > 2 (frequente, mas não diagnóstica)\n• O FSH relativo insuficiente impede a maturação folicular:\n  Folículos ficam parados em 2 a 9 mm (morfologia em colar)", fill="#701a75", font=get_font(13))

    draw.rounded_rectangle([455, 530, 845, 805], radius=8, fill="#f8fafc", outline="#cbd5e1")
    draw.text((470, 542), "Riscos Sistêmicos a Longo Prazo", fill="#0f172a", font=get_font(14, bold=True))
    draw.text((470, 568), "• Câncer de Endométrio (risco 3x maior devido ao estrogênio contínuo)\n• Diabetes Mellitus Tipo 2 (rastrear com TOTG 75g a cada 1-3 anos)\n• Doença Hepática Gordurosa Metabólica (DHGM / esteatose)\n• Síndrome da Apneia Obstrutiva do Sono (SAOS)\n• Dislipidemia aterogênica (HDL baixo, triglicerídeos altos)\n• Depressão, ansiedade e transtornos de autoimagem", fill="#334155", font=get_font(12))

    # Coluna 3: Tratamento Guiado pelo Alvo
    draw.rounded_rectangle([880, 130, 1270, 820], radius=12, fill="#ffffff", outline="#cbd5e1", width=2)
    draw.rounded_rectangle([880, 130, 1270, 175], radius=10, fill="#15803d")
    draw.text((895, 142), "TRATAMENTO GUIADO PELO OBJETIVO", fill="#ffffff", font=get_font(16, bold=True))

    treats = [
        ("Base Universal (Todas as Pacientes)", "MUDANÇA DO ESTILO DE VIDA\nPerda de 5 a 10% do peso corporal restaura a ovulação espontânea em muitas pacientes e melhora o perfil metabólico.", "#f0fdf4", "#166534"),
        ("Sem Desejo de Gestação", "ANTICONCEPCIONAL COMBINADO (ACO)\nProteção endometrial + supressão de LH + aumento de SHBG.\nSe hirsutismo persistir após 6 meses de ACO: Associar Espironolactona (sempre com contracepção!).", "#eff6ff", "#1e40af"),
        ("Desejo de Gestação (Fertilidade)", "LETROZOL (INIBIDOR DA AROMATASE)\nPrimeira Linha de Indução Ovulatória (2,5 a 7,5 mg/dia por 5 dias). Superior ao Clomifeno em nascidos vivos (Legro, NEJM 2014). Menor risco de gestação múltipla.", "#fefce8", "#854d0e"),
        ("Resistência Insulínica / DM2", "METFORMINA\nCoadjuvante metabólico especialmente se IMC > 25 kg/m² ou intolerância à glicose. Não substitui letrozol para fertilidade.", "#f8fafc", "#334155")
    ]

    y = 190
    for t_title, t_desc, bg, col in treats:
        draw.rounded_rectangle([895, y, 1255, y + 140], radius=8, fill=bg, outline="#cbd5e1")
        draw.text((910, y + 10), t_title, fill=col, font=get_font(14, bold=True))
        draw.text((910, y + 36), t_desc, fill="#334155", font=get_font(12))
        y += 152

    draw_footer(draw, W, H)
    out_path = os.path.join(IMG_DIR, "sop_rotterdam_fisiopatologia.jpg")
    im.save(out_path, quality=95)
    print(f"[OK] Gerado: {out_path}")

# ==============================================================================
# 4. MIOMATOSE UTERINA & CLASSIFICAÇÃO FIGO (M42)
# ==============================================================================
def create_diagram_miomatose():
    W, H = 1350, 880
    im = Image.new("RGB", (W, H), "#f8fafc")
    draw = ImageDraw.Draw(im)
    
    draw_header(draw, W, "LEIOMIOMATOSE UTERINA: CLASSIFICAÇÃO FIGO (0 A 8)", "Mapeamento Topográfico • Degenerações Típicas • Opções Cirúrgicas e Medicamentosas")

    # Painel Esquerdo: Classificação FIGO 0 a 8
    draw.rounded_rectangle([30, 130, 750, 820], radius=12, fill="#ffffff", outline="#cbd5e1", width=2)
    draw.rounded_rectangle([30, 130, 750, 175], radius=10, fill="#0f172a")
    draw.text((45, 142), "SISTEMA DE CLASSIFICAÇÃO FIGO (SUBTIPOS 0 A 8)", fill="#ffffff", font=get_font(16, bold=True))

    figo_types = [
        ("FIGO 0", "Submucoso pediculado 100% intracavitário", "Sangramento torrencial, anemia grave. Conduta: Miomectomia histeroscópica."),
        ("FIGO 1", "Submucoso com componente intramural < 50%", "Menorragia volumosa, infertilidade. Conduta: Miomectomia histeroscópica."),
        ("FIGO 2", "Submucoso com componente intramural >= 50%", "Cólica e sangramento. Pode exigir preparo com análogo de GnRH ou 2 tempos."),
        ("FIGO 3", "Intramural que contata o endométrio (100% miometrial)", "Aumento do fluxo menstrual. Avaliar DIU-LNG, ácido tranexâmico ou cirurgia."),
        ("FIGO 4", "Intramural puro (sem contato com mucosa ou serosa)", "Aumento de volume uterino. Sangramento e sensação de peso pélvico."),
        ("FIGO 5", "Subseroso com componente intramural >= 50%", "Sintomas de compressão sobre bexiga (polaciúria) ou reto (constipação)."),
        ("FIGO 6", "Subseroso com componente intramural < 50%", "Compressivo. Miomectomia laparoscópica se sintomático."),
        ("FIGO 7", "Subseroso pediculado", "Maior risco de TORÇÃO AGUDA (dor súbita e abdome agudo). Cirurgia de ressecção."),
        ("FIGO 8", "Outros (Cervical, Parasita no ligamento largo)", "Obstrução ureteral, dispareunia profunda, retenção urinária.")
    ]

    y = 190
    for f_code, f_sub, f_act in figo_types:
        draw.rounded_rectangle([45, y, 735, y + 62], radius=8, fill="#f8fafc", outline="#e2e8f0")
        draw.rounded_rectangle([55, y + 8, 135, y + 54], radius=6, fill="#be123c")
        draw.text((62, y + 16), f_code, fill="#ffffff", font=get_font(15, bold=True))
        draw.text((145, y + 8), f_sub, fill="#0f172a", font=get_font(13, bold=True))
        draw.text((145, y + 30), f_act, fill="#64748b", font=get_font(11))
        y += 68

    # Painel Direito Superior: Degenerações
    draw.rounded_rectangle([770, 130, 1320, 460], radius=12, fill="#ffffff", outline="#cbd5e1", width=2)
    draw.rounded_rectangle([770, 130, 1320, 175], radius=10, fill="#831843")
    draw.text((785, 142), "DEGENERAÇÕES DOS LEIOMIOMAS", fill="#ffffff", font=get_font(16, bold=True))

    degen = [
        ("Hialina (Mais Comum)", "Substituição do tecido muscular liso por matriz hialina amorfa. Ocorre em até 65% dos miomas. Curso benigno assintomático."),
        ("Rubra / Vermelha / Carnosa", "Infarto hemorrágico agudo por trombose venosa, clássico na GESTAÇÃO (2º trimestre). Causa DOR INTENSA, febre e leucocitose. Conduta CONSERVADORA (analgesia + AINE por curto período)."),
        ("Cística / Calcificada", "Mais prevalente na pós-menopausa após hipoestrogenismo prolongado (achado radiológico clássico 'em casca de ovo')."),
        ("Sarcomatosa (Leiomiossarcoma)", "Raríssima (< 0,5%). Suspeitar se CRESCIMENTO RÁPIDO NA PÓS-MENOPAUSA. Geralmente surge 'de novo' e não por transformação maligna.")
    ]
    y = 190
    for d_title, d_desc in degen:
        draw.rounded_rectangle([785, y, 1305, y + 58], radius=8, fill="#fdf2f8", outline="#fbcfe8")
        draw.text((795, y + 6), d_title, fill="#9d174d", font=get_font(13, bold=True))
        draw.text((795, y + 26), d_desc, fill="#701a75", font=get_font(11))
        y += 66

    # Painel Direito Inferior: Estratégias Terapêuticas
    draw.rounded_rectangle([770, 480, 1320, 820], radius=12, fill="#ffffff", outline="#cbd5e1", width=2)
    draw.rounded_rectangle([770, 480, 1320, 525], radius=10, fill="#1e293b")
    draw.text((785, 492), "ESTRATÉGIAS TERAPÊUTICAS & CONDUTAS", fill="#ffffff", font=get_font(16, bold=True))

    therapies = [
        ("Manejo Clínico Medicamentoso", "• DIU-LNG 52 mg: excelente para controle de sangramento (exige cavidade não distorcida)\n• Ácido Tranexâmico / AINE: reduzem sangramento sem diminuir volume tumoral\n• Análogos de GnRH (Leuprorrelina): uso pré-operatório por 3-6 meses para reduzir volume e corrigir anemia"),
        ("Miomectomia (Preservação da Fertilidade)", "• Histeroscópica: tipos 0 e 1, e alguns tipo 2 selecionados (< 4-5 cm)\n• Laparoscópica / Laparotômica: intramurais e subserosos sintomáticos\n• ⚠️ Alerta: Miomectomia com abertura de cavidade endometrial indica cesárea futura"),
        ("Tratamentos Definitivos e Intervencionistas", "• Embolização das Artérias Uterinas (EAU): ótima opção para quem NÃO deseja gestar\n• Histerectomia: tratamento curativo definitivo (indicação cirúrgica ginecológica mais comum)\n• ⚠️ Morcelamento de miomas: deve ser sempre CONTIDO (em bolsa) para evitar disseminar sarcoma oculto")
    ]
    y = 540
    for t_title, t_desc in therapies:
        draw.rounded_rectangle([785, y, 1305, y + 84], radius=8, fill="#f1f5f9", outline="#e2e8f0")
        draw.text((795, y + 8), t_title, fill="#0f172a", font=get_font(13, bold=True))
        draw.text((795, y + 28), t_desc, fill="#334155", font=get_font(11))
        y += 92

    draw_footer(draw, W, H)
    out_path = os.path.join(IMG_DIR, "miomatose_uterina_figo_classificacao.jpg")
    im.save(out_path, quality=95)
    print(f"[OK] Gerado: {out_path}")

# ==============================================================================
# 5. ADENOMIOSE VS ENDOMETRIOSE (M43 & M44)
# ==============================================================================
def create_diagram_adenomiose_endometriose():
    W, H = 1350, 900
    im = Image.new("RGB", (W, H), "#f8fafc")
    draw = ImageDraw.Draw(im)
    
    draw_header(draw, W, "ADENOMIOSE VS ENDOMETRIOSE: QUADRO COMPARATIVO COMPLETO", "Critérios MUSA • Diretriz ESHRE 2022 • Diagnóstico por Imagem e Abordagem Terapêutica")

    # Coluna 1: Adenomiose
    draw.rounded_rectangle([30, 130, 660, 850], radius=12, fill="#ffffff", outline="#cbd5e1", width=2)
    draw.rounded_rectangle([30, 130, 660, 175], radius=10, fill="#0284c7")
    draw.text((45, 142), "ADENOMIOSE (GLÂNDULAS NO MIOMÉTRIO)", fill="#ffffff", font=get_font(17, bold=True))

    adeno_data = [
        ("Definição & Perfil Típico", "Presença de glândulas e estroma endometrial ectópicos DENTRO do miométrio, circundados por hipertrofia muscular lisa reativa.\nTípico em: Mulheres de 40 a 50 anos, multíparas, com histórico de cirurgia uterina prévia (cesárea, curetagem)."),
        ("Tríade Clínica Clássica", "1. Sangramento uterino anormal abundante (menorragia volumosa)\n2. Dismenorreia secundária progressiva\n3. Útero difusamente aumentado (até 12 semanas), globoso, amolecido ('boggy'), simétrico e doloroso ao toque bimanual."),
        ("Achados Ultrassonográficos (Critérios MUSA)", "• Miométrio assimétrico e espessado (parede posterior > anterior)\n• Cistos miometriais hipoecoicos (glândulas com sangue represado)\n• Sombras acústicas estriadas 'em persiana veneziana' ou 'em chuva'\n• Ilhotas hiperecogênicas subendometriais e perda de nitidez da zona juncional"),
        ("Ressonância Magnética (Padrão de Excelência)", "Zona Juncional miometrial com espessura >= 12 mm confirma o diagnóstico (zona < 8 mm afasta adenomiose)."),
        ("Conduta e Tratamento", "• Clínico: DIU de Levonorgestrel 52 mg (1ª linha de escolha - alta eficácia na dor e sangramento), Dienogeste 2 mg/dia, ACO contínuo, AINEs.\n• Definitivo: Histerectomia total (única cura definitiva para multíparas com prole completa e refratariedade sintomática).")
    ]
    y = 190
    for title, desc in adeno_data:
        draw.rounded_rectangle([45, y, 645, y + 120], radius=8, fill="#f0f9ff", outline="#bae6fd")
        draw.text((55, y + 8), title, fill="#0369a1", font=get_font(14, bold=True))
        draw.text((55, y + 32), desc, fill="#0c4a6e", font=get_font(11))
        y += 130

    # Coluna 2: Endometriose
    draw.rounded_rectangle([690, 130, 1320, 850], radius=12, fill="#ffffff", outline="#cbd5e1", width=2)
    draw.rounded_rectangle([690, 130, 1320, 175], radius=10, fill="#be123c")
    draw.text((705, 142), "ENDOMETRIOSE (GLÂNDULAS FORA DO ÚTERO)", fill="#ffffff", font=get_font(17, bold=True))

    endo_data = [
        ("Definição & Epidemiologia", "Tecido endometrial (glândulas e estroma) implantado FORA da cavidade uterina (ovários, peritônio, ligamentos uterossacros, intestino, bexiga).\nAfeta ~10% das mulheres em idade fértil e 30 a 50% das inférteis. Atraso diagnóstico médio de 7 a 10 anos."),
        ("Quadro Clínico: Os '4 Ds' + Infertilidade", "• Dismenorreia secundária progressiva incapacitante\n• Dispareunia de profundidade (fundo de saco e ligamentos uterossacros)\n• Disquezia cíclica (dor ao evacuar no período menstrual)\n• Disúria cíclica e dor pélvica crônica não menstrual (> 6 meses)\n• Infertilidade conjugal primária ou secundária"),
        ("Diretriz ESHRE 2022: O Novo Paradigma", "A VIDEOLAPAROSCOPIA CIRÚRGICA NÃO É MAIS OBRIGATÓRIA PARA O DIAGNÓSTICO!\nO tratamento clínico empírico (AINE + Progestagênio / ACO contínuo) DEVE ser iniciado diante da suspeita clínica e história típica."),
        ("Diagnóstico por Imagem Especializado", "• USG Transvaginal com Preparo Intestinal: padrão para endometriose profunda, endometriomas ('vidro fosco') e sliding sign negativo.\n• Ressonância Magnética da Pelve: estadiamento e mapeamento pré-cirúrgico.\n• CA-125: Não usar para diagnóstico (baixa sensibilidade/especificidade)."),
        ("Manejo da Dor vs Manejo da Infertilidade", "• Dor: AINE + Dienogeste 2 mg/dia ou DIU-LNG 52 mg ou ACO contínuo. Cirurgia excisional apenas para refratárias ou lesões obstrutivas.\n• Fertilidade: Supressão hormonal NÃO melhora fertilidade! Evitar cistectomias repetidas de endometriomas (reduz reserva ovariana). Indicar FIV.")
    ]
    y = 190
    for title, desc in endo_data:
        draw.rounded_rectangle([705, y, 1305, y + 120], radius=8, fill="#fff1f2", outline="#fecdd3")
        draw.text((715, y + 8), title, fill="#9f1239", font=get_font(14, bold=True))
        draw.text((715, y + 32), desc, fill="#881337", font=get_font(11))
        y += 130

    draw_footer(draw, W, H)
    out_path = os.path.join(IMG_DIR, "adenomiose_vs_endometriose.jpg")
    im.save(out_path, quality=95)
    print(f"[OK] Gerado: {out_path}")

# ==============================================================================
# 6. CISTOS E MASSAS ANEXIAIS: IOTA & O-RADS (M45)
# ==============================================================================
def create_diagram_massas_anexiais():
    W, H = 1350, 900
    im = Image.new("RGB", (W, H), "#f8fafc")
    draw = ImageDraw.Draw(im)
    
    draw_header(draw, W, "MASSAS ANEXIAIS: REGRAS IOTA, SISTEMA O-RADS & TORÇÃO", "Estratificação de Malignidade • Marcadores Tumorais • Emergência Cirúrgica da Torção")

    # Coluna 1: Regras Simples IOTA
    draw.rounded_rectangle([30, 130, 430, 850], radius=12, fill="#ffffff", outline="#cbd5e1", width=2)
    draw.rounded_rectangle([30, 130, 430, 175], radius=10, fill="#1e293b")
    draw.text((45, 142), "REGRAS SIMPLES IOTA", fill="#ffffff", font=get_font(16, bold=True))

    iota_b = [
        ("B1", "Cisto unilocular simples"),
        ("B2", "Componente sólido < 7 mm"),
        ("B3", "Presença de sombra acústica posterior"),
        ("B4", "Tumor multilocular liso < 10 cm"),
        ("B5", "Ausência de vascularização ao Doppler")
    ]
    draw.rounded_rectangle([45, 190, 415, 415], radius=8, fill="#f0fdf4", outline="#bbf7d0")
    draw.text((55, 198), "Critérios de Benignidade (B)", fill="#166534", font=get_font(14, bold=True))
    y = 222
    for code, desc in iota_b:
        draw.text((55, y), f"• {code}: {desc}", fill="#14532d", font=get_font(12))
        y += 36

    iota_m = [
        ("M1", "Tumor sólido irregular"),
        ("M2", "Ascite na cavidade peritoneal"),
        ("M3", ">= 4 projeções papilares internas"),
        ("M4", "Multilocular-sólido irregular >= 10 cm"),
        ("M5", "Fluxo sanguíneo muito intenso ao Doppler")
    ]
    draw.rounded_rectangle([45, 430, 415, 655], radius=8, fill="#fef2f2", outline="#fecaca")
    draw.text((55, 438), "Critérios de Malignidade (M)", fill="#991b1b", font=get_font(14, bold=True))
    y = 462
    for code, desc in iota_m:
        draw.text((55, y), f"• {code}: {desc}", fill="#7f1d1d", font=get_font(12))
        y += 36

    draw.rounded_rectangle([45, 670, 415, 830], radius=8, fill="#f8fafc", outline="#cbd5e1")
    draw.text((55, 680), "Regra de Decisão IOTA:", fill="#0f172a", font=get_font(13, bold=True))
    draw.text((55, 704), "• Apenas critérios B = Lesão Benigna\n• Apenas critérios M = Lesão Maligna\n• Ambos presentes ou nenhum = Inconclusivo\n  (exige avaliação especializada por RM\n  ou ultrassonografista experiente)", fill="#334155", font=get_font(12))

    # Coluna 2: Sistema O-RADS US
    draw.rounded_rectangle([450, 130, 890, 850], radius=12, fill="#ffffff", outline="#cbd5e1", width=2)
    draw.rounded_rectangle([450, 130, 890, 175], radius=10, fill="#be123c")
    draw.text((465, 142), "SISTEMA O-RADS US (ACR 2022)", fill="#ffffff", font=get_font(16, bold=True))

    orads_scores = [
        ("O-RADS 1", "Normal fisiológico (folículo / corpo lúteo <= 3 cm na pré-menopausa). Risco de malignidade: 0%. Conduta: Nenhuma.", "#f8fafc", "#475569"),
        ("O-RADS 2", "Quase certamente benigno (cisto simples < 10 cm, dermoide ou endometrioma típicos). Risco: < 1%. Conduta: Expectante ou seguimento.", "#f0fdf4", "#166534"),
        ("O-RADS 3", "Baixo risco (cisto simples >= 10 cm, multilocular liso sem sólido). Risco: 1 a < 10%. Conduta: Ginecologista geral / USG especializado.", "#fefce8", "#854d0e"),
        ("O-RADS 4", "Risco intermediário (multilocular com sólido ou projeção papilar). Risco: 10 a < 50%. Conduta: Ginecologista Oncológico / RM.", "#fff7ed", "#9a3412"),
        ("O-RADS 5", "Alto risco de malignidade (tumor sólido irregular, ascite, papila com Doppler intenso). Risco: >= 50%. Conduta: Ginecologista Oncológico imediato.", "#fef2f2", "#991b1b")
    ]
    y = 190
    for code, desc, bg, col in orads_scores:
        draw.rounded_rectangle([465, y, 875, y + 105], radius=8, fill=bg, outline="#cbd5e1")
        draw.text((475, y + 8), code, fill=col, font=get_font(15, bold=True))
        draw.text((475, y + 32), desc, fill="#334155", font=get_font(12))
        y += 115

    draw.rounded_rectangle([465, 765, 875, 830], radius=8, fill="#fee2e2", outline="#fca5a5")
    draw.text((475, 775), "⚠️ REGRA: NUNCA PUNCIONAR MASSA COM SUSPEITA DE CÂNCER!", fill="#991b1b", font=get_font(12, bold=True))
    draw.text((475, 796), "A punção rompe a cápsula e dissemina células na cavidade peritoneal.", fill="#7f1d1d", font=get_font(11))

    # Coluna 3: Marcadores Tumorais & Torção de Ovário
    draw.rounded_rectangle([910, 130, 1320, 850], radius=12, fill="#ffffff", outline="#cbd5e1", width=2)
    draw.rounded_rectangle([910, 130, 1320, 175], radius=10, fill="#0f172a")
    draw.text((925, 142), "MARCADORES & TORÇÃO ANEXIAL", fill="#ffffff", font=get_font(16, bold=True))

    draw.rounded_rectangle([925, 190, 1305, 470], radius=8, fill="#f8fafc", outline="#cbd5e1")
    draw.text((935, 198), "Painel de Marcadores Tumorais Ovarianos", fill="#0f172a", font=get_font(14, bold=True))
    draw.text((935, 222), "• CA-125: Câncer epitelial seroso. Alta utilidade na pós-menopausa\n  (na pré-menopausa sobe por endometriose, mioma, gravidez)\n• HE4 & Índice ROMA: Maior especificidade para câncer epitelial\n• AFP (Alfafetoproteína): Tumor do Seio Endodérmico\n• beta-hCG: Coriocarcinoma ovariano e disgerminoma\n• LDH: Disgerminoma puro\n• Inibina: Tumor de Células da Granulosa (corpúsculos Call-Exner)\n• CEA / CA 19-9: Tumor mucinoso ou metástase de TGI (Krukenberg)\n* Criança/adolescente com massa: SEMPRE dosar AFP, hCG e LDH!", fill="#334155", font=get_font(11))

    # Emergência: Torção Anexial
    draw.rounded_rectangle([925, 490, 1305, 830], radius=8, fill="#fef2f2", outline="#fecaca")
    draw.text((935, 500), "🚨 EMERGÊNCIA: TORÇÃO ANEXIAL", fill="#991b1b", font=get_font(15, bold=True))
    draw.text((935, 526), "Clínica Típica:\n• Dor pélvica súbita, excruciante, unilateral\n• Náuseas e vômitos intensos em 70-85% dos casos\n• Massa anexial palpável (frequentemente > 5 cm / dermoide)\n\nUltrassonografia com Doppler:\n• Ovário aumentado e edemaciado com folículos periféricos\n• 'Sinal do redemoinho' (whirlpool sign) no pedículo vascular\n• ⚠️ PEGADINHA: Fluxo ao Doppler NÃO descarta torção!\n\nConduta Cirúrgica Mandatória:\n• LAPAROSCOPIA DE URGÊNCIA IMEDIATA\n• DESTORÇÃO E PRESERVAÇÃO DO OVÁRIO\n• Mesmo que o ovário esteja arroxeado/escuro, destorcer e esperar!\n  A grande maioria recupera viabilidade e função endócrina.", fill="#7f1d1d", font=get_font(12))

    draw_footer(draw, W, H)
    out_path = os.path.join(IMG_DIR, "massas_anexiais_orads_iota.jpg")
    im.save(out_path, quality=95)
    print(f"[OK] Gerado: {out_path}")

# ==============================================================================
# 7. DOR PÉLVICA AGUDA & CRÔNICA (M46)
# ==============================================================================
def create_diagram_dor_pelvica():
    W, H = 1300, 880
    im = Image.new("RGB", (W, H), "#f8fafc")
    draw = ImageDraw.Draw(im)
    
    draw_header(draw, W, "DOR PÉLVICA: AGUDA, DISMENORREIA & DOR PÉLVICA CRÔNICA", "Raciocínio Algorítmico • Diferencial com Causas Não Ginecológicas • Abordagem da DPC")

    # Coluna 1: Abordagem da Dor Pélvica Aguda
    draw.rounded_rectangle([30, 130, 630, 820], radius=12, fill="#ffffff", outline="#cbd5e1", width=2)
    draw.rounded_rectangle([30, 130, 630, 175], radius=10, fill="#e11d48")
    draw.text((45, 142), "1. DOR PÉLVICA AGUDA: RACIOCÍNIO CLÍNICO", fill="#ffffff", font=get_font(16, bold=True))

    steps = [
        ("PASSO 1: O Teste de Gravidez (beta-hCG)", "SEMPRE PRIMEIRO! Mulher em idade fértil com dor aguda exige teste imediato.\n• beta-hCG Positivo: Gravidez ectópica até prova em contrário! Outros: Abortamento, corpo lúteo roto da gestação precoce.\n• beta-hCG Negativo: Seguir para investigação de causas ginecológicas e não ginecológicas."),
        ("PASSO 2: Estabilidade Hemodinâmica", "• Paciente Instável (Hipotensa, taquicárdica, abdome rígido/peritoneal):\n  Indicação cirúrgica imediata (Gravidez ectópica rota, rotura de cisto hemorrágico com hemoperitônio maciço, abscesso tubo-ovariano roto).\n• Paciente Estável: Exame físico detalhado + USG Transvaginal + Urina."),
        ("PASSO 3: Achados e Hipóteses Diagnósticas", "• Dor súbita + vômitos + massa ovariana: Torção anexial (laparoscopia urgente)\n• Dor na fase lútea pós-coito + líquido livre: Corpo lúteo hemorrágico roto\n• Febre + dor à mobilização do colo + corrimento: DIP / Abscesso tubo-ovariano\n• Dor no meio do ciclo (dia 14) autolimitada: Mittelschmerz (dor da ovulação)"),
        ("PASSO 4: Causas Não Ginecológicas Essenciais", "• Gastrointestinais: Apendicite aguda (migração periumbilical para FID), diverticulite aguda, gastroenterite, obstrução intestinal.\n• Urológicas: Litíase renal / cólica nefrética (dor em flanco que irradia para vulva, hematúria), ITU / pielonefrite aguda.")
    ]
    y = 190
    for title, desc in steps:
        draw.rounded_rectangle([45, y, 615, y + 140], radius=8, fill="#fff1f2", outline="#fecdd3")
        draw.text((55, y + 8), title, fill="#9f1239", font=get_font(14, bold=True))
        draw.text((55, y + 34), desc, fill="#4c0519", font=get_font(11))
        y += 152

    # Coluna 2: Dismenorreia & Dor Pélvica Crônica
    draw.rounded_rectangle([660, 130, 1270, 820], radius=12, fill="#ffffff", outline="#cbd5e1", width=2)
    draw.rounded_rectangle([660, 130, 1270, 175], radius=10, fill="#0f172a")
    draw.text((675, 142), "2. DISMENORREIA & DOR PÉLVICA CRÔNICA (DPC)", fill="#ffffff", font=get_font(16, bold=True))

    # Tabela Dismenorreia
    draw.rounded_rectangle([675, 190, 1255, 410], radius=8, fill="#f8fafc", outline="#cbd5e1")
    draw.text((685, 200), "Dismenorreia Primária vs Secundária", fill="#0f172a", font=get_font(15, bold=True))
    draw.text((685, 226), "Dismenorreia Primária:\n• Início 6 a 12 meses após a menarca (quando ciclos se tornam ovulatórios)\n• Fisiopatologia: Hiperprodução de Prostaglandina F2-alfa (vasoconstrição/isquemia)\n• Exame físico rigorosamente normal. Tratamento: AINE + ACO.\n\nDismenorreia Secundária:\n• Início após os 25 anos ou piora progressiva em mulher antes assintomática\n• Causas: Endometriose, Adenomiose, Miomatose, DIP prévia, DIU de cobre\n• ⚠️ Alerta: Dismenorreia que não responde a AINE + ACO exige investigar endometriose!", fill="#334155", font=get_font(12))

    # Dor Pélvica Crônica (DPC >= 6 meses)
    draw.rounded_rectangle([675, 430, 1255, 805], radius=8, fill="#eff6ff", outline="#bfdbfe")
    draw.text((685, 440), "Dor Pélvica Crônica (DPC >= 6 Meses de Duração)", fill="#1e3a8a", font=get_font(15, bold=True))
    draw.text((685, 468), "Abordagem Multissistêmica (Causas Frequentemente Coexistem!):\n\n• Ginecológica: Endometriose profunda, adenomiose, síndrome da congestão\n  pélvica (varizes pélvicas com dor que piora em pé e no fim do dia).\n• Urológica: Síndrome da bexiga dolorosa / cistite intersticial (dor com\n  enchimento vesical que alivia na micção; urocultura sempre estéril).\n• Gastrointestinal: Síndrome do Intestino Irritável (critérios Roma IV).\n• Musculoesquelética: Disfunção miofascial do assoalho pélvico (hipertonia,\n  pontos-gatilho dolorosos na palpação dos elevadores do ânus).\n• Psicossocial: Transtorno de estresse pós-traumático, histórico de abuso\n  sexual ou físico (rastrear ativamente e com acolhimento).\n\nTratamento Multidisciplinar:\nFisioterapia pélvica, neuromoduladores (duloxetina, amitriptilina, gabapentina),\npsicoterapia cognitivo-comportamental e manejo hormonal específico.", fill="#1e40af", font=get_font(12))

    draw_footer(draw, W, H)
    out_path = os.path.join(IMG_DIR, "dor_pelvica_aguda_cronica.jpg")
    im.save(out_path, quality=95)
    print(f"[OK] Gerado: {out_path}")

# ==============================================================================
# 8. CLIMATÉRIO & MENOPAUSA (M47)
# ==============================================================================
def create_diagram_climaterio_menopausa():
    W, H = 1350, 900
    im = Image.new("RGB", (W, H), "#f8fafc")
    draw = ImageDraw.Draw(im)
    
    draw_header(draw, W, "CLIMATÉRIO, MENOPAUSA & TERAPIA HORMONAL (TH)", "Janela de Oportunidade • Síndrome Geniturinária • Manejo Seguro e Prevenção da Osteoporose")

    # Coluna 1: Conceitos e Diagnóstico
    draw.rounded_rectangle([30, 130, 430, 850], radius=12, fill="#ffffff", outline="#cbd5e1", width=2)
    draw.rounded_rectangle([30, 130, 430, 175], radius=10, fill="#0f172a")
    draw.text((45, 142), "CONCEITOS & MANIFESTAÇÕES", fill="#ffffff", font=get_font(16, bold=True))

    defs = [
        ("Menopausa", "Data da última menstruação, confirmada após 12 meses consecutivos de amenorreia (diagnóstico retrospectivo). Idade média: 51 anos (48-50 no Brasil)."),
        ("Climatério & Perimenopausa", "Período biológico de transição reprodutiva. Inicia-se com irregularidade menstrual e sintomas vasomotores até 1 ano pós-menopausa."),
        ("Insuficiência Ovariana Prematura (IOP)", "Menopausa antes dos 40 anos: Amenorreia >= 4 meses com FSH > 25 UI/L em 2 dosagens (intervalo >= 4 semanas)."),
        ("Diagnóstico Clínico", "Em mulheres >= 45 anos com sintomas vasomotores e irregularidade: O DIAGNÓSTICO É CLÍNICO. NÃO é necessário dosar FSH!"),
        ("Sintomas Vasomotores (Fogachos)", "Ondas de calor e suores noturnos: sintoma mais frequente (afeta até 80%) e principal indicação para Terapia Hormonal sistêmica."),
        ("Síndrome Geniturinária (SGM)", "Secura vaginal, dispareunia, ardor e ITU de repetição. Mucosa pálida, pH > 5. Progressiva e NÃO melhora espontaneamente.")
    ]
    y = 190
    for title, desc in defs:
        draw.rounded_rectangle([45, y, 415, y + 95], radius=8, fill="#f8fafc", outline="#e2e8f0")
        draw.text((55, y + 8), title, fill="#0f172a", font=get_font(13, bold=True))
        draw.text((55, y + 28), desc, fill="#475569", font=get_font(11))
        y += 105

    # Coluna 2: Terapia Hormonal & Janela de Oportunidade
    draw.rounded_rectangle([450, 130, 890, 850], radius=12, fill="#ffffff", outline="#cbd5e1", width=2)
    draw.rounded_rectangle([450, 130, 890, 175], radius=10, fill="#be123c")
    draw.text((465, 142), "TERAPIA HORMONAL (TH): REGRAS DE OURO", fill="#ffffff", font=get_font(16, bold=True))

    rules = [
        ("A 'Janela de Oportunidade'", "Benefício claramente supera o risco quando iniciada em mulheres com IDADE < 60 ANOS ou MENOS DE 10 ANOS DE MENOPAUSA.\nIniciar tardiamente (> 60 anos) pode desestabilizar placas de ateroma já formadas.", "#fff1f2", "#9f1239"),
        ("Regra Fundamental do Útero", "• Com Útero: ESTROGÊNIO + PROGESTAGÊNIO (o progestagênio protege o endométrio contra hiperplasia e câncer).\n  Preferir Progesterona Micronizada 100 mg ou DIU-LNG 52 mg.\n• Sem Útero (Histerectomizada): ESTROGÊNIO ISOLADO.", "#eff6ff", "#1e40af"),
        ("Via Transdérmica de Escolha", "Estradiol transdérmico (gel ou adesivo) NÃO aumenta risco de TEV ou AVC (evita primeira passagem hepática).\nObrigatória em: Obesas, hipertensas, hipertrigliceridemia e tabagistas.", "#f0fdf4", "#166534"),
        ("Contraindicações Absolutas à TH Sistêmica", "• Sangramento vaginal sem diagnóstico esclarecido\n• Câncer de mama (atual ou prévio) ou endométrio\n• Tromboembolismo venoso agudo ou prévio grave\n• Doença arterial coronariana aguda, infarto ou AVC prévios\n• Hepatopatia ativa grave descompensada", "#fef2f2", "#991b1b")
    ]
    y = 190
    for r_title, r_desc, bg, col in rules:
        draw.rounded_rectangle([465, y, 875, y + 145], radius=8, fill=bg, outline="#cbd5e1")
        draw.text((475, y + 10), r_title, fill=col, font=get_font(14, bold=True))
        draw.text((475, y + 36), r_desc, fill="#334155", font=get_font(11))
        y += 158

    # Coluna 3: Opções Não Hormonais, SGM Local & Osteoporose
    draw.rounded_rectangle([910, 130, 1320, 850], radius=12, fill="#ffffff", outline="#cbd5e1", width=2)
    draw.rounded_rectangle([910, 130, 1320, 175], radius=10, fill="#15803d")
    draw.text((925, 142), "ALTERNATIVAS & OSTEOPOROSE", fill="#ffffff", font=get_font(16, bold=True))

    draw.rounded_rectangle([925, 190, 1305, 390], radius=8, fill="#fdf2f8", outline="#fbcfe8")
    draw.text((935, 200), "Alternativas Não Hormonais para Fogachos", fill="#831843", font=get_font(14, bold=True))
    draw.text((935, 226), "• Inibidores da Recaptação: Venlafaxina, Desvenlafaxina\n• Gabapentina: excelente benefício para fogachos noturnos e insônia\n• Fezolinetante: antagonista do receptor NK3 no hipotálamo\n\n⚠️ ALERTA ONCOLÓGICO MANDATÓRIO:\nParoxetina e Fluoxetina inibem o CYP2D6 e NUNCA devem ser usadas\nem mulheres em tratamento de câncer de mama com Tamoxifeno!", fill="#701a75", font=get_font(11))

    draw.rounded_rectangle([925, 405, 1305, 590], radius=8, fill="#eff6ff", outline="#bfdbfe")
    draw.text((935, 415), "Tratamento da Síndrome Geniturinária (SGM)", fill="#1e3a8a", font=get_font(14, bold=True))
    draw.text((935, 440), "1. Hidratantes vaginais regulares e lubrificantes na atividade sexual\n2. Estrogênio Vaginal em Baixa Dose (Promestrieno, Estriol creme):\n   • Absorção sistêmica insignificante\n   • Não requer progestagênio de proteção\n   • Pode ser usado continuamente com grande segurança clínica", fill="#1e40af", font=get_font(11))

    draw.rounded_rectangle([925, 605, 1305, 830], radius=8, fill="#f8fafc", outline="#cbd5e1")
    draw.text((935, 615), "Osteoporose na Pós-Menopausa", fill="#0f172a", font=get_font(14, bold=True))
    draw.text((935, 638), "• Rastreamento com Densitometria Óssea (DEXA): Todas >= 65 anos\n• Diagnóstico: T-score <= -2,5 (colo do fêmur ou coluna lombar)\n  ou fratura por fragilidade óssea prévia\n• Tratamento de 1ª Linha: Bisfosfonatos (Alendronato, Ácido Zoledrônico)\n  Tomar em jejum com água e permanecer em pé por 30 minutos\n• Cálcio 1.000-1.200 mg/dia + Vitamina D 800-1.000 UI/dia + Exercícios", fill="#334155", font=get_font(11))

    draw_footer(draw, W, H)
    out_path = os.path.join(IMG_DIR, "climaterio_menopausa_th.jpg")
    im.save(out_path, quality=95)
    print(f"[OK] Gerado: {out_path}")

# ==============================================================================
# 9. AMENORREIAS: OS 4 COMPARTIMENTOS & AMENORREIA PRIMÁRIA (M48)
# ==============================================================================
def create_diagram_amenorreias():
    W, H = 1350, 900
    im = Image.new("RGB", (W, H), "#f8fafc")
    draw = ImageDraw.Draw(im)
    
    draw_header(draw, W, "INVESTIGAÇÃO DAS AMENORREIAS: OS 4 COMPARTIMENTOS", "Amenorreia Secundária (Fluxograma com Teste da Progesterona) • Amenorreia Primária (MRKH vs Morris)")

    # Coluna 1: Definições e os 4 Compartimentos
    draw.rounded_rectangle([30, 130, 420, 850], radius=12, fill="#ffffff", outline="#cbd5e1", width=2)
    draw.rounded_rectangle([30, 130, 420, 175], radius=10, fill="#0f172a")
    draw.text((45, 142), "OS 4 COMPARTIMENTOS", fill="#ffffff", font=get_font(16, bold=True))

    comps = [
        ("Compartimento I: Trato de Saída / Útero", "Útero, endométrio e vagina.\nCausas: Síndrome de Asherman (sinéquias pós-curetagem), MRKH, septo transverso, hímen imperfurado.\nFSH: Normal | Estradiol: Normal"),
        ("Compartimento II: Ovário", "Gônada produtora de estrogênio.\nCausas: Insuficiência Ovariana Prematura (IOP), Turner (45,X), Swyer (46,XY), quimioterapia.\nFSH: ELEVADO | Estradiol: BAIXO"),
        ("Compartimento III: Hipófise", "Glândula adenoipofisária secretora de FSH/LH.\nCausas: Prolactinomas, Síndrome de Sheehan (necrose pós-hemorragia de parto), craniofaringiomas.\nFSH: Baixo/Normal | Estradiol: Baixo"),
        ("Compartimento IV: Hipotálamo", "Centro gerador de pulsos de GnRH.\nCausas: Amenorreia Hipotalâmica Funcional (estresse, perda de peso, atleta/RED-S), Síndrome de Kallmann.\nFSH: Baixo/Normal | Estradiol: Baixo")
    ]
    y = 190
    for title, desc in comps:
        draw.rounded_rectangle([45, y, 405, y + 145], radius=8, fill="#eff6ff", outline="#bfdbfe")
        draw.text((55, y + 8), title, fill="#1e3a8a", font=get_font(13, bold=True))
        draw.text((55, y + 36), desc, fill="#1e40af", font=get_font(11))
        y += 158

    # Coluna 2: Amenorreia Secundária (Fluxograma Clínico)
    draw.rounded_rectangle([440, 130, 870, 850], radius=12, fill="#ffffff", outline="#cbd5e1", width=2)
    draw.rounded_rectangle([440, 130, 870, 175], radius=10, fill="#be123c")
    draw.text((455, 142), "AMENORREIA SECUNDÁRIA: PASSO A PASSO", fill="#ffffff", font=get_font(16, bold=True))

    steps_sec = [
        ("Passo 1: beta-hCG (SEMPRE)", "Gravidez é a causa mais comum de amenorreia secundária!\nSe positivo = Pré-natal."),
        ("Passo 2: TSH & Prolactina", "Descartar hipotireoidismo primário (TRH estimula prolactina) e Prolactinoma (tratar com Cabergolina)."),
        ("Passo 3: Teste da Progesterona (Medroxiprogesterona 10 mg por 7-10 dias)", "• SANFROU: Havia estrogênio prévio e trato de saída pérvio!\n  Diagnóstico: ANOVULAÇÃO CRÔNICA (ex: SOP).\n• NÃO SANGROU: Seguir para o Passo 4."),
        ("Passo 4: Teste de Estrogênio + Progesterona (E+P por 21 dias)", "• NÃO SANGROU: Defeito anatômico no trato de saída!\n  Diagnóstico: COMPARTIMENTO I (Síndrome de Asherman).\n• SANGROU: O útero é pérvio. Falta estrogênio funcional! Seguir para Passo 5."),
        ("Passo 5: Dosagem de FSH", "• FSH Alto (> 30 UI/L): Falência ovariana (Compartimento II / IOP).\n• FSH Baixo ou Normal: Defeito hipofisário ou hipotalâmico (Compartimento III/IV).")
    ]
    y = 190
    for title, desc in steps_sec:
        draw.rounded_rectangle([455, y, 855, y + 115], radius=8, fill="#fdf2f8", outline="#fbcfe8")
        draw.text((465, y + 8), title, fill="#831843", font=get_font(13, bold=True))
        draw.text((465, y + 36), desc, fill="#701a75", font=get_font(11))
        y += 128

    # Coluna 3: Amenorreia Primária (MRKH vs Morris)
    draw.rounded_rectangle([890, 130, 1320, 850], radius=12, fill="#ffffff", outline="#cbd5e1", width=2)
    draw.rounded_rectangle([890, 130, 1320, 175], radius=10, fill="#15803d")
    draw.text((905, 142), "AMENORREIA PRIMÁRIA: MRKH VS MORRIS", fill="#ffffff", font=get_font(16, bold=True))

    draw.rounded_rectangle([905, 190, 1305, 305], radius=8, fill="#f8fafc", outline="#cbd5e1")
    draw.text((915, 198), "Algoritmo pelo Exame Físico", fill="#0f172a", font=get_font(14, bold=True))
    draw.text((915, 224), "1. Mamas Presentes (Há Estrogênio) + Útero Ausente ao USG:\n   Investigar MRKH vs Insensibilidade Androgênica (Morris)\n2. Mamas Ausentes (Falta Estrogênio) + Útero Presente:\n   Dosar FSH (FSH Alto = Turner 45,X; FSH Baixo = Kallmann/SNC)", fill="#334155", font=get_font(11))

    # Tabela Comparativa MRKH vs Morris
    draw.rounded_rectangle([905, 320, 1305, 560], radius=8, fill="#f0fdf4", outline="#bbf7d0")
    draw.text((915, 330), "Síndrome de MRKH (Agenesia Mülleriana)", fill="#166534", font=get_font(14, bold=True))
    draw.text((915, 356), "• Cariótipo: 46,XX (Genótipo e gônadas femininas)\n• Gônadas: Ovários normais e funcionantes (ovula!)\n• Pelos Pubianos e Axilares: NORMAIS\n• Mamas: Normais (Tanner V)\n• Útero e terço superior de vagina: Ausentes (vagina curta em fundo cego)\n• Testosterona: Níveis femininos normais\n• Conduta: USG Renal (rastrear agenesia/rim pélvico) + Dilatadores de Frank", fill="#14532d", font=get_font(11))

    draw.rounded_rectangle([905, 575, 1305, 830], radius=8, fill="#fff7ed", outline="#fed7aa")
    draw.text((915, 585), "Insensibilidade Androgênica Completa (Morris)", fill="#9a3412", font=get_font(14, bold=True))
    draw.text((915, 612), "• Cariótipo: 46,XY (Genótipo masculino)\n• Gônadas: Testículos intra-abdominais / hérnia inguinal bilateral\n• Pelos Pubianos e Axilares: AUSENTES OU MUITO ESCASSOS\n• Mamas: Normais (aromatização periférica da testosterona)\n• Útero: Ausente (pela ação do hormônio antimülleriano dos testículos)\n• Testosterona: Níveis masculinos normais ou elevados\n• Conduta: Gonadectomia bilateral PÓS-PUBERAL (risco tumoral de 5-30%)\n  seguida de Terapia Hormonal estrogênica e dilatadores de vagina", fill="#7c2d12", font=get_font(11))

    draw_footer(draw, W, H)
    out_path = os.path.join(IMG_DIR, "amenorreias_4_compartimentos.jpg")
    im.save(out_path, quality=95)
    print(f"[OK] Gerado: {out_path}")

# ==============================================================================
# 10. INFERTILIDADE CONJUGAL & INVESTIGAÇÃO (M49)
# ==============================================================================
def create_diagram_infertilidade():
    W, H = 1300, 880
    im = Image.new("RGB", (W, H), "#f8fafc")
    draw = ImageDraw.Draw(im)
    
    draw_header(draw, W, "INVESTIGAÇÃO BÁSICA DO CASAL INFÉRTIL", "Abordagem Simultânea • Critérios Seminais OMS 2021 • Tratamentos Guiados e FIV")

    # Coluna 1: Definição & Linha do Tempo
    draw.rounded_rectangle([30, 130, 420, 820], radius=12, fill="#ffffff", outline="#cbd5e1", width=2)
    draw.rounded_rectangle([30, 130, 420, 175], radius=10, fill="#0f172a")
    draw.text((45, 142), "QUANDO INICIAR A INVESTIGAÇÃO?", fill="#ffffff", font=get_font(15, bold=True))

    draw.rounded_rectangle([45, 190, 405, 370], radius=8, fill="#eff6ff", outline="#bfdbfe")
    draw.text((55, 198), "Definição de Infertilidade Conjugal", fill="#1e3a8a", font=get_font(14, bold=True))
    draw.text((55, 224), "Ausência de gestação clínica após 12 meses\nde relações sexuais regulares desprotegidas.\n\nLinha do Tempo por Idade Materna:\n• Mulher < 35 anos: Investigar após 12 meses\n• Mulher >= 35 anos: Investigar após 6 meses\n• Mulher > 40 anos ou histórico conhecido\n  (DIP prévia, endometriose grave, oligoamenorreia,\n  quimioterapia): INVESTIGAR IMEDIATAMENTE!", fill="#1e40af", font=get_font(12))

    draw.rounded_rectangle([45, 385, 405, 595], radius=8, fill="#fef2f2", outline="#fecaca")
    draw.text((55, 395), "⚠️ REGRA: INVESTIGAÇÃO SIMULTÂNEA!", fill="#991b1b", font=get_font(13, bold=True))
    draw.text((55, 422), "A investigação pertence AO CASAL e deve\nser realizada de forma CONCOMITANTE.\n\nO FATOR MASCULINO está presente em\n40 a 50% dos casais inférteis (isolado ou\nassociado ao fator feminino).\n\nNUNCA investigar apenas a mulher antes de\nobter o espermograma do parceiro!", fill="#7f1d1d", font=get_font(12, bold=True))

    draw.rounded_rectangle([45, 610, 405, 805], radius=8, fill="#f8fafc", outline="#cbd5e1")
    draw.text((55, 620), "Orientações Gerais do Casal", fill="#0f172a", font=get_font(13, bold=True))
    draw.text((55, 644), "• Ácido Fólico 400 mcg/dia (prevenção de DNT)\n• IMC saudável (19 a 29 kg/m²)\n• Cessação imediata do tabagismo\n• Relações sexuais a cada 1 a 2 dias na janela fértil\n• Moderação rigorosa no consumo de álcool", fill="#334155", font=get_font(12))

    # Coluna 2: Os 4 Pilares da Investigação
    draw.rounded_rectangle([440, 130, 860, 820], radius=12, fill="#ffffff", outline="#cbd5e1", width=2)
    draw.rounded_rectangle([440, 130, 860, 175], radius=10, fill="#be123c")
    draw.text((455, 142), "OS 4 PILARES DA INVESTIGAÇÃO", fill="#ffffff", font=get_font(16, bold=True))

    pillars = [
        ("1. Fator Ovulatório (~25%)", "• Ciclos regulares previsíveis (24-38 dias) sugerem ovulação\n• Confirmação: Progesterona na fase lútea média (> 3 ng/mL no dia 21)\n• Exames complementares: TSH, Prolactina, curvas de temperatura/LH"),
        ("2. Reserva Ovariana", "• Hormônio Antimülleriano (AMH) e Contagem de Folículos Antrais (CFA)\n• Predizem a resposta à estimulação ovariana na FIV (não a fertilidade espontânea!)"),
        ("3. Fator Tuboperitoneal (~25-30%)", "• Histerossalpingografia (HSG): avalia perviedade tubária e cavidade\n• ⚠️ Hidrossalpinge detectada: Exige SALPINGECTOMIA antes de FIV\n  (o líquido intratubário é tóxico ao embrião e sua remoção dobra o sucesso!)"),
        ("4. Fator Uterino", "• USG transvaginal, histerossonografia e histeroscopia cirúrgica\n• Identifica pólipos, miomas submucosos, septos uterinos e sinéquias")
    ]
    y = 190
    for p_title, p_desc in pillars:
        draw.rounded_rectangle([455, y, 845, y + 140], radius=8, fill="#fff1f2", outline="#fecdd3")
        draw.text((465, y + 8), p_title, fill="#9f1239", font=get_font(13, bold=True))
        draw.text((465, y + 32), p_desc, fill="#4c0519", font=get_font(11))
        y += 152

    # Coluna 3: Espermograma OMS 2021 & Tratamentos
    draw.rounded_rectangle([880, 130, 1270, 820], radius=12, fill="#ffffff", outline="#cbd5e1", width=2)
    draw.rounded_rectangle([880, 130, 1270, 175], radius=10, fill="#15803d")
    draw.text((895, 142), "ESPERMOGRAMA OMS & CONDUTAS", fill="#ffffff", font=get_font(16, bold=True))

    draw.rounded_rectangle([895, 190, 1255, 430], radius=8, fill="#f0fdf4", outline="#bbf7d0")
    draw.text((905, 198), "Critérios Seminais Mínimos (OMS 2021 - 6ª Ed)", fill="#166534", font=get_font(13, bold=True))
    draw.text((905, 222), "• Volume ejaculado: >= 1,4 mL\n• Concentração espermática: >= 16 milhões/mL\n• Número total de espermatozoides: >= 39 milhões\n• Motilidade Progressiva (PR): >= 30%\n• Motilidade Total (PR + NP): >= 42%\n• Morfologia Estrita de Kruger: >= 4% de formas normais\n• Vitalidade: >= 54% de espermatozoides vivos\n* Alteração exige confirmação em 2ª amostra após 2 a 3 meses.", fill="#14532d", font=get_font(11))

    draw.rounded_rectangle([895, 445, 1255, 805], radius=8, fill="#f8fafc", outline="#cbd5e1")
    draw.text((905, 455), "Condutas Guiadas pela Causa", fill="#0f172a", font=get_font(14, bold=True))
    draw.text((905, 480), "• Anovulação por SOP: Letrozol (1ª linha de indução ovulatória)\n• Fator Tubário Leve / Fator Masculino Leve:\n  Inseminação Intrauterina (IIU) com indução leve\n• Fator Tubário Bilateral / Obstrução:\n  Fertilização In Vitro (FIV clássica)\n• Fator Masculino Grave (Oligo/Astenozoospermia grave):\n  FIV com Injeção Intracitoplasmática de Espermatozoide (ICSI)\n• Falência Ovariana Prematura (IOP):\n  FIV com Ovodoação\n\n🚨 Síndrome de Hiperestímulo Ovariano (SHO):\nPrevenção: Gatilho com agonista de GnRH + congelamento de todos os embriões.", fill="#334155", font=get_font(11))

    draw_footer(draw, W, H)
    out_path = os.path.join(IMG_DIR, "infertilidade_casal_investigacao.jpg")
    im.save(out_path, quality=95)
    print(f"[OK] Gerado: {out_path}")

def build_all():
    print("=== INICIANDO GERAÇÃO DOS 10 INFOGRÁFICOS DE GINECOLOGIA GERAL ===")
    create_diagram_ciclo_menstrual()
    create_diagram_palm_coein()
    create_diagram_sop()
    create_diagram_miomatose()
    create_diagram_adenomiose_endometriose()
    create_diagram_massas_anexiais()
    create_diagram_dor_pelvica()
    create_diagram_climaterio_menopausa()
    create_diagram_amenorreias()
    create_diagram_infertilidade()
    print("=== TODOS OS 10 INFOGRÁFICOS FORAM GERADOS COM SUCESSO! ===")

if __name__ == "__main__":
    build_all()
