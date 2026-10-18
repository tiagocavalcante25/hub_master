/**
 * app.js - Motor Dinâmico do Portal de Oncologia Ginecológica, Mastologia e Cirurgia
 * Recursos: Dark/Light Mode, Font-Size Acessível, Busca em Tempo Real, 
 * 4 Calculadoras Clínicas, 15 Casos Interativos USMLE, Flashcards e Modal Viewer.
 */

document.addEventListener('DOMContentLoaded', () => {
  // Inicialização de Ícones Lucide
  if (window.lucide) {
    lucide.createIcons();
  }

  initTheme();
  initFontSize();
  initGlobalSearch();
  initClinicalTools();
  initClinicalCases();
  initFlashcards();
  initImageViewer();
});

/* ==========================================================================
   1. GERENCIADOR DE TEMA (DARK / LIGHT)
   ========================================================================== */
function initTheme() {
  const themeToggle = document.getElementById('theme-toggle');
  if (!themeToggle) return;

  themeToggle.addEventListener('click', () => {
    const isDark = document.documentElement.classList.toggle('dark');
    localStorage.setItem('theme', isDark ? 'dark' : 'light');
    if (window.lucide) lucide.createIcons();
  });
}

/* ==========================================================================
   2. GERENCIADOR DE TAMANHO DE FONTE ACESSÍVEL
   ========================================================================== */
function initFontSize() {
  const btnDecrease = document.getElementById('font-decrease');
  const btnReset = document.getElementById('font-reset');
  const btnIncrease = document.getElementById('font-increase');

  const setSize = (size) => {
    document.documentElement.setAttribute('data-font-size', size);
    localStorage.setItem('fontSizePreference', size);
  };

  if (btnDecrease) btnDecrease.addEventListener('click', () => setSize('small'));
  if (btnReset) btnReset.addEventListener('click', () => setSize('medium'));
  if (btnIncrease) btnIncrease.addEventListener('click', () => setSize('large'));
}

/* ==========================================================================
   3. BUSCA GLOBAL EM TEMPO REAL
   ========================================================================== */
function initGlobalSearch() {
  const searchInput = document.getElementById('global-search');
  if (!searchInput) return;

  searchInput.addEventListener('input', (e) => {
    const term = e.target.value.toLowerCase().trim();
    const modules = document.querySelectorAll('.module-card');
    let visibleCount = 0;

    modules.forEach(mod => {
      const text = mod.innerText.toLowerCase();
      if (!term || text.includes(term)) {
        mod.style.display = 'block';
        visibleCount++;
      } else {
        mod.style.display = 'none';
      }
    });

    const noResults = document.getElementById('no-search-results');
    if (noResults) {
      noResults.style.display = visibleCount === 0 ? 'block' : 'none';
    }
  });

  // Atalho de Teclado Ctrl+K ou Cmd+K
  window.addEventListener('keydown', (e) => {
    if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === 'k') {
      e.preventDefault();
      searchInput.focus();
    }
  });
}

/* ==========================================================================
   4. CALCULADORAS CLÍNICAS INTERATIVAS
   ========================================================================== */
