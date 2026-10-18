/**
 * app.js - Lógica Interativa do Portal de Ginecologia Geral (Parte 5)
 * Baseado no Guia Obstetrícia e Ginecologia Parte 5 (USMLE Step 2 CK / FEBRASGO / SUS / ACOG / FIGO / ESHRE)
 */

document.addEventListener('DOMContentLoaded', () => {
  initTheme();
  initFontSize();
  initHeaderHeightSync();
  initFabBackToTop();
  initReadingProgressBar();
  initMobileNav();
  initSearch();
  initPalmCoeinClassifier();
  initEndometrialBiopsyCalculator();
  initFigoMyomaMapper();
  initSopRotterdamCalculator();
  initEndometriosisESHREGuide();
  initAdnexalMassORADSCalculator();
  initAmenorrheaDecisionTree();
  initMenopauseHTEvaluator();
  initSemenAnalysisCalculator();
  initFlashcards();
  initQuiz();
  initLightbox();
});

/* ==========================================================================
   0. SINCRONIZAÇÃO DINÂMICA DE ALTURA DO CABEÇALHO FIXO (FLEX-WRAP)
   ========================================================================== */
function syncHeaderHeight() {
  const header = document.querySelector('header');
  if (!header) return;
  const height = header.offsetHeight;
  if (height > 0) {
    document.documentElement.style.setProperty('--header-height', `${height + 16}px`);
  }
}

function initHeaderHeightSync() {
  syncHeaderHeight();
  window.addEventListener('resize', syncHeaderHeight, { passive: true });
  window.addEventListener('load', syncHeaderHeight, { passive: true });
  const header = document.querySelector('header');
  if (header && typeof ResizeObserver !== 'undefined') {
    const ro = new ResizeObserver(() => {
      syncHeaderHeight();
    });
    ro.observe(header);
  }
}

/* ==========================================================================
   1. GERENCIAMENTO DE TEMA (DARK / LIGHT)
   ========================================================================== */
function initTheme() {
  const themeToggles = document.querySelectorAll('.theme-toggle-btn, #theme-toggle');
  const html = document.documentElement;

  function updateThemeUI() {
    const isDark = html.classList.contains('dark');
    themeToggles.forEach(btn => {
      btn.setAttribute('aria-label', isDark ? 'Ativar modo claro' : 'Ativar modo escuro');
      btn.setAttribute('title', isDark ? 'Ativar modo claro' : 'Ativar modo escuro');
    });
  }

  function toggleTheme() {
    const isDark = html.classList.contains('dark');
    if (isDark) {
      html.classList.remove('dark');
      localStorage.setItem('theme', 'light');
    } else {
      html.classList.add('dark');
      localStorage.setItem('theme', 'dark');
    }
    updateThemeUI();
  }

  themeToggles.forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      toggleTheme();
    });
  });

  updateThemeUI();
}

/* ==========================================================================
   1.2 CONTROLE DINÂMICO DE TAMANHO DE FONTE (A / A+ / A++)
   ========================================================================== */
function initFontSize() {
  const html = document.documentElement;
  const savedSize = localStorage.getItem('fontSizePreference') || 'normal';
  setFontSize(savedSize);

  const fontButtons = document.querySelectorAll('[data-font-size-set]');
  fontButtons.forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      const targetSize = btn.getAttribute('data-font-size-set');
      setFontSize(targetSize);
      localStorage.setItem('fontSizePreference', targetSize);
    });
  });

  function setFontSize(size) {
    if (['normal', 'large', 'xlarge'].includes(size)) {
      html.setAttribute('data-font-size', size);
    } else {
      html.setAttribute('data-font-size', 'normal');
    }
    document.querySelectorAll('[data-font-size-set]').forEach(btn => {
      const btnSize = btn.getAttribute('data-font-size-set');
      if (btnSize === size) {
        btn.classList.add('bg-rose-600', 'text-white', 'shadow-sm', 'active');
        btn.classList.remove('text-slate-600', 'dark:text-slate-400', 'hover:bg-slate-200', 'dark:hover:bg-slate-800');
      } else {
        btn.classList.remove('bg-rose-600', 'text-white', 'shadow-sm', 'active');
        btn.classList.add('text-slate-600', 'dark:text-slate-400');
      }
    });
    requestAnimationFrame(syncHeaderHeight);
  }
}

/* ==========================================================================
   1.3 BOTÃO FLUTUANTE VOLTAR AO TOPO (FAB)
   ========================================================================== */
function initFabBackToTop() {
  const fab = document.getElementById('fab-back-to-top');
  if (!fab) return;

  function toggleFab() {
    if (window.scrollY > 350) {
      fab.classList.remove('fab-hidden');
      fab.classList.add('fab-visible');
    } else {
      fab.classList.remove('fab-visible');
      fab.classList.add('fab-hidden');
    }
  }

  window.addEventListener('scroll', toggleFab, { passive: true });
  fab.addEventListener('click', (e) => {
    e.preventDefault();
    window.scrollTo({
      top: 0,
      behavior: 'smooth'
    });
  });

  toggleFab();
}

/* ==========================================================================
   1.3.1 BARRA DE PROGRESSO DE LEITURA
   ========================================================================== */
function initReadingProgressBar() {
  const bar = document.getElementById('reading-progress');
  if (!bar) return;

  function updateProgress() {
    const totalHeight = document.documentElement.scrollHeight - window.innerHeight;
    if (totalHeight > 0) {
      const progress = (window.scrollY / totalHeight) * 100;
      bar.style.width = Math.min(100, Math.max(0, progress)) + '%';
    }
  }

  window.addEventListener('scroll', updateProgress, { passive: true });
  window.addEventListener('resize', updateProgress, { passive: true });
  updateProgress();
}

/* ==========================================================================
   2. NAVEGAÇÃO SUPERIOR FIXA (ACESSO DIRETO AOS MÓDULOS E FERRAMENTAS)
   ========================================================================== */
function initMobileNav() {
  const anchorLinks = document.querySelectorAll('a[href^="#"]');
  anchorLinks.forEach((link) => {
    link.addEventListener('click', (e) => {
      const href = link.getAttribute('href');
      if (!href) return;

      if (href === '#') {
        e.preventDefault();
        window.scrollTo({ top: 0, behavior: 'smooth' });
        return;
      }

      const targetId = href.slice(1);
      const targetEl = document.getElementById(targetId);
      if (!targetEl) return;

      e.preventDefault();

      // Se houver filtro de busca ativo ocultando o módulo alvo, restaura a visualização
      const searchInput = document.getElementById('global-search');
      const parentModule = targetEl.closest('.module-card');
      if (parentModule && parentModule.style.display === 'none') {
        if (searchInput) searchInput.value = '';
        document.querySelectorAll('.module-card').forEach((m) => {
          m.style.display = '';
        });
        const noResults = document.getElementById('search-no-results');
        if (noResults) noResults.classList.add('hidden');
      }

      const header = document.querySelector('header');
      const headerOffset = header ? header.offsetHeight + 16 : 140;
      const elementTop = targetEl.getBoundingClientRect().top + window.scrollY;
      const offsetPosition = Math.max(0, elementTop - headerOffset);

      window.scrollTo({
        top: offsetPosition,
        behavior: 'smooth'
      });

      if (history.pushState) {
        history.pushState(null, '', href);
      }

      // Destaque sutil temporário na ferramenta/módulo selecionado
      targetEl.classList.add('ring-2', 'ring-rose-500/70');
      setTimeout(() => {
        targetEl.classList.remove('ring-2', 'ring-rose-500/70');
      }, 1400);
    });
  });
}

/* ==========================================================================
   3. BUSCA GLOBAL INTELIGENTE (CTRL + K)
   ========================================================================== */
function initSearch() {
  const searchInput = document.getElementById('global-search');
  if (!searchInput) return;

  function handleSearch(query) {
    const q = query.toLowerCase().trim();
    const modules = document.querySelectorAll('.module-card');

    let matchCount = 0;
    modules.forEach((mod) => {
      const text = mod.textContent.toLowerCase();
      if (!q || text.includes(q)) {
        mod.style.display = '';
        matchCount++;
      } else {
        mod.style.display = 'none';
      }
    });

    const noResults = document.getElementById('search-no-results');
    if (noResults) {
      if (matchCount === 0 && q) {
        noResults.classList.remove('hidden');
      } else {
        noResults.classList.add('hidden');
      }
    }
  }

  searchInput.addEventListener('input', (e) => handleSearch(e.target.value));

  window.addEventListener('keydown', (e) => {
    if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === 'k') {
      e.preventDefault();
      searchInput.focus();
      searchInput.select();
    }
  });
}

/* ==========================================================================
   4. CLASSIFICADOR INTERATIVO PALM-COEIN (FIGO 2018)
   ========================================================================== */
