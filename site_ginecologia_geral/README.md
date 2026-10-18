# Ginecologia Geral — Portal Interativo de Decisão Clínica

> **Guia Completo de Ginecologia Geral (Parte 5 — Módulos 40 ao 49)**  
> Alinhado aos padrões: **USMLE Step 2 CK / Step 3**, **Residência Médica em GO / R+**, **FEBRASGO**, **PCDT / SUS**, **FIGO 2018** e **ESHRE 2022**.

---

## 🌟 Visão Geral

Este projeto é uma plataforma web estática, altamente interativa, responsiva e moderna, desenvolvida para estudo aprofundado, fixação ativa e tomada de decisão clínica rápida em Ginecologia Geral.

### 🔬 O Que Está Incluído:
1. **10 Módulos Clínicos Completos (M40 ao M49):**
   - **M40:** O Ciclo Menstrual em 1 Minuto (Eixo HHO, Fases Folicular e Lútea, Parâmetros FIGO)
   - **M41:** Sangramento Uterino Anormal (SUA) e Classificação PALM-COEIN FIGO
   - **M41.8:** Síndrome dos Ovários Policísticos (SOP: Rotterdam 2023, Fisiopatologia da Resistência à Insulina & Indução com Letrozol)
   - **M42:** Miomatose Uterina (Classificação FIGO 0 a 8, Degeneração Rubra Gestacional & Miomectomias)
   - **M43:** Adenomiose (Critérios Ultrassonográficos MUSA & Ressonância com Zona Juncional $\ge$ 12 mm)
   - **M44:** Endometriose (Os '4 Ds', Mapeamento Profundo com Preparo Intestinal & Diretrizes ESHRE 2022 de Tratamento Empírico)
   - **M45:** Cistos e Massas Anexiais (Regras Simples IOTA, Categorias ACR O-RADS US 1 a 5 & Emergência da Torção Ovariana)
   - **M46:** Dor Pélvica (Algoritmo da Dor Aguda com $\beta$-hCG, Dismenorreia Primária vs Secundária & Dor Pélvica Crônica - DPC $\ge$ 6 Meses)
   - **M47:** Climatério, Menopausa e Terapia Hormonal (Janela de Oportunidade < 60 anos, Esquemas com/sem Útero, SGM Local & Osteoporose)
   - **M48:** Investigação das Amenorreias (Os 4 Compartimentos, Teste da Progesterona & Diferencial MRKH 46,XX vs Morris 46,XY e Turner 45,X)
   - **M49:** Infertilidade Básica (Investigação Simultânea do Casal, Espermograma OMS 2021 6ª Edição, Hidrossalpinge pré-FIV & Indução Ovulatória)

2. **10 Infográficos Médicos em Alta Resolução (HD) com Lightbox e Zoom/Pan:**
   - Diagramas anatômicos, fluxogramas de conduta e tabelas comparativas vetoriais.
   - Padrão visual SUS / FEBRASGO / FIGO / ESHRE com tipografia 100% legível em português.

3. **6 Ferramentas e Calculadoras Clínicas Interativas:**
   - **Navegador Interativo PALM-COEIN:** Exploração de cada letra com analogias, clínica, roteiro diagnóstico e conduta.
   - **Calculadora de Risco e Indicação de Biópsia Endometrial (ACOG):** Ponto de corte por idade ($\ge$ 45 anos), espessura na pós-menopausa (> 4 mm), estrogênio sem oposição, Lynch e tamoxifeno.
   - **Mapeador e Estadiador de Miomas FIGO (Subtipos 0 a 8):** Visualização topográfica anatômica com sintomas típicos e plano terapêutico.
   - **Avaliador Diagnóstico de SOP (Critérios de Rotterdam 2023):** Fenotipagem (A, B, C, D), checagem de diagnósticos de exclusão e plano terapêutico individualizado (metabolismo, contracepção e gravidez com letrozol).
   - **Guia de Decisão na Endometriose (Diretriz ESHRE 2022):** Tratamento empírico sem necessidade inicial de laparoscopia, conduta na dor vs conduta na fertilidade.
   - **Estratificador de Risco de Massas Anexiais O-RADS US & IOTA:** Probabilidade de malignidade, correlação com CA-125 e critérios de encaminhamento à oncologia ginecológica.
   - **Árvore de Decisão das Amenorreias:** Fluxograma interativo com os 4 compartimentos e algoritmo primário mamas x útero.
   - **Avaliador de Elegibilidade para Terapia Hormonal (TH):** Validação da janela de oportunidade, seleção de via transdérmica e contraindicações absolutas.
   - **Calculadora de Espermograma (Critérios OMS 2021):** Análise dos limites inferiores de referência e conduta do casal.