function initClinicalTools() {
  // Calculadora BI-RADS
  const biradsSelect = document.getElementById('calc-birads-finding');
  const biradsResult = document.getElementById('calc-birads-result');
  if (biradsSelect && biradsResult) {
    biradsSelect.addEventListener('change', () => {
      const val = biradsSelect.value;
      const data = {
        'incompleto': { cat: 'BI-RADS 0', risco: 'N/A', cond: 'Necessita avaliação adicional (USG, compressão focal, magnificação ou comparação com anteriores)', badge: 'bg-slate-500' },
        'cisto_simples': { cat: 'BI-RADS 2', risco: '0% (Benigno)', cond: 'Seguimento de rastreamento habitual por faixa etária', badge: 'bg-emerald-600' },
        'fibroadenoma_estavel': { cat: 'BI-RADS 2', risco: '0% (Benigno)', cond: 'Seguimento de rastreamento habitual por faixa etária', badge: 'bg-emerald-600' },
        'nodulo_circunscrito_novo': { cat: 'BI-RADS 3', risco: '< 2% (Provavelmente Benigno)', cond: 'Controle radiológico precoce semestral por 2 a 3 anos', badge: 'bg-amber-500' },
        'nodulo_indistinto': { cat: 'BI-RADS 4B', risco: '10% a 50% (Média Suspeição)', cond: 'Biópsia por agulha grossa (Core Biopsy guiada por imagem)', badge: 'bg-orange-600' },
        'massa_espiculada': { cat: 'BI-RADS 5', risco: '> 95% (Altamente Suspeito)', cond: 'Biópsia imediata (Core Biopsy) e planejamento oncológico', badge: 'bg-rose-600' },
        'calcificacoes_pleomorficas': { cat: 'BI-RADS 5', risco: '> 95% (Altamente Suspeito)', cond: 'Biópsia por agulha grossa (Mamotomia a vácuo com clipe) imediata', badge: 'bg-rose-600' }
      };

      const res = data[val];
      if (res) {
        biradsResult.innerHTML = `
          <div class="p-4 rounded-xl border border-slate-200 dark:border-slate-700 bg-white dark:bg-slate-800 space-y-2">
            <div class="flex items-center justify-between">
              <span class="text-xs font-bold uppercase tracking-wider text-slate-500">Resultado Oficial</span>
              <span class="px-2.5 py-0.5 rounded-full text-xs font-extrabold text-white ${res.badge}">${res.cat}</span>
            </div>
            <p class="text-sm font-semibold text-slate-900 dark:text-white">Risco de Malignidade: <span class="font-normal text-rose-600 dark:text-rose-400 font-bold">${res.risco}</span></p>
            <p class="text-xs text-slate-600 dark:text-slate-300"><strong>Conduta:</strong> ${res.cond}</p>
          </div>
        `;
      }
    });
  }

  // Simulador Rastreamento Colo (INCA 2024-2025 vs ASCCP 2019)
  const btnSimColo = document.getElementById('btn-sim-colo');
  if (btnSimColo) {
    btnSimColo.addEventListener('click', () => {
      const age = parseInt(document.getElementById('sim-colo-age').value) || 30;
      const cito = document.getElementById('sim-colo-cito').value;
      const hpv = document.getElementById('sim-colo-hpv').value;
      const resDiv = document.getElementById('sim-colo-result');

      let condINCA = "";
      let condASCCP = "";

      // ===== INCA 2024-2025 / PORTARIA GM/MS 820/2024: DNA-HPV PRIMÁRIO =====
      if (age < 25) {
        condINCA = "🚫 Abaixo da idade de rastreamento no Brasil (inicia aos 25 anos). Não rastrear!";
      } else {
        // Algoritmo DNA-HPV primário a cada 5 anos (25-64a)
        if (hpv === 'negativo') {
          condINCA = "✅ DNA-HPV NEGATIVO: Repetir DNA-HPV em 5 anos (rastreamento de rotina SUS).";
        } else if (hpv === '16_18') {
          condINCA = "🚨 HPV 16/18 POSITIVO: COLPOSCOPIA IMEDIATA (independente do resultado citológico).";
        } else if (hpv === 'outro_alto') {
          // HPV outro tipo oncogênico -> triagem reflexa com citologia
          if (cito === 'nilm') {
            condINCA = "⚠️ HPV OUTRO ALTO RISCO + Citologia NILM: Repetir DNA-HPV em 12 meses.";
          } else if (cito === 'asc-us' || cito === 'lsil') {
            condINCA = "🚨 HPV OUTRO ALTO RISCO + ASC-US/LSIL: Encaminhar para COLPOSCOPIA.";
          } else if (cito === 'hsil' || cito === 'asc-h' || cito === 'agc') {
            condINCA = "🚨 HPV OUTRO ALTO RISCO + HSIL/ASC-H/AGC: COLPOSCOPIA IMEDIATA (alto risco de lesão precursora).";
          }
        }
      }

      // ===== ASCCP 2019 (Referência Internacional Baseada em Risco) =====
      if (hpv === '16_18') {
        condASCCP = "🚨 HPV 16/18+: COLPOSCOPIA IMEDIATA (risco imediato de NIC 3+ ~5-8%).";
      } else if (cito === 'hsil') {
        condASCCP = "🚨 HSIL: Colposcopia ou Excisão Direta Ver e Tratar (risco de NIC 3+ > 60%).";
      } else if (cito === 'asc-h') {
        condASCCP = "🚨 ASC-H: COLPOSCOPIA IMEDIATA (risco de NIC 3+ ~30-40%).";
      } else if (cito === 'agc') {
        condASCCP = "🚨 AGC: Colposcopia + Avaliação Endocervical + Endometrial (se ≥35 anos ou fatores de risco).";
      } else if (hpv === 'outro_alto' && (cito === 'asc-us' || cito === 'lsil')) {
        condASCCP = "⚠️ HPV outro alto risco + ASC-US/LSIL: Colposcopia recomendada (risco de NIC 3+ ≥ 4%).";
      } else if (cito === 'asc-us' && hpv === 'negativo') {
        condASCCP = "✅ ASC-US + HPV-: Rastreamento regular em 5 anos (risco de NIC 3+ < 0,5%).";
      } else if (cito === 'nilm' && hpv === 'negativo') {
        condASCCP = "✅ NILM + HPV-: Rastreamento regular a cada 5 anos com DNA-HPV primário.";
      } else if (cito === 'lsil' && hpv === 'negativo') {
        condASCCP = "✅ LSIL + HPV-: Rastreamento regular em 5 anos (alta taxa de regressão espontânea).";
      } else {
        condASCCP = "ℹ️ Combinação sob avaliação clínica individualizada (ASCCP 2019).";
      }

      // Nota especial HIV+
      const hivNote = "<p class='text-[10px] text-amber-700 dark:text-amber-300 mt-2 border-t border-amber-200 dark:border-amber-800 pt-1'><strong>🎗️ Paciente HIV+:</strong> Rastreamento com DNA-HPV primário aos 25 anos (ou início da atividade sexual). Repetir em 12 meses; se negativos, manter a cada 3 anos. Se CD4 < 200 céls/mm³: citologia semestral.</p>";

      resDiv.innerHTML = `
        <div class="grid grid-cols-1 md:grid-cols-2 gap-3 mt-3">
          <div class="p-3.5 rounded-xl bg-sky-50 dark:bg-sky-950/40 border border-sky-200 dark:border-sky-800">
            <span class="text-[10px] font-bold uppercase text-sky-700 dark:text-sky-300 flex items-center gap-1">
              🇧🇷 Brasil — INCA 2024-2025 / SUS (DNA-HPV Primário)
            </span>
            <p class="text-xs text-slate-800 dark:text-slate-200 mt-1">${condINCA}</p>
            ${hivNote}
          </div>
          <div class="p-3.5 rounded-xl bg-purple-50 dark:bg-purple-950/40 border border-purple-200 dark:border-purple-800">
            <span class="text-[10px] font-bold uppercase text-purple-700 dark:text-purple-300 flex items-center gap-1">
              🌐 Internacional — ASCCP 2019 (Risk-Based Management)
            </span>
            <p class="text-xs text-slate-800 dark:text-slate-200 mt-1">${condASCCP}</p>
          </div>
        </div>
      `;
      if (window.lucide) lucide.createIcons();
    });
  }

  // Classificador Molecular FIGO 2023 Endométrio (Hierarquia Estrita TCGA / FIGO 2023)
  const btnCalcEndo = document.getElementById('btn-calc-endo');
  if (btnCalcEndo) {
    btnCalcEndo.addEventListener('click', () => {
      const pole = document.getElementById('endo-pole').value;
      const mmr = document.getElementById('endo-mmr').value;
      const p53 = document.getElementById('endo-p53').value;
      const out = document.getElementById('endo-result');

      // HIERARQUIA OBRIGATÓRIA: 1. POLEmut -> 2. MMRd -> 3. p53abn -> 4. NSMP
      let sub = "", prog = "", cond = "", cor = "", badge = "", sufixo = "";

      if (pole === 'mutado') {
        sub = "POLE ultramutado (POLEmut)";
        prog = "Excelente Prognóstico — Sobrevida global > 95% em 5 anos";
        cond = "Descalonamento terapêutico: permite dispensar quimioterapia e radioterapia adjuvante em estádios I-II.";
        cor = "text-emerald-600 dark:text-emerald-400 border-emerald-500";
        badge = "bg-emerald-600";
        sufixo = "POLEmut";
      } else if (mmr === 'deficiente') {
        sub = "Instabilidade de Microssatélites (MMRd / MSI-H)";
        prog = "Prognóstico Intermediário-Favorável";
        cond = "ALTA SENSIBILIDADE À IMUNOTERAPIA: Dostarlimabe (ensaio RUBY) ou Pembrolizumabe (ensaio NRG-GY018) adjuvante. Obrigatório teste genético para rastreio de Síndrome de Lynch.";
        cor = "text-sky-600 dark:text-sky-400 border-sky-500";
        badge = "bg-sky-600";
        sufixo = "MMRd";
      } else if (p53 === 'anomalo') {
        sub = "p53 Anômalo (p53abn — mutação de TP53)";
        prog = "Pior Prognóstico — Alto Risco de Recorrência Precoce e Metástase";
        cond = "Quimioterapia sistêmica adjuvante INTENSIVA (Carboplatina + Paclitaxel) OBRIGATÓRIA. Radioterapia pélvica complementar se invasão miometrial > 50% ou estroma cervical.";
        cor = "text-rose-600 dark:text-rose-400 border-rose-500";
        badge = "bg-rose-600";
        sufixo = "p53abn";
      } else {
        sub = "Sem Perfil Molecular Específico (NSMP / p53wt / MMRp / POLEwt)";
        prog = "Prognóstico Intermediário";
        cond = "Tratamento cirúrgico padrão (HTA + BSO + SLN). Adjuvância guiada por fatores clinicopatológicos: grau histológico, invasão miometrial (≥50%), invasão linfovascular (LVSI). Sensibilidade a hormonioterapia (ER/PR+).";
        cor = "text-amber-600 dark:text-amber-400 border-amber-500";
        badge = "bg-amber-600";
        sufixo = "NSMP";
      }

      out.innerHTML = `
        <div class="p-4 rounded-xl border bg-white dark:bg-slate-800 mt-3 ${cor}">
          <div class="flex items-center justify-between mb-2">
            <h4 class="font-extrabold text-sm uppercase tracking-wide">${sub}</h4>
            <span class="px-2 py-0.5 rounded-full text-[10px] font-extrabold text-white ${badge}">${sufixo}</span>
          </div>
          <p class="text-xs font-semibold text-slate-800 dark:text-slate-200 mb-2">${prog}</p>
          <p class="text-xs text-slate-700 dark:text-slate-300"><strong>Conduta FIGO 2023 / ESGO-ESTRO-ESP:</strong> ${cond}</p>
          <p class="text-[10px] text-slate-500 dark:text-slate-400 mt-2 border-t border-slate-200 dark:border-slate-700 pt-2">
            🧬 Estadiamento integrado FIGO 2023 com sufixo molecular: ex. <strong>Stage IB1 ${sufixo}</strong>
          </p>
        </div>
      `;
    });
  }

  // 4. Calculadora de Risco de TEV — Escore de Caprini (2010) + ACERTO / ERAS 2023
  const btnCalcCaprini = document.getElementById('btn-calc-caprini');
  if (btnCalcCaprini) {
    btnCalcCaprini.addEventListener('click', () => {
      const checks = document.querySelectorAll('.caprini-chk:checked');
      let score = 0;
      checks.forEach(c => score += parseInt(c.value));

      let risco = "", profilaxia = "", cor = "", badge = "";

      if (score <= 1) {
        risco = "Baixíssimo (< 1%)";
        profilaxia = "Mobilização precoce ativa + deambulação no pós-operatório. Profilaxia farmacológica não indicada de rotina.";
        cor = "text-emerald-600 dark:text-emerald-400 border-emerald-500"; badge = "bg-emerald-600";
      } else if (score === 2) {
        risco = "Baixo (1-2%)";
        profilaxia = "Compressão pneumática intermitente (CPI) / meias elásticas + deambulação precoce no dia da cirurgia.";
        cor = "text-sky-600 dark:text-sky-400 border-sky-500"; badge = "bg-sky-600";
      } else if (score >= 3 && score <= 4) {
        risco = "Moderado (3-5%)";
        profilaxia = "Enoxaparina 40 mg SC 1x/dia (iniciar 12h pré-op ou 6-12h pós-op) + métodos mecânicos (CPI). Manter durante toda a internação hospitalar.";
        cor = "text-amber-600 dark:text-amber-400 border-amber-500"; badge = "bg-amber-600";
      } else if (score >= 5 && score <= 7) {
        risco = "Alto (5-10%)";
        profilaxia = "Enoxaparina 40 mg SC 1x/dia + CPI + meias. <strong>PROFILAXIA ESTENDIDA POR 28 DIAS</strong> no pós-operatório (obrigatória em cirurgia oncológica abdominal/laparoscópica).";
        cor = "text-orange-600 dark:text-orange-400 border-orange-500"; badge = "bg-orange-600";
      } else {
        risco = "Muito Alto (> 10%)";
        profilaxia = "Enoxaparina 40 mg SC 1x/dia (ajustar para 0,5 mg/kg se peso ≥ 100 kg) + CPI intra e pós-operatória. <strong>PROFILAXIA ESTENDIDA POR 28 A 35 DIAS PÓS-OP</strong>. Se contraindicação hemorrágica: CPI contínua ou filtro de veia cava temporário.";
        cor = "text-rose-600 dark:text-rose-400 border-rose-500"; badge = "bg-rose-600";
      }

      const pesoNote = "<p class='text-[10px] text-amber-700 dark:text-amber-300 mt-2 border-t border-amber-200 dark:border-amber-800 pt-1'><strong>⚖️ Ajustes de Dose:</strong> Se peso ≥ 100 kg ou IMC ≥ 40 kg/m²: Enoxaparina 0,5 mg/kg SC 1x/dia (ex: 120 kg = 60 mg). Profilaxia cirúrgica com Cefazolina: aumentar para 3g EV se peso ≥ 120 kg.</p>";

      document.getElementById('caprini-result').innerHTML = `
        <div class="p-4 rounded-xl border bg-white dark:bg-slate-800 mt-3 ${cor}">
          <div class="flex items-center justify-between mb-2">
            <span class="font-extrabold text-sm uppercase tracking-wide">Escore Caprini: ${score} Pontos</span>
            <span class="px-2 py-0.5 rounded-full text-[10px] font-extrabold text-white ${badge}">${risco.split('(')[0].trim()}</span>
          </div>
          <p class="text-xs font-semibold text-slate-800 dark:text-slate-200 mb-2">Risco de TEV em 30 dias: ${risco.split('(')[1]?.replace(')','') || risco}</p>
          <p class="text-xs text-slate-700 dark:text-slate-300"><strong>Conduta (ACERTO/ERAS 2023 + ACCP/ASCO):</strong> ${profilaxia}</p>
          ${pesoNote}
        </div>
      `;
    });
  }
}