const PALM_COEIN_DATA = {
  P: {
    category: "Estrutural (PALM)",
    title: "Pólipo Endometrial ou Endocervical",
    analogia: "Uma pequena verruga ou projeção benigna vascularizada na parede do endométrio.",
    clinica: "Sangramento intermenstrual (escape/spotting) ou sangramento pós-menopausa. Muitas vezes assintomático.",
    diagnostico: "Ultrassonografia transvaginal, histerossonografia (distensão líquida da cavidade) ou histeroscopia diagnóstica.",
    conduta: "Polipectomia histeroscópica ambulatorial ou em centro cirúrgico. Biópsia e análise histopatológica para descartar atipia/malignidade."
  },
  A: {
    category: "Estrutural (PALM)",
    title: "Adenomiose",
    analogia: "O papel de parede do útero invadiu o tijolo (glândulas e estroma endometriais no miométrio).",
    clinica: "Dismenorreia secundária progressiva + sangramento uterino abundante em multípara de 40 a 50 anos. Útero globoso, aumentado e amolecido ('boggy').",
    diagnostico: "USG transvaginal (critérios MUSA 2022: miométrio assimétrico, cistos miometriais, sombras em persiana/leque) ou RM (zona juncional >= 8 mm ou relação ZJ/miométrio > 40%; clássica >= 12 mm).",
    conduta: "Clínica: DIU de Levonorgestrel 52 mg (1ª linha), dienogeste 2 mg/dia (alta eficácia, porém off-RENAME/não padronizado no SUS; no SUS usa-se medroxiprogesterona ou noretisterona), AINE, ACO contínuo. Definitiva: Histerectomia se prole completa e refratariedade."
  },
  L: {
    category: "Estrutural (PALM)",
    title: "Leiomioma Uterino (Mioma)",
    analogia: "Nós de madeira no músculo uterino dependentes de estrogênio e progesterona.",
    clinica: "Submucosos (FIGO 0-2): sangramento torrencial e infertilidade. Intramurais/Subserosos (FIGO 3-7): volume, sensação de peso e compressão de bexiga/reto.",
    diagnostico: "USG transvaginal com Doppler (nódulo sólido hipoecoico com sombra em leque), histeroscopia para submucosos e RM para mapeamento múltiplo.",
    conduta: "Submucoso sintomático: Miomectomia histeroscópica. Miomas múltiplos/volumosos: Análogos de GnRH pré-op (uso estritamente limitado a no máximo 6 meses sem terapia 'add-back' para prevenir perda de massa óssea), embolização de artérias uterinas (se não desejar gestar) ou histerectomia."
  },
  M: {
    category: "Estrutural (PALM)",
    title: "Malignidade & Hiperplasia Endometrial",
    analogia: "O tapete começou a proliferar desordenadamente por excesso de adubo (estrogênio sem oposição).",
    clinica: "Sangramento pós-menopausa (investigar sempre!) ou SUA em mulher >= 45 anos (ou < 45 anos com obesidade, SOP ou Lynch).",
    diagnostico: "USG transvaginal (espessura endometrial > 4 mm na pós-menopausa sem TH, ou > 8 mm com TH combinada contínua). Atenção: no uso de Tamoxifeno, o corte de 4 mm perde especificidade por reatividade estromal benigna cística, indicando-se histeroscopia com biópsia dirigida. Sempre descartar lesão cervical concomitante.",
    conduta: "Hiperplasia sem atipia: Progestagênio (DIU-LNG preferido). Hiperplasia com atipia (NIE) ou Câncer: Histerectomia total com anexectomia bilateral e estadiamento cirúrgico."
  },
  C: {
    category: "Não Estrutural (COEIN)",
    title: "Coagulopatia",
    analogia: "Falta de 'tampões' químicos de coagulação no sangue para conter o sangramento.",
    clinica: "Menorragia intensa desde a menarca, história familiar, hematomas espontâneos, epistaxe frequente ou hemorragia pós-parto/extração dentária.",
    diagnostico: "Triagem para Doença de von Willebrand (diretriz ISTH/ASH 2021: dosagem simultânea de vWF:Ag e atividade funcional vWF:RCo ou vWF:GPIbM; vWF:CB se discordância), Fator VIII, coagulograma completo e plaquetas.",
    conduta: "Manejo conjunto com Hematologia: Ácido tranexâmico nos dias de fluxo, DIU-LNG, DDAVP (desmopressina) e concentrados de fator vWF/VIII conforme necessidade."
  },
  O: {
    category: "Não Estrutural (COEIN)",
    title: "Ovulatória (Disfunção Ovulatória)",
    analogia: "Prédio sem cimento: o endométrio cresce sob estímulo de estrogênio, mas sem ovulação não há progesterona, desabando de forma irregular.",
    clinica: "Ciclos irregulares com atrasos de 40 a 90 dias seguidos de sangramentos volumosos prolongados. Muito comum em SOP, adolescência, perimenopausa, hipotireoidismo e hiperprolactinemia.",
    diagnostico: "Excluir gestação (beta-hCG), dosar TSH, Prolactina, avaliar critérios de SOP e teste da progesterona.",
    conduta: "Restaurar a oposição progestacional: Anticoncepcional hormonal combinado, progestagênio cíclico/contínuo ou DIU-LNG. Correção de hipotireoidismo e estilo de vida."
  },
  E: {
    category: "Não Estrutural (COEIN)",
    title: "Endometrial (Disfunção Primária)",
    analogia: "Desbalanço local de prostaglandinas vasoativas (relação PGF2alfa/PGE2 reduzida) e lise acelerada de coágulos por hiperfibrinólise endometrial local.",
    clinica: "Ciclos ovulatórios regulares previsíveis, porém com volume excessivo ou sangramento prolongado, sem lesão estrutural ou coagulopatia sistêmica (diagnóstico de exclusão).",
    diagnostico: "Exclusão rigorosa de lesões estruturais por USG e histeroscopia, e confirmação de função ovulatória normal.",
    conduta: "DIU de Levonorgestrel 52 mg (padrão-ouro clínico), Ácido Tranexâmico durante o fluxo menstrual ou AINEs (ácido mefenâmico, naproxeno)."
  },
  I: {
    category: "Não Estrutural (COEIN)",
    title: "Iatrogênica",
    analogia: "Efeito adverso direto de fármacos ou dispositivos introduzidos pelo médico.",
    clinica: "Sangramento de escape ('spotting') nos primeiros meses de DIU ou implante, esquecimento de pílula anticoncepcional, anticoagulantes orais ou uso de tamoxifeno.",
    diagnostico: "Anamnese medicamentosa minuciosa temporalmente correlacionada com o início do sangramento.",
    conduta: "Ajuste de dose ou formulação hormonal, reforço de adesão terapêutica, ajuste de anticoagulação e conduta expectante nos primeiros 3-6 meses de métodos de progesterona."
  },
  N: {
    category: "Não Estrutural (COEIN)",
    title: "Não Classificada",
    analogia: "Causas raras ou anomalias mecânicas adquiridas que não se enquadram nas categorias anteriores.",
    clinica: "Sangramento pós-menstrual persistente escuro (em 'borra de café'), malformações vasculares ou endometrite crônica.",
    diagnostico: "Istmocele (nicho de cicatriz de cesárea prévia visualizado ao USG com líquido acumulado) ou Malformação Arteriovenosa (MAV com fluxo turbulento ao Doppler colorido).",
    conduta: "Istmocele: Correção histeroscópica ou laparoscópica. MAV: Embolização por radiologia intervencionista (nunca curetar às cegas pelo risco de hemorragia fatal!)."
  }
};

function initPalmCoeinClassifier() {
  const buttons = document.querySelectorAll('.palm-btn');
  const detailsBox = document.getElementById('palm-details');
  if (!detailsBox || buttons.length === 0) return;

  function renderCategory(letter) {
    const data = PALM_COEIN_DATA[letter];
    if (!data) return;

    buttons.forEach(b => {
      if (b.dataset.letter === letter) {
        b.classList.add('ring-2', 'ring-rose-500', 'font-black', 'scale-105');
      } else {
        b.classList.remove('ring-2', 'ring-rose-500', 'font-black', 'scale-105');
      }
    });

    detailsBox.innerHTML = `
      <div class="p-5 rounded-2xl border-2 border-rose-200 dark:border-rose-900 bg-white/90 dark:bg-slate-900/90 shadow-lg space-y-4 transition-all">
        <div class="flex items-center justify-between flex-wrap gap-2">
          <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-rose-600 text-white font-extrabold flex items-center justify-center text-lg shadow-sm">${letter}</span>
            <h4 class="text-base sm:text-lg font-black text-slate-900 dark:text-white">${data.title}</h4>
          </div>
          <span class="px-2.5 py-1 text-xs font-bold rounded-full ${letter in {'P':1,'A':1,'L':1,'M':1} ? 'bg-amber-100 text-amber-900 dark:bg-amber-950 dark:text-amber-300' : 'bg-blue-100 text-blue-900 dark:bg-blue-950 dark:text-blue-300'}">${data.category}</span>
        </div>

        <div class="p-3 rounded-xl bg-amber-50 dark:bg-amber-950/30 border border-amber-200 dark:border-amber-800 text-xs sm:text-sm text-amber-900 dark:text-amber-200 flex items-start gap-2">
          <span class="text-base">🎈</span>
          <div><strong>Analogia Didática:</strong> ${data.analogia}</div>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-3 text-xs sm:text-sm">
          <div class="p-3 rounded-xl bg-slate-50 dark:bg-slate-800/60 border border-slate-200 dark:border-slate-700">
            <strong class="text-slate-900 dark:text-white flex items-center gap-1 mb-1">🩺 Manifestação Clínica</strong>
            <p class="text-slate-600 dark:text-slate-300">${data.clinica}</p>
          </div>
          <div class="p-3 rounded-xl bg-slate-50 dark:bg-slate-800/60 border border-slate-200 dark:border-slate-700">
            <strong class="text-slate-900 dark:text-white flex items-center gap-1 mb-1">🔬 Roteiro Diagnóstico</strong>
            <p class="text-slate-600 dark:text-slate-300">${data.diagnostico}</p>
          </div>
          <div class="p-3 rounded-xl bg-slate-50 dark:bg-slate-800/60 border border-slate-200 dark:border-slate-700">
            <strong class="text-slate-900 dark:text-white flex items-center gap-1 mb-1">💊 Conduta e Tratamento</strong>
            <p class="text-slate-600 dark:text-slate-300">${data.conduta}</p>
          </div>
        </div>
      </div>
    `;

    if (window.lucide) lucide.createIcons();
  }

  buttons.forEach(btn => {
    btn.addEventListener('click', () => {
      renderCategory(btn.dataset.letter);
    });
  });

  // Inicializa com a letra 'L' (Leiomioma)
  renderCategory('L');
}

/* ==========================================================================
   5. CALCULADORA DE INDICAÇÃO DE BIÓPSIA ENDOMETRIAL (ACOG / FIGO)
   ========================================================================== */
function initEndometrialBiopsyCalculator() {
  const ageSelect = document.getElementById('bx-age');
  const postMenoCheck = document.getElementById('bx-postmeno');
  const thicknessInput = document.getElementById('bx-thickness');
  const unopposedCheck = document.getElementById('bx-unopposed');
  const lynchCheck = document.getElementById('bx-lynch');
  const tamoxCheck = document.getElementById('bx-tamoxifen');
  const resultBox = document.getElementById('bx-result');

  if (!ageSelect || !resultBox) return;

  function evaluateBiopsy() {
    const age = parseInt(ageSelect.value) || 30;
    const isPostMeno = postMenoCheck ? postMenoCheck.checked : false;
    const thickness = parseFloat(thicknessInput ? thicknessInput.value : 0) || 0;
    const hasUnopposed = unopposedCheck ? unopposedCheck.checked : false;
    const hasLynch = lynchCheck ? lynchCheck.checked : false;
    const usesTamoxifen = tamoxCheck ? tamoxCheck.checked : false;

    let reasons = [];
    let isIndicated = false;
    let urgencyLevel = "low";

    if (isPostMeno) {
      if (thickness > 4) {
        isIndicated = true;
        urgencyLevel = "high";
        reasons.push(`Sangramento pós-menopausa com endométrio > 4 mm (${thickness} mm) — corte de segurança ultrassonográfica ultrapassado.`);
      } else if (thickness <= 4 && thickness > 0) {
        reasons.push(`Endométrio <= 4 mm (${thickness} mm): Causa mais comum é atrofia (60-80%). Observar; biopsiar se o sangramento persistir.`);
      } else {
        isIndicated = true;
        reasons.push("Sangramento pós-menopausa sem medida ultrassonográfica confiável — biópsia indicada.");
      }
      if (usesTamoxifen) {
        isIndicated = true;
        reasons.push("Uso de Tamoxifeno com sangramento: o corte de 4 mm não se aplica devido à reatividade estromal cística. Investigar com histeroscopia e biópsia dirigida.");
      }
    } else {
      if (age >= 45) {
        isIndicated = true;
        urgencyLevel = "moderate";
        reasons.push("Idade >= 45 anos com sangramento uterino anormal (critério formal ACOG para biópsia endometrial ambulatorial).");
      } else {
        if (hasUnopposed) {
          isIndicated = true;
          urgencyLevel = "high";
          reasons.push("Idade < 45 anos com exposição prolongada a estrogênio sem oposição (obesidade IMC >= 30, anovulação crônica/SOP) — indicação formal ACOG/FEBRASGO de alta suspeição.");
        }
        if (hasLynch) {
          isIndicated = true;
          urgencyLevel = "high";
          reasons.push("Síndrome de Lynch (risco cumulativo de câncer de endométrio de 40-60% ao longo da vida — indicação mandatória).");
        }
        if (usesTamoxifen) {
          isIndicated = true;
          urgencyLevel = "high";
          reasons.push("Uso de Tamoxifeno com SUA: risco aumentado de hiperplasia/adenocarcinoma (indicação formal de histeroscopia com biópsia dirigida).");
        }
      }
    }

    if (isIndicated) {
      resultBox.className = "p-4 rounded-xl border-2 bg-rose-50 dark:bg-rose-950/40 border-rose-500 text-rose-900 dark:text-rose-200 space-y-2";
      resultBox.innerHTML = `
        <div class="flex items-center gap-2 font-black text-sm text-rose-700 dark:text-rose-400">
          <i data-lucide="alert-triangle" class="w-5 h-5"></i> BIÓPSIA ENDOMETRIAL FORMALMENTE INDICADA
        </div>
        <div class="text-xs leading-relaxed">
          <strong>Critérios Detectados:</strong>
          <ul class="list-disc list-inside mt-1 font-semibold text-rose-800 dark:text-rose-300">
            ${reasons.map(r => `<li>${r}</li>`).join('')}
          </ul>
          <span class="block mt-2">
            <strong>Método de Escolha:</strong> Biópsia ambulatorial com <strong>cânula de Pipelle</strong> (alta sensibilidade para afecções difusas). Se material insuficiente, estenose cervical, sangramento persistente ou suspeita focal: realizar <strong>histeroscopia cirúrgica com biópsia dirigida</strong>.<br>
            <strong class="text-rose-800 dark:text-rose-300">⚠️ Nota de Segurança:</strong> O exame especular e a citologia oncótica/HPV do colo uterino devem sempre preceder ou acompanhar a investigação endometrial para descartar neoplasia cervical primária.
          </span>
        </div>
      `;
    } else {
      resultBox.className = "p-4 rounded-xl border-2 bg-emerald-50 dark:bg-emerald-950/40 border-emerald-500 text-emerald-900 dark:text-emerald-200 space-y-2";
      resultBox.innerHTML = `
        <div class="flex items-center gap-2 font-black text-sm text-emerald-700 dark:text-emerald-400">
          <i data-lucide="check-circle" class="w-5 h-5"></i> BAIXO RISCO DE MALIGNIDADE — BIÓPSIA INICIAL DISPENSADA
        </div>
        <p class="text-xs leading-relaxed">
          ${reasons.length > 0 ? reasons.join('<br>') : 'Paciente jovem sem fatores de alto risco para hiperplasia ou neoplasia endometrial.'}<br>
          <strong>Conduta:</strong> Tratamento clínico inicial (ACO, DIU-LNG, AINE ou Ácido Tranexâmico). Indicar biópsia apenas se houver falha do tratamento clínico ou sangramento persistente.
        </p>
      `;
    }

    if (window.lucide) lucide.createIcons();
  }

  [ageSelect, thicknessInput].forEach(el => { if (el) el.addEventListener('input', evaluateBiopsy); });
  [postMenoCheck, unopposedCheck, lynchCheck, tamoxCheck].forEach(el => { if (el) el.addEventListener('change', evaluateBiopsy); });

  evaluateBiopsy();
}

