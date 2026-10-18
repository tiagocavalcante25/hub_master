/**
 * app.js - Motor Dinâmico do Dashboard Mestre Internato GO
 * Recursos: Gamificação (Passaporte do Aluno com persistência em localStorage),
 * Filtros de Trilha, Busca em Tempo Real, Desafio Clínico do Dia e Estatísticas.
 */

document.addEventListener('DOMContentLoaded', () => {
  if (window.lucide) {
    lucide.createIcons();
  }

  initTheme();
  initFontSize();
  initProgressTracker();
  initFilterTabs();
  initGlobalSearch();
  initDailyChallenge();
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
   3. GAMIFICAÇÃO & RASTREADOR DE PROGRESSO ("PASSAPORTE DO ALUNO")
   ========================================================================== */
const STORAGE_KEY_PROGRESS = 'internato_go_completed_portals';

function getCompletedPortals() {
  try {
    const saved = localStorage.getItem(STORAGE_KEY_PROGRESS);
    return saved ? JSON.parse(saved) : [];
  } catch (e) {
    return [];
  }
}

function saveCompletedPortals(list) {
  localStorage.setItem(STORAGE_KEY_PROGRESS, JSON.stringify(list));
}

function initProgressTracker() {
  let completed = getCompletedPortals();
  const checkboxes = document.querySelectorAll('.portal-check');
  const progressBar = document.getElementById('progress-bar-fill');
  const progressText = document.getElementById('progress-text');
  const progressBadge = document.getElementById('progress-rank-badge');
  const completedCountEl = document.getElementById('completed-count');

  const updateUI = () => {
    const total = 8;
    const current = completed.length;
    const pct = Math.round((current / total) * 100);

    if (progressBar) progressBar.style.width = `${pct}%`;
    if (progressText) progressText.innerText = `${pct}% Concluído (${current} de ${total} Portais)`;
    if (completedCountEl) completedCountEl.innerText = `${current} / ${total}`;

    // Níveis de Gamificação
    let rankText = "🔰 Interno Calouro";
    let rankColor = "bg-slate-100 text-slate-700 dark:bg-slate-800 dark:text-slate-300";

    if (pct >= 100) {
      rankText = "👑 Master em GO (Pronto para USMLE / Residência!)";
      rankColor = "bg-amber-100 text-amber-900 dark:bg-amber-950 dark:text-amber-300 border border-amber-300";
    } else if (pct >= 75) {
      rankText = "🏆 Fellow Ivy League";
      rankColor = "bg-purple-100 text-purple-900 dark:bg-purple-950 dark:text-purple-300";
    } else if (pct >= 50) {
      rankText = "⚡ Médico Residente R1";
      rankColor = "bg-indigo-100 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-300";
    } else if (pct >= 25) {
      rankText = "🩺 Interno Clínico";
      rankColor = "bg-sky-100 text-sky-900 dark:bg-sky-950 dark:text-sky-300";
    }

    if (progressBadge) {
      progressBadge.className = `px-3 py-1 rounded-full text-xs font-extrabold uppercase tracking-wider transition-all ${rankColor}`;
      progressBadge.innerText = rankText;
    }

    // Atualiza estado visual de cada card
    checkboxes.forEach(cb => {
      const portalId = cb.dataset.portalId;
      const isDone = completed.includes(portalId);
      cb.checked = isDone;

      const card = document.getElementById(`card-${portalId}`);
      const statusBadge = document.getElementById(`status-${portalId}`);

      if (card) {
        if (isDone) {
          card.classList.add('completed-portal');
        } else {
          card.classList.remove('completed-portal');
        }
      }

      if (statusBadge) {
        if (isDone) {
          statusBadge.innerHTML = `<span class="inline-flex items-center gap-1 text-emerald-600 dark:text-emerald-400 font-bold text-[11px]"><i data-lucide="check-circle" class="w-3.5 h-3.5"></i> Dominado</span>`;
        } else {
          statusBadge.innerHTML = `<span class="inline-flex items-center gap-1 text-slate-400 text-[11px]"><i data-lucide="circle" class="w-3.5 h-3.5"></i> Pendente</span>`;
        }
      }
    });

    if (window.lucide) lucide.createIcons();
  };

  checkboxes.forEach(cb => {
    cb.addEventListener('change', (e) => {
      const pid = e.target.dataset.portalId;
      if (e.target.checked) {
        if (!completed.includes(pid)) completed.push(pid);
      } else {
        completed = completed.filter(id => id !== pid);
      }
      saveCompletedPortals(completed);
      updateUI();
    });
  });

  // Botão Resetar Progresso
  const btnResetProgress = document.getElementById('btn-reset-progress');
  if (btnResetProgress) {
    btnResetProgress.addEventListener('click', () => {
      if (confirm("Deseja realmente reiniciar todo o progresso do seu passaporte?")) {
        completed = [];
        saveCompletedPortals(completed);
        updateUI();
      }
    });
  }

  // Executa atualização inicial
  updateUI();
}

/* ==========================================================================
   4. FILTROS POR TRILHA DE APRENDIZAGEM
   ========================================================================== */
function initFilterTabs() {
  const filterBtns = document.querySelectorAll('.filter-tab-btn');
  const cards = document.querySelectorAll('.portal-card');

  filterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      filterBtns.forEach(b => {
        b.classList.remove('bg-indigo-600', 'text-white', 'shadow-md');
        b.classList.add('bg-white', 'dark:bg-slate-800', 'text-slate-700', 'dark:text-slate-300');
      });

      btn.classList.remove('bg-white', 'dark:bg-slate-800', 'text-slate-700', 'dark:text-slate-300');
      btn.classList.add('bg-indigo-600', 'text-white', 'shadow-md');

      const filter = btn.dataset.filter;

      cards.forEach(card => {
        const categories = (card.dataset.categories || '').split(' ');
        if (filter === 'all' || categories.includes(filter)) {
          card.style.display = 'flex';
        } else {
          card.style.display = 'none';
        }
      });
    });
  });
}