/* ==========================================================================
   5. CENTRAL DE CASOS CLÍNICOS (15 CASOS USMLE INTERATIVOS)
   ========================================================================== */
const CASOS_DATA = [
  {
    id: 1,
    title: "Caso 1: Rastreamento Cervical em Paciente HIV-Positiva",
    enunciado: "Mulher de 32 anos, com diagnóstico recente de infecção por HIV em uso estável de antirretrovirais (contagem de linfócitos T-CD4+ de 450 céls/mm³ e carga viral indetectável há 6 meses), comparece para consulta ginecológica preventiva. Ela nunca realizou citologia oncótica cervical. Ao exame especular: colo uterino sem lesões visíveis macroscopicamente. Qual é o protocolo correto de rastreamento cervical para esta paciente?",
    options: [
      { id: 'A', text: "Realizar citologia cervical a cada 3 anos iniciando aos 25 anos, idêntico à população geral" },
      { id: 'B', text: "Realizar citologia cervical semestral no primeiro ano; se ambos normais, manter seguimento citológico anual", correct: true },
      { id: 'C', text: "Encaminhar diretamente para conização a frio diagnóstica independentemente da citologia" },
      { id: 'D', text: "Realizar teste de DNA-HPV a cada 5 anos isoladamente sem citologia" },
      { id: 'E', text: "Não há indicação de rastreamento se a carga viral do HIV estiver indetectável" }
    ],
    explicacaoIvy: "Mulheres vivendo com HIV têm maior persistência de infecção por subtipos oncogênicos do HPV e risco até 5 a 6 vezes maior de câncer cervical invasor (que é doença definidora de AIDS). Conforme as diretrizes vigentes do Ministério da Saúde do Brasil (2023/2024), OMS e CDC/ACOG: no modelo citológico tradicional, realiza-se citologia a cada 6 meses no primeiro ano; se ambos normais, seguimento anual enquanto CD4 > 200 céls/mm³ (se CD4 < 200, mantém-se semestral). Na nova diretriz de DNA-HPV primário (MS/INCA 2024-2025): inicia-se teste molecular de DNA-HPV aos 25 anos (ou início da atividade sexual); se negativo, repete-se em 12 meses e, mantendo-se negativo, o intervalo é de 3 em 3 anos (com citologia reflexa de triagem apenas se HPV positivo).",
    analogia5Anos: "Como os soldadinhos do corpo dessa moça estão se recuperando de um vírus travesso (o HIV), nós temos que vigiar a portinha do útero com o dobro de atenção! Olhamos de 6 em 6 meses no começo, e se estiver tudo limpinho, olhamos uma vez por ano para garantir que nenhum bichinho faça bagunça!"
  },
  {
    id: 2,
    title: "Caso 2: Sangramento Pós-Menopausa e Eco Endometrial de 7 mm",
    enunciado: "Mulher de 58 anos, menopausa há 6 anos, relata episódio de sangramento vaginal em pequena quantidade há 3 semanas. Nega uso de terapia hormonal. IMC = 33 kg/m². Ultrassonografia transvaginal evidencia útero de volume normal e eco endometrial medindo 7 mm, com ecotextura heterogênea. Ovários atróficos. Qual é a conduta diagnóstica imediata padrão-ouro?",
    options: [
      { id: 'A', text: "Tranquilizar a paciente e repetir a ultrassonografia transvaginal em 6 meses" },
      { id: 'B', text: "Prescrever progestagênio oral por 10 dias para teste de privação hormonal" },
      { id: 'C', text: "Realizar biópsia endometrial ambulatorial (com cânula de Pipelle ou guiada por histeroscopia)", correct: true },
      { id: 'D', text: "Indicar histerectomia total com salpingo-ooforectomia bilateral de urgência" },
      { id: 'E', text: "Solicitar ressonância magnética de pelve e dosagem de CA-125 antes de qualquer procedimento" }
    ],
    explicacaoIvy: "Regra de ouro da ginecologia: Sangramento pós-menopausa é câncer de endométrio até que se prove o contrário (representa malignidade em 10% dos casos). Na USG transvaginal em mulheres na pós-menopausa sem terapia hormonal, a espessura endometrial normal é de até 4 mm. Um eco endometrial ≥ 4 mm associado a sangramento impõe a realização de amostragem tecidual endometrial (biópsia ambulatorial com Pipelle ou histeroscopia com biópsia direcionada).",
    analogia5Anos: "Na vovó, o forninho da casinha já dormiu e não pode soltar nenhuma gotinha de sangue. Se saiu sangue e o colchãozinho do útero está mais gordinho que 4 milímetros, o médico tem que beliscar um pedacinho com uma cânula fininha para olhar no microscópio!"
  },
  {
    id: 3,
    title: "Caso 3: Nódulo Mamário Palpável em Mulher de 24 Anos",
    enunciado: "Mulher de 24 anos procura atendimento relatando nódulo palpável na mama direita há 2 meses. Ao exame físico: nódulo de 2 cm no quadrante superior lateral direito, móvel, bem delimitado, consistência fibroelástica, indolor, sem alterações na pele sobrejacente e sem linfonodomegalias axilares. Qual é o exame de imagem inicial de escolha?",
    options: [
      { id: 'A', text: "Mamografia digital bilateral com compressão localizada" },
      { id: 'B', text: "Ultrassonografia das mamas", correct: true },
      { id: 'C', text: "Ressonância magnética das mamas com contraste paramagnético" },
      { id: 'D', text: "Punção aspirativa por agulha fina (PAAF) às cegas sem exame de imagem" },
      { id: 'E', text: "Termografia mamária digital" }
    ],
    explicacaoIvy: "Em mulheres com menos de 30 anos com nódulo mamário palpável, o exame de imagem inicial de escolha é a Ultrassonografia Mamária. Mamas jovens possuem parênquima fibroglandular extremamente denso, o que reduz drasticamente a sensibilidade da mamografia, além de expor a paciente desnecessariamente a radiação ionizante. A USG diferencia com facilidade nódulos císticos de sólidos (como o fibroadenoma, que é a causa mais prevalente nessa idade).",
    analogia5Anos: "Em meninas bem jovens, a mama é durinha e cheia de glândula como uma massinha de modelar firme. A máquina de mamografia de raio-X não consegue enxergar direito através dessa massinha! O ultrassom usa ondas de som suaves para ver se a bolinha é um cisto de água ou uma massinha benigna!"
  },
  {
    id: 4,
    title: "Caso 4: Mastite Puerperal com Piora Clínica e Flutuação",
    enunciado: "Puérpera de 26 anos, no 20º dia pós-parto normal em aleitamento materno exclusivo, vinha em tratamento ambulatorial para mastite puerperal em mama esquerda com cefalexina há 5 dias. Ela retorna relatando persistência de febre (38,6°C) e piora da dor. Ao exame físico: eritema e calor em quadrante superior externo da mama esquerda, com área dolorosa de 4 cm apresentando sensação de flutuação central à palpação. Qual é o diagnóstico e a conduta recomendada?",
    options: [
      { id: 'A', text: "Carcinoma inflamatório de mama; realizar mastectomia radical imediata" },
      { id: 'B', text: "Abscesso mamário puerperal; realizar esvaziamento por aspiração com agulha guiada por USG (ou drenagem cirúrgica) e manter amamentação", correct: true },
      { id: 'C', text: "Ingurgitamento mamário fisiológico; orientar massagens circulares vigorosas e banhos quentes" },
      { id: 'D', text: "Abscesso mamário; suspender a amamentação bilateralmente com cabergolina" },
      { id: 'E', text: "Mastite viral; trocar antibiótico por aciclovir e manter repouso absoluto" }
    ],
    explicacaoIvy: "Mastite bacteriana que não melhora após 48 a 72 horas de antibioticoterapia adequada deve levantar forte suspeita de Abscesso Mamário (coleção purulenta). A presença de flutuação ao exame físico é sinal patognomônico. O tratamento de escolha envolve o esvaziamento da coleção purulenta, preferencialmente por aspiração com agulha guiada por ultrassonografia (menos dolorosa, preserva a estética e permite continuidade imediata da lactação) e ajuste do antibiótico. A amamentação deve ser MANTIDA na mama contralateral e também na afetada (se a incisão/dor permitir e a boca do bebê não tocar na lesão). Conforme o Protocolo ABM 36 (2022) endossado pela Sociedade Brasileira de Pediatria (SBP) e Ministério da Saúde (2023): É CONTRAINDICADO o uso de bombas mecânicas de extração láctea nas primeiras 24-48 horas de mastite aguda/ingurgitamento intenso, pois a pressão mecânica lesiona os alvéolos inflamados e exacerba o edema tecidual.",
    analogia5Anos: "Se a fábrica de leitinho inflamou e formou uma bolsinha com catarro/pus (abscesso), o médico tira aquele pus com uma seringa fininha no ultrassom para a mamãe não sentir dor. E a mamãe PODE continuar dando o tetê para o bebê, porque o leitinho ajuda a limpar os caninhos!"
  },
  {
    id: 5,
    title: "Caso 5: Lesão Ureteral Iatrogênica Pós-Histerectomia Abdominal",
    enunciado: "Mulher de 44 anos submeteu-se a histerectomia total abdominal difícil por útero miomatoso de 1.100g e aderências pélvicas há 4 dias. No 4º dia de pós-operatório, queixa-se de febre baixa (37,9°C), náuseas e dor em flanco esquerdo irradiando para a fossa ilíaca. Ao exame físico: sinal de Giordano positivo à esquerda. Exames laboratoriais: Creatinina sérica elevada de 0,8 para 1,9 mg/dL e leucocitose de 14.500/mm³. Qual é o exame padrão-ouro para o diagnóstico?",
    options: [
      { id: 'A', text: "Radiografia simples de abdome em posição ortostática" },
      { id: 'B', text: "Urotomografia computadorizada com contraste intravenoso e fase excretora tardia", correct: true },
      { id: 'C', text: "Cistoscopia ambulatorial com biópsia da cúpula vesical" },
      { id: 'D', text: "Ressonância magnética de coluna lombar" },
      { id: 'E', text: "Urocultura seriada e reavaliação em 14 dias" }
    ],
    explicacaoIvy: "A lesão do ureter (ligadura acidental ou desvascularização/queimadura térmica) é uma das complicações mais temidas da cirurgia ginecológica. Costuma manifestar-se alguns dias após a cirurgia com dor lombar, febre, hidronefrose ou urinoma. O exame padrão-ouro para avaliar a integridade da árvore urinária e diagnosticar extravasamento de contraste ou obstrução ureteral é a Urotomografia (TC de abdome e pelve com contraste iodado nas fases nefrográfica e excretora tardia).\n\n⏱️ JANELA TERAPÊUTICA CRÍTICA DE CONDUTA:\n1. Reconhecimento intraoperatório: Reparo imediato obrigatório (ureteroureterostomia primária sobre duplo J nas lesões altas/médias sem perda de substância; reimplante ureterovesical com psoas hitch ou Boari flap nas lesões baixas próximas à bexiga).\n2. Diagnóstico em até 72h de pós-operatório: Tentativa imediata de passagem de cateter duplo J retrógrado por cistoscopia (taxa de sucesso > 85%, permitindo cicatrização guiada sem reoperação aberta).\n3. Diagnóstico tardio (> 72h, fístula ureterovaginal ou estenose/isquemia consolidada): Descompressão renal de urgência com nefrostomia percutânea e reparo cirúrgico definitivo tardio eletivo após 6 a 12 semanas (após resolução do processo inflamatório intenso).",
    analogia5Anos: "O caninho que leva o xixi do rim para a bexiga (ureter) passa coladinho nos vasos do útero ('a água passa debaixo da ponte'). Se durante a cirurgia o médico sem querer machucou esse caninho, o xixi pode ficar preso e inchar o rim. A tomografia com contraste desenha o caninho e mostra exatamente onde o caninho vazou!"
  },
  {
    id: 6,
    title: "Caso 6: Citologia com AGC (Células Glandulares Atípicas)",
    enunciado: "Mulher de 42 anos, assintomática, realiza citologia de rastreamento de rotina cujo laudo retorna: 'Células glandulares atípicas de significado indeterminado (AGC / AGUS)'. O teste para HPV de alto risco realizado concomitantemente é negativo. Qual é a conduta preconizada pelas diretrizes vigentes (ASCCP / INCA)?",
    options: [
      { id: 'A', text: "Tranquilizar a paciente e repetir a citologia oncótica em 3 anos" },
      { id: 'B', text: "Colposcopia com avaliação do canal endocervical (escovado/curetagem) e avaliação endometrial (biópsia)", correct: true },
      { id: 'C', text: "Cauterização química do colo com ácido tricloroacético a 90%" },
      { id: 'D', text: "Histerectomia simples sem necessidade de investigação prévia" },
      { id: 'E', text: "Iniciar antibioticoterapia com metronidazol e repetir em 30 dias" }
    ],
    explicacaoIvy: "O achado de AGC (Atypical Glandular Cells) carrega alto risco de patologia maligna subjacente (cerca de 20 a 30% têm NIC 2+, adenocarcinoma in situ ou adenocarcinoma invasor de endocérvice ou de endométrio). Por isso, as diretrizes internacionais (ASCCP) e nacionais (INCA) recomendam avaliação imediata com Colposcopia + Avaliação Endocervical. Em mulheres com ≥ 35 anos (ou com fatores de risco para câncer de endométrio em qualquer idade), a avaliação do endométrio com biópsia endometrial é mandatória!",
    analogia5Anos: "Células glandulares atípicas são como um alarme de incêndio sério na fábrica de muco do útero. Mesmo que o teste de HPV tenha dado negativo, temos que olhar a portinha do útero (colposcopia) e o forrinho lá dentro (endométrio) para ter certeza absoluta de que não tem nenhum tumorzinho escondido!"
  },
  {
    id: 7,
    title: "Caso 7: Câncer de Colo Uterino em Paciente Jovem Desejando Fertilidade",
    enunciado: "Mulher de 28 anos, nuligesta, com diagnóstico anatomopatológico de carcinoma de células escamosas invasor de colo uterino. Ressonância magnética de pelve evidencia tumor confinado ao colo medindo 1,6 cm no maior diâmetro, sem invasão dos paramétrios e sem linfonodomegalias suspeitas (FIGO 2018 Estádio IB1). A paciente tem forte desejo reprodutivo futuro. Qual é a opção cirúrgica oncológica padrão que preserva a fertilidade?",
    options: [
      { id: 'A', text: "Histerectomia radical de Wertheim-Meigs por via aberta" },
      { id: 'B', text: "Traquelectomia radical com linfadenectomia pélvica", correct: true },
      { id: 'C', text: "Radioquimioterapia definitiva exclusiva" },
      { id: 'D', text: "Conização simples a laser sem dissecção linfonodal" },
      { id: 'E', text: "Ooforectomia bilateral exclusiva mantendo o útero intacto" }
    ],
    explicacaoIvy: "Para pacientes jovens com câncer invasor de colo uterino em estádio inicial (IB1 pelo FIGO 2018, lesões < 2 cm sem invasão paramétrial ou linfonodal) que desejam preservar a fertilidade, o tratamento cirúrgico padrão-ouro conservador é a Traquelectomia Radical (resseca-se o colo uterino, paramétrios mediais e terço superior da vagina, com confecção de cerclagem no istmo uterino e linfadenectomia pélvica). O corpo do útero e os ovários são preservados, permitindo futuras gestações (por cesariana agendada).",
    analogia5Anos: "Essa paciente jovem quer muito ter um bebê! Como o tumorzinho é pequeno e está só na pontinha do gargalo do útero, o cirurgião retira apenas o gargalo (o colo) e a raiz ao redor, mas guarda a casinha do bebê (o corpo do útero) e os ovários intactos para ela poder ser mamãe no futuro!"
  },
  {
    id: 8,
    title: "Caso 8: Massa Ovariana Suspeita na Pós-Menopausa e Marcadores",
    enunciado: "Mulher de 62 anos apresenta queixa de distensão abdominal progressiva e saciedade precoce há 3 meses. Ao exame físico: palpa-se massa pélvica de limites imprecisos e nodularidade no fundo de saco de Douglas. Ultrassonografia transvaginal revela massa cística complexa de 8 cm no ovário direito, com septos espessos (> 3 mm), projeções papilares internas e presença de ascite na cavidade peritoneal. Exames laboratoriais mostram CA-125 = 480 U/mL (referência < 35 U/mL). Qual é a principal suspeita histopatológica e a conduta cirúrgica padrão?",
    options: [
      { id: 'A', text: "Teratoma cístico maduro; realizar punção aspirativa transvaginal guiada por USG" },
      { id: 'B', text: "Carcinoma seroso de alto grau de ovário; laparotomia exploradora para estadiamento cirúrgico completo e citorredução ótima", correct: true },
      { id: 'C', text: "Endometrioma ovariano bilateral; prescrever análogo de GnRH por 6 meses" },
      { id: 'D', text: "Cisto folicular funcional; observação clínica com repetição ultrassonográfica em 3 meses" },
      { id: 'E', text: "Abscesso tubo-ovariano crônico; drenagem percutânea exclusiva" }
    ],
    explicacaoIvy: "Massa ovariana complexa na pós-menopausa associada a ascite, projeções papilares e CA-125 muito elevado é altamente sugestiva de Carcinoma Epitelial de Ovário (sendo o Carcinoma Seroso de Alto Grau o subtipo mais prevalente, com origem molecular frequentemente na fímbria tubária / STIC). O estadiamento no câncer de ovário é CIRÚRGICO (FIGO): exige laparotomia mediana ampla para inspeção peritoneal, histerectomia total, salpingo-ooforectomia bilateral, omentectomia infracólica, biópsias peritoneais/linfonodais e citorredução visando doença residual zero (R0). A punção aspirativa de cisto anexial suspeito é formalmente CONTRAINDICADA em tumores potencialmente ressecáveis pelo alto risco de rotura capsular, extravasamento de líquido maligno e disseminação peritoneal (transformando estádio IA em IC1). A punção ou biópsia percutânea é permitida apenas em casos selecionados de doença sabidamente irressecável/avançada para confirmação histopatológica antes do início de quimioterapia neoadjuvante.",
    analogia5Anos: "Quando uma senhora tem um cisto cheio de divisórias duras dentro do ovário, líquido na barriga (ascite) e o exame de sangue mostra uma proteína muito alta (CA-125), nós nunca furamos esse cisto por fora para ele não vazar! O cirurgião abre com muito cuidado no hospital para retirar tudo com perfeição!"
  },
  {
    id: 9,
    title: "Caso 9: Teratoma Cístico Maduro e Risco de Torção",
    enunciado: "Mulher de 22 anos é admitida no pronto-socorro com dor súbita e intensa em fossa ilíaca direita há 4 horas, acompanhada de náuseas e vômitos. Nega febre ou corrimento vaginal. Teste de gravidez na urina negativo. Ao exame físico: descompressão dolorosa positiva em fossa ilíaca direita, sem sinais de irritação peritoneal generalizada. A ultrassonografia transvaginal com Doppler evidencia massa ovariana direita de 7 cm com áreas hiperecogênicas com atenuação posterior (gordura e calcificações) e ausência de fluxo arterial e venoso ao Doppler colorido. Qual é a etiologia do tumor e a complicação aguda associada?",
    options: [
      { id: 'A', text: "Cistoadenoma mucinoso; rotura espontânea com pseudomixoma peritoneal" },
      { id: 'B', text: "Cisto de corpo lúteo hemorrágico; hemoperitônio maciço com choque" },
      { id: 'C', text: "Teratoma cístico maduro (cisto dermoide); torção anexial aguda", correct: true },
      { id: 'D', text: "Abscesso tubo-ovariano; sepse pélvica bacteriana" },
      { id: 'E', text: "Fibroma ovariano; síndrome de Meigs aguda" }
    ],
    explicacaoIvy: "O teratoma cístico maduro (dermoide) é o tumor ovariano benigno mais comum em mulheres jovens abaixo de 30 anos. Contém tecidos das três camadas germinativas (ectoderma, mesoderma, endoderma), com dentes, ossos, pelos e sebo. Por ser um tumor móvel, com densidade heterogênea e centro de gravidade excêntrico, apresenta a maior taxa de Torção Ovariana/Anexial (~15%). A torção interrompe o retorno venoso e o fluxo arterial ovariano, provocando isquemia e dor aguda lancinante. Trata-se de uma emergência cirúrgica (laparoscopia com destorção e cistectomia).",
    analogia5Anos: "Um cisto dermoide é um cisto misterioso que tem cabelinho, gordura e até dentinhos dentro! Como ele é pesado e tem uma parte gordinha, ele pode dar uma pirueta e dar um nó no ovário (torção), cortando o sangue e dando uma dor de barriga horrível que precisa de cirurgia rápida!"
  },
  {
    id: 10,
    title: "Caso 10: Rastreamento em Paciente com Mutação BRCA1",
    enunciado: "Mulher de 29 anos, assintomática, comparece para consulta de genética e oncologia. Sua mãe faleceu de câncer de mama aos 36 anos e sua tia materna teve câncer de ovário aos 42 anos. O sequenciamento genético da paciente identificou uma mutação patogênica em heterozigose no gene BRCA1. O exame físico das mamas é estritamente normal. Qual é a estratégia de rastreamento e redução de risco recomendada para esta paciente?",
    options: [
      { id: 'A', text: "Mamografia anual iniciando apenas aos 40 anos e ultrassonografia transvaginal semestral" },
      { id: 'B', text: "Ressonância magnética das mamas anual a partir dos 25 anos; salpingo-ooforectomia redutora de risco entre 35 e 40 anos", correct: true },
      { id: 'C', text: "Mastectomia radical bilateral obrigatória imediata sem opção de vigilância clínica" },
      { id: 'D', text: "Dosagem semestral de CA-125 associada a mamografia bienal" },
      { id: 'E', text: "Prescrição de raloxifeno a partir dos 30 anos sem necessidade de exames de imagem adicionais" }
    ],
    explicacaoIvy: "Portadoras de mutação no gene BRCA1 possuem risco cumulativo de câncer de mama de até 70% e de câncer de ovário de 40 a 44%. O rastreamento de mama inicia-se precocemente aos 25 anos com Ressonância Magnética anual (adicionando-se mamografia anual a partir dos 30 anos). Para o câncer de ovário, não existe método eficaz de rastreamento (CA-125 e USG têm baixa sensibilidade em lesões iniciais); portanto, a conduta de maior impacto em sobrevida é a Salpingo-Ooforectomia Bilateral Redutora de Risco entre 35 e 40 anos (após prole concluída).",
    analogia5Anos: "Essa jovem tem um livrinho de instruções na célula (gene BRCA1) que veio com uma falha de fábrica. Para proteger as mamas dela, nós tiramos fotos superprecisas com ressonância todo ano a partir dos 25 anos. E quando ela já tiver seus bebezinhos, retiramos os ovários por cirurgia para que o câncer nunca apareça!"
  },
  {
    id: 11,
    title: "Caso 11: Lesão Cervical Visível Macroscopicamente ao Exame Especular",
    enunciado: "Mulher de 49 anos, tabagista, relata queixa de sinusorragia (sangramento vaginal após relações sexuais) e corrimento fétido há 3 meses. Ela traz um laudo de citologia oncótica (Papanicolau) realizado há 2 meses que veio laudado como: 'Negativo para lesão intraepitelial ou malignidade (NILM) com atipias reativas'. Ao realizar o exame especular, o médico visualiza lesão vegetante, ulcerada, friável e sangrante ao toque, medindo 3,5 cm, ocupando o lábio anterior do colo uterino. Qual é a conduta correta imediata?",
    options: [
      { id: 'A', text: "Tranquilizar a paciente com base no laudo citológico recente e tratar vaginite inespecífica" },
      { id: 'B', text: "Repetir a citologia oncótica cervical em 6 meses" },
      { id: 'C', text: "Realizar biópsia direta da lesão visível com pinça de Gaylor no próprio consultório", correct: true },
      { id: 'D', text: "Solicitar histeroscopia diagnóstica ambulatorial" },
      { id: 'E', text: "Prescrever estrogênio tópico para atrofia e reavaliar em 60 dias" }
    ],
    explicacaoIvy: "Regra de ouro indiscutível da oncologia ginecológica: Qualquer lesão visível macroscopicamente suspeita no colo uterino DEVE SER BIOPSIADA DIRETAMENTE, independentemente de resultados citológicos anteriores! O exame citopatológico (Papanicolau) tem taxa de falso-negativo de até 30 a 50%, especialmente em carcinomas avançados com sangramento ativo e necrose tecidual superficial que impedem a coleta de células escamosas viáveis. Nunca atrase o diagnóstico de um câncer visível confiando em um laudo citológico negativo!",
    analogia5Anos: "Não importa se um papelzinho antigo disse que estava tudo bem: se o médico abrir a portinha com o espéculo e vir com os próprios olhos uma couve-flor feia e sangrando, ele tem que pegar uma pinça e beliscar um pedacinho na hora para testar no microscópio!"
  },
  {
    id: 12,
    title: "Caso 12: Histeroscopia com Glicina a 1,5% e Hiponatremia Aguda",
    enunciado: "Mulher de 46 anos é submetida a histeroscopia cirúrgica com ressectoscópio monopolar para miomectomia de mioma submucoso FIGO 1 de 4,5 cm. O meio de distensão utilizado é glicina a 1,5%. A cirurgia é trabalhosa e dura 55 minutos. O sistema de controle de fluidos acusa um déficit de absorção de 1.450 mL. Pouco antes do término, a paciente (sob sedação) apresenta agitação psicomotora, náuseas intensas, cefaleia e evolui subitamente com crise convulsiva tônico-clônica generalizada. O ionograma de urgência revela sódio sérico = 111 mEq/L. Qual é o diagnóstico e o tratamento de emergência indicado?",
    options: [
      { id: 'A', text: "Sobrecarga volêmica hipertônica; administrar furosemida e bicarbonato de sódio" },
      { id: 'B', text: "Intoxicação por anestésico local; administrar emulsão lipídica a 20%" },
      { id: 'C', text: "Hiponatremia hiposmolar aguda com edema cerebral por absorção de glicina; administrar Salina Hipertônica a 3%", correct: true },
      { id: 'D', text: "Acidente vascular cerebral isquêmico agudo; realizar trombólise com alteplase" },
      { id: 'E', text: "Crise de hipoglicemia reativa; administrar glicose a 50% intravenosa" }
    ],
    explicacaoIvy: "A histeroscopia com instrumentos monopolares exige meios de distensão não eletrolíticos (como glicina a 1,5% ou sorbitol/manitol). A absorção intravascular rápida de grande volume desse líquido hipotônico sem sódio dilui o sangue e reduz a osmolalidade plasmática, gerando passagem de água para o tecido cerebral (edema cerebral agudo, hipertensão intracraniana e convulsões). Em pacientes com hiponatremia sintomática grave aguda (Na < 120 mEq/L com convulsão), a conduta imediata é a infusão de Solução Salina Hipertônica a 3% com monitorização em UTI para elevar o sódio de forma controlada.\n\n⚠️ LIMITES E METAS DE CORREÇÃO (PREVENÇÃO DE DESMIELINIZAÇÃO OSMÓTICA / MIELINÓLISE PONTINA):\n• Meta nas primeiras 6 horas: Elevar o Na+ sérico em 4 a 6 mEq/L (máximo absoluto de 8 mEq/L em 6h), o que já reverte o edema cerebral e cessa as convulsões.\n• Limite em 24 horas: Nunca exceder 10 a 12 mEq/L de elevação em 24h (e ≤ 18 mEq/L em 48h).\n• Fórmula de infusão: Volume de NaCl a 3% (mL) = [Na desejado - Na atual] × Peso (kg) × 0,6.\n• Monitorização: Dosagem seriada de eletrólitos a cada 1-2 horas nas primeiras 6h, depois a cada 4h.\n• Se elevação rápida involuntária (> 1 mEq/L/h): Interromper a salina hipertônica, infundir SG 5% (D5W) e administrar Desmopressina (DDAVP) 2 a 4 mcg EV para 'frear' a subida osmótica excessiva.",
    analogia5Anos: "O médico usou uma água especial sem salzinho (glicina) para ligar o aparelho elétrico dentro do útero. O corpo puxou tanta água sem salzinho para o sangue que o cérebro inchou e deu convulsão. O remédio salvador é colocar sorinho bem salgadinho a 3% na veia imediatamente para desinchar o cérebro!"
  },
  {
    id: 13,
    title: "Caso 13: Líquen Escleroso Vulvar e Risco de Malignidade",
    enunciado: "Mulher de 67 anos relata prurido vulvar intenso e crônico há 2 anos, pior à noite, que prejudica o sono e causa dispareunia. Ao exame ginecológico: pele da vulva atrófica, de coloração branco-marfim com aspecto de 'papel de cigarro', envolvendo grandes e pequenos lábios e região perianal em formato de 'figura em 8'. Observa-se reabsorção parcial dos pequenos lábios e estenose do introito. A mucosa vaginal interna é normal. Qual é o tratamento de primeira linha e o risco oncológico associado se não tratada?",
    options: [
      { id: 'A', text: "Creme de estrogênio conjugado tópico; risco de adenocarcinoma de endométrio" },
      { id: 'B', text: "Pomada de propionato de clobetasol a 0,05% em esquema regressivo; risco de Carcinoma de Células Escamosas (CCE) de vulva", correct: true },
      { id: 'C', text: "Nistatina em creme com hidrocortisona; risco de melanoma vulvar" },
      { id: 'D', text: "Imiquimode creme a 5%; risco de sarcoma de partes moles" },
      { id: 'E', text: "Vulvectomia profilática total imediata; risco nulo de recidiva" }
    ],
    explicacaoIvy: "O líquen escleroso vulvar é uma dermatose inflamatória crônica autoimune. O tratamento padrão-ouro de primeira linha é o corticoide tópico de ultra-alta potência (propionato de clobetasol a 0,05% em pomada). O líquen escleroso confere um risco aumentado de 2 a 5% de desenvolvimento de Carcinoma de Células Escamosas (CCE) de vulva através da via da neoplasia intraepitelial vulvar diferenciada (dVIN, associada a mutações de TP53 e independente de HPV). O tratamento contínuo com corticoide reduz o prurido, melhora a anatomia e diminui a incidência de transformação maligna.",
    analogia5Anos: "O líquen escleroso deixa a pelezinha de fora branca e fina como papelzinho amassado e dá uma coceira sem fim. A melhor pomadinha do mundo é o clobetasol (um corticoide bem forte). Se a paciente não tratar e ficar coçando e machucando por muitos anos, aquela pelezinha sofrida pode virar um câncer de vulva!"
  },
  {
    id: 14,
    title: "Caso 14: Lesão Vesical no Intraoperatório e Reparo",
    enunciado: "Durante a realização de uma histerectomia total por videolaparoscopia em paciente com duas cesáreas prévias, durante a dissecção difícil da plica vesicouterina, o cirurgião observa subitamente acúmulo de líquido claro na pelve e visualiza gás na bolsa coletora da sonda vesical de demora. Qual é a conduta imediata para confirmação diagnóstica e reparo cirúrgico?",
    options: [
      { id: 'A', text: "Instilação de solução salina estéril com azul de metileno pela sonda de Foley; sutura da lesão em 2 planos com fio absorvível e manutenção da sonda por 7 a 14 dias", correct: true },
      { id: 'B', text: "Conversão imediata para laparotomia e nefrostomia bilateral de urgência" },
      { id: 'C', text: "Aplicação isolada de cola de fibrina sem sutura e retirada da sonda em 24 horas" },
      { id: 'D', text: "Colocação de dreno de sucção na cúpula vaginal e alta no dia seguinte" },
      { id: 'E', text: "Cauterização ampla das bordas da bexiga com eletrocautério monopolar" }
    ],
    explicacaoIvy: "A lesão de bexiga (especialmente na cúpula durante a dissecção da plica vesicouterina) é a complicação urológica mais frequente na cirurgia pélvica ginecológica. O teste de azul de metileno ou soro estéril infundido pela sonda de Foley confirma prontamente o extravasamento e demarca a lesão. Lesões na cúpula vesical longe dos meatos ureterais podem ser reparadas por via laparoscópica em duas camadas (camada mucosa/muscular e camada seromuscular) com fio absorvível fino (ex: Vicryl 3-0). A sonda vesical de Foley deve ser mantida por 7 a 14 dias para permitir cicatrização sem tensão hidrostática.",
    analogia5Anos: "A bexiga do xixi fica grudadinha na frente do útero. Se durante a cirurgia o instrumento fez um furinho na bexiga, o médico joga uma aguinha azul pela sondinha para ver onde está vazando, dá pontinhos com fio absorvível em duas camadas e deixa a sondinha de xixi por uma semana para a bexiga sarar sem esticar!"
  },
  {
    id: 15,
    title: "Caso 15: Deiscência de Cúpula Vaginal com Evisceração Intestinal",
    enunciado: "Mulher de 38 anos, submetida a histerectomia total laparoscópica há 5 semanas, comparece à emergência em choque emocional e dor pélvica aguda intensa logo após ter a primeira relação sexual pós-operatória. Ao exame ginecológico em posição ginecológica, visualizam-se várias alças de intestino delgado viáveis exteriorizando-se através do introito vaginal. Qual é a conduta inicial emergencial prioritária antes da transferência imediata ao centro cirúrgico?",
    options: [
      { id: 'A', text: "Empurrar vigorosamente as alças intestinais secas para dentro da vagina com os dedos no leito da emergência" },
      { id: 'B', text: "Cobrir as alças intestinais com compressas estéreis umedecidas em soro fisiológico morno, iniciar hidratação venosa e antibioticoterapia de amplo espectro", correct: true },
      { id: 'C', text: "Tracionar as alças para inspecionar o mesentério no consultório" },
      { id: 'D', text: "Prescrever analgésico oral e programar cirurgia eletiva após 12 horas de jejum" },
      { id: 'E', text: "Realizar tamponamento vaginal compressivo com gazes secas e espéculo de metal rígido" }
    ],
    explicacaoIvy: "A deiscência de cúpula vaginal com evisceração intestinal é uma emergência cirúrgica que ocorre mais comumente após histerectomia laparoscópica após retorno precoce à atividade sexual. O manejo imediato envolve estabilização hemodinâmica, hidratação das alças expostas com compressas estéreis embebidas em solução salina morna para prevenir necrose/desidratação e hipotermia, antibioticoterapia intravenosa cobrindo flora entérica/vaginal e laparoscopia/laparotomia de urgência para avaliação da viabilidade intestinal e ressutura da cúpula vaginal.",
    analogia5Anos: "Se a costurinha do fundo da vagina arrebentou e o intestino saiu para fora, NUNCA puxe nem empurre a seco! Cubra imediatamente com paninho estéril molhado em água morninha para o intestino não secar nem passar frio, tome sorinho na veia e corra para o centro cirúrgico para o cirurgião consertar!"
  },
  {
    id: 16,
    title: "Caso 16: Hemorragia Pós-Parto por Atonia Uterina — Protocolo dos 4 Ts e Ensaio WOMAN",
    enunciado: "Puérpera de 32 anos, G2P1, evolui com parto vaginal eutócico há 25 minutos. Apresenta sangramento vaginal volumoso contínuo com perda hemática estimada em 1.300 mL. Ao exame físico: útero flácido, com fundo acima da cicatriz umbilical, não contraindo após massagem uterina inicial. Sinais vitais: PA 85/50 mmHg, FC 124 bpm, tempo de enchimento capilar de 4 segundos. Acesso venoso calibroso duplo já obtido e sonda vesical de demora instalada. Qual é a conduta farmacológica sequencial imediata recomendada pelas diretrizes internacionais (FIGO / OMS / FEBRASGO) e ensaio clínico WOMAN?",
    options: [
      { id: 'A', text: "Administrar ergotamina isolada e aguardar 30 minutos antes de infundir cristaloides" },
      { id: 'B', text: "Massagem uterina bimanual contínua (Hamilton) + Ocitocina em infusão/bolo + Misoprostol 800 mcg sublingual/retal + Ácido Tranexâmico 1g EV nos primeiros 180 min; se refratário, Balão Intrauterino (Bakri) e laparotomia com suturas hemostáticas (B-Lynch) antes de histerectomia", correct: true },
      { id: 'C', text: "Indicar histerectomia total abdominal imediata sem tentar manobras farmacológicas ou mecânicas conservadoras" },
      { id: 'D', text: "Administrar apenas soro fisiológico aquecido e prescrever sulfato de magnésio intravenoso" },
      { id: 'E', text: "Realizar curetagem uterina às cegas sem suporte hemodinâmico prévio" }
    ],
    explicacaoIvy: "A Hemorragia Pós-Parto (HPP) é a principal causa de mortalidade materna evitável no mundo. O mnemônico dos 4 Ts orienta a etiologia: 1) Tono (atonia uterina, 70-80% dos casos); 2) Trauma (lacerações de trajeto/colo/vagina); 3) Tecido (restos placentários retidos); 4) Trombina (coagulopatias).\n\nPROTOCOLO SEQUENCIAL DE CHOQUE HEMORRÁGICO:\n1. TÔNUS: Massagem bimanual (manobra de Hamilton) + Ocitocina (primeira linha: 5-10 UI EV lento ou 20-40 UI em infusão) + Metilergometrina 0,2 mg IM (contraindicada se hipertensão/pré-eclâmpsia) + Misoprostol 800 mcg sublingual/retal + Carbetocina (se disponível).\n2. ÁCIDO TRANEXÂMICO (Ensaio Clínico WOMAN): 1g EV em 10 minutos administrado impreterivelmente nas primeiras 3 horas pós-parto (reduz a mortalidade por sangramento em mais de 30%; repetir 1g após 30 min se persistência do sangramento).\n3. REANIMAÇÃO HEMOSTÁTICA: Protocolo de transfusão maciça (1:1:1 de concentrado de hemácias, plasma fresco congelado e plaquetas) e reposição de crioprecipitado se fibrinogênio < 200 mg/dL.\n4. MEDIDAS CONSERVADORAS INTERVENCIONISTAS: Balão de tamponamento intrauterino (Bakri com 300 a 500 mL de soro morno), suturas hemostáticas uterinas compressivas (B-Lynch, Hayman), ligadura bilateral das artérias uterinas/hipogástricas e embolização angiográfica.\n5. HISTERECTOMIA DE CONTROLE DE DANOS: Não postergar se choque refratário para salvar a vida da paciente.",
    analogia5Anos: "O útero da mamãe trabalhou muito para o bebê nascer e ficou cansado e molinho (atonia), sem conseguir fechar as torneirinhas de sangue. O médico faz massagem na barriga, dá remédios para o útero apertar (ocitocina, misoprostol), coloca um remédio que ajuda a fazer a casquinha no sangue (ácido tranexâmico) e pode colocar um balãozinho inflado por dentro para estancar tudo e proteger a mamãe!"
  }
];