/* ==========================================================================
   6. MAPEADOR ANATÔMICO DE MIOMAS (FIGO 0 A 8)
   ========================================================================== */
const MYOMA_FIGO_DATA = {
  0: { local: "Submucoso Pediculado Intracavitário", sintoma: "Sangramento torrencial, anemia grave, infertilidade e abortamento.", conduta: "Miomectomia histeroscópica ambulatorial ou em centro cirúrgico. Alta taxa de preservação uterina." },
  1: { local: "Submucoso com invasão intramural < 50%", sintoma: "Sangramento abundante, menorragia, dismenorreia e falha de implantação.", conduta: "Miomectomia histeroscópica (técnica em um ou dois tempos se > 3 cm)." },
  2: { local: "Submucoso com invasão intramural >= 50%", sintoma: "Sangramento importante e cólicas uterinas.", conduta: "Avaliar preparo pré-operatório com agonista de GnRH por 3 a 6 meses (máximo 6 meses sem terapia add-back) para reduzir volume e vascularização; miomectomia histeroscópica (geralmente em dois tempos) ou laparoscópica." },
  3: { local: "Intramural contatando a cavidade endometrial (100% intramural, sem protrusão intracavitária)", sintoma: "Menorragia e aumento do fluxo sanguíneo menstrual.", conduta: "Tratamento clínico com DIU-LNG, ácido tranexâmico ou miomectomia laparoscópica/laparotômica se desejo gestacional e refratariedade." },
  4: { local: "Intramural puro (sem contato com endométrio nem serosa)", sintoma: "Aumento do volume uterino, sangramento e sensação de peso.", conduta: "Tratamento clínico (ACO, progestagênios, DIU-LNG). Se volumoso: Miomectomia laparoscópica ou embolização de artérias uterinas (se não desejar gestar)." },
  5: { local: "Subseroso com componente intramural >= 50%", sintoma: "Sensação de compressão pélvica, polaciúria ou constipação intestinal.", conduta: "Observação se assintomático. Cirúrgico se compressivo: Miomectomia laparoscópica." },
  6: { local: "Subseroso com componente intramural < 50%", sintoma: "Sintomas compressivos sobre bexiga, reto ou ureteres.", conduta: "Miomectomia laparoscópica preservando a cavidade endometrial." },
  7: { local: "Subseroso Pediculado", sintoma: "Risco agudo de torção do pedículo (dor pélvica súbita e abdome agudo ginecológico).", conduta: "Laparoscopia para ligadura e ressecção do pedículo. Evitar embolização devido ao risco de necrose livre e sepse intra-abdominal." },
  8: { local: "Outros (Cervical, Parasita no ligamento largo)", sintoma: "Dispareunia, obstrução urinária, compressão ureteral com hidronefrose.", conduta: "Ressecção cirúrgica com dissecção cuidadosa do trajeto ureteral." }
};

function initFigoMyomaMapper() {
  const figoSelect = document.getElementById('figo-select');
  const outputBox = document.getElementById('figo-output');
  if (!figoSelect || !outputBox) return;

  function updateMyomaInfo() {
    const val = parseInt(figoSelect.value) || 0;
    const data = MYOMA_FIGO_DATA[val];
    if (!data) return;

    outputBox.innerHTML = `
      <div class="p-4 rounded-xl border border-slate-200 dark:border-slate-700 bg-white dark:bg-slate-800 space-y-3">
        <div class="flex items-center justify-between flex-wrap gap-2">
          <span class="px-2.5 py-1 text-xs font-black rounded-lg bg-rose-600 text-white">FIGO Tipo ${val}</span>
          <span class="text-xs font-bold text-slate-500 dark:text-slate-400">${val <= 2 ? 'Submucoso (Gera Sangramento)' : val <= 4 ? 'Intramural (Volume/Sangramento)' : 'Subseroso/Outro (Gera Compressão)'}</span>
        </div>
        <div>
          <h5 class="text-sm font-extrabold text-slate-900 dark:text-white">${data.local}</h5>
          <p class="text-xs text-slate-600 dark:text-slate-300 mt-1"><strong>Sintomas Típicos:</strong> ${data.sintoma}</p>
        </div>
        <div class="p-3 rounded-lg bg-slate-50 dark:bg-slate-900/60 border border-slate-200 dark:border-slate-800 text-xs">
          <strong class="text-rose-600 dark:text-rose-400">Conduta Recomendada:</strong> ${data.conduta}
        </div>
      </div>
    `;
  }

  figoSelect.addEventListener('change', updateMyomaInfo);
  updateMyomaInfo();
}

/* ==========================================================================
   7. CALCULADORA DE SOP (CRITÉRIOS DE ROTTERDAM 2023)
   ========================================================================== */
function initSopRotterdamCalculator() {
  const anovCheck = document.getElementById('sop-anov');
  const hyperCheck = document.getElementById('sop-hyper');
  const usgCheck = document.getElementById('sop-usg');
  const amhCheck = document.getElementById('sop-amh');
  const amhValueInput = document.getElementById('sop-amh-value');
  const exclCheck = document.getElementById('sop-excl');
  const fertCheck = document.getElementById('sop-fertility');
  const resultBox = document.getElementById('sop-result');

  if (!anovCheck || !hyperCheck || !resultBox) return;

  function evaluateSOP() {
    const hasAnov = anovCheck.checked;
    const hasHyper = hyperCheck.checked;
    const hasUSG = usgCheck ? usgCheck.checked : false;
    const amhVal = amhValueInput ? parseFloat(amhValueInput.value) : 0;
    const hasAMH = amhCheck ? (amhCheck.checked && (amhVal >= 4.9 || isNaN(amhVal) || amhVal === 0)) : false;
    const hasMorphology = hasUSG || hasAMH;

    const isExclChecked = exclCheck ? exclCheck.checked : false;
    const wantsFertility = fertCheck ? fertCheck.checked : false;

    let count = (hasAnov ? 1 : 0) + (hasHyper ? 1 : 0) + (hasMorphology ? 1 : 0);

    if (!isExclChecked) {
      resultBox.className = "p-4 rounded-xl border-2 bg-amber-50 dark:bg-amber-950/40 border-amber-500 text-amber-900 dark:text-amber-200 space-y-2";
      resultBox.innerHTML = `
        <div class="flex items-center gap-2 font-black text-sm text-amber-700 dark:text-amber-400">
          <i data-lucide="alert-circle" class="w-5 h-5"></i> PASSO OBRIGATÓRIO: EXCLUSÃO DE OUTRAS ETIOLOGIAS
        </div>
        <p class="text-xs leading-relaxed">
          SOP é um <strong>diagnóstico de exclusão</strong>! Antes de fechar o diagnóstico, é obrigatório solicitar:<br>
          • <strong>beta-hCG</strong> (descartar gravidez);<br>
          • <strong>TSH</strong> (descartar hipotireoidismo);<br>
          • <strong>Prolactina</strong> (descartar hiperprolactinemia);<br>
          • <strong>17-OH-Progesterona</strong> (descartar Hiperplasia Adrenal Congênita não clássica);<br>
          • Se virilização rápida ou testosterona > 150-200 ng/dL: excluir neoplasia adrenal/ovariana (DHEA-S).
        </p>
      `;
      if (window.lucide) lucide.createIcons();
      return;
    }

    if (count >= 2) {
      let fenotipo = "";
      if (hasAnov && hasHyper && hasMorphology) fenotipo = "Fenótipo A (Clássico Completo: Anovulação + Hiperandrogenismo + Morfologia/AMH)";
      else if (hasAnov && hasHyper && !hasMorphology) fenotipo = "Fenótipo B (Clássico Sem Alteração Ovariana: Anovulação + Hiperandrogenismo)";
      else if (!hasAnov && hasHyper && hasMorphology) fenotipo = "Fenótipo C (Ovulatório: Hiperandrogenismo + Morfologia/AMH)";
      else if (hasAnov && !hasHyper && hasMorphology) fenotipo = "Fenótipo D (Não Androgênico: Anovulação + Morfologia/AMH)";

      let morphDetail = "";
      if (hasAMH && hasUSG) morphDetail = "Critério ovariano confirmado por USG e AMH elevado (>= 4.9 ng/mL).";
      else if (hasAMH) morphDetail = "Critério ovariano confirmado por AMH sérico elevado (Rotterdam 2023 alternativa validada à USG).";
      else if (hasUSG) morphDetail = "Critério ovariano confirmado por padrão ultrassonográfico policístico (>= 20 folículos ou volume >= 10 mL).";

      resultBox.className = "p-4 rounded-xl border-2 bg-emerald-50 dark:bg-emerald-950/40 border-emerald-500 text-emerald-900 dark:text-emerald-200 space-y-2";
      resultBox.innerHTML = `
        <div class="flex items-center gap-2 font-black text-sm text-emerald-700 dark:text-emerald-400">
          <i data-lucide="check-circle" class="w-5 h-5"></i> DIAGNÓSTICO DE SOP CONFIRMADO (CRITÉRIOS DE ROTTERDAM 2023)
        </div>
        <div class="text-xs leading-relaxed">
          <strong>Classificação:</strong> <span class="font-bold underline">${fenotipo}</span>.<br>
          ${morphDetail ? `<span class="text-[11px] text-emerald-800 dark:text-emerald-300 block mb-1">• ${morphDetail}</span>` : ''}
          <div class="mt-2 p-3 bg-emerald-100/70 dark:bg-emerald-900/40 rounded-lg">
            <strong>Plano Terapêutico Guiado pelo Objetivo:</strong><br>
            • <em>Pilar Fundamental (todas):</em> Mudança do estilo de vida (perda de 5-10% do peso restaura a ovulação em até 50% dos casos). Rastrear diabetes (TOTG 75g) e dislipidemia.<br>
            ${wantsFertility ? `
              • <strong>Desejo de Engravidar:</strong> <strong>Letrozol (2,5 a 7,5 mg/dia por 5 dias)</strong> é a 1ª linha recomendada internacionalmente (Rotterdam 2023; Legro NEJM 2014).<br>
              <em>⚠️ Nota Prática Brasil / SUS:</em> O Letrozol é formalmente off-label no Brasil pela ANVISA para indução ovulatória e não é fornecido pelo SUS; no protocolo público brasileiro, o <strong>Citrato de Clomifeno</strong> é a medicação padronizada na rede. Monitorar rigorosamente o risco de Síndrome de Hiperestimulação Ovariana (SHO).
            ` : `
              • <strong>Sem Desejo de Gestação:</strong> Anticoncepcional hormonal combinado (ACO) para proteção endometrial e controle de acne/hirsutismo. Sempre avaliar contraindicações da OMS (Cat 4: enxaqueca com aura, tabagismo >= 35 anos, trombofilia, HAS grave). Se hirsutismo persistente após 6 meses de ACO, associar <strong>Espironolactona</strong> (sempre com método contraceptivo seguro pela teratogenia).
            `}
            <br>• Se resistência à insulina acentuada ou pré-diabetes: Associar <strong>Metformina</strong>.
          </div>
        </div>
      `;
    } else {
      resultBox.className = "p-4 rounded-xl border-2 bg-slate-100 dark:bg-slate-800 border-slate-300 dark:border-slate-700 text-slate-700 dark:text-slate-300 space-y-2";
      resultBox.innerHTML = `
        <div class="flex items-center gap-2 font-bold text-sm">
          <i data-lucide="info" class="w-5 h-5"></i> CRITÉRIOS DE ROTTERDAM INSUFICIENTES (${count}/3)
        </div>
        <p class="text-xs">
          A paciente preenche apenas ${count} critério(s). São necessários pelo menos 2 dos 3 critérios para confirmação diagnóstica de SOP após exclusão de outras endocrinopatias.
        </p>
      `;
    }

    if (window.lucide) lucide.createIcons();
  }

  [anovCheck, hyperCheck, usgCheck, amhCheck, exclCheck, fertCheck].forEach(el => {
    if (el) el.addEventListener('change', evaluateSOP);
  });
  if (amhValueInput) amhValueInput.addEventListener('input', evaluateSOP);

  evaluateSOP();
}