/* ==========================================================================
   5. BUSCA GLOBAL EM TEMPO REAL
   ========================================================================== */
function initGlobalSearch() {
  const searchInput = document.getElementById('global-search');
  if (!searchInput) return;

  searchInput.addEventListener('input', (e) => {
    const term = e.target.value.toLowerCase().trim();
    const cards = document.querySelectorAll('.portal-card');
    let visibleCount = 0;

    cards.forEach(card => {
      const text = card.innerText.toLowerCase();
      if (!term || text.includes(term)) {
        card.style.display = 'flex';
        visibleCount++;
      } else {
        card.style.display = 'none';
      }
    });

    const noResults = document.getElementById('no-search-results');
    if (noResults) {
      noResults.style.display = visibleCount === 0 ? 'block' : 'none';
    }
  });

  // Atalho Ctrl+K ou Cmd+K
  window.addEventListener('keydown', (e) => {
    if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === 'k') {
      e.preventDefault();
      searchInput.focus();
    }
  });
}

/* ==========================================================================
   6. DESAFIO CLÍNICO DO DIA (ROLETA RÁPIDA DE CASOS)
   ========================================================================== */
const DESAFIOS_CLINICOS = [
  {
    pergunta: "Mulher de 26 anos com enxaqueca com aura solicita anticoncepção. Qual método é formalmente contraindicado (MEC 4)?",
    opcoes: [
      { texto: "DIU com Levonorgestrel", correta: false },
      { texto: "Anticoncepcional Oral Combinado (com estrogênio)", correta: true },
      { texto: "Implante subdérmico de etonogestrel", correta: false },
      { texto: "DIU de Cobre", correta: false }
    ],
    explicacao: "Estrogênios somados ao vasoespasmo cortical da aura aumentam drasticamente o risco de AVC isquêmico (MEC 4).",
    portalLink: "site_planejamento_violencia_sus/index.html",
    portalNome: "Portal 8: Planejamento Reprodutivo, Violência & SUS"
  },
  {
    pergunta: "Gestante de 32 semanas apresenta PA = 165/110 mmHg e proteinúria maciça. Qual o medicamento de escolha para prevenção de convulsões?",
    opcoes: [
      { texto: "Sulfato de Magnésio (Esquema de Pritchard ou Zuspan)", correta: true },
      { texto: "Diazepam intravenoso", correta: false },
      { texto: "Fenitoína", correta: false },
      { texto: "Hidralazina em monoterapia", correta: false }
    ],
    explicacao: "O Sulfato de Magnésio é o padrão-ouro mundial para profilaxia e tratamento das crises convulsivas da eclâmpsia.",
    portalLink: "site_urgencias_obstetricas/index.html",
    portalNome: "Portal 4: Urgências e Emergências Obstétricas"
  },
  {
    pergunta: "No trabalho de parto, a dilatação cervical estaciona em 6 cm por 2 horas com contrações eficientes e proporção cefalopélvica adequada. Qual a definição gráfica?",
    opcoes: [
      { texto: "Fase ativa prolongada", correta: false },
      { texto: "Parada secundária da dilatação", correta: true },
      { texto: "Parto precipitado", correta: false },
      { texto: "Período pélvico prolongado", correta: false }
    ],
    explicacao: "Parada secundária da dilatação ocorre quando não há progressão da dilatação cervical por 2 horas consecutivas na fase ativa.",
    portalLink: "site_parto_puerperio/index.html",
    portalNome: "Portal 3: Assistência ao Parto & Puerpério"
  },
  {
    pergunta: "Mulher de 24 anos apresenta corrimento acinzentado fétido com odor de peixe que piora após relação. Microscopia revela 'clue cells' e pH > 4,5. Qual o diagnóstico?",
    opcoes: [
      { texto: "Candidíase Vulvovaginal", correta: false },
      { texto: "Vaginose Bacteriana (Critérios de Amsel)", correta: true },
      { texto: "Tricomoníase", correta: false },
      { texto: "Cervicite por Chlamydia", correta: false }
    ],
    explicacao: "Presença de clue cells, pH > 4,5, teste das aminas positivo e corrimento homogêneo fecham o diagnóstico de Vaginose Bacteriana pelos critérios de Amsel.",
    portalLink: "site_infeccoes_ists/index.html",
    portalNome: "Portal 6: Infecções Ginecológicas & ISTs"
  },
  {
    pergunta: "Mamografia de rastreamento revela nódulo espiculado com microcalcificações pleomórficas agrupadas. Classificação BI-RADS 5. Qual a conduta?",
    opcoes: [
      { texto: "Repetir mamografia em 6 meses", correta: false },
      { texto: "Biópsia percutânea histológica mandatória (Core biopsy / Mamotomia)", correta: true },
      { texto: "Solicitar apenas ultrassonografia de rotina", correta: false },
      { texto: "Alta ambulatorial por 1 ano", correta: false }
    ],
    explicacao: "BI-RADS 5 possui probabilidade de malignidade superior a 95%, exigindo biópsia histológica imediata.",
    portalLink: "site_onco_masto_cirurgia/index.html",
    portalNome: "Portal 7: Oncologia Ginecológica, Mastologia e Cirurgia"
  }
];