let casosRespondidos = 0;
let casosAcertos = 0;

function initClinicalCases() {
  const container = document.getElementById('casos-clinicos-container');
  if (!container) return;

  container.innerHTML = CASOS_DATA.map((caso, idx) => `
    <div class="glass-card p-5 sm:p-6 mb-6 transition-all" id="caso-card-${caso.id}">
      <div class="flex items-center justify-between gap-2 mb-3">
        <span class="px-2.5 py-1 rounded-md text-xs font-bold uppercase tracking-wider bg-rose-100 text-rose-800 dark:bg-rose-950 dark:text-rose-300">
          Caso Clínico ${caso.id} de ${CASOS_DATA.length}
        </span>
        <span class="text-xs text-slate-400 font-mono">USMLE Step 2/3</span>
      </div>

      <h3 class="text-base sm:text-lg font-bold text-slate-900 dark:text-white mb-3">${caso.title}</h3>
      <p class="text-sm text-slate-700 dark:text-slate-300 leading-relaxed mb-4">${caso.enunciado}</p>

      <div class="space-y-2 mb-4">
        ${caso.options.map(opt => `
          <button type="button" 
            class="caso-opt-btn w-full text-left p-3 rounded-xl border border-slate-200 dark:border-slate-700 hover:border-rose-400 dark:hover:border-rose-500 bg-white/80 dark:bg-slate-800/80 hover:bg-rose-50/50 dark:hover:bg-rose-950/20 text-xs sm:text-sm text-slate-800 dark:text-slate-200 transition-all flex items-start gap-2.5"
            data-caso="${caso.id}" data-opt="${opt.id}" data-correct="${opt.correct ? 'true' : 'false'}">
            <span class="w-6 h-6 rounded-full bg-slate-100 dark:bg-slate-700 flex items-center justify-center font-bold text-xs flex-shrink-0 text-slate-700 dark:text-slate-300">${opt.id}</span>
            <span class="flex-1">${opt.text}</span>
          </button>
        `).join('')}
      </div>

      <!-- Feedback Oculto Inicialmente -->
      <div id="caso-feedback-${caso.id}" class="hidden space-y-3 pt-4 border-t border-slate-200 dark:border-slate-700">
        <div id="caso-status-${caso.id}" class="p-3 rounded-xl font-bold text-xs sm:text-sm"></div>

        <div class="p-4 rounded-xl bg-slate-50 dark:bg-slate-900/60 border border-slate-200 dark:border-slate-800">
          <h4 class="text-xs font-extrabold uppercase tracking-wider text-rose-600 dark:text-rose-400 mb-1.5 flex items-center gap-1.5">
            <i data-lucide="award" class="w-4 h-4"></i> Raciocínio Fisiopatológico Ivy League / USMLE
          </h4>
          <p class="text-xs sm:text-sm text-slate-700 dark:text-slate-300 leading-relaxed">${caso.explicacaoIvy}</p>
        </div>

        <div class="p-4 rounded-xl bg-amber-50 dark:bg-amber-950/30 border border-amber-200 dark:border-amber-900">
          <h4 class="text-xs font-extrabold uppercase tracking-wider text-amber-700 dark:text-amber-400 mb-1.5 flex items-center gap-1.5">
            🎈 Didática para Criança de 5 Anos
          </h4>
          <p class="text-xs sm:text-sm text-amber-900 dark:text-amber-200 leading-relaxed">${caso.analogia5Anos}</p>
        </div>
      </div>
    </div>
  `).join('');

  if (window.lucide) lucide.createIcons();

  // Listener para Opções
  document.querySelectorAll('.caso-opt-btn').forEach(btn => {
    btn.addEventListener('click', function() {
      const casoId = this.dataset.caso;
      const card = document.getElementById(`caso-card-${casoId}`);
      if (card.dataset.answered === 'true') return; // Bloqueia repetição

      card.dataset.answered = 'true';
      const isCorrect = this.dataset.correct === 'true';

      casosRespondidos++;
      if (isCorrect) casosAcertos++;
      updateScoreboard();

      // Desabilita botões deste caso e destaca o correto
      const buttons = card.querySelectorAll('.caso-opt-btn');
      buttons.forEach(b => {
        b.disabled = true;
        b.classList.add('cursor-default');
        if (b.dataset.correct === 'true') {
          b.classList.remove('border-slate-200', 'dark:border-slate-700');
          b.classList.add('border-emerald-500', 'bg-emerald-50', 'dark:bg-emerald-950/40', 'text-emerald-900', 'dark:text-emerald-200');
        } else if (b === this && !isCorrect) {
          b.classList.remove('border-slate-200', 'dark:border-slate-700');
          b.classList.add('border-rose-500', 'bg-rose-50', 'dark:bg-rose-950/40', 'text-rose-900', 'dark:text-rose-200');
        }
      });

      // Exibe Feedback
      const feedback = document.getElementById(`caso-feedback-${casoId}`);
      const statusBox = document.getElementById(`caso-status-${casoId}`);
      feedback.classList.remove('hidden');

      if (isCorrect) {
        statusBox.className = "p-3 rounded-xl font-bold text-xs sm:text-sm bg-emerald-100 dark:bg-emerald-950 text-emerald-800 dark:text-emerald-300 border border-emerald-300 dark:border-emerald-800";
        statusBox.innerHTML = "✅ Resposta Correta! Excelente raciocínio clínico.";
      } else {
        statusBox.className = "p-3 rounded-xl font-bold text-xs sm:text-sm bg-rose-100 dark:bg-rose-950 text-rose-800 dark:text-rose-300 border border-rose-300 dark:border-rose-800";
        statusBox.innerHTML = "❌ Resposta Incorreta. Revise os detalhes fisiopatológicos abaixo:";
      }

      if (window.lucide) lucide.createIcons();
    });
  });
}

