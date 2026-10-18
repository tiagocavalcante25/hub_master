# 🏥 Hub Master — Ecossistema Interativo de Ginecologia e Obstetrícia (8 Portais)
### Nível Ivy League · USMLE Step 2 CK / Step 2 CS / Step 3 · Revalida · Residência Médica · FEBRASGO & SUS

Bem-vindo ao repositório central do **Ecossistema Interativo do Internato de Ginecologia e Obstetrícia**. Este projeto integra **8 portais especializados** através de um **Dashboard Mestre Gamificado** ([`index.html`](file:///c:/Users/Admin/Downloads/INTERNATO%20GO/index.html)).

---

## 🗺️ Mapa dos 8 Portais Especializados

| # | Portal Especializado | Diretório / Link | Principais Temas e Ferramentas |
|---|---|---|---|
| **01** | **Fundamentos em GO** | [`site_fundamentos_go/`](file:///c:/Users/Admin/Downloads/INTERNATO%20GO/site_fundamentos_go/index.html) | Semiologia, Exame Especular, Toque Bimanual, Pelvimetria, Índice de Bishop e Segurança do Paciente. |
| **02** | **Obstetrícia & Materno-Fetal** | [`site_obstetricia/`](file:///c:/Users/Admin/Downloads/INTERNATO%20GO/site_obstetricia/index.html) | Pré-Natal, 4 Manobras de Leopold, Cardiotocografia (CTG), Doppler Fetal, DMG e Isoimunização Rh. |
| **03** | **Assistência ao Parto & Puerpério** | [`site_parto_puerperio/`](file:///c:/Users/Admin/Downloads/INTERNATO%20GO/site_parto_puerperio/index.html) | Mecanismo do Parto, Partograma da OMS, Distocias (McRoberts), Hemorragia Pós-Parto (Bakri) e Lactação. |
| **04** | **Urgências e Emergências Obstétricas** | [`site_urgencias_obstetricas/`](file:///c:/Users/Admin/Downloads/INTERNATO%20GO/site_urgencias_obstetricas/index.html) | Pré-Eclâmpsia, Eclâmpsia (Sulfato de Magnésio), Síndrome HELLP, DPP vs Placenta Prévia, Ectópica e Mola. |
| **05** | **Ginecologia Geral & Endocrinologia** | [`site_ginecologia_geral/`](file:///c:/Users/Admin/Downloads/INTERNATO%20GO/site_ginecologia_geral/index.html) | Ciclo Menstrual, SUA (PALM-COEIN), SOP (Rotterdam), Endometriose, Miomatose e Amenorreias. |
| **06** | **Infecções Ginecológicas & ISTs** | [`site_infeccoes_ists/`](file:///c:/Users/Admin/Downloads/INTERNATO%20GO/site_infeccoes_ists/index.html) | Vulvovaginites (Critérios de Amsel), Cervicites, DIP (Monif), Úlceras Genitais, Sífilis e HIV na Gestação. |
| **07** | **Oncologia, Mastologia & Cirurgia** | [`site_onco_masto_cirurgia/`](file:///c:/Users/Admin/Downloads/INTERNATO%20GO/site_onco_masto_cirurgia/index.html) | Rastreamento do Colo, Colposcopia, Mamografia BI-RADS, Câncer de Mama/Ovário/Endométrio e Cirurgia Pélvica. |
| **08** | **Planejamento, Violência, Bioética & SUS** | [`site_planejamento_violencia_sus/`](file:///c:/Users/Admin/Downloads/INTERNATO%20GO/site_planejamento_violencia_sus/index.html) | Critérios MEC OMS, LARCs, Lei 14.443/22, Violência Sexual (PEP 72h), Maria da Penha, Aborto Legal e THM/DEXA. |

---

## 🎮 Funcionalidades do Dashboard Mestre (`index.html`)

1. **Passaporte do Aluno (Gamificação com Persistência Local)**:
   - Marque cada portal como estudado e acompanhe sua evolução de **🔰 Interno Calouro** até **👑 Master em GO** com barra de progresso animada salva no `localStorage`.
2. **Filtros Inteligentes por Cenário de Atuação**:
   - Filtre os portais instantaneamente entre: *Todos (8)*, *🚨 Plantão & Sala de Parto*, *🏥 Ambulatório & SUS*, ou *🔬 Oncologia & Cirurgia*.
3. **Busca Global em Tempo Real (`Ctrl + K`)**:
   - Pesquise por qualquer patologia, medicamento, epônimo ou diretriz e localize imediatamente o portal correspondente.
4. **Desafio Clínico Relâmpago**:
   - Sorteie questões rápidas estilo USMLE/Residência com correção imediata e link direto para o portal do tema.
5. **Central de Atalhos para Calculadoras Clínicas**:
   - Acesso em 1 clique para os simuladores de Critérios MEC, BI-RADS, Sulfato de Magnésio, Partograma, Janela da THM e Corrimentos.
6. **Responsividade Móvel Total**:
   - Barra superior fixa (`position: fixed`), controle de tamanho de fonte (`A- / A / A+`), Modo Escuro/Claro e blindagem contra rolagem horizontal (`overflow-x: hidden`).

---

## 🚀 Como Publicar Todo o Ecossistema no GitHub Pages de Uma Só Vez

Como o Dashboard Mestre está na raiz (`index.html`) e referencia os 8 sites como subpastas relativas, você pode publicar **todos os 8 sites + o Dashboard Central** em um único repositório do GitHub:

```bash
cd "c:\Users\Admin\Downloads\INTERNATO GO"
git init
git add .
git commit -m "feat: ecossistema completo internato GO com dashboard central e 8 portais"
git branch -M main
git remote add origin https://github.com/SEU_USUARIO/internato-go.git
git push -u origin main
```

Depois, em **Settings** > **Pages**, selecione a branch `main` e a pasta `/ (root)`. O endereço principal abrirá o **Hub Master** e todos os 8 portais funcionarão integrados!