let desafioAtualIdx = 0;

function initDailyChallenge() {
  const container = document.getElementById('daily-challenge-box');
  const btnNextChallenge = document.getElementById('btn-next-challenge');
  if (!container) return;

  const renderChallenge = () => {
    const item = DESAFIOS_CLINICOS[desafioAtualIdx];
    container.innerHTML = `
      <div class="space-y-3">
        <div class="flex items-center justify-between text-xs text-indigo-600 dark:text-indigo-400 font-bold uppercase tracking-wider">
          <span>Caso Clínico Rápido</span>
          <span class="text-slate-400 font-mono">${item.portalNome}</span>
        </div>
        <p class="text-xs sm:text-sm font-semibold text-slate-800 dark:text-slate-200 leading-relaxed">${item.pergunta}</p>

        <div class="space-y-1.5 pt-1">
          ${item.opcoes.map((opt, idx) => `
            <button type="button" class="challenge-opt-btn w-full text-left p-2.5 rounded-xl border border-slate-200 dark:border-slate-700 bg-white/70 dark:bg-slate-800/70 hover:bg-indigo-50 dark:hover:bg-indigo-950/30 text-xs text-slate-800 dark:text-slate-200 transition-all flex items-center gap-2"
              data-correct="${opt.correta}">
              <span class="w-5 h-5 rounded-full bg-slate-100 dark:bg-slate-700 flex items-center justify-center font-bold text-[10px] text-slate-600 dark:text-slate-300">${String.fromCharCode(65 + idx)}</span>
              <span class="flex-1">${opt.texto}</span>
            </button>
          `).join('')}
        </div>

        <div id="challenge-feedback" class="hidden p-3 rounded-xl border text-xs space-y-2 mt-2">
          <div id="challenge-status" class="font-bold"></div>
          <p id="challenge-expl" class="text-slate-700 dark:text-slate-300"></p>
          <a href="${item.portalLink}" class="inline-flex items-center gap-1.5 font-bold text-indigo-600 dark:text-indigo-400 hover:underline">
            Explorar este tema no ${item.portalNome} <i data-lucide="arrow-right" class="w-3.5 h-3.5"></i>
          </a>
        </div>
      </div>
    `;

    if (window.lucide) lucide.createIcons();

    // Handlers
    const buttons = container.querySelectorAll('.challenge-opt-btn');
    const feedbackBox = document.getElementById('challenge-feedback');
    const statusBox = document.getElementById('challenge-status');
    const explBox = document.getElementById('challenge-expl');

    buttons.forEach(btn => {
      btn.addEventListener('click', function() {
        const isCorrect = this.dataset.correct === 'true';
        buttons.forEach(b => {
          b.disabled = true;
          if (b.dataset.correct === 'true') {
            b.classList.add('border-emerald-500', 'bg-emerald-50', 'dark:bg-emerald-950/40', 'text-emerald-900', 'dark:text-emerald-200');
          } else if (b === this && !isCorrect) {
            b.classList.add('border-rose-500', 'bg-rose-50', 'dark:bg-rose-950/40', 'text-rose-900', 'dark:text-rose-200');
          }
        });

        feedbackBox.classList.remove('hidden');
        if (isCorrect) {
          feedbackBox.className = "p-3 rounded-xl border border-emerald-300 dark:border-emerald-800 bg-emerald-50 dark:bg-emerald-950/40 text-xs space-y-2 mt-2";
          statusBox.innerHTML = "✅ Resposta Exata! Excelente raciocínio clínico.";
        } else {
          feedbackBox.className = "p-3 rounded-xl border border-rose-300 dark:border-rose-800 bg-rose-50 dark:bg-rose-950/40 text-xs space-y-2 mt-2";
          statusBox.innerHTML = "❌ Resposta Incorreta. Revise o raciocínio abaixo:";
        }
        explBox.innerText = item.explicacao;

        if (window.lucide) lucide.createIcons();
      });
    });
  };

  if (btnNextChallenge) {
    btnNextChallenge.addEventListener('click', () => {
      desafioAtualIdx = (desafioAtualIdx + 1) % DESAFIOS_CLINICOS.length;
      renderChallenge();
    });
  }

  renderChallenge();
}