4. **Ferramentas Ativas de Aprendizado:**
   - **High-Yield Review (Top 35 Pérolas Rápidas):** Síntese objetiva das regras mais cobradas em provas.
   - **15 Flashcards 3D Interativos:** Cartões com animação tridimensional de virada para memorização espaçada.
   - **Simulado Clínico (15 Vinhetas Estilo USMLE Step 2 CK / Residência):** Casos clínicos com feedback imediato, justificativas detalhadas e pontuação em tempo real.
   - **Busca Global Instantânea (`Ctrl + K`):** Localização instantânea de termos, critérios e fármacos.
   - **Modo Claro / Escuro (Dark Mode):** Alternância suave com persistência em `localStorage` e proteção anti-FOUC.

---

## 🚀 Como Fazer o Deploy no GitHub Pages

O site é **100% estático** (HTML5, Tailwind CSS via CDN, Vanilla JavaScript e CSS moderno), pronto para publicação direta.

### Opção A: Via Terminal Git (Recomendado)

1. Abra o terminal na pasta do projeto:
   ```bash
   cd "c:\Users\Admin\Downloads\INTERNATO GO\site_ginecologia_geral"
   ```

2. Inicialize o repositório e faça o primeiro commit:
   ```bash
   git init
   git add .
   git commit -m "feat: Portal Interativo de Ginecologia Geral (Parte 5)"
   ```

3. Crie um novo repositório no seu GitHub (exemplo: `ginecologia-geral`).

4. Conecte o repositório remoto e envie os arquivos:
   ```bash
   git branch -M main
   git remote add origin https://github.com/SEU_USUARIO/ginecologia-geral.git
   git push -u origin main
   ```

5. Ative o **GitHub Pages**:
   - Vá no seu repositório no GitHub -> **Settings** -> **Pages** (menu lateral esquerdo).
   - Em **Build and deployment** > **Source**, selecione: **Deploy from a branch**.
   - Em **Branch**, selecione `main` e pasta `/ (root)`.
   - Clique em **Save**.
   - Em 1 a 2 minutos, seu site estará acessível na URL:  
     `https://SEU_USUARIO.github.io/ginecologia-geral/`

---

### Opção B: Upload Direto no GitHub Web

1. Crie um novo repositório no GitHub (ex: `ginecologia-geral`).
2. Clique em **Add file** -> **Upload files**.
3. Arraste todos os arquivos e pastas da pasta `site_ginecologia_geral`:
   - `index.html`
   - `.nojekyll` (fundamental para evitar que o GitHub ignore arquivos com sublinhado ou hífen)
   - Pasta `assets/` (com `css/`, `js/` e `img/`)
4. Clique em **Commit changes**.
5. Em **Settings** -> **Pages**, selecione a branch `main` e pasta `/ (root)` e clique em **Save**.

---

## 📂 Estrutura de Arquivos

```text
site_ginecologia_geral/
├── .nojekyll                  # Garante carregamento correto no GitHub Pages
├── index.html                 # Página principal completa com todos os módulos
├── README.md                  # Manual do projeto e instruções de deploy
├── assets/
│   ├── css/
│   │   └── custom.css         # Glassmorphism, 3D flip card, lightbox
│   ├── js/
│   │   └── app.js             # Lógica de cálculo, simuladores, quiz, flashcards
│   └── img/
│       ├── ciclo_menstrual_eixo_hho.jpg
│       ├── sangramento_uterino_palm_coein.jpg
│       ├── sop_rotterdam_fisiopatologia.jpg
│       ├── miomatose_uterina_figo_classificacao.jpg
│       ├── adenomiose_vs_endometriose.jpg
│       ├── massas_anexiais_orads_iota.jpg
│       ├── dor_pelvica_aguda_cronica.jpg
│       ├── climaterio_menopausa_th.jpg
│       ├── amenorreias_4_compartimentos.jpg
│       └── infertilidade_casal_investigacao.jpg
└── scripts/
    ├── build_site.py          # Script gerador do index.html
    ├── build_ginecologia_diagrams.py # Gerador dos 10 infográficos em alta resolução
    └── verify_site.py         # Script de testes automatizados do site
```

---

## 🛡️ Licença e Referências Médicas
- **FEBRASGO:** Tratado de Ginecologia e Manuais de Orientação Clínica.
- **Ministério da Saúde do Brasil / SUS:** Protocolos Clínicos e Diretrizes Terapêuticas (PCDT).
- **FIGO:** Menstrual Disorders Committee (Classificação PALM-COEIN 2018 e Classificação de Leiomiomas).
- **ESHRE:** Endometriosis Guideline 2022 & PCOS International Evidence-based Guideline 2023.
- **ACOG:** Practice Bulletins (Abnormal Uterine Bleeding, Endometrial Intraepithelial Neoplasia, Hormone Therapy).
- **ACR:** O-RADS Ultrasound Committee (O-RADS US System 2022).
- **OMS:** Manual de Análise e Processamento Seminal Humano (6ª Edição, 2021).