/* ==========================================================================
   8. DIRETRIZ ESHRE 2022: ENDOMETRIOSE E CONDUTA
   ========================================================================== */
function initEndometriosisESHREGuide() {
  const painSelect = document.getElementById('endo-pain-level');
  const desireFertCheck = document.getElementById('endo-fertility');
  const usgDeepCheck = document.getElementById('endo-deep-usg');
  const resultBox = document.getElementById('endo-result');

  if (!painSelect || !resultBox) return;

  function updateGuide() {
    const pain = painSelect.value;
    const wantsFert = desireFertCheck ? desireFertCheck.checked : false;
    const hasDeepLesion = usgDeepCheck ? usgDeepCheck.checked : false;

    let plan = "";

    if (wantsFert) {
      plan = `
        <strong class="text-rose-700 dark:text-rose-400">Abordagem Focada em Fertilidade (ESHRE 2022):</strong><br>
        • ⚠️ <strong>Atenção:</strong> Supressão hormonal (ACO/Dienogeste) <em>não melhora a fertilidade</em> e impede a gravidez durante o uso!<br>
        • Na endometriose mínima/leve: Excisão cirúrgica laparoscópica aumenta a chance de concepção espontânea.<br>
        • <strong>Endometriomas e FIV (Ponto de Corte 3 cm):</strong> A cistectomia ovariana reduz a reserva ovariana (queda do AMH). Conforme ESHRE 2022, <strong>endometriomas < 3 cm assintomáticos não devem ser operados antes da FIV</strong> (proceder diretamente à captação). A cirurgia é considerada apenas se > 3 cm associado a dor refratária, dificuldade de acesso aos folículos ou suspeita de malignidade.<br>
        • Casos moderados/graves, idade >= 35 anos ou fator masculino associado: Encaminhar precocemente para <strong>FIV</strong>.
      `;
    } else {
      if (hasDeepLesion) {
        plan = `
          <strong class="text-rose-700 dark:text-rose-400">Endometriose Profunda com Mapeamento Positivo:</strong><br>
          • <strong>1ª Linha:</strong> Tratamento clínico hormonal contínuo (<strong>Dienogeste 2 mg/dia</strong> [observação: medicamento de referência, porém off-RENAME/não padronizado no SUS; no SUS usa-se medroxiprogesterona ou ACO contínuo] ou DIU-LNG 52 mg) + AINE nas crises de dor.<br>
          • <strong>Indicação Cirúrgica Absoluta:</strong> Sinais de suboclusão intestinal, estenose ureteral com hidronefrose, falha terapêutica incapacitante ou suspeita de malignidade.<br>
          • Manter supressão hormonal pós-operatória contínua para prevenir recorrência (20 a 50% em 5 anos sem medicação).
        `;
      } else {
        plan = `
          <strong class="text-emerald-700 dark:text-emerald-400">Dor Suspeita (Diretriz ESHRE 2022 - Tratamento Empírico):</strong><br>
          • <em>A laparoscopia diagnóstica NÃO é obrigatória para iniciar o tratamento!</em><br>
          • Iniciar imediatamente tratamento hormonal empírico: <strong>ACO contínuo</strong> ou <strong>Progestagênio</strong> (Dienogeste 2 mg/dia ou medroxiprogesterona no SUS) associado a AINE.<br>
          • Solicitar Ultrassom Transvaginal com Preparo Intestinal ou Ressonância Magnética com protocolo específico para endometriose.<br>
          • Reavaliar resposta em 3 a 6 meses.
        `;
      }
    }

    resultBox.innerHTML = `
      <div class="p-4 rounded-xl border border-slate-200 dark:border-slate-700 bg-white dark:bg-slate-800 text-xs sm:text-sm leading-relaxed">
        ${plan}
      </div>
    `;
  }

  painSelect.addEventListener('change', updateGuide);
  if (desireFertCheck) desireFertCheck.addEventListener('change', updateGuide);
  if (usgDeepCheck) usgDeepCheck.addEventListener('change', updateGuide);

  updateGuide();
}

/* ==========================================================================
   9. ESTRATIFICADOR DE MASSAS ANEXIAIS (O-RADS US & IOTA)
   ========================================================================== */
function initAdnexalMassORADSCalculator() {
  const oradsSelect = document.getElementById('orads-score');
  const postMenoCheck = document.getElementById('orads-postmeno');
  const ca125Input = document.getElementById('orads-ca125');
  const resultBox = document.getElementById('orads-result');

  if (!oradsSelect || !resultBox) return;

  function updateRisk() {
    const score = parseInt(oradsSelect.value) || 2;
    const isPostMeno = postMenoCheck ? postMenoCheck.checked : false;
    const ca125 = parseFloat(ca125Input ? ca125Input.value : 0) || 0;

    let riskPercent = "";
    let action = "";
    let badgeClass = "";

    switch (score) {
      case 1:
        riskPercent = "0% (Normal Fisiológico)";
        action = "Estruturas ovarianas fisiológicas (folículo ou corpo lúteo <= 3 cm na pré-menopausa). Nenhuma conduta necessária.";
        badgeClass = "bg-emerald-100 text-emerald-900 dark:bg-emerald-950 dark:text-emerald-300";
        break;
      case 2:
        riskPercent = "< 1% (Quase certamente benigno)";
        action = "Cisto simples unilocular < 10 cm, cisto dermoide típico < 10 cm, endometrioma clássico < 10 cm ou cisto hemorrágico. Seguimento ultrassonográfico anual ou expectante.<br><span class='text-amber-800 dark:text-amber-300 font-semibold block mt-1'>⚠️ Ressalva O-RADS: Se dermoide ou endometrioma atingir >= 10 cm ou apresentar componente sólido vascularizado ao Doppler colorido, escalona para O-RADS 3 ou 4 (avaliação especializada ou RM).</span>";
        badgeClass = "bg-emerald-100 text-emerald-900 dark:bg-emerald-950 dark:text-emerald-300";
        break;
      case 3:
        riskPercent = "1% a < 10% (Baixo risco de malignidade)";
        action = "Cisto unilocular >= 10 cm, multilocular liso sem sólido com Doppler baixo. Avaliação com ginecologista geral ou ultrassonografia especializada/RM.";
        badgeClass = "bg-amber-100 text-amber-900 dark:bg-amber-950 dark:text-amber-300";
        break;
      case 4:
        riskPercent = "10% a < 50% (Risco intermediário de malignidade)";
        action = "Lesão multilocular com componente sólido ou projeção papilar. Avaliação formal com Ginecologista Oncológico e Ressonância Magnética (O-RADS RM).";
        badgeClass = "bg-orange-100 text-orange-900 dark:bg-orange-950 dark:text-orange-300";
        break;
      case 5:
        riskPercent = ">= 50% (Alto risco de malignidade)";
        action = "Tumor sólido irregular, ascite peritoneal ou >= 4 projeções papilares com fluxo intenso ao Doppler. Encaminhamento IMEDIATO ao Ginecologista Oncológico para estadiamento cirúrgico (nunca puncionar!).";
        badgeClass = "bg-rose-600 text-white";
        break;
    }

    let caAlert = "";
    if (ca125 > 35 && isPostMeno) {
      caAlert = `<div class="mt-2 p-2.5 rounded-lg bg-rose-100 dark:bg-rose-950/60 border border-rose-300 dark:border-rose-800 text-rose-900 dark:text-rose-200 text-xs font-semibold">⚠️ ALERTA CA-125: Na pós-menopausa, CA-125 > 35 U/mL (${ca125} U/mL) associado a massa anexial é critério formal para avaliação por Ginecologista Oncológico!</div>`;
    } else if (ca125 > 200 && !isPostMeno) {
      caAlert = `<div class="mt-2 p-2.5 rounded-lg bg-rose-100 dark:bg-rose-950/60 border border-rose-300 dark:border-rose-800 text-rose-900 dark:text-rose-200 text-xs font-semibold">⚠️ ALERTA CA-125: Na pré-menopausa, CA-125 muito elevado (> 200 U/mL) justifica avaliação oncológica (descartar neoplasia epitelial).</div>`;
    }

    resultBox.innerHTML = `
      <div class="p-4 rounded-xl border border-slate-200 dark:border-slate-700 bg-white dark:bg-slate-800 space-y-2">
        <div class="flex items-center justify-between flex-wrap gap-2">
          <span class="text-sm font-black text-slate-900 dark:text-white">Classificação O-RADS ${score}</span>
          <span class="px-2.5 py-1 text-xs font-bold rounded-full ${badgeClass}">Risco: ${riskPercent}</span>
        </div>
        <p class="text-xs text-slate-600 dark:text-slate-300 leading-relaxed">${action}</p>
        ${caAlert}
      </div>
    `;
  }

  oradsSelect.addEventListener('change', updateRisk);
  if (postMenoCheck) postMenoCheck.addEventListener('change', updateRisk);
  if (ca125Input) ca125Input.addEventListener('input', updateRisk);

  updateRisk();
}

/* ==========================================================================
   10. ÁRVORE DE DECISÃO DAS AMENORREIAS (PRIMÁRIA & SECUNDÁRIA)
   ========================================================================== */