function updateScoreboard() {
  const elRespondidos = document.getElementById('score-respondidos');
  const elAcertos = document.getElementById('score-acertos');
  const elPct = document.getElementById('score-pct');

  if (elRespondidos) elRespondidos.innerText = casosRespondidos;
  if (elAcertos) elAcertos.innerText = casosAcertos;
  if (elPct) {
    const pct = casosRespondidos > 0 ? Math.round((casosAcertos / casosRespondidos) * 100) : 0;
    elPct.innerText = `${pct}%`;
  }
}

/* ==========================================================================
   6. FLASHCARDS INTERATIVOS (FLIP 3D)
   ========================================================================== */
const FLASHCARDS_DATA = [
  { q: "Qual o mecanismo das oncoproteínas E6 e E7 do HPV?", a: "E6 liga-se à E6AP e degrada a proteína p53 no proteassoma (perda da apoptose e ativação de hTERT). E7 liga-se à pRb e libera o fator E2F (induzindo fase S descontrolada e superexpressão de p16)." },
  { q: "Qual a novidade das Diretrizes USPSTF 2024 para rastreamento de mama?", a: "Mamografia BIENAL para todas as mulheres com risco habitual dos 40 aos 74 anos (antes iniciava aos 50 anos). No SUS ainda vigora bem bienal dos 50 aos 69 anos." },
  { q: "O que provou o ensaio LACC em câncer de colo uterino?", a: "Que a cirurgia minimamente invasiva (laparoscópica/robótica) teve PIOR sobrevida livre de progressão e maior mortalidade do que a cirurgia aberta radical em tumores ≥ IB1." },
  { q: "Quais os 4 subtipos moleculares do câncer de endométrio (TCGA / FIGO 2023)?", a: "1. POLE ultramutado (excelente prognóstico)\n2. MMRd / MSI-H (alta sensibilidade à imunoterapia)\n3. NSMP (perfil intermediário, hormônio-dependente)\n4. p53 anômalo (pior prognóstico / alto risco)." },
  { q: "O que estabeleceu o ensaio ACOSOG Z0011 em câncer de mama?", a: "Que em cirurgia conservadora com RT total e 1 a 2 linfonodos sentinela positivos (sem invasão extracapsular macroscópica), o esvaziamento axilar completo pode ser DISPENSADO." },
  { q: "Qual a relação anatômica do ureter com a artéria uterina?", a: "'Water under the bridge' (A água passa por baixo da ponte): o ureter cruza por BAIXO da artéria uterina a cerca de 1,5 a 2 cm lateralmente ao colo uterino." },
  { q: "Por que se preconiza Salpingectomia Oportunista Bilateral em histerectomias benignas?", a: "Porque o Carcinoma Seroso de Alto Grau de ovário tem origem na fímbria tubária (lesão precursora STIC). A salpingectomia reduz drasticamente o risco de câncer de ovário." },
  { q: "Qual a conduta emergencial imediata na evisceração de cúpula vaginal?", a: "Cobrir as alças intestinais com compressas estéreis umedecidas em SORO FISIOLÓGICO MORNO, hidratação venosa, antibióticos de amplo espectro e retorno imediato ao Centro Cirúrgico!" }
];

