# 🏥 Portal de Oncologia Ginecológica, Mastologia e Cirurgia Ginecológica
## Guia Interativo de Alta Definição • Parte 7 (USMLE Step 2 CK / CS / Step 3 + Ivy League Standard)

---

### 🌐 Deploy no GitHub Pages
Este portal foi construído em formato **SPA (Single Page Application) estática moderna**, 100% autossuficiente e sem necessidade de backend, perfeitamente compatível com o GitHub Pages.
- O arquivo `.nojekyll` já está incluído na raiz deste diretório para evitar problemas de processamento de pastas com sublinhado ou assets estáticos.
- Para publicar no GitHub Pages:
  1. Crie ou utilize o repositório no GitHub.
  2. Faça o upload/push do conteúdo desta pasta (`site_onco_masto_cirurgia`).
  3. Vá em **Settings > Pages > Branch: main > Folder: / (root) > Save**.
  4. O site estará disponível em `https://<seu-usuario>.github.io/<repositorio>/`.

---

### 📱 Princípios de Responsividade Móvel e Fluidez
- `overflow-x: hidden !important;` aplicado ao elemento `html` e `body`.
- Todos os contêineres e imagens configurados com `max-width: 100%` e `width: 100%` fluido.
- `word-wrap: break-word` e `overflow-wrap: break-word` ativados globalmente para prevenir estouro de texto em telas estreitas.
- Barra de navegação superior fixa com `position: fixed` no topo (`z-index: 50`) com compensação de espaçamento no body.
- Sem menu lateral redundante (navegação direta e limpa).
- Seletor de acessibilidade para redimensionamento de fonte (`A- / A / A+`).
- Alternador de tema Escuro / Claro (*Dark / Light Mode*) com persistência no `localStorage`.

---

### 🖼️ Galeria de Imagens Ultra-Realistas & Infográficos Incluídos
1. `colposcopia_cervical_real.jpg`: Fotografia colposcópica de alta resolução demonstrando epitélio acetobranco, pontilhado e mosaico.
2. `anatomia_mama_axila_real.jpg`: Modelo anatômico 3D da mama e drenagem axilar com os 3 Níveis de Berg.
3. `cirurgia_pelvica_ureter_real.jpg`: Campo cirúrgico pélvico de alta precisão mostrando a relação "Water under the bridge" (ureter sob artéria uterina).
4. `laparoscopia_pelvica_real.jpg`: Visão laparoscópica em alta definição da cavidade pélvica, útero e anexos com pneumoperitônio.
5. `mamografia_birads_real.jpg`: Mamografia diagnóstica lado a lado: parênquima normal vs carcinoma espiculado BI-RADS 5.
6. `histeroscopia_patologia_real.jpg`: Visão endoscópica de histeroscopia cirúrgica com mioma submucoso FIGO 1 e óstios tubários.
7. `hpv_oncogenese_molecular_e6_e7.jpg`: Infográfico molecular E6/p53, E7/pRb e superexpressão de p16INK4a.
8. `algoritmo_rastreamento_colo_asccp_inca.jpg`: Fluxograma comparativo de rastreamento de colo de útero (INCA 2024-2025 vs ASCCP 2019).
9. `birads_classificacao_condutas.jpg`: Tabela oficial ACR BI-RADS 6ª Edição com risco de câncer e conduta.
10. `cancer_mama_subtipos_moleculares.jpg`: Subtipos moleculares de câncer de mama e ensaio ACOSOG Z0011.
11. `endometrio_classificacao_molecular_figo2023.jpg`: Os 4 subtipos moleculares do TCGA e estadiamento FIGO 2023.
12. `vias_histerectomia_anatomia_cirurgica.jpg`: Hierarquia ACOG de vias de histerectomia e relações anatômicas críticas.
13. `complicacoes_cirurgicas_urologicas_eras.jpg`: Lesão de bexiga, lesão de ureter, febre pós-operatória e protocolo ERAS.

---

### 🛠️ Recursos Interativos
- **Calculadora de BI-RADS 6ª Edição**: Seleciona o achado e entrega categoria, risco percentual e conduta.
- **Simulador de Rastreamento de Colo Uterino**: Entrada de idade, citologia e teste de DNA-HPV com resposta simultânea do INCA e da ASCCP.
- **Classificador Molecular do Câncer de Endométrio (FIGO 2023)**: Entrada de POLE, MMR e p53 com estratificação de prognóstico e imunoterapia.
- **Central de Casos Clínicos (15 Casos do USMLE Step 2 CK / Step 3)**: Questões de múltipla escolha com gabarito imediato, comentários fisiopatológicos da Ivy League e analogias para crianças de 5 anos (🎈), além de placar com pontuação ao vivo.
- **Flashcards High-Yield em 3D**: Cartões que giram com um clique para memorização rápida.
- **Busca Global em Tempo Real**: Filtro instantâneo por texto ou atalho de teclado `Ctrl + K`.
- **Modal Lightbox de Imagem**: Ampliação em tela cheia com alta fidelidade para estudo detalhado.