function initAmenorrheaDecisionTree() {
  const typeSelect = document.getElementById('amen-type');
  const stepContainer = document.getElementById('amen-steps');
  if (!typeSelect || !stepContainer) return;

  function renderTree() {
    const isPrimary = typeSelect.value === 'primary';

    if (isPrimary) {
      stepContainer.innerHTML = `
        <div class="p-4 rounded-xl border border-indigo-200 dark:border-indigo-900 bg-indigo-50/50 dark:bg-indigo-950/30 space-y-3 text-xs sm:text-sm">
          <h5 class="font-black text-indigo-950 dark:text-indigo-200 flex items-center gap-2">
            <span class="px-2 py-0.5 rounded bg-indigo-600 text-white text-xs">Algoritmo</span> Amenorreia Primária (Mamas vs Útero)
          </h5>
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
            <div class="p-3 bg-white dark:bg-slate-800 rounded-xl border border-slate-200 dark:border-slate-700">
              <strong class="text-slate-900 dark:text-white block mb-1">Mamas Normais + Útero Ausente</strong>
              <p class="text-slate-600 dark:text-slate-300">
                <strong>Solicitar Cariótipo e Testosterona:</strong><br>
                • <strong>46,XX + Testosterona Feminina:</strong> Síndrome de Mayer-Rokitansky-Küster-Hauser (MRKH). Ovários normais, pelos normais. Rastrear anomalias renais (USG de rins). Tratamento: Dilatadores de Frank.<br>
                • <strong>46,XY + Testosterona Masculina:</strong> Síndrome de Morris (Insensibilidade Androgênica Completa). Testículos intra-abdominais, pelos escassos. Tratamento: Gonadectomia pós-puberal (risco tumoral) + TH.
              </p>
            </div>
            <div class="p-3 bg-white dark:bg-slate-800 rounded-xl border border-slate-200 dark:border-slate-700">
              <strong class="text-slate-900 dark:text-white block mb-1">Mamas Ausentes + Útero Presente</strong>
              <p class="text-slate-600 dark:text-slate-300">
                <strong>Falta Estrogênio — Dosar FSH:</strong><br>
                • <strong>FSH Alto:</strong> Disgenesia gonadal (Ovário quebrado). Cariótipo: Síndrome de Turner (45,X - baixa estatura, pescoço alado, coarctação de aorta) ou Swyer (46,XY - risco tumoral).<br>
                • <strong>FSH Baixo/Normal:</strong> Hipogonadismo hipogonadotrófico (Hipotálamo/Hipófise). Síndrome de Kallmann (com anosmia), estresse grave ou tumor de SNC.
              </p>
            </div>
          </div>
        </div>
      `;
    } else {
      stepContainer.innerHTML = `
        <div class="p-4 rounded-xl border border-rose-200 dark:border-rose-900 bg-rose-50/50 dark:bg-rose-950/30 space-y-3 text-xs sm:text-sm">
          <h5 class="font-black text-rose-950 dark:text-rose-200 flex items-center gap-2">
            <span class="px-2 py-0.5 rounded bg-rose-600 text-white text-xs">Algoritmo</span> Amenorreia Secundária (4 Compartimentos)
          </h5>
          <div class="space-y-2">
            <div class="p-3 bg-white dark:bg-slate-800 rounded-xl border border-slate-200 dark:border-slate-700">
              <strong>1º Passo: beta-hCG sempre primeiro!</strong> Gravidez é a causa mais comum de amenorreia secundária.
            </div>
            <div class="p-3 bg-white dark:bg-slate-800 rounded-xl border border-slate-200 dark:border-slate-700">
              <strong>2º Passo: TSH e Prolactina.</strong> Descartar hipotireoidismo primário e prolactinoma/hiperprolactinemia farmacológica.
            </div>
            <div class="p-3 bg-white dark:bg-slate-800 rounded-xl border border-slate-200 dark:border-slate-700">
              <strong>3º Passo: Teste da Progesterona (Medroxiprogesterona 10 mg/dia por 7-10 dias).</strong><br>
              • <strong>Sangrou após suspensão (privação):</strong> Havia estrogênio prévio e trato de saída pérvio = <em>Anovulação</em> (ex: SOP).<br>
              • ⚠️ <strong>Red Flag:</strong> Sangramento <em>durante</em> o uso da progesterona ou sangramento atípico é sinal de alerta para hiperplasia ou neoplasia endometrial, exigindo investigação histopatológica imediata.<br>
              • <strong>Não sangrou:</strong> Realizar teste do Estrogênio + Progesterona (E+P por 21 dias).<br>
              &nbsp;&nbsp;&nbsp;&nbsp;- <em>Não sangrou após E+P:</em> Causa anatômica/obstrutiva no compartimento I (<strong>Síndrome de Asherman</strong> após curetagem/infecção). Padrão-ouro diagnóstico e terapêutico: <strong>Histeroscopia cirúrgica com lise de sinéquias</strong>.<br>
              &nbsp;&nbsp;&nbsp;&nbsp;- <em>Sangrou após E+P:</em> O trato de saída é pérvio e o endométrio responde. Falta estrogênio endógeno → <strong>Dosar FSH</strong>: Se alto = Compartimento II (Falência Ovariana Prematura / IOP); Se baixo/normal = Compartimento III/IV (Hipófise / Hipotálamo / RED-S).
            </div>
          </div>
        </div>
      `;
    }
  }

  typeSelect.addEventListener('change', renderTree);
  renderTree();
}

/* ==========================================================================
   11. AVALIADOR DE TERAPIA HORMONAL DA MENOPAUSA (TH)
   ========================================================================== */
function initMenopauseHTEvaluator() {
  const ageInput = document.getElementById('ht-age');
  const yearsInput = document.getElementById('ht-years');
  const uterusCheck = document.getElementById('ht-uterus');
  const vteCheck = document.getElementById('ht-vte');
  const breastCheck = document.getElementById('ht-breast');
  const gsmCheck = document.getElementById('ht-gsm');
  const resultBox = document.getElementById('ht-result');

  if (!ageInput || !resultBox) return;

  function evaluateHT() {
    const age = parseInt(ageInput.value) || 52;
    const years = parseInt(yearsInput.value) || 2;
    const hasUterus = uterusCheck ? uterusCheck.checked : false;
    const hasVTE = vteCheck ? vteCheck.checked : false;
    const hasBreastCancer = breastCheck ? breastCheck.checked : false;
    const hasGSM = gsmCheck ? gsmCheck.checked : false;

    if (hasGSM) {
      resultBox.className = "p-4 rounded-xl border-2 bg-indigo-50 dark:bg-indigo-950/40 border-indigo-500 text-indigo-900 dark:text-indigo-200 space-y-2";
      resultBox.innerHTML = `
        <div class="flex items-center gap-2 font-black text-sm text-indigo-700 dark:text-indigo-400">
          <i data-lucide="check-circle" class="w-5 h-5"></i> SÍNDROME GENITURINÁRIA DA MENOPAUSA (SGM) ISOLADA
        </div>
        <div class="text-xs leading-relaxed space-y-1">
          <p><strong>Padrão-Ouro Terapêutico:</strong> Estrogênio vaginal em dose ultrabaixa (estriol, promestrieno ou estradiol creme/óvulo) ou hidratantes/lubrificantes vaginais não hormonais.</p>
          <p>• <strong>Sem Necessidade de Progesterona:</strong> A absorção sistêmica do estrogênio vaginal em baixas doses é desprezível e <em>não induz proliferação endometrial</em>. Paciente com útero intacto NÃO necessita de oposição progestacional.</p>
          <p>• <strong>Janela de Oportunidade Não se Aplica:</strong> Pode ser prescrito com segurança em qualquer idade (> 60 anos ou > 10 anos pós-menopausa), com rápido alívio de atrofia, disúria, queimação e dispareunia.</p>
          <p>• <em>Em histórico de câncer de mama:</em> Hidratantes vaginais são 1ª linha; estrogênio vaginal em dose mínima pode ser ponderado em casos refratários graves após discussão multidisciplinar formal com o oncologista.</p>
        </div>
      `;
      if (window.lucide) lucide.createIcons();
      return;
    }

    if (hasBreastCancer) {
      resultBox.className = "p-4 rounded-xl border-2 bg-rose-50 dark:bg-rose-950/40 border-rose-500 text-rose-900 dark:text-rose-200 space-y-2";
      resultBox.innerHTML = `
        <div class="flex items-center gap-2 font-black text-sm text-rose-700 dark:text-rose-400">
          <i data-lucide="alert-octagon" class="w-5 h-5"></i> CONTRAINDICAÇÃO ABSOLUTA À TERAPIA HORMONAL SISTÊMICA
        </div>
        <p class="text-xs leading-relaxed">
          Histórico de câncer de mama ou neoplasia estrogênio-dependente contraindica TH sistêmica.<br>
          <strong>Alternativas Seguras Não Hormonais para Fogachos:</strong><br>
          • <strong>Venlafaxina</strong> (ou desvenlafaxina);<br>
          • <strong>Gabapentina</strong> (excelente se insônia/fogachos noturnos);<br>
          • <strong>Fezolinetante</strong> (antagonista do receptor NK3 no hipotálamo);<br>
          • ⚠️ <em>Evitar Paroxetina e Fluoxetina</em> se paciente estiver em uso de Tamoxifeno (inibem CYP2D6 e anulam o efeito antineoplásico do tamoxifeno!).
        </p>
      `;
      if (window.lucide) lucide.createIcons();
      return;
    }

    const inWindow = (age < 60 && years < 10);

    let route = "Oral ou Transdérmica";
    let routeNote = "";
    if (hasVTE) {
      route = "Transdérmica Obrigatória (Adesivo ou Gel)";
      routeNote = "A via transdérmica não tem primeira passagem hepática e não aumenta a síntese de fatores pró-trombóticos, sendo a via mandatória na paciente com risco cardiovascular aumentado ou histórico de trombofilia.";
    }

    let regimen = hasUterus 
      ? "Estrogênio + Progestagênio (Progesterona Micronizada 100 mg contínua ou 200 mg cíclica [menor risco mamário/trombótico, off-RENAME] ou Acetato de Medroxiprogesterona 2,5-5 mg [padronizado no SUS] ou DIU-LNG 52 mg para PROTEÇÃO ENDOMETRIAL)"
      : "Estrogênio Isolado (paciente histerectomizada não necessita de progesterona)";

    if (inWindow) {
      resultBox.className = "p-4 rounded-xl border-2 bg-emerald-50 dark:bg-emerald-950/40 border-emerald-500 text-emerald-900 dark:text-emerald-200 space-y-2";
      resultBox.innerHTML = `
        <div class="flex items-center gap-2 font-black text-sm text-emerald-700 dark:text-emerald-400">
          <i data-lucide="check-circle" class="w-5 h-5"></i> DENTRO DA JANELA DE OPORTUNIDADE (BENEFÍCIO > RISCO)
        </div>
        <div class="text-xs leading-relaxed">
          Mulher com < 60 anos e < 10 anos de menopausa apresenta balanço amplamente favorável para alívio de sintomas vasomotores e proteção óssea.<br>
          <strong>Esquema Recomendado:</strong> ${regimen}.<br>
          <strong>Via Preferencial:</strong> ${route}. ${routeNote}
        </div>
      `;
    } else {
      resultBox.className = "p-4 rounded-xl border-2 bg-amber-50 dark:bg-amber-950/40 border-amber-500 text-amber-900 dark:text-amber-200 space-y-2";
      resultBox.innerHTML = `
        <div class="flex items-center gap-2 font-black text-sm text-amber-700 dark:text-amber-400">
          <i data-lucide="alert-triangle" class="w-5 h-5"></i> FORA DA JANELA CLÁSSICA (INDIVIDUALIZAÇÃO RIGOROSA)
        </div>
        <p class="text-xs leading-relaxed">
          Mulher com >= 60 anos ou >= 10 anos de menopausa apresenta maior risco cardiovascular basal (placas ateroscleróticas prévias instabilizadas pelo estrogênio oral).<br>
          • <strong>Diretrizes NAMS/IMS 2022:</strong> A janela não é contraindicação absoluta, mas exige indicação estrita, via exclusivamente <strong>transdérmica na menor dose eficaz</strong> e prévia estratificação de risco lipídico/cardiovascular.<br>
          • Se sintomas vasomotores intensos refratários: priorizar moduladores não hormonais (venlafaxina, gabapentina, fezolinetante).
        </p>
      `;
    }

    if (window.lucide) lucide.createIcons();
  }

  [ageInput, yearsInput].forEach(el => el.addEventListener('input', evaluateHT));
  [uterusCheck, vteCheck, breastCheck, gsmCheck].forEach(el => {
    if (el) el.addEventListener('change', evaluateHT);
  });

  evaluateHT();
}

/* ==========================================================================
   12. CALCULADORA DE ESPERMOGRAMA (OMS 2021) & INFERTILIDADE
   ========================================================================== */