let currentCardIdx = 0;

function initFlashcards() {
  const cardContainer = document.getElementById('flashcard-container');
  const btnPrev = document.getElementById('card-prev');
  const btnNext = document.getElementById('card-next');
  const cardCounter = document.getElementById('card-counter');

  if (!cardContainer) return;

  const renderCard = () => {
    const card = FLASHCARDS_DATA[currentCardIdx];
    cardContainer.classList.remove('flipped');
    cardContainer.innerHTML = `
      <div class="flashcard-inner relative w-full min-h-[180px] sm:min-h-[220px] rounded-2xl cursor-pointer p-6 flex flex-col justify-between shadow-md">
        <div class="flashcard-front absolute inset-0 rounded-2xl bg-gradient-to-br from-rose-500 via-pink-600 to-indigo-600 text-white p-6 flex flex-col justify-between">
          <div class="flex items-center justify-between text-xs font-bold uppercase tracking-wider text-rose-100">
            <span>Pergunta High-Yield</span>
            <span class="flex items-center gap-1"><i data-lucide="rotate-cw" class="w-3.5 h-3.5"></i> Toque para virar</span>
          </div>
          <p class="text-base sm:text-xl font-bold my-auto text-center">${card.q}</p>
          <div class="text-[11px] text-center text-rose-200">Clique no card para revelar a resposta oficial</div>
        </div>

        <div class="flashcard-back absolute inset-0 rounded-2xl bg-slate-900 border border-slate-700 text-white p-6 flex flex-col justify-between">
          <div class="flex items-center justify-between text-xs font-bold uppercase tracking-wider text-emerald-400">
            <span>Resposta Padrão USMLE</span>
            <span class="flex items-center gap-1"><i data-lucide="check" class="w-3.5 h-3.5"></i> Revisado</span>
          </div>
          <p class="text-xs sm:text-sm font-medium my-auto text-slate-200 leading-relaxed whitespace-pre-line text-left">${card.a}</p>
          <div class="text-[11px] text-center text-slate-400">Toque para desvirar</div>
        </div>
      </div>
    `;

    if (cardCounter) cardCounter.innerText = `${currentCardIdx + 1} de ${FLASHCARDS_DATA.length}`;
    if (window.lucide) lucide.createIcons();

    cardContainer.onclick = () => cardContainer.classList.toggle('flipped');
  };

  if (btnPrev) {
    btnPrev.addEventListener('click', () => {
      currentCardIdx = (currentCardIdx - 1 + FLASHCARDS_DATA.length) % FLASHCARDS_DATA.length;
      renderCard();
    });
  }

  if (btnNext) {
    btnNext.addEventListener('click', () => {
      currentCardIdx = (currentCardIdx + 1) % FLASHCARDS_DATA.length;
      renderCard();
    });
  }

  renderCard();
}

/* ==========================================================================
   7. MODAL DE VISUALIZAÇÃO DE IMAGENS EM ALTA RESOLUÇÃO
   ========================================================================== */
function initImageViewer() {
  const modal = document.getElementById('image-modal');
  const modalImg = document.getElementById('modal-img');
  const modalCaption = document.getElementById('modal-caption');
  const modalClose = document.getElementById('modal-close');

  if (!modal || !modalImg) return;

  document.querySelectorAll('.img-zoom-hover').forEach(img => {
    img.addEventListener('click', function() {
      modalImg.src = this.src;
      modalCaption.innerText = this.getAttribute('alt') || 'Imagem de Alta Definição';
      modal.classList.remove('hidden');
    });
  });

  const closeModal = () => modal.classList.add('hidden');

  if (modalClose) modalClose.addEventListener('click', closeModal);
  modal.addEventListener('click', (e) => {
    if (e.target === modal || e.target.id === 'modal-backdrop') closeModal();
  });

  window.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && !modal.classList.contains('hidden')) closeModal();
  });
}