function initSemenAnalysisCalculator() {
  const volInput = document.getElementById('semen-vol');
  const concInput = document.getElementById('semen-conc');
  const motInput = document.getElementById('semen-mot');
  const morphInput = document.getElementById('semen-morph');
  const resultBox = document.getElementById('semen-result');

  if (!concInput || !motInput || !resultBox) return;

  function evaluateSemen() {
    const vol = parseFloat(volInput ? volInput.value : 1.5) || 1.5;
    const conc = parseFloat(concInput.value) || 0;
    const mot = parseFloat(motInput.value) || 0;
    const morph = parseFloat(morphInput ? morphInput.value : 0) || 0;
    const totalCount = Math.round(conc * vol * 10) / 10;

    let alterations = [];

    if (vol < 1.4) alterations.push(`Hipospermia (Volume Seminal: ${vol} mL | Referência OMS 2021: >= 1.4 a 1.5 mL)`);
    if (conc < 16) alterations.push(`Oligozoospermia (Concentração: ${conc} M/mL | Referência OMS 2021: >= 16 M/mL)`);
    if (totalCount < 39) alterations.push(`Contagem Total Reduzida (Total: ${totalCount} M/ejaculado | Referência OMS 2021: >= 39 milhões/ejaculado)`);
    if (mot < 30) alterations.push(`Astenozoospermia (Motilidade Progressiva: ${mot}% | Referência OMS 2021: >= 30%)`);
    if (morph < 4) alterations.push(`Teratozoospermia (Morfologia Normal Kruger: ${morph}% | Referência OMS 2021: >= 4%)`);

    if (alterations.length === 0) {
      resultBox.className = "p-4 rounded-xl border border-emerald-500 bg-emerald-50 dark:bg-emerald-950/40 text-emerald-900 dark:text-emerald-200 text-xs";
      resultBox.innerHTML = `
        <strong class="font-bold flex items-center gap-1 text-emerald-700 dark:text-emerald-400">
          <i data-lucide="check" class="w-4 h-4"></i> Normozoospermia (Parâmetros Seminais Normais - OMS 2021)
        </strong>
        O espermograma preenche todos os critérios da 6ª edição OMS (Volume: ${vol} mL | Concentração: ${conc} M/mL | Total: ${totalCount} M | Motilidade: ${mot}% | Morfologia: ${morph}%).<br>
        <span class="block mt-1 text-emerald-800 dark:text-emerald-300">• Prosseguir com a investigação simultânea dos fatores femininos (reserva ovariana, tubas uterinas e cavidade endometrial).</span>
      `;
    } else {
      resultBox.className = "p-4 rounded-xl border border-rose-500 bg-rose-50 dark:bg-rose-950/40 text-rose-900 dark:text-rose-200 text-xs";
      resultBox.innerHTML = `
        <strong class="font-bold flex items-center gap-1 text-rose-700 dark:text-rose-400">
          <i data-lucide="alert-circle" class="w-4 h-4"></i> Alteração no Espermograma Detectada
        </strong>
        <ul class="list-disc list-inside mt-1 font-medium">
          ${alterations.map(a => `<li>${a}</li>`).join('')}
        </ul>
        <div class="mt-2 space-y-1 font-semibold text-rose-950 dark:text-rose-300">
          <p>• <strong>Conduta Inicial:</strong> Repetir o espermograma em 2 a 3 meses (ciclo da espermatogênese é de ~74 dias) e encaminhar ao Urologista/Andrologista.</p>
          <p>• <strong>Indicação de Teste de Fragmentação do DNA Espermático (DFI):</strong> Indicado em perdas gestacionais recorrentes, falhas prévias de FIV/ICSI ou varicocele clínica (DFI > 20-30% associa-se a dano genômico espermático).</p>
          <p>• <strong>Fator Grave (concentração < 5 M/mL ou astenozoospermia grave):</strong> Avaliar indicação direta para Reprodução Assistida de alta complexidade (FIV com ICSI).</p>
        </div>
      `;
    }

    if (window.lucide) lucide.createIcons();
  }

  [volInput, concInput, motInput, morphInput].forEach(el => {
    if (el) el.addEventListener('input', evaluateSemen);
  });

  evaluateSemen();
}

/* ==========================================================================
   13. FLASHCARDS 3D INTERATIVOS (15 CARDS HIGH-YIELD)
   ========================================================================== */
const FLASHCARDS_DATA = [
  {
    category: "Módulo 40: Ciclo Menstrual",
    q: "Qual a regra fisiológica fundamental que explica o sangramento uterino disfuncional anovulatório?",
    a: "É o 'estrogênio sem oposição de progesterona'. O endométrio cresce continuamente como um prédio sem cimento e desaba de forma irregular e fragmentada."
  },
  {
    category: "Módulo 41: Sangramento Uterino Anormal",
    q: "Qual o tratamento medicamentoso ambulatorial mais eficaz para redução do volume do fluxo menstrual?",
    a: "O DIU liberador de Levonorgestrel 52 mg (redução de 70 a 90% do fluxo sanguíneo menstrual, superior aos anticoncepcionais orais)."
  },
  {
    category: "Módulo 41: Sangramento Pós-Menopausa",
    q: "Qual o ponto de corte da espessura endometrial na pós-menopausa para indicar biópsia endometrial?",
    a: "Espessura endometrial > 4 mm ao ultrassom transvaginal em mulher sem terapia hormonal. Se em uso de tamoxifeno, o corte de 4 mm não se aplica."
  },
  {
    category: "Módulo 41: Síndrome dos Ovários Policísticos",
    q: "Qual o fármaco de primeira linha para indução da ovulação em pacientes com SOP que desejam engravidar?",
    a: "Letrozol (inibidor da aromatase), padrão internacional (Rotterdam 2023; Legro NEJM 2014). Nota SUS: No Brasil é formalmente off-label pela ANVISA e não fornecido na rede; no SUS usa-se Citrato de Clomifeno. Monitorar risco de Síndrome de Hiperestimulação Ovariana (SHO)."
  },
  {
    category: "Módulo 42: Miomatose Uterina",
    q: "Qual mioma uterino tem maior probabilidade de sofrer torção aguda e causar abdome agudo ginecológico?",
    a: "O mioma subseroso pediculado (FIGO Tipo 7), devido ao seu eixo longo móvel."
  },
  {
    category: "Módulo 42: Miomatose Uterina",
    q: "Qual o papel do análogo de GnRH (Leuprorrelina) no manejo dos grandes leiomiomas uterinos?",
    a: "Uso pré-operatório por 3 a 6 meses para reduzir volume e corrigir anemia grave. O uso é estritamente limitado a no máximo 6 meses sem terapia add-back para prevenir perda óssea acelerada e osteopenia severa."
  },
  {
    category: "Módulo 43: Adenomiose",
    q: "Como se caracteriza o útero ao toque bimanual na paciente com adenomiose uterina?",
    a: "Útero difusamente aumentado (até 12 semanas), globoso, amolecido ('boggy'), simétrico e doloroso à palpação (diferente do mioma, que é nodular e firme)."
  },
  {
    category: "Módulo 44: Endometriose",
    q: "Quais são os clássicos '4 Ds' da apresentação clínica da endometriose?",
    a: "1. Dismenorreia progressiva;\n2. Dispareunia de profundidade;\n3. Disquezia (dor ao evacuar no período menstrual);\n4. Disúria cíclica."
  },
  {
    category: "Módulo 44: Endometriose (Diretriz ESHRE 2022)",
    q: "Endometriomas ovarianos devem ser ressecados cirurgicamente antes de ciclos de FIV?",
    a: "NÃO, se forem menores que 3 cm e assintomáticos! A cistectomia reduz a reserva ovariana (queda expressiva de AMH) sem aumentar taxas de nascidos vivos na FIV. A cirurgia é restrita a casos > 3 cm com dor refratária ou suspeita de malignidade."
  },
  {
    category: "Módulo 45: Massas Anexiais",
    q: "O que é a Síndrome de Meigs cobrada clássicamente em provas de título e residência?",
    a: "Tríade composta por: 1. Fibroma ovariano benigno; 2. Ascite; 3. Derrame pleural (frequentemente à direita), que se resolvem completamente após a remoção do tumor."
  },
  {
    category: "Módulo 45: Torção Anexial",
    q: "A presença de fluxo arterial ao mapeamento Doppler exclui o diagnóstico de torção de ovário?",
    a: "NÃO! O ovário possui dupla vascularização (uterina e ovariana) e o fluxo arterial pode persistir. A suspeita clínica com dor súbita exige laparoscopia de urgência."
  },
  {
    category: "Módulo 47: Climatério e Menopausa",
    q: "O que define a 'Janela de Oportunidade' para a TH e qual a conduta na Síndrome Geniturinária (SGM)?",
    a: "Janela clássica: < 60 anos ou < 10 anos pós-menopausa. Já na SGM (atrofia vulvovaginal isolada), o estrogênio tópico vaginal pode ser usado em qualquer idade, não tem absorção sistêmica relevante e NÃO necessita de progesterona para proteção endometrial."
  },
  {
    category: "Módulo 47: Menopausa & Oncologia",
    q: "Por que a paroxetina e fluoxetina são contraindicadas para tratar fogachos em mulheres usando Tamoxifeno?",
    a: "Porque são inibidores potentes do citocromo CYP2D6, impedindo a conversão do tamoxifeno no seu metabólito ativo endoxifeno e aumentando o risco de recidiva do câncer de mama!"
  },
  {
    category: "Módulo 48: Amenorreia Primária",
    q: "Qual a diferença semiológica crucial entre Síndrome de MRKH e Insensibilidade Androgênica (Morris)?",
    a: "Os pelos pubianos e axilares! Em MRKH (46,XX) os pelos são normais. Na insensibilidade androgênica completa (46,XY) os pelos são ausentes ou muito escassos."
  },
  {
    category: "Módulo 49: Infertilidade",
    q: "Qual a conduta mandatória diante do diagnóstico de hidrossalpinge antes da realização de FIV?",
    a: "Salpingectomia (ou oclusão tubária proximal), pois o fluido estagnado na tuba é tóxico ao embrião e sua remoção dobra a taxa de gravidez por FIV."
  }
];

function initFlashcards() {
  let currentIndex = 0;
  const card = document.getElementById('flashcard');
  const catOut = document.getElementById('fc-category');
  const qOut = document.getElementById('fc-question');
  const aOut = document.getElementById('fc-answer');
  const countOut = document.getElementById('fc-counter');
  const prevBtn = document.getElementById('fc-prev');
  const nextBtn = document.getElementById('fc-next');
  const flipBtn = document.getElementById('fc-flip');

  if (!card || !qOut || !aOut) return;

  function renderCard() {
    card.classList.remove('card-flipped');
    const item = FLASHCARDS_DATA[currentIndex];
    catOut.textContent = item.category;
    qOut.textContent = item.q;
    aOut.innerHTML = item.a.replace(/\n/g, '<br>');
    if (countOut) countOut.textContent = `${currentIndex + 1} de ${FLASHCARDS_DATA.length}`;
  }

  card.addEventListener('click', () => {
    card.classList.toggle('card-flipped');
  });

  if (flipBtn) {
    flipBtn.addEventListener('click', (e) => {
      e.stopPropagation();
      card.classList.toggle('card-flipped');
    });
  }

  if (prevBtn) {
    prevBtn.addEventListener('click', (e) => {
      e.stopPropagation();
      if (currentIndex > 0) {
        currentIndex--;
        renderCard();
      }
    });
  }

  if (nextBtn) {
    nextBtn.addEventListener('click', (e) => {
      e.stopPropagation();
      if (currentIndex < FLASHCARDS_DATA.length - 1) {
        currentIndex++;
        renderCard();
      }
    });
  }

  renderCard();
}

/* ==========================================================================
   14. SIMULADO CLÍNICO INTERATIVO (15 VINHETAS ESTILO USMLE STEP 2 CK)
   ========================================================================== */
const QUIZ_DATA = [
  {
    id: 1,
    stem: "Adolescente de 14 anos, menarca há 1 ano, comparece à emergência com sangramento menstrual contínuo há 10 dias e hemoglobina de 7,8 g/dL. Refere histórico de sangramento gengival frequente e hemorragia volumosa após extração dentária há 6 meses. O teste de gravidez na urina é negativo. Qual o próximo passo mais apropriado na investigação diagnóstica?",
    options: [
      "Solicitar histeroscopia com biópsia endometrial para afastar pólipo",
      "Solicitar dosagem do antígeno do fator de von Willebrand, atividade do cofator de ristocetina e fator VIII",
      "Prescrever anticoncepcional oral combinado e dar alta sem novos exames",
      "Indicar curetagem uterina hemostática de urgência"
    ],
    correct: 1,
    explanation: "Em adolescentes com sangramento uterino abundante desde a menarca associado a histórico de sangramento mucoso ou hemostasia prejudicada após procedimentos, a causa mais comum é coagulopatia hereditária, especificamente a Doença de von Willebrand (responsável por até 20-30% desses casos graves)."
  },
  {
    id: 2,
    stem: "Mulher de 62 anos, menopausa aos 50 anos sem uso de terapia hormonal, apresenta sangramento vaginal vermelho vivo em pequena quantidade há 2 semanas. Ao exame especular, mucosa atrófica sem lesões cervicais visíveis. Ultrassonografia transvaginal revela eco endometrial homogêneo medindo 9 mm. Qual a conduta indicada?",
    options: [
      "Tranquilizar a paciente e orientar retorno se houver piora, pois 9 mm é compatível com atrofia",
      "Prescrever creme vaginal de estriol por 30 dias para tratar vaginite atrófica",
      "Realizar biópsia endometrial ambulatorial (com cânula de Pipelle ou histeroscopia)",
      "Indicar histerectomia total imediata por laparotomia"
    ],
    correct: 2,
    explanation: "Sangramento na pós-menopausa é suspeito de neoplasia de endométrio até prova em contrário (presente em ~10% dos casos). Na ausência de TH, um endométrio > 4 mm exige obrigatoriamente estudo histopatológico por biópsia endometrial ou histeroscopia com biópsia dirigida."
  },
  {
    id: 3,
    stem: "Mulher de 29 anos, solteira, IMC de 34 kg/m², queixa-se de menstruações a cada 60 a 90 dias, acne facial intensa e hirsutismo progressivo. Nega desejo de gestação no momento. beta-hCG é negativo; TSH, Prolactina e 17-hidroxiprogesterona estão normais. Qual o tratamento de primeira escolha para o manejo do hiperandrogenismo e proteção endometrial?",
    options: [
      "Anticoncepcional hormonal combinado oral e mudança do estilo de vida com dieta e atividade física",
      "Letrozol 2,5 mg/dia por 5 dias consecutivos a cada ciclo",
      "Curetagem uterina aspirativa semestral",
      "Espironolactona isolada sem método contraceptivo"
    ],
    correct: 0,
    explanation: "O quadro preenche critérios de Rotterdam para SOP. Em pacientes sem desejo reprodutivo imediato, a base terapêutica é a mudança do estilo de vida associada a anticoncepcional hormonal combinado, que suprime a secreção de LH, reduz a produção ovariana de andrógenos, eleva a SHBG e protege o endométrio contra hiperplasia."
  },
  {
    id: 4,
    stem: "A mesma paciente da questão anterior, agora com 31 anos e casada, retorna à consulta após perder 8% do peso corporal, relatando que agora deseja engravidar ativamente há 8 meses sem sucesso. O espermograma do parceiro é rigorosamente normal e a histerossalpingografia demonstra tubas pérvias. Qual a primeira linha medicamentosa para indução da ovulação?",
    options: [
      "Citrato de Clomifeno",
      "Letrozol (inibidor da aromatase)",
      "Gonadotrofina coriônica humana (hCG) recombinante",
      "Fertilização in vitro imediata"
    ],
    correct: 1,
    explanation: "Segundo a Diretriz Internacional de SOP 2023 e grandes ensaios clínicos randomizados (Legro et al., NEJM 2014), o Letrozol é formalmente a primeira linha para indução da ovulação na anovulação por SOP, apresentando maiores taxas de ovulação monofolicular e maiores índices de nascidos vivos em comparação ao clomifeno."
  },
  {
    id: 5,
    stem: "Mulher de 38 anos, nuligesta com desejo reprodutivo presente, queixa-se de menorragia volumosa com coágulos e fraqueza progressiva (Hb 8,5 g/dL). Ultrassom e histeroscopia revelam nódulo submucoso completamente intracavitário pediculado de 3 cm (FIGO tipo 0). Qual a conduta cirúrgica de escolha?",
    options: [
      "Miomectomia laparotômica com incisão fúndica profunda",
      "Histerectomia total laparoscópica",
      "Miomectomia histeroscópica ambulatorial ou em centro cirúrgico com reposição de ferro",
      "Embolização de artérias uterinas exclusiva"
    ],
    correct: 2,
    explanation: "Miomas submucosos FIGO 0 (e a maioria dos tipos 1) com até 4-5 cm de diâmetro têm como padrão-ouro a ressecção histeroscópica. É um procedimento minimamente invasivo, preserva a integridade miometrial e o útero para gestação futura e soluciona eficazmente o sangramento."
  },
  {
    id: 6,
    stem: "Mulher de 27 anos refere dor menstrual incapacitante progressiva há 5 anos, dispareunia profunda e dor para evacuar durante o fluxo menstrual (disquezia). Ao toque vaginal, palpa-se nodularidade dolorosa em ligamentos uterossacros. Ultrassonografia pélvica de rotina é laudada como normal. A paciente não deseja engravidar no momento. Qual a conduta inicial recomendada segundo as diretrizes modernas da ESHRE?",
    options: [
      "Indicar videolaparoscopia imediata, pois a biópsia é obrigatória antes de qualquer medicação",
      "Iniciar tratamento clínico empírico com AINE e progestagênio (ou ACO contínuo) e solicitar ultrassom transvaginal com preparo intestinal",
      "Prescrever analgésicos simples e orientar que cólica menstrual é fisiológica nessa idade",
      "Indicar ooforectomia bilateral laparoscópica"
    ],
    correct: 1,
    explanation: "Conforme a diretriz ESHRE 2022, o retardo diagnóstico da endometriose deve ser combatido iniciando-se tratamento clínico empírico hormonal sem necessidade mandatória de laparoscopia cirúrgica prévia. Exames de imagem avançados (USG com preparo intestinal ou RM) devem ser solicitados para mapeamento da doença profunda."
  },
  {
    id: 7,
    stem: "Mulher de 24 anos procura o pronto-atendimento com dor súbita e excruciante em fossa ilíaca esquerda há 3 horas, acompanhada de múltiplos episódios de vômitos. O beta-hCG é negativo. Ao ultrassom, ovário esquerdo aumentado de volume (8 cm) com massa heterogênea ecogênica (provável dermoide) e presença de fluxo vascular detectado ao Doppler. Qual a conduta correta?",
    options: [
      "Internar na enfermaria e aguardar melhora clínica com analgésicos, pois o fluxo Doppler preservado descarta torção",
      "Laparoscopia cirúrgica de urgência para destorção ovariana e cistectomia, preservando o parênquima gonadal",
      "Ooforectomia esquerda imediata sem destorção para evitar embolia pulmonar",
      "Punção percutânea guiada por ultrassom do cisto ovariano"
    ],
    correct: 1,
    explanation: "A presença de fluxo vascular ao Doppler NÃO exclui torção anexial (o ovário possui dupla vascularização e a torção pode ser intermitente ou venosa inicial). A conduta em mulher jovem é laparoscopia de urgência com destorção e preservação ovariana (mesmo com aspecto escurecido inicial, a maioria recupera a viabilidade)."
  },
  {
    id: 8,
    stem: "Mulher de 58 anos apresenta aumento do volume abdominal. Ultrassonografia pélvica revela massa anexial direita de 9 cm com projeções papilares internas vascularizadas, componente sólido irregular e líquido livre abundante na cavidade (ascite). A dosagem de CA-125 é de 480 U/mL. Qual a melhor conduta?",
    options: [
      "Puncionar a massa por via transvaginal para citologia antes de operar",
      "Encaminhar imediatamente ao ginecologista oncológico para laparotomia exploradora e estadiamento cirúrgico",
      "Iniciar anticoncepcional oral em dose dupla por 6 meses para regredir a lesão",
      "Repetir a ultrassonografia em 1 ano para avaliar velocidade de crescimento"
    ],
    correct: 1,
    explanation: "Massa ovariana complexa na pós-menopausa com componentes sólidos, ascite e CA-125 elevado preenche critérios O-RADS 5 (> 50% de risco de malignidade). A punção é formalmente contraindicada pelo risco de disseminação de células malignas na cavidade peritoneal. A conduta é encaminhamento imediato à oncologia ginecológica."
  },
  {
    id: 9,
    stem: "Mulher de 51 anos, última menstruação há 14 meses, queixa-se de fogachos intensos diários que prejudicam seu sono e trabalho. Possui útero intacto, IMC de 32 kg/m² e histórico de hipertensão arterial controlada. Não possui histórico de trombose ou neoplasias. Qual o esquema de Terapia Hormonal (TH) mais seguro?",
    options: [
      "Estradiol transdérmico (gel ou adesivo) associado à Progesterona micronizada oral contínua",
      "Estrogênios conjugados orais isolados sem progesterona",
      "Etinilestradiol oral em alta dose associado a levonorgestrel oral",
      "Contraindicar qualquer tipo de terapia hormonal e prescrever apenas chá de amora"
    ],
    correct: 0,
    explanation: "A paciente está na janela de oportunidade (< 60 anos e < 10 anos de menopausa). Por ter útero, necessita obrigatoriamente de progestagênio associado para proteção endometrial. Por ter obesidade e hipertensão (fatores de risco para TEV), a via transdérmica é a preferida, pois não tem passagem de primeira fase hepática e não induz fatores pró-coagulantes."
  },
  {
    id: 10,
    stem: "Mulher de 48 anos em tratamento adjuvante para câncer de mama receptor de estrogênio positivo com Tamoxifeno apresenta ondas de calor incapacitantes. Qual dos seguintes antidepressivos deve ser RIGOROSAMENTE EVITADO no manejo dos seus sintomas vasomotores?",
    options: [
      "Venlafaxina",
      "Gabapentina",
      "Paroxetina",
      "Desvenlafaxina"
    ],
    correct: 2,
    explanation: "A Paroxetina (e também a Fluoxetina) é um potente inibidor da enzima CYP2D6, responsável por converter o pró-fármaco tamoxifeno no seu metabólito ativo endoxifeno. O uso concomitante reduz drasticamente a eficácia do tratamento antineoplásico, aumentando a recidiva do câncer de mama. Alternativas seguras incluem venlafaxina, gabapentina ou fezolinetante."
  },
  {
    id: 11,
    stem: "Mulher de 32 anos desenvolve amenorreia secundária há 8 meses após curetagem uterina indicada por retenção placentária e endometrite pós-parto. O teste de gravidez é negativo; TSH, Prolactina e FSH estão estritamente normais. Ao realizar o teste do Estrogênio + Progesterona (E+P) por 21 dias, a paciente não apresenta nenhum sangramento de privação. Qual o diagnóstico e conduta?",
    options: [
      "Falência Ovariana Precoce; indicar reposição hormonal",
      "Síndrome de Asherman; realizar histeroscopia cirúrgica para lise de sinéquias intrauterinas",
      "Adenoma hipofisário produtor de ACTH; solicitar ressonância magnética de crânio",
      "Anovulação crônica simples; induzir com acetato de medroxiprogesterona"
    ],
    correct: 1,
    explanation: "A ausência de sangramento após o teste de estrogênio + progesterona prova falha no compartimento I (útero/trato de saída). O antecedente de curetagem vigorosa com infecção uterina é o fator de risco clássico para a Síndrome de Asherman (aderências/sinéquias intrauterinas que obliteram a cavidade endometrial), cujo padrão-ouro é a lise histeroscópica."
  },
  {
    id: 12,
    stem: "Corredora de elite de 19 anos, com baixo percentual de gordura corporal (IMC 16,8 kg/m²), apresenta amenorreia há 1 ano e fratura de estresse em metatarso. Exames revelam FSH e LH diminuídos, estradiol sérico muito baixo e TSH normal. Qual a base do tratamento fisiopatológico para restaurar a função menstrual e a densidade mineral óssea?",
    options: [
      "Prescrever anticoncepcional oral combinado monofásico em alta dose",
      "Aumentar a disponibilidade energética por meio de ajuste calórico na dieta e redução da carga de treinos",
      "Indicar cirurgia ortopédica e repouso absoluto no leito",
      "Administrar citrato de clomifeno diariamente"
    ],
    correct: 1,
    explanation: "Trata-se de Amenorreia Hipotalâmica Funcional no contexto da Tríade da Mulher Atleta / RED-S (Deficiência Relativa de Energia no Esporte). O mecanismo causal é a baixa disponibilidade energética que suprime a pulsatilidade do GnRH. O tratamento fundamental é restaurar o equilíbrio energético com equipe multidisciplinar. Nota Crítica: ACO oral NÃO é recomendado para ganho de massa óssea (etinilestradiol deprime a produção hepática de IGF-1). Se necessária reposição óssea farmacológica, a recomendação (Endocrine Society) é 17-beta estradiol transdérmico associado a progesterona cíclica."
  },
  {
    id: 13,
    stem: "Jovem de 17 anos procura ginecologista por amenorreia primária. Ao exame físico: mamas bem desenvolvidas (Tanner IV-V), pelos pubianos e axilares quase ausentes, genitália externa feminina com vagina curta em fundo cego. Ultrassonografia pélvica demonstra ausência de útero e ovários. O cariótipo revela 46,XY e os níveis de testosterona estão na faixa masculina adulta. Qual o diagnóstico e a conduta recomendada?",
    options: [
      "Síndrome de Turner; reposição de GH e estrogênio",
      "Síndrome de Mayer-Rokitansky-Küster-Hauser; ultrassom de vias urinárias e vaginoplastia",
      "Síndrome de Insensibilidade Androgênica Completa (Morris); gonadectomia bilateral após o término da puberdade",
      "Hiperplasia adrenal congênita; reposição crônica de glicocorticoide"
    ],
    correct: 2,
    explanation: "A presença de fenótipo feminino com mamas desenvolvidas (conversão periférica de andrógenos em estrogênio pela aromatase), ausência de pelos (insensibilidade dos receptores androgênicos), vagina em fundo cego, cariótipo 46,XY e testosterona masculina caracteriza a Síndrome de Morris. A conduta inclui gonadectomia após o desenvolvimento puberal completo devido ao risco de neoplasia maligna de células germinativas nas gônadas retidas."
  },
  {
    id: 14,
    stem: "Adolescente de 16 anos comparece à consulta com amenorreia primária. Apresenta baixa estatura desproporcional (1,43 m), pescoço alado, tórax largo com hipertelorismo mamário e ausência de caracteres sexuais secundários (Tanner I). A dosagem de FSH é de 96 UI/L. Qual o exame confirmatório e qual a avaliação cardiovascular imediata obrigatória?",
    options: [
      "Cariótipo (suspeita de Síndrome de Turner 45,X) e ecocardiograma transtorácico",
      "Ressonância magnética de sela túrcica e dosagem de GH",
      "Biópsia endometrial ambulatorial e teste de estrogênio",
      "Laparoscopia exploradora e angiografia coronariana"
    ],
    correct: 0,
    explanation: "Quadro clássico de disgenesia gonadal por Síndrome de Turner (45,X ou variantes em mosaico), apresentando hipogonadismo hipergonadotrófico (FSH muito elevado). O exame diagnóstico é o cariótipo. A avaliação ecocardiográfica é obrigatória devido à alta prevalência de malformações aórticas congênitas, especialmente valva aórtica bicúspide e coarctação da aorta."
  },
  {
    id: 15,
    stem: "Casal jovem procura atendimento após 14 meses de relações sexuais regulares desprotegidas sem gravidez. A mulher tem 30 anos, ciclos menstruais regulares de 28 dias e histórico prévio de Doença Inflamatória Pélvica tratada aos 23 anos. Qual deve ser o primeiro passo na abordagem diagnóstica do casal?",
    options: [
      "Investigar exclusivamente a mulher com histerossalpingografia imediata, dispensando o homem até o final do processo",
      "Realizar investigação simultânea do casal com espermograma do parceiro, confirmação da ovulação e histerossalpingografia",
      "Indicar cirurgia laparoscópica de emergência antes de qualquer exame laboratorial",
      "Orientar que aguardem mais 12 meses antes de iniciar qualquer investigação"
    ],
    correct: 1,
    explanation: "A infertilidade é definida após 12 meses em mulheres < 35 anos e sua investigação deve SEMPRE ser realizada de forma simultânea no casal, uma vez que o fator masculino está presente (isolado ou associado) em 40 a 50% dos casos. A avaliação inclui espermograma, comprovação da ovulação e avaliação tuboperitoneal (especialmente pelo histórico de DIP)."
  },
  {
    id: 16,
    stem: "Mulher de 26 anos dá entrada na emergência com dor pélvica aguda súbita em cólica de forte intensidade, tontura e síncope ao levantar. Refere atraso menstrual de 6 semanas e sangramento vaginal escuro em pequena quantidade. Ao exame: pálida (3+/4+), sudoreica, PA 80/50 mmHg, FC 124 bpm, abdome distendido com sinais francos de irritação peritoneal (defesa involuntária e dor intensa à mobilização do colo uterino - sinal de Proust positivo). Teste rápido urinário para beta-hCG é positivo. Qual a conduta imediata mandatória?",
    options: [
      "Aguardar transferência para realização de ultrassonografia transvaginal e dosagem quantitativa de beta-hCG",
      "Ressuscitação volêmica imediata com 2 acessos calibrosos e intervenção cirúrgica de urgência (laparotomia ou laparoscopia)",
      "Prescrever metotrexato intramuscular em dose única de 50 mg/m²",
      "Realizar curetagem uterina na sala de emergência para esvaziamento de abortamento incompleto"
    ],
    correct: 1,
    explanation: "Trata-se de Gravidez Ectópica Rota com Choque Hipovolêmico e Hemoperitônio Maciço (abdome agudo hemorrágico). Diante de instabilidade hemodinâmica franca (choque) e peritonite, é ERRO GRAVE retardar a cirurgia para fazer ultrassom ou dosagens seriadas de hCG. A conduta salvadora de vida é acesso venoso calibroso com ressuscitação volêmica agressiva e laparotomia/laparoscopia imediata para hemostasia cirúrgica."
  }
];

function initQuiz() {
  const container = document.getElementById('quiz-container');
  const scoreDisplay = document.getElementById('quiz-score-display');
  const resetBtn = document.getElementById('quiz-reset-btn');

  if (!container) return;

  let userAnswers = {};

  function renderQuiz() {
    container.innerHTML = "";
    userAnswers = {};
    if (scoreDisplay) scoreDisplay.textContent = `Pontuação: 0 de ${QUIZ_DATA.length} respondidas`;

    QUIZ_DATA.forEach((q, idx) => {
      const qCard = document.createElement('div');
      qCard.className = "p-5 rounded-2xl border border-slate-200 dark:border-slate-800 bg-white/80 dark:bg-slate-900/80 shadow-sm space-y-3 transition-all";
      qCard.id = `quiz-card-${q.id}`;

      let optionsHTML = q.options.map((opt, optIdx) => `
        <button type="button" data-qid="${q.id}" data-opt="${optIdx}" 
          class="quiz-opt-btn w-full text-left p-3 rounded-xl border border-slate-200 dark:border-slate-700 hover:bg-slate-50 dark:hover:bg-slate-800 text-xs sm:text-sm font-medium transition-all text-slate-800 dark:text-slate-200 flex items-start gap-2.5">
          <span class="w-5 h-5 rounded-full border border-slate-400 flex items-center justify-center text-xs font-bold shrink-0 mt-0.5">${String.fromCharCode(65 + optIdx)}</span>
          <span class="leading-relaxed">${opt}</span>
        </button>
      `).join('');

      qCard.innerHTML = `
        <div class="flex items-center justify-between gap-2">
          <span class="px-2.5 py-0.5 text-xs font-extrabold rounded-md bg-rose-100 text-rose-800 dark:bg-rose-950 dark:text-rose-300">Questão ${idx + 1} de ${QUIZ_DATA.length}</span>
          <span class="text-xs font-semibold text-slate-400">USMLE Step 2 CK / Residência</span>
        </div>
        <p class="text-xs sm:text-sm text-slate-800 dark:text-slate-200 font-medium leading-relaxed">${q.stem}</p>
        <div class="space-y-2 pt-1" id="quiz-options-${q.id}">
          ${optionsHTML}
        </div>
        <div id="quiz-feedback-${q.id}" class="hidden p-3.5 rounded-xl text-xs sm:text-sm leading-relaxed mt-2 transition-all"></div>
      `;

      container.appendChild(qCard);
    });

    attachOptionListeners();
  }

  function attachOptionListeners() {
    document.querySelectorAll('.quiz-opt-btn').forEach(btn => {
      btn.addEventListener('click', (e) => {
        const qid = parseInt(btn.dataset.qid);
        const selected = parseInt(btn.dataset.opt);
        if (userAnswers[qid] !== undefined) return;

        userAnswers[qid] = selected;
        const qData = QUIZ_DATA.find(item => item.id === qid);
        const isCorrect = selected === qData.correct;

        const parentOptions = document.getElementById(`quiz-options-${qid}`);
        parentOptions.querySelectorAll('.quiz-opt-btn').forEach((b, idx) => {
          b.disabled = true;
          if (idx === qData.correct) {
            b.classList.add('border-emerald-500', 'bg-emerald-50', 'dark:bg-emerald-950/60', 'text-emerald-900', 'dark:text-emerald-200', 'font-bold');
            b.querySelector('span').classList.add('bg-emerald-600', 'text-white', 'border-emerald-600');
          } else if (idx === selected && !isCorrect) {
            b.classList.add('border-rose-500', 'bg-rose-50', 'dark:bg-rose-950/60', 'text-rose-900', 'dark:text-rose-200');
            b.querySelector('span').classList.add('bg-rose-600', 'text-white', 'border-rose-600');
          }
        });

        const fb = document.getElementById(`quiz-feedback-${qid}`);
        fb.classList.remove('hidden');
        if (isCorrect) {
          fb.className = "p-3.5 rounded-xl text-xs sm:text-sm leading-relaxed mt-2 bg-emerald-50 dark:bg-emerald-950/50 border border-emerald-300 dark:border-emerald-800 text-emerald-900 dark:text-emerald-200";
          fb.innerHTML = `<strong>Correto!</strong> ${qData.explanation}`;
        } else {
          fb.className = "p-3.5 rounded-xl text-xs sm:text-sm leading-relaxed mt-2 bg-rose-50 dark:bg-rose-950/50 border border-rose-300 dark:border-rose-800 text-rose-900 dark:text-rose-200";
          fb.innerHTML = `<strong>Incorreto.</strong> A alternativa correta é a letra <strong>${String.fromCharCode(65 + qData.correct)}</strong>.<br>${qData.explanation}`;
        }

        updateScore();
      });
    });
  }

  function updateScore() {
    let answered = Object.keys(userAnswers).length;
    let correctCount = 0;
    Object.keys(userAnswers).forEach(qid => {
      const q = QUIZ_DATA.find(x => x.id === parseInt(qid));
      if (q && userAnswers[qid] === q.correct) correctCount++;
    });

    if (scoreDisplay) {
      scoreDisplay.textContent = `Pontuação: ${correctCount} acertos de ${answered} respondidas (${Math.round((correctCount / (answered || 1)) * 100)}%)`;
    }
  }

  if (resetBtn) {
    resetBtn.addEventListener('click', renderQuiz);
  }

  renderQuiz();
}

/* ==========================================================================
   15. HD LIGHTBOX MODAL (COM ZOOM E ARRASTAR)
   ========================================================================== */
function initLightbox() {
  const modal = document.getElementById('lightbox-modal');
  const img = document.getElementById('lightbox-img');
  const caption = document.getElementById('lightbox-caption');
  const closeBtn = document.getElementById('lightbox-close');
  const zoomInBtn = document.getElementById('lightbox-zoom-in');
  const zoomOutBtn = document.getElementById('lightbox-zoom-out');
  const resetBtn = document.getElementById('lightbox-reset');

  if (!modal || !img) return;

  let scale = 1;
  let isDragging = false;
  let startX = 0, startY = 0, translateX = 0, translateY = 0;

  function updateTransform() {
    img.style.transform = `translate(${translateX}px, ${translateY}px) scale(${scale})`;
  }

  function openLightbox(src, alt) {
    img.src = src;
    caption.textContent = alt || "";
    scale = 1;
    translateX = 0;
    translateY = 0;
    updateTransform();
    modal.classList.remove('hidden');
    modal.classList.add('flex');
    document.body.style.overflow = 'hidden';
  }

  function closeLightbox() {
    modal.classList.add('hidden');
    modal.classList.remove('flex');
    document.body.style.overflow = '';
  }

  document.querySelectorAll('.zoomable-image').forEach(el => {
    el.addEventListener('click', () => {
      openLightbox(el.src, el.alt || el.getAttribute('title') || "");
    });
  });

  if (closeBtn) closeBtn.addEventListener('click', closeLightbox);
  modal.addEventListener('click', (e) => {
    if (e.target === modal) closeLightbox();
  });

  window.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && !modal.classList.contains('hidden')) {
      closeLightbox();
    }
  });

  if (zoomInBtn) {
    zoomInBtn.addEventListener('click', (e) => {
      e.stopPropagation();
      scale = Math.min(scale + 0.3, 3.5);
      updateTransform();
    });
  }

  if (zoomOutBtn) {
    zoomOutBtn.addEventListener('click', (e) => {
      e.stopPropagation();
      scale = Math.max(scale - 0.3, 0.7);
      updateTransform();
    });
  }

  if (resetBtn) {
    resetBtn.addEventListener('click', (e) => {
      e.stopPropagation();
      scale = 1;
      translateX = 0;
      translateY = 0;
      updateTransform();
    });
  }

  // Arrastar com mouse
  img.addEventListener('mousedown', (e) => {
    if (scale <= 1) return;
    isDragging = true;
    startX = e.clientX - translateX;
    startY = e.clientY - translateY;
    e.preventDefault();
  });

  window.addEventListener('mousemove', (e) => {
    if (!isDragging) return;
    translateX = e.clientX - startX;
    translateY = e.clientY - startY;
    updateTransform();
  });

  window.addEventListener('mouseup', () => {
    isDragging = false;
  });
}
