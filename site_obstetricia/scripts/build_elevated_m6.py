# -*- coding: utf-8 -*-
"""
Builder for elevated, native Modulo 6 in site_obstetricia.
"""
import os

base_dir = r"c:\Users\Admin\Downloads\INTERNATO GO\hub_master\site_obstetricia"
comp_file = os.path.join(base_dir, "components", "modulo-6-ctg-doppler.html")

html_content = '''<!-- ==================== MÓDULO 6: MONITORAMENTO DO BEM-ESTAR FETAL, CTG & DOPPLER ==================== -->
<section id="modulo-6" class="glass-panel p-4 sm:p-8 rounded-3xl glow-card space-y-12">
  
  <!-- CABEÇALHO DO MÓDULO 06 -->
  <div class="flex flex-wrap items-center justify-between gap-4 border-b border-slate-200 dark:border-slate-800 pb-5">
    <div class="space-y-1">
      <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-teal-500/10 border border-teal-500/20 text-teal-600 dark:text-teal-400 text-xs font-black uppercase tracking-widest">
        <i class="fa-solid fa-heart-pulse"></i> Módulo 06 • Monitoramento do Bem-Estar Fetal
      </div>
      <h2 class="text-2xl sm:text-3xl lg:text-4xl font-black text-slate-900 dark:text-white tracking-tight">
        Vitalidade Fetal: Sofrimento Fetal Agudo e Crônico, CTG, PBF & Doppler
      </h2>
      <p class="text-xs sm:text-sm text-slate-600 dark:text-slate-300">
        Diretrizes Integradas: <strong>IDOMED (Prof. Phelipe Balbi)</strong> • <strong>FEBRASGO (Tratado 2019/2024)</strong> • <strong>Manual de Gestação de Alto Risco MS (2012/2022)</strong> • <strong>Zugaib / Rezende</strong> • <strong>Consenso Delphi 2016</strong> • <strong>Hospital Albert Einstein</strong>
      </p>
    </div>
    <div class="flex items-center gap-2">
      <button onclick="toggleAudioNarration('modulo-6-content')" class="audio-narrate-btn text-xs font-bold px-3.5 py-2 rounded-xl border border-slate-200 dark:border-slate-700 bg-white dark:bg-slate-800 hover:border-teal-500 flex items-center gap-2 transition-all shadow-sm">
        <i class="fa-solid fa-volume-high text-teal-500"></i> Ouvir Módulo 6
      </button>
    </div>
  </div>

  <div id="modulo-6-content" class="space-y-12">

    <!-- =========================================================================
         1. SOFRIMENTO FETAL AGUDO (SFA) - FISIOPATOLOGIA & ETIOLOGIAS COMPLETAS
         ========================================================================= -->
    <div class="space-y-4">
      <div class="flex items-center gap-3">
        <span class="w-8 h-8 rounded-xl bg-teal-600 text-white flex items-center justify-center font-black text-sm shadow-md">1</span>
        <div>
          <h3 class="text-lg sm:text-xl font-bold text-slate-900 dark:text-white">Sofrimento Fetal Agudo (SFA): Fisiopatologia & Etiologia Completa</h3>
          <p class="text-xs text-slate-500">Diminuição acentuada e súbita da oxigenação fetal, culminando em acidose metabólica e risco de asfixia</p>
        </div>
      </div>

      <!-- Alerta Fisiopatológico de Destaque -->
      <div class="p-4 sm:p-5 rounded-2xl bg-gradient-to-r from-teal-50 via-cyan-50 to-emerald-50 dark:from-slate-900 dark:via-slate-900/90 dark:to-teal-950/40 border border-teal-200 dark:border-teal-900 text-slate-800 dark:text-slate-200 text-xs sm:text-sm leading-relaxed space-y-2">
        <div class="flex items-center gap-2 font-bold text-teal-700 dark:text-teal-400">
          <i class="fa-solid fa-stethoscope"></i> Definição Primordial de Sofrimento Fetal Agudo (SFA)
        </div>
        <p>
          O <strong>Sofrimento Fetal Agudo (SFA)</strong> caracteriza-se pela <strong>diminuição acentuada da oxigenação fetal</strong> (hipoxemia $\rightarrow$ hipóxia tecidual), que obriga o feto a utilizar o metabolismo anaeróbico, resultando no acúmulo de ácido lático, queda do pH e <strong>acidose metabólica</strong>. Sem intervenção tempestiva, evolui para disfunção miocárdica, edema cerebral e óbito perinatal.
        </p>
      </div>

      <!-- Grid de 5 Grupos Etiológicos -->
      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4 text-xs">
        
        <!-- Etiologia 1: Hiperatividade Uterina -->
        <div class="p-4 rounded-2xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 shadow-sm space-y-2">
          <div class="flex items-center gap-2 font-bold text-rose-600 dark:text-rose-400 text-sm">
            <i class="fa-solid fa-bolt"></i> Hiperatividade Uterina
          </div>
          <p class="text-slate-600 dark:text-slate-400">Colapso dos vasos espiralados miometriais pelo aumento do tônus e frequência contrátil:</p>
          <ul class="space-y-1 list-disc list-inside text-slate-700 dark:text-slate-300">
            <li><strong>Administração excessiva de ocitócitos</strong> (taquissistolia iatrogênica por ocitocina ou misoprostol);</li>
            <li><strong>Desproporção Cefalopélvica (DCP)</strong> gerando contrações desordenadas e hipertonia miometrial;</li>
            <li><strong>Descolamento Prematuro de Placenta (DPP)</strong> com hipertonia uterina de base característica ("útero lenhoso");</li>
            <li><strong>Polidramnia</strong> com sobredistensão miometrial aguda;</li>
            <li><strong>Período expulsivo prolongado</strong> com esforço contínuo.</li>
          </ul>
        </div>

        <!-- Etiologia 2: Hipotensão Materna -->
        <div class="p-4 rounded-2xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 shadow-sm space-y-2">
          <div class="flex items-center gap-2 font-bold text-amber-600 dark:text-amber-400 text-sm">
            <i class="fa-solid fa-heart-crack"></i> Hipotensão Materna
          </div>
          <p class="text-slate-600 dark:text-slate-400">Redução crítica da pressão de perfusão no espaço interviloso placentário:</p>
          <ul class="space-y-1 list-disc list-inside text-slate-700 dark:text-slate-300">
            <li><strong>Anestesia de condução</strong> (raquianestesia/peridural por vasodilatação e bloqueio simpático pré-ganglionar);</li>
            <li><strong>Hemorragias obstétricas agudas</strong> (placenta prévia sangrante, rotura uterina, DPP);</li>
            <li><strong>Decúbito dorsal (Efeito Poseiro)</strong>: compressão do útero gravídico sobre a veia cava inferior e aorta. Reversão imediata com <strong>Decúbito Lateral Esquerdo (DLE)</strong>!</li>
          </ul>
        </div>

        <!-- Etiologia 3: Gestação de Alto Risco -->
        <div class="p-4 rounded-2xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 shadow-sm space-y-2">
          <div class="flex items-center gap-2 font-bold text-purple-600 dark:text-purple-400 text-sm">
            <i class="fa-solid fa-hospital-user"></i> Gestação de Alto Risco
          </div>
          <p class="text-slate-600 dark:text-slate-400">O estresse do trabalho de parto incide sobre uma reserva placentária já exaurida:</p>
          <ul class="space-y-1 list-disc list-inside text-slate-700 dark:text-slate-300">
            <li><strong>Agudização de uma insuficiência uteroplacentária crônica</strong>;</li>
            <li>Síndromes hipertensivas (Pré-Eclâmpsia / Eclâmpsia com endoteliose capilar);</li>
            <li>Diabetes com vasculopatia (Classes F, R, T de Priscilla White);</li>
            <li>Restrição de Crescimento Intrauterino (RCIU) prévio sem reserva funcional de glicogênio hepático.</li>
          </ul>
        </div>

        <!-- Etiologia 4: Acidentes com o Cordão Umbilical -->
        <div class="p-4 rounded-2xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 shadow-sm space-y-2">
          <div class="flex items-center gap-2 font-bold text-cyan-600 dark:text-cyan-400 text-sm">
            <i class="fa-solid fa-link-slash"></i> Acidentes de Cordão
          </div>
          <p class="text-slate-600 dark:text-slate-400">Interrupção mecânica direta do fluxo da veia e artérias umbilicais:</p>
          <ul class="space-y-1 list-disc list-inside text-slate-700 dark:text-slate-300">
            <li><strong>Prolapso de cordão umbilical</strong> (emergência obstétrica extrema após amniorrexe com apresentação desprendida);</li>
            <li><strong>Nó verdadeiro de cordão</strong> que se aperta durante a descida cefálica;</li>
            <li><strong>Compressão funicular por Oligodramnia ou RPMO</strong> (perda do coxim protetor da geleia de Wharton).</li>
          </ul>
        </div>

        <!-- Etiologia 5: Parto Prolongado & Exaustão -->
        <div class="p-4 rounded-2xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 shadow-sm space-y-2 sm:col-span-2 lg:col-span-2">
          <div class="flex items-center gap-2 font-bold text-teal-600 dark:text-teal-400 text-sm">
            <i class="fa-solid fa-clock"></i> Parto Prolongado & Falência de Progressão
          </div>
          <p class="text-slate-600 dark:text-slate-400">
            Trabalhos de parto com dilatação estacionária, parada secundária da descida ou período expulsivo superior a 2 horas (em multíparas) ou 3 horas (em nulíparas) levam a microtraumas cefálicos repetidos, edema de polo cefálico, desidratação e esgotamento do tamponamento fetal de bicarbonato, precipitando acidose fetal mesmo em concepto previamente saudável.
          </p>
        </div>

      </div>
    </div>

    <!-- =========================================================================
         2. MOBILOGRAMA (TESTE DE MOVIMENTAÇÃO FETAL) + SIMULADOR INTERATIVO
         ========================================================================= -->
    <div class="space-y-4">
      <div class="flex items-center gap-3">
        <span class="w-8 h-8 rounded-xl bg-teal-600 text-white flex items-center justify-center font-black text-sm shadow-md">2</span>
        <div>
          <h3 class="text-lg sm:text-xl font-bold text-slate-900 dark:text-white">Monitorização dos Movimentos Fetais: O Mobilograma Clínico</h3>
          <p class="text-xs text-slate-500">Método de rastreamento biofísico simples, domiciliar e de alta sensibilidade para vitalidade fetal</p>
        </div>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-xs">
        <div class="p-4 rounded-2xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 space-y-2">
          <h4 class="font-bold text-teal-700 dark:text-teal-300 uppercase tracking-wide flex items-center gap-2">
            <i class="fa-solid fa-calendar-check"></i> Cronologia & Protocolo do Mobilograma
          </h4>
          <ul class="space-y-1.5 list-disc list-inside text-slate-700 dark:text-slate-300 leading-relaxed">
            <li><strong>Início da percepção materna:</strong> 18 a 20 semanas em primigestas (16 a 18 semanas em multíparas).</li>
            <li><strong>Consolidação do padrão de sono/vigília:</strong> 26 a 32 semanas de gestação.</li>
            <li><strong>Protocolo Pós-Prandial (Teste de 1 hora):</strong> Gestante deitada em <strong>Decúbito Lateral Esquerdo (DLE)</strong> após as principais refeições. Espera-se de <strong>5 a 10 movimentos fetais em 1 hora</strong>. Se resultado inadequado: <em>estender a contagem por mais 1 hora</em>.</li>
            <li><strong>Protocolo de Atividades Habituais:</strong> Contagem ao longo do dia; considera-se <strong>ANORMAL menos de 10 movimentos em 12 horas</strong>.</li>
            <li><strong>Conduta diante de teste alterado:</strong> Encaminhamento IMEDIATO para realização de <strong>Cardiotocografia (CTG) basal</strong> ou <strong>Perfil Biofísico Fetal (PBF)</strong>!</li>
          </ul>
        </div>

        <!-- SIMULADOR INTERATIVO DO MOBILOGRAMA -->
        <div class="p-5 rounded-2xl bg-teal-50/70 dark:bg-slate-900/90 border border-teal-300 dark:border-teal-800 space-y-3">
          <div class="flex items-center justify-between">
            <span class="text-xs font-black uppercase text-teal-700 dark:text-teal-300 tracking-wider">
              <i class="fa-solid fa-calculator"></i> Simulador Interativo do Mobilograma
            </span>
            <span class="px-2 py-0.5 rounded text-[10px] font-bold bg-teal-200 dark:bg-teal-900 text-teal-900 dark:text-teal-100">Ferramenta Rápida</span>
          </div>
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-2">
            <div>
              <label class="block text-[11px] font-bold text-slate-700 dark:text-slate-300 mb-1">Método de Avaliação:</label>
              <select id="mobilograma-modo" class="w-full p-2 text-xs rounded-xl border border-slate-300 dark:border-slate-700 bg-white dark:bg-slate-800">
                <option value="pos_refeicao">Após refeição em DLE (1 a 2 horas)</option>
                <option value="12_horas">Atividades diárias usuais (12 horas)</option>
              </select>
            </div>
            <div>
              <label class="block text-[11px] font-bold text-slate-700 dark:text-slate-300 mb-1">Movimentos Contados:</label>
              <input type="number" id="mobilograma-movs" min="0" max="60" value="3" class="w-full p-2 text-xs rounded-xl border border-slate-300 dark:border-slate-700 bg-white dark:bg-slate-800">
            </div>
            <div id="mob-tempo-box" class="sm:col-span-2">
              <label class="block text-[11px] font-bold text-slate-700 dark:text-slate-300 mb-1">Tempo de Observação no Teste Pós-Refeição:</label>
              <select id="mobilograma-tempo" class="w-full p-2 text-xs rounded-xl border border-slate-300 dark:border-slate-700 bg-white dark:bg-slate-800">
                <option value="1">1 hora inicial</option>
                <option value="2">2 horas (estendido após 1ª hora insuficiente)</option>
              </select>
            </div>
          </div>
          <button onclick="avaliarMobilograma()" class="w-full py-2 px-4 rounded-xl bg-teal-600 hover:bg-teal-700 text-white font-bold text-xs transition-colors shadow">
            Analisar Movimentação Fetal & Conduta
          </button>
          <div id="mobilograma-resultado" class="hidden p-3 rounded-xl border text-xs"></div>
        </div>
      </div>
    </div>

    <!-- =========================================================================
         3. MICROANÁLISE DE SANGUE FETAL & TESTES DE MATURIDADE PULMONAR
         ========================================================================= -->
    <div class="space-y-4">
      <div class="flex items-center gap-3">
        <span class="w-8 h-8 rounded-xl bg-teal-600 text-white flex items-center justify-center font-black text-sm shadow-md">3</span>
        <div>
          <h3 class="text-lg sm:text-xl font-bold text-slate-900 dark:text-white">Microanálise de Sangue Fetal & Testes de Maturidade Pulmonar (L/E e Clements)</h3>
          <p class="text-xs text-slate-500">Manejo invasivo clássico de Saling, relação Lecitina/Esfingomielina e teste da estabilidade da espuma</p>
        </div>
      </div>

      <div class="grid grid-cols-1 lg:grid-cols-3 gap-4 text-xs">
        
        <!-- Microanálise de Sangue Fetal (Saling) -->
        <div class="p-4 rounded-2xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 space-y-2">
          <h4 class="font-bold text-slate-900 dark:text-white flex items-center gap-2">
            <i class="fa-solid fa-vial-virus text-rose-500"></i> Microanálise de Escalpe Fetal (Saling)
          </h4>
          <p class="text-slate-600 dark:text-slate-400">
            Considerada historicamente o padrão mais fidedigno para titulação direta da gasometria e pH fetal intraparto:
          </p>
          <div class="space-y-1.5 text-[11px]">
            <div class="p-2 rounded-xl bg-emerald-50 dark:bg-emerald-950/30 border border-emerald-200 dark:border-emerald-800 text-emerald-900 dark:text-emerald-300">
              <strong>pH &gt; 7,25:</strong> Padrão Fisiológico Normal (manter vigilância de parto).
            </div>
            <div class="p-2 rounded-xl bg-amber-50 dark:bg-amber-950/30 border border-amber-200 dark:border-amber-800 text-amber-900 dark:text-amber-300">
              <strong>pH 7,20 a 7,24:</strong> Estado Pré-Acidótico (repetir punção em 15–30 min).
            </div>
            <div class="p-2 rounded-xl bg-rose-50 dark:bg-rose-950/30 border border-rose-200 dark:border-rose-800 text-rose-900 dark:text-rose-300">
              <strong>pH &lt; 7,20:</strong> Acidose Metabólica Grave instalada (<strong>PARTO IMEDIATO</strong>).
            </div>
          </div>
          <p class="text-[10px] text-slate-400 pt-1">
            <em>Limitações:</em> Procedimento invasivo, exige amniorrexe, colo dilatado $\ge 2$ cm e amnioscópio com fonte de luz.
          </p>
        </div>

        <!-- Relação L/E e Teste de Clements -->
        <div class="p-4 rounded-2xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 space-y-2">
          <h4 class="font-bold text-slate-900 dark:text-white flex items-center gap-2">
            <i class="fa-solid fa-lungs text-teal-500"></i> Maturidade Pulmonar Fetal
          </h4>
          <div class="space-y-1.5 text-slate-700 dark:text-slate-300 text-[11px]">
            <strong class="text-teal-700 dark:text-teal-300 block">Relação Lecitina/Esfingomielina (L/E):</strong>
            <p>Avalia a concentração de surfactantes pulmonares no líquido amniótico:</p>
            <ul class="list-disc list-inside space-y-0.5">
              <li><strong class="text-rose-600">L/E &lt; 1,5:</strong> Imaturidade pulmonar evidente;</li>
              <li><strong class="text-amber-600">L/E 1,5 a 1,9:</strong> Imaturidade duvidosa;</li>
              <li><strong class="text-emerald-600">L/E &gt; 2,0:</strong> Maturidade pulmonar fetal estabelecida.</li>
            </ul>

            <strong class="text-teal-700 dark:text-teal-300 block mt-2">Teste de Clements (Teste da Espuma):</strong>
            <p>Pesquisa a maturidade pela tensão superficial do LA mediante estabilidade das bolhas em diluição alcoólica a 1/2:</p>
            <div class="p-2 rounded-lg bg-teal-50 dark:bg-teal-950/40 text-[10px] text-teal-900 dark:text-teal-200 font-mono">
              Técnica (Manual MS 2012): 0,5 mL LA + 0,5 mL SF 0,9% + 1 mL etanol 95% ➔ agitar vigorosamente 15 seg ➔ leitura aos 15 min.
            </div>
            <p><strong>Interpretação:</strong> Halo completo de bolhas estáveis na superfície = <em>Resultado Positivo (Maturidade Assegurada)</em>.</p>
          </div>
        </div>

        <!-- SIMULADOR INTERATIVO CLEMENTS & L/E -->
        <div class="p-4 rounded-2xl bg-slate-100/80 dark:bg-slate-800/60 border border-slate-300 dark:border-slate-700 space-y-3">
          <h4 class="font-bold text-slate-900 dark:text-white flex items-center gap-2 text-xs">
            <i class="fa-solid fa-flask text-cyan-500"></i> Calculadora de Maturidade Pulmonar
          </h4>
          <div class="space-y-2">
            <div>
              <label class="block text-[11px] font-bold text-slate-600 dark:text-slate-400 mb-1">Relação L/E no Líquido Amniótico:</label>
              <input type="number" step="0.1" id="le-valor" value="2.2" class="w-full p-2 text-xs rounded-xl border border-slate-300 dark:border-slate-700 bg-white dark:bg-slate-900">
            </div>
            <div>
              <label class="block text-[11px] font-bold text-slate-600 dark:text-slate-400 mb-1">Resultado do Teste de Clements:</label>
              <select id="clements-resultado" class="w-full p-2 text-xs rounded-xl border border-slate-300 dark:border-slate-700 bg-white dark:bg-slate-900">
                <option value="positivo">Positivo (Halo completo de bolhas estáveis)</option>
                <option value="duvidoso">Incompleto (Apenas bolhas esparsas)</option>
                <option value="negativo">Negativo (Nenhuma bolha após 15 min)</option>
              </select>
            </div>
            <button onclick="avaliarMaturidadePulmonar()" class="w-full py-2 px-3 rounded-xl bg-cyan-600 hover:bg-cyan-700 text-white font-bold text-xs transition-colors shadow">
              Interpretar Maturidade Fetal
            </button>
            <div id="maturidade-res" class="hidden p-3 rounded-xl border text-xs"></div>
          </div>
        </div>

      </div>
    </div>

    <!-- =========================================================================
         4. ELIMINAÇÃO DE MECÔNIO & AUSCULTA FETAL INTERMITENTE
         ========================================================================= -->
    <div class="space-y-4">
      <div class="flex items-center gap-3">
        <span class="w-8 h-8 rounded-xl bg-teal-600 text-white flex items-center justify-center font-black text-sm shadow-md">4</span>
        <div>
          <h3 class="text-lg sm:text-xl font-bold text-slate-900 dark:text-white">Eliminação de Mecônio & Ausculta Fetal Intermitente</h3>
          <p class="text-xs text-slate-500">Significado prognóstico do líquido meconial e protocolo cronometrado de ausculta no trabalho de parto</p>
        </div>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-xs">
        
        <!-- MECÔNIO -->
        <div class="p-5 rounded-2xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 space-y-3">
          <div class="flex items-center gap-2 text-amber-600 dark:text-amber-400 font-bold text-sm">
            <i class="fa-solid fa-biohazard"></i> Fisiopatologia da Eliminação de Mecônio
          </div>
          <ul class="space-y-2 text-slate-700 dark:text-slate-300">
            <li><strong>Preditor de Sofrimento Fetal Agudo e Asfixia:</strong> A hipóxia estimula o reflexo vagal, aumentando a peristalse intestinal e relaxando o esfíncter anal fetal.</li>
            <li><strong>Maturação do TGI a Termo:</strong> Em fetos $\ge 40$ semanas, pode representar simples maturação neurológica e parassimpática entérica sem asfixia associada.</li>
            <li><strong>Estimulação Vagal Mecânica:</strong> A compressão transitória de cordão umbilical ou polo cefálico induz descarga vagal com eliminação meconial reflexa.</li>
            <li><strong class="text-emerald-600 dark:text-emerald-400">Pérola de Prova:</strong> Em <strong>10% a 20% dos partos com mecônio</strong>, NÃO há complicação fetal! Contudo, líquido espesso ("purê de ervilha" - Grau III de Storch) impõe monitorização contínua com CTG.</li>
            <li><strong>Manejo do RN:</strong> Se o RN nascer vigoroso (bom tônus e respiração espontânea), manter junto à mãe; a intubação com aspiração traqueal direta só é indicada se o concepto nascer <em>deprimido</em> (Diretrizes SBP/ILCOR).</li>
          </ul>
        </div>

        <!-- AUSCULTA INTERMITENTE -->
        <div class="p-5 rounded-2xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 space-y-3">
          <div class="flex items-center gap-2 text-teal-600 dark:text-teal-400 font-bold text-sm">
            <i class="fa-solid fa-ear-listen"></i> Protocolo de Ausculta Fetal Intermitente (Sonar / Pinard)
          </div>
          <div class="overflow-x-auto">
            <table class="w-full text-[11px] text-left border-collapse">
              <thead>
                <tr class="border-b border-slate-200 dark:border-slate-800 text-slate-500">
                  <th class="py-1.5 font-bold">Fase do Parto</th>
                  <th class="py-1.5 font-bold text-emerald-600">Baixo Risco</th>
                  <th class="py-1.5 font-bold text-rose-600">Alto Risco</th>
                </tr>
              </thead>
              <tbody class="divide-y divide-slate-100 dark:divide-slate-800 text-slate-700 dark:text-slate-300">
                <tr>
                  <td class="py-1.5 font-semibold">Fase Latente</td>
                  <td class="py-1.5" colspan="2">A cada 1 hora</td>
                </tr>
                <tr>
                  <td class="py-1.5 font-semibold">Fase Ativa (Dilatação)</td>
                  <td class="py-1.5 font-bold text-emerald-600">A cada 30 minutos</td>
                  <td class="py-1.5 font-bold text-rose-600">A cada 15 minutos</td>
                </tr>
                <tr>
                  <td class="py-1.5 font-semibold">Período Expulsivo</td>
                  <td class="py-1.5 font-bold text-emerald-600">A cada 15 minutos</td>
                  <td class="py-1.5 font-bold text-rose-600">A cada 5 minutos</td>
                </tr>
              </tbody>
            </table>
          </div>
          <div class="p-2.5 rounded-xl bg-amber-50 dark:bg-amber-950/30 border border-amber-200 dark:border-amber-900 text-[11px] space-y-1 text-slate-800 dark:text-slate-200">
            <p><strong>Como Auscultar:</strong> Deve ser iniciada <em>durante a contração uterina</em> e persistir por <strong>pelo menos 30 segundos</strong> após o seu término (para detectar desacelerações tardias/DIP II).</p>
            <p><strong class="text-rose-600 dark:text-rose-400">Definição de SFA na Ausculta:</strong> Bradicardia persistente (&lt; 110 bpm) por pelo menos <strong>50% da duração</strong> de, no mínimo, <strong>três contrações consecutivas</strong>.</p>
          </div>
        </div>

      </div>
    </div>

    <!-- =========================================================================
         5. CARDIOTOCOGRAFIA (CTG) - OS 4 PARÂMETROS & ONDAS SVG DOS DIPs
         ========================================================================= -->
    <div class="space-y-6">
      <div class="flex items-center gap-3">
        <span class="w-8 h-8 rounded-xl bg-teal-600 text-white flex items-center justify-center font-black text-sm shadow-md">5</span>
        <div>
          <h3 class="text-lg sm:text-xl font-bold text-slate-900 dark:text-white">Cardiotocografia (CTG): Os 4 Parâmetros, Categorização & Ondas de Desaceleração</h3>
          <p class="text-xs text-slate-500">Registro simultâneo da FCF e da tocodinamometria uterina por 20 minutos com análise do sistema nervoso autônomo fetal</p>
        </div>
      </div>

      <!-- Condições do Exame e 4 Parâmetros Vitais -->
      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 text-xs">
        
        <!-- FCF Basal -->
        <div class="p-4 rounded-2xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 space-y-1.5 shadow-sm">
          <span class="text-[10px] font-black uppercase text-teal-600 tracking-wider">Parâmetro 1</span>
          <h4 class="font-bold text-slate-900 dark:text-white text-sm">FCF Linha de Base</h4>
          <p class="text-slate-500 text-[11px]">Média da FCF determinada em janela de 10 minutos estáveis:</p>
          <div class="p-2 rounded-xl bg-slate-50 dark:bg-slate-800 space-y-1">
            <div class="flex justify-between font-bold text-emerald-600"><span>Normal:</span><span>110 a 160 bpm</span></div>
            <div class="flex justify-between text-rose-600 font-semibold"><span>Bradicardia:</span><span>&lt; 110 bpm</span></div>
            <div class="flex justify-between text-amber-600 font-semibold"><span>Taquicardia:</span><span>&gt; 160 bpm</span></div>
          </div>
          <span class="text-[10px] text-slate-400 block italic">Taquicardia sustentada: febre materna, corioamnionite, atropina ou hipóxia inicial compensada.</span>
        </div>

        <!-- Variabilidade -->
        <div class="p-4 rounded-2xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 space-y-1.5 shadow-sm">
          <span class="text-[10px] font-black uppercase text-teal-600 tracking-wider">Parâmetro 2</span>
          <h4 class="font-bold text-slate-900 dark:text-white text-sm">Variabilidade da FCF</h4>
          <p class="text-slate-500 text-[11px]">Oscilações batimento a batimento (equilíbrio simpático-vagal):</p>
          <div class="p-2 rounded-xl bg-slate-50 dark:bg-slate-800 space-y-0.5 text-[11px]">
            <p><strong>Ausente:</strong> amplitude não detectada (0 bpm)</p>
            <p><strong>Mínima:</strong> amplitude $\le$ 5 bpm (sono/sedação/hipóxia)</p>
            <p class="text-emerald-600 font-bold"><strong>Moderada (Normal):</strong> amplitude 6 a 25 bpm</p>
            <p><strong>Acentuada (Saltatória):</strong> amplitude &gt; 25 bpm</p>
            <p class="text-rose-600 font-extrabold pt-1 border-t border-slate-200 dark:border-slate-700">
              🚨 <strong>Sinusoidal:</strong> Ondas em sino 2-5 ciclos/min, amplitude 5-15 bpm por 15-30s = <strong>ANEMIA FETAL GRAVE</strong>!
            </p>
          </div>
        </div>

        <!-- Acelerações Transitórias -->
        <div class="p-4 rounded-2xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 space-y-1.5 shadow-sm">
          <span class="text-[10px] font-black uppercase text-teal-600 tracking-wider">Parâmetro 3</span>
          <h4 class="font-bold text-slate-900 dark:text-white text-sm">Acelerações Transitórias</h4>
          <p class="text-slate-500 text-[11px]">Ascensões abruptas acima da linha de base:</p>
          <div class="p-2.5 rounded-xl bg-emerald-50 dark:bg-emerald-950/30 border border-emerald-200 dark:border-emerald-900 text-emerald-900 dark:text-emerald-200 text-[11px] space-y-1">
            <p class="font-bold">Critério de Feto Reativo ($\ge 32$ semanas):</p>
            <p>$\ge 2$ acelerações associadas a movimentos com amplitude $\ge 15$ bpm e duração $\ge 15$ segundos em 20 minutos de traçado.</p>
            <p class="text-[10px] text-emerald-700 dark:text-emerald-300">Em fetos &lt; 32 semanas: $\ge 2$ acelerações de $\ge 10$ bpm por $\ge 10$ segundos em 20-40 min.</p>
          </div>
        </div>

        <!-- Desacelerações -->
        <div class="p-4 rounded-2xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 space-y-1.5 shadow-sm">
          <span class="text-[10px] font-black uppercase text-teal-600 tracking-wider">Parâmetro 4</span>
          <h4 class="font-bold text-slate-900 dark:text-white text-sm">Padrões de Desaceleração</h4>
          <p class="text-slate-500 text-[11px]">Quedas transitórias abaixo da linha de base:</p>
          <div class="p-2 rounded-xl bg-slate-50 dark:bg-slate-800 space-y-1 text-[11px]">
            <p><strong>DIP I (Cefálico):</strong> Formato em V, espelho da contração (Vagal). Fisiológico.</p>
            <p><strong>DIP II (Tardio):</strong> Formato em U, nadir após o pico (Asfixia placentária). Patológico!</p>
            <p><strong>DIP III (Variável):</strong> Umbilical. Favorável se tiver "ombros"; desfavorável se queda &gt; 60 bpm ou formato em W.</p>
          </div>
        </div>

      </div>

      <!-- PAINEL COMPARATIVO DAS 3 DESACELERAÇÕES COM TRAÇADOS VETORIAIS NATIVOS EM SVG -->
      <div class="grid grid-cols-1 md:grid-cols-3 gap-5 text-xs">
        
        <!-- CARD DIP I COM SVG NATIVO -->
        <div class="p-4 rounded-3xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 space-y-3 shadow-md">
          <div class="flex items-center justify-between">
            <span class="px-2.5 py-0.5 rounded-full text-[10px] font-black bg-emerald-100 text-emerald-800 dark:bg-emerald-950 dark:text-emerald-300 border border-emerald-300">Fisiológico</span>
            <span class="font-bold text-slate-700 dark:text-slate-300">DIP Tipo I</span>
          </div>
          <h4 class="font-bold text-sm text-slate-900 dark:text-white">Desaceleração Precoce / Cefálica</h4>
          
          <!-- SVG Vetorial Nativo DIP I -->
          <div class="rounded-2xl overflow-hidden border border-slate-200 dark:border-slate-800 bg-slate-950 p-2 shadow-inner">
            <svg viewBox="0 0 500 200" class="w-full h-auto select-none" xmlns="http://www.w3.org/2000/svg">
              <defs>
                <pattern id="gridDIP1" width="25" height="20" patternUnits="userSpaceOnUse">
                  <path d="M 25 0 L 0 0 0 20" fill="none" stroke="#334155" stroke-width="0.5" stroke-opacity="0.4"/>
                </pattern>
              </defs>
              <rect width="500" height="200" fill="#0b1120"/>
              <rect width="500" height="200" fill="url(#gridDIP1)"/>
              
              <!-- FCF Labels -->
              <text x="12" y="24" fill="#10b981" font-size="10" font-family="monospace" font-weight="bold">FCF (bpm)</text>
              <text x="460" y="45" fill="#64748b" font-size="9" font-family="monospace">160</text>
              <text x="460" y="65" fill="#10b981" font-size="9" font-family="monospace" font-weight="bold">140 (Basal)</text>
              <text x="460" y="85" fill="#64748b" font-size="9" font-family="monospace">120</text>
              <text x="460" y="105" fill="#f43f5e" font-size="9" font-family="monospace">100</text>
              <line x1="10" y1="65" x2="450" y2="65" stroke="#10b981" stroke-width="1" stroke-dasharray="3,3" stroke-opacity="0.4"/>
              
              <!-- Curva FCF DIP I: Síncrona -->
              <path d="M 20,64 Q 50,66 80,64 T 140,65 C 165,65 190,75 220,95 C 235,105 245,105 250,105 C 255,105 265,105 280,95 C 310,75 335,65 360,65 T 420,64" 
                    fill="none" stroke="#10b981" stroke-width="2.5" stroke-linecap="round"/>
              
              <!-- TOCO Channel -->
              <line x1="10" y1="130" x2="490" y2="130" stroke="#1e293b" stroke-width="1"/>
              <text x="12" y="146" fill="#38bdf8" font-size="10" font-family="monospace" font-weight="bold">TOCO (mmHg)</text>
              <text x="460" y="162" fill="#38bdf8" font-size="9" font-family="monospace">60 (Acme)</text>
              <text x="460" y="190" fill="#64748b" font-size="9" font-family="monospace">10 (Tônus)</text>
              
              <!-- Contração síncrona com pico em x=250 -->
              <path d="M 20,190 L 140,190 C 180,190 215,160 250,160 C 285,160 320,190 360,190 L 420,190" 
                    fill="none" stroke="#38bdf8" stroke-width="2.5" stroke-linecap="round"/>
              
              <!-- Síncronismo Nadir = Acme -->
              <line x1="250" y1="105" x2="250" y2="160" stroke="#fbbf24" stroke-width="1.5" stroke-dasharray="3,2"/>
              <circle cx="250" cy="105" r="3.5" fill="#fbbf24"/>
              <circle cx="250" cy="160" r="3.5" fill="#fbbf24"/>
              <rect x="180" y="112" width="140" height="18" rx="4" fill="#0f172a" stroke="#fbbf24" stroke-width="1"/>
              <text x="250" y="124" fill="#fbbf24" font-size="9" font-family="sans-serif" font-weight="bold" text-anchor="middle">Nadir = Acme (Síncrono)</text>
            </svg>
          </div>

          <ul class="space-y-1 text-slate-600 dark:text-slate-300 text-[11px] list-disc list-inside">
            <li><strong>Morfologia:</strong> Formato gradual em "U" ou "V" simétrico.</li>
            <li><strong>Sincronia:</strong> Início, nadir e fim ocorrem <strong>em espelho com a contração uterina</strong>.</li>
            <li><strong>Causa:</strong> Compressão mecânica do polo cefálico no trajeto de parto com reflexo vagal transitório.</li>
            <li><strong>Conduta:</strong> <strong>Conservadora / Expectante</strong>. Não traduz hipóxia nem indica cesárea!</li>
          </ul>
        </div>

        <!-- CARD DIP II COM SVG NATIVO -->
        <div class="p-4 rounded-3xl bg-white dark:bg-slate-900 border border-rose-300 dark:border-rose-900 space-y-3 shadow-md">
          <div class="flex items-center justify-between">
            <span class="px-2.5 py-0.5 rounded-full text-[10px] font-black bg-rose-100 text-rose-800 dark:bg-rose-950 dark:text-rose-300 border border-rose-300">Grave / Patológico</span>
            <span class="font-bold text-rose-600">DIP Tipo II</span>
          </div>
          <h4 class="font-bold text-sm text-slate-900 dark:text-white">Desaceleração Tardia / Placentária</h4>
          
          <!-- SVG Vetorial Nativo DIP II -->
          <div class="rounded-2xl overflow-hidden border border-slate-200 dark:border-slate-800 bg-slate-950 p-2 shadow-inner">
            <svg viewBox="0 0 500 200" class="w-full h-auto select-none" xmlns="http://www.w3.org/2000/svg">
              <defs>
                <pattern id="gridDIP2" width="25" height="20" patternUnits="userSpaceOnUse">
                  <path d="M 25 0 L 0 0 0 20" fill="none" stroke="#334155" stroke-width="0.5" stroke-opacity="0.4"/>
                </pattern>
              </defs>
              <rect width="500" height="200" fill="#0b1120"/>
              <rect width="500" height="200" fill="url(#gridDIP2)"/>
              
              <!-- FCF Labels -->
              <text x="12" y="24" fill="#f43f5e" font-size="10" font-family="monospace" font-weight="bold">FCF (bpm)</text>
              <text x="460" y="45" fill="#64748b" font-size="9" font-family="monospace">160</text>
              <text x="460" y="65" fill="#94a3b8" font-size="9" font-family="monospace" font-weight="bold">140</text>
              <text x="460" y="85" fill="#64748b" font-size="9" font-family="monospace">120</text>
              <text x="460" y="105" fill="#f43f5e" font-size="9" font-family="monospace">100</text>
              <line x1="10" y1="65" x2="450" y2="65" stroke="#64748b" stroke-width="1" stroke-dasharray="3,3" stroke-opacity="0.4"/>
              
              <!-- DIP II Curve: Starts late after contraction peak -->
              <path d="M 20,65 L 180,65 C 205,65 225,72 250,88 C 270,102 285,108 295,108 C 305,108 325,100 350,82 C 375,68 395,65 415,65 L 430,65" 
                    fill="none" stroke="#f43f5e" stroke-width="2.5" stroke-linecap="round"/>
              
              <!-- Contraction Channel -->
              <line x1="10" y1="130" x2="490" y2="130" stroke="#1e293b" stroke-width="1"/>
              <text x="12" y="146" fill="#38bdf8" font-size="10" font-family="monospace" font-weight="bold">TOCO (mmHg)</text>
              <text x="460" y="162" fill="#38bdf8" font-size="9" font-family="monospace">60 (Pico)</text>
              <text x="460" y="190" fill="#64748b" font-size="9" font-family="monospace">10 (Tônus)</text>
              
              <!-- Contraction: peaks at x=200 -->
              <path d="M 20,190 L 120,190 C 150,190 175,160 200,160 C 225,160 250,190 280,190 L 430,190" 
                    fill="none" stroke="#38bdf8" stroke-width="2.5" stroke-linecap="round"/>
              
              <!-- Decalagem / Lag Time indicator -->
              <line x1="200" y1="65" x2="200" y2="160" stroke="#38bdf8" stroke-width="1" stroke-dasharray="2,2"/>
              <circle cx="200" cy="160" r="3.5" fill="#38bdf8"/>
              
              <line x1="295" y1="65" x2="295" y2="190" stroke="#f43f5e" stroke-width="1" stroke-dasharray="2,2"/>
              <circle cx="295" cy="108" r="3.5" fill="#f43f5e"/>
              
              <!-- Lag time arrow between 200 and 295 -->
              <line x1="200" y1="45" x2="295" y2="45" stroke="#fbbf24" stroke-width="1.5"/>
              <polygon points="200,45 206,42 206,48" fill="#fbbf24"/>
              <polygon points="295,45 289,42 289,48" fill="#fbbf24"/>
              
              <rect x="200" y="24" width="125" height="18" rx="4" fill="#0f172a" stroke="#fbbf24" stroke-width="1"/>
              <text x="262" y="36" fill="#fbbf24" font-size="9" font-family="sans-serif" font-weight="bold" text-anchor="middle">Decalagem &gt; 20-30s</text>
            </svg>
          </div>

          <ul class="space-y-1 text-slate-600 dark:text-slate-300 text-[11px] list-disc list-inside">
            <li><strong>Morfologia:</strong> Desaceleração gradual e arredondada em "U".</li>
            <li><strong>Sincronia:</strong> Início e nadir atrasados com relação ao acme da contração (<strong>decalagem &gt; 20 segundos</strong>).</li>
            <li><strong>Causa:</strong> <strong>Insuficiência uteroplacentária</strong> gerando hipóxia tecidual e acúmulo de ácido lático.</li>
            <li><strong>Conduta:</strong> Ressuscitação intrauterina (DLE, O2, hidratação, suspender ocitocina); se persistente = <strong>Cesariana de emergência</strong>!</li>
          </ul>
        </div>

        <!-- CARD DIP III COM SVG NATIVO -->
        <div class="p-4 rounded-3xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 space-y-3 shadow-md">
          <div class="flex items-center justify-between">
            <span class="px-2.5 py-0.5 rounded-full text-[10px] font-black bg-cyan-100 text-cyan-800 dark:bg-cyan-950 dark:text-cyan-300 border border-cyan-300">Cordão Umbilical</span>
            <span class="font-bold text-cyan-600">DIP Tipo III</span>
          </div>
          <h4 class="font-bold text-sm text-slate-900 dark:text-white">Desaceleração Variável / Umbilical</h4>
          
          <!-- SVG Vetorial Nativo DIP III -->
          <div class="rounded-2xl overflow-hidden border border-slate-200 dark:border-slate-800 bg-slate-950 p-2 shadow-inner">
            <svg viewBox="0 0 500 200" class="w-full h-auto select-none" xmlns="http://www.w3.org/2000/svg">
              <defs>
                <pattern id="gridDIP3" width="25" height="20" patternUnits="userSpaceOnUse">
                  <path d="M 25 0 L 0 0 0 20" fill="none" stroke="#334155" stroke-width="0.5" stroke-opacity="0.4"/>
                </pattern>
              </defs>
              <rect width="500" height="200" fill="#0b1120"/>
              <rect width="500" height="200" fill="url(#gridDIP3)"/>
              
              <!-- FCF Labels -->
              <text x="12" y="24" fill="#06b6d4" font-size="10" font-family="monospace" font-weight="bold">FCF (bpm)</text>
              <text x="460" y="45" fill="#64748b" font-size="9" font-family="monospace">160</text>
              <text x="460" y="65" fill="#94a3b8" font-size="9" font-family="monospace" font-weight="bold">140</text>
              <text x="460" y="85" fill="#64748b" font-size="9" font-family="monospace">120</text>
              <text x="460" y="105" fill="#64748b" font-size="9" font-family="monospace">100</text>
              <text x="460" y="125" fill="#f43f5e" font-size="9" font-family="monospace">70</text>
              <line x1="10" y1="65" x2="450" y2="65" stroke="#64748b" stroke-width="1" stroke-dasharray="3,3" stroke-opacity="0.4"/>
              
              <!-- DIP III Curve: Initial shoulder, steep plunge, W shape, recovery shoulder -->
              <path d="M 20,65 L 160,65 Q 175,50 185,50 Q 195,55 200,80 L 215,120 Q 225,122 232,95 Q 240,92 248,120 Q 258,122 268,75 Q 278,50 288,50 Q 298,55 308,65 L 430,65" 
                    fill="none" stroke="#06b6d4" stroke-width="2.5" stroke-linecap="round"/>
              
              <!-- Contraction Channel -->
              <line x1="10" y1="130" x2="490" y2="130" stroke="#1e293b" stroke-width="1"/>
              <text x="12" y="146" fill="#38bdf8" font-size="10" font-family="monospace" font-weight="bold">TOCO (mmHg)</text>
              <path d="M 20,190 L 130,190 C 170,190 210,160 250,160 C 290,160 330,190 370,190 L 430,190" 
                    fill="none" stroke="#38bdf8" stroke-width="2.5" stroke-linecap="round"/>
              
              <!-- Callout tags -->
              <rect x="150" y="15" width="85" height="16" rx="4" fill="#083344" stroke="#06b6d4" stroke-width="1"/>
              <text x="192" y="26" fill="#06b6d4" font-size="8" font-family="sans-serif" font-weight="bold" text-anchor="middle">Ombro Inicial</text>
              
              <rect x="195" y="125" width="105" height="16" rx="4" fill="#4c0519" stroke="#f43f5e" stroke-width="1"/>
              <text x="247" y="136" fill="#f43f5e" font-size="8" font-family="sans-serif" font-weight="bold" text-anchor="middle">Queda &lt; 30s / Forma W</text>
            </svg>
          </div>

          <ul class="space-y-1 text-slate-600 dark:text-slate-300 text-[11px]">
            <li><strong>Morfologia:</strong> Queda abrupta sem relação temporal fixa com as contrações.</li>
            <li><strong class="text-emerald-600">Favorável:</strong> Aceleração transitória antes e depois ("ombros" ou <em>shoulders</em> preservados).</li>
            <li><strong class="text-rose-600">Desfavorável (Critérios de Kubli):</strong> Queda &gt; 60 bpm (ou FCF &lt; 60 bpm); duração &gt; 60 segundos; perda dos ombros; ou <strong>desaceleração bifásica dupla (formato em "W")</strong>!</li>
            <li><strong>Conduta:</strong> Mudar para DLE, ofertar hidratação IV e oxigenioterapia materna; se persistir desfavorável = Cesariana.</li>
          </ul>
        </div>

      </div>

      <!-- QUADRO 47 DO MANUAL TÉCNICO DE ALTO RISCO (MS 2012) -->
      <div class="p-5 rounded-3xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 shadow-sm space-y-3">
        <div class="flex items-center justify-between border-b border-slate-200 dark:border-slate-800 pb-2">
          <h4 class="font-bold text-sm text-slate-900 dark:text-white flex items-center gap-2">
            <i class="fa-solid fa-table-list text-teal-500"></i> Quadro 47: Interpretação e Conduta na Cardiotocografia de Repouso (MS 2012)
          </h4>
          <span class="text-[10px] font-mono text-slate-400">Manual Técnico de Alto Risco / Ministério da Saúde</span>
        </div>

        <div class="overflow-x-auto">
          <table class="w-full text-left text-xs border-collapse">
            <thead>
              <tr class="bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-300">
                <th class="p-2.5 font-bold border-b border-slate-200 dark:border-slate-700">Parâmetro</th>
                <th class="p-2.5 font-bold text-emerald-700 dark:text-emerald-400 border-b border-slate-200 dark:border-slate-700">Padrões Normais / Tranquilizadores</th>
                <th class="p-2.5 font-bold text-amber-700 dark:text-amber-400 border-b border-slate-200 dark:border-slate-700">Padrões Suspeitos / Não Tranquilizadores</th>
                <th class="p-2.5 font-bold text-rose-700 dark:text-rose-400 border-b border-slate-200 dark:border-slate-700">Padrões Patológicos</th>
              </tr>
            </thead>
            <tbody class="divide-y divide-slate-100 dark:divide-slate-800 text-[11px] text-slate-700 dark:text-slate-300">
              <tr>
                <td class="p-2 font-bold text-slate-900 dark:text-white">FCF Basal</td>
                <td class="p-2">110 a 160 bpm</td>
                <td class="p-2">100–110 bpm; &gt; 160 bpm por &lt; 30 min; ou elevação da linha de base</td>
                <td class="p-2 font-semibold text-rose-600">Bradicardia &lt; 100 bpm; Taquicardia &gt; 160 bpm por &gt; 30 min; ou linha de base errática</td>
              </tr>
              <tr>
                <td class="p-2 font-bold text-slate-900 dark:text-white">Variabilidade</td>
                <td class="p-2">6–25 bpm (moderada) ou $\le$ 5 bpm por &lt; 40 min</td>
                <td class="p-2">$\le$ 5 bpm (ausente ou mínima) por 40 a 80 minutos</td>
                <td class="p-2 font-semibold text-rose-600">$\le$ 5 bpm por &gt; 80 min; $\ge$ 25 bpm por &gt; 10 min; ou Padrão Sinusoidal</td>
              </tr>
              <tr>
                <td class="p-2 font-bold text-slate-900 dark:text-white">Desacelerações</td>
                <td class="p-2">Ausência ou desaceleração variável ocasional &lt; 30 seg</td>
                <td class="p-2">Desaceleração variável de 30 a 60 segundos</td>
                <td class="p-2 font-semibold text-rose-600">Desacelerações variáveis &gt; 60 seg ou Desacelerações tardias (DIP II) recorrentes</td>
              </tr>
              <tr>
                <td class="p-2 font-bold text-slate-900 dark:text-white">Acelerações ($\ge 32$ semanas)</td>
                <td class="p-2">$\ge 2$ com $\ge 15$ bpm por 15s em &lt; 40 min (ou resposta ao estímulo sonoro aos 20 min)</td>
                <td class="p-2">$\le 2$ acelerações de 15 bpm por 15s de 40 a 80 minutos</td>
                <td class="p-2 font-semibold text-rose-600">$\le 2$ acelerações de 15 bpm por 15s por mais de 80 minutos</td>
              </tr>
              <tr>
                <td class="p-2 font-bold text-slate-900 dark:text-white">Acelerações (&lt; 32 semanas)</td>
                <td class="p-2">$\ge 2$ com $\ge 10$ bpm por 10s em &lt; 40 min</td>
                <td class="p-2">$\le 2$ acelerações de 10 bpm por 10s de 40 a 80 minutos</td>
                <td class="p-2 font-semibold text-rose-600">$\le 2$ acelerações de 10 bpm por 10s por mais de 80 minutos</td>
              </tr>
              <tr class="bg-slate-50 dark:bg-slate-800/50 font-bold">
                <td class="p-2.5 text-slate-900 dark:text-white">CONDUTA OFICIAL</td>
                <td class="p-2.5 text-emerald-700 dark:text-emerald-400">Não há necessidade de avaliação adicional (seguir rotina clínica).</td>
                <td class="p-2.5 text-amber-700 dark:text-amber-400">Avaliação adicional necessária (PBF, Doppler) ou repetição em 12h.</td>
                <td class="p-2.5 text-rose-700 dark:text-rose-400">Avaliação adicional urgente ou PARTO IMEDIATO, conforme quadro clínico.</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <!-- CATEGORIAS I, II E III DA CTG (NICHD / ACOG / FIGO) -->
      <div class="grid grid-cols-1 md:grid-cols-3 gap-4 text-xs">
        <div class="p-4 rounded-2xl bg-emerald-50 dark:bg-emerald-950/30 border border-emerald-300 dark:border-emerald-800 space-y-2">
          <div class="flex items-center justify-between">
            <span class="font-bold text-emerald-800 dark:text-emerald-200 text-sm">Categoria I</span>
            <span class="px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-200 text-emerald-900 dark:bg-emerald-900 dark:text-emerald-100">Normal</span>
          </div>
          <p class="text-emerald-900 dark:text-emerald-300 font-semibold">Exige TODOS os parâmetros a seguir:</p>
          <ul class="space-y-1 list-disc list-inside text-slate-700 dark:text-slate-300 text-[11px]">
            <li>Linha de base entre 110 e 160 bpm;</li>
            <li>Variabilidade moderada (6 a 25 bpm);</li>
            <li>Ausência de desacelerações tardias ou variáveis;</li>
            <li>Desaceleração precoce presente ou ausente;</li>
            <li>Acelerações presentes ou ausentes.</li>
          </ul>
          <p class="text-[10px] text-emerald-800 dark:text-emerald-300 font-bold">Conduta: Seguimento de rotina habitual.</p>
        </div>

        <div class="p-4 rounded-2xl bg-amber-50 dark:bg-amber-950/30 border border-amber-300 dark:border-amber-800 space-y-2">
          <div class="flex items-center justify-between">
            <span class="font-bold text-amber-800 dark:text-amber-200 text-sm">Categoria II</span>
            <span class="px-2 py-0.5 rounded text-[10px] font-bold bg-amber-200 text-amber-900 dark:bg-amber-900 dark:text-amber-100">Indeterminado</span>
          </div>
          <p class="text-amber-900 dark:text-amber-300 font-semibold">Qualquer traçado que não se enquadre em I nem em III:</p>
          <ul class="space-y-1 list-disc list-inside text-slate-700 dark:text-slate-300 text-[11px]">
            <li>Taquicardia ou bradicardia sem perda de variabilidade;</li>
            <li>Variabilidade mínima ou acentuada;</li>
            <li>Ausência de acelerações após estímulo;</li>
            <li>Desacelerações variáveis com variabilidade mínima/moderada.</li>
          </ul>
          <p class="text-[10px] text-amber-800 dark:text-amber-300 font-bold">Conduta: Vigilância contínua, ressuscitação intrauterina (DLE, hidratação) e reavaliação.</p>
        </div>

        <div class="p-4 rounded-2xl bg-rose-50 dark:bg-rose-950/30 border border-rose-300 dark:border-rose-800 space-y-2">
          <div class="flex items-center justify-between">
            <span class="font-bold text-rose-800 dark:text-rose-200 text-sm">Categoria III</span>
            <span class="px-2 py-0.5 rounded text-[10px] font-bold bg-rose-200 text-rose-900 dark:bg-rose-900 dark:text-rose-100 animate-pulse">Anormal / Urgente</span>
          </div>
          <p class="text-rose-900 dark:text-rose-300 font-semibold">Ausência de variabilidade associada a QUALQUER UM:</p>
          <ul class="space-y-1 list-disc list-inside text-slate-700 dark:text-slate-300 text-[11px]">
            <li>Desacelerações tardias recorrentes ($\ge 50\%$ das contrações);</li>
            <li>Desacelerações variáveis recorrentes ($\ge 50\%$ das contrações);</li>
            <li>Bradicardia sustentada;</li>
            <li><strong>Padrão Sinusoidal</strong> verdadeiro.</li>
          </ul>
          <p class="text-[10px] text-rose-800 dark:text-rose-300 font-bold">Conduta: PARTO IMEDIATO pela via mais rápida disponível!</p>
        </div>
      </div>

      <!-- CASCATA DINÂMICA NATIVA DE ADAPTAÇÃO FETAL À HIPÓXIA (FEBRASGO / VINTZILEOS) -->
      <div class="p-6 rounded-3xl bg-slate-900 text-white shadow-xl space-y-5 border border-slate-800">
        <div class="flex flex-wrap items-center justify-between gap-2 border-b border-slate-800 pb-3">
          <div>
            <span class="text-[10px] font-black uppercase text-teal-400 tracking-widest">Tratado de Obstetrícia FEBRASGO 2019 • Fisiologia de Vintzileos</span>
            <h4 class="text-base sm:text-lg font-bold">Cascata Progressiva de Adaptação Cardiovascular e Biofísica na Hipóxia Fetal</h4>
          </div>
          <span class="px-3 py-1 rounded-full text-xs font-bold bg-teal-500/20 text-teal-300 border border-teal-500/30">
            Regressão Neurobiológica
          </span>
        </div>

        <!-- Linha do Tempo / Stepper Interativo de Hipóxia -->
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-5 gap-3 text-xs">
          
          <!-- Estágio 1 -->
          <div class="p-3.5 rounded-2xl bg-slate-800/80 border border-slate-700 space-y-2 relative">
            <div class="flex items-center justify-between">
              <span class="w-6 h-6 rounded-full bg-teal-500 text-slate-950 font-black text-xs flex items-center justify-center">1</span>
              <span class="text-[10px] font-bold text-teal-400 uppercase">Compensação</span>
            </div>
            <h5 class="font-bold text-white text-xs">Hipoxemia Transitória</h5>
            <p class="text-[11px] text-slate-300 leading-tight">
              Ativação de quimiorreceptores aórticos/carotídeos. Feto perde <strong>Acelerações Transitórias</strong> na CTG. Variabilidade basal ainda preservada.
            </p>
            <div class="p-1.5 rounded-lg bg-teal-950/60 text-teal-300 text-[10px] font-mono border border-teal-800/40">
              CTG: Não-Reativo
            </div>
          </div>

          <!-- Estágio 2 -->
          <div class="p-3.5 rounded-2xl bg-slate-800/80 border border-slate-700 space-y-2 relative">
            <div class="flex items-center justify-between">
              <span class="w-6 h-6 rounded-full bg-cyan-500 text-slate-950 font-black text-xs flex items-center justify-center">2</span>
              <span class="text-[10px] font-bold text-cyan-400 uppercase">Bulbo</span>
            </div>
            <h5 class="font-bold text-white text-xs">Inibição Respiratória</h5>
            <p class="text-[11px] text-slate-300 leading-tight">
              A hipóxia tecidual contínua inibe os neurônios do centro respiratório bulbar. Feto cessa os <strong>Movimentos Respiratórios Fetais (MRF)</strong>.
            </p>
            <div class="p-1.5 rounded-lg bg-cyan-950/60 text-cyan-300 text-[10px] font-mono border border-cyan-800/40">
              PBF: MRF = 0 pt
            </div>
          </div>

          <!-- Estágio 3 -->
          <div class="p-3.5 rounded-2xl bg-slate-800/80 border border-slate-700 space-y-2 relative">
            <div class="flex items-center justify-between">
              <span class="w-6 h-6 rounded-full bg-amber-500 text-slate-950 font-black text-xs flex items-center justify-center">3</span>
              <span class="text-[10px] font-bold text-amber-400 uppercase">Subcórtex</span>
            </div>
            <h5 class="font-bold text-white text-xs">Inibição Cinética</h5>
            <p class="text-[11px] text-slate-300 leading-tight">
              Inibição dos núcleos motores subcorticais e núcleos da base. Feto cessa os <strong>Movimentos Corpóreos Globais</strong> para poupar oxigênio.
            </p>
            <div class="p-1.5 rounded-lg bg-amber-950/60 text-amber-300 text-[10px] font-mono border border-amber-800/40">
              PBF: Movs = 0 pt
            </div>
          </div>

          <!-- Estágio 4 -->
          <div class="p-3.5 rounded-2xl bg-slate-800/80 border border-rose-900/60 space-y-2 relative">
            <div class="flex items-center justify-between">
              <span class="w-6 h-6 rounded-full bg-rose-500 text-white font-black text-xs flex items-center justify-center">4</span>
              <span class="text-[10px] font-bold text-rose-400 uppercase">Tronco</span>
            </div>
            <h5 class="font-bold text-white text-xs">Acidemia & Hipotonia</h5>
            <p class="text-[11px] text-slate-300 leading-tight">
              Acidose metabólica severa ($pH &lt; 7,20$). Inibição do centro regulador do tônus no tronco encefálico. Feto perde o <strong>Tônus Muscular</strong> (membros flácidos).
            </p>
            <div class="p-1.5 rounded-lg bg-rose-950/60 text-rose-300 text-[10px] font-mono border border-rose-800/40">
              PBF: Tônus = 0 pt
            </div>
          </div>

          <!-- Estágio 5 -->
          <div class="p-3.5 rounded-2xl bg-red-950/60 border border-red-500/60 space-y-2 relative">
            <div class="flex items-center justify-between">
              <span class="w-6 h-6 rounded-full bg-red-600 text-white font-black text-xs flex items-center justify-center animate-pulse">5</span>
              <span class="text-[10px] font-bold text-red-400 uppercase">Terminal</span>
            </div>
            <h5 class="font-bold text-white text-xs">Falência Miocárdica</h5>
            <p class="text-[11px] text-slate-300 leading-tight">
              Sobrecarga do ventrículo direito e acidose do miocárdio. Surge <strong>Onda 'a' Reversa no Ducto Venoso</strong>, desacelerações tardias repetidas e risco iminente de óbito.
            </p>
            <div class="p-1.5 rounded-lg bg-red-900/60 text-red-200 text-[10px] font-mono border border-red-500 font-bold animate-pulse">
              🚨 PARTO IMEDIATO!
            </div>
          </div>

        </div>
      </div>

      <!-- ESTÍMULO VIBROACÚSTICO (EVA) & CRONOGRAMA DE INDICAÇÃO -->
      <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-xs">
        <div class="p-4 rounded-2xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 space-y-2">
          <h4 class="font-bold text-slate-900 dark:text-white flex items-center gap-2">
            <i class="fa-solid fa-bullhorn text-cyan-500"></i> Estímulo Vibroacústico (EVA)
          </h4>
          <p class="text-slate-600 dark:text-slate-300">
            Aplica-se uma fonte sonora vibratória sobre o polo cefálico fetal por 1 a 3 segundos, emitindo estímulo acústico que provoca despertar e movimentação fetal de curta duração:
          </p>
          <div class="p-3 rounded-xl bg-cyan-50 dark:bg-cyan-950/30 border border-cyan-200 dark:border-cyan-900 text-cyan-950 dark:text-cyan-200 font-semibold">
            Resposta Normal: Aceleração da FCF de no mínimo <strong>15 bpm</strong> por pelo menos <strong>15 segundos</strong> ocorrendo em até <strong>15 segundos</strong> após o estímulo sonoro.
          </div>
          <p class="text-[11px] text-slate-500 italic">
            Excelente para afastar sono fisiológico fetal quando o feto se apresenta hiporreativo na CTG inicial de 20 minutos.
          </p>
        </div>

        <div class="p-4 rounded-2xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 space-y-2">
          <h4 class="font-bold text-slate-900 dark:text-white flex items-center gap-2">
            <i class="fa-solid fa-calendar-days text-teal-500"></i> Cronograma de Indicação da CTG
          </h4>
          <div class="space-y-1.5 text-slate-700 dark:text-slate-300 text-[11px]">
            <p><strong>Monitorização Anteparto:</strong> Indicada a partir de 26 a 28 semanas (idealmente entre <strong>32 e 34 semanas</strong>):</p>
            <ul class="list-disc list-inside space-y-0.5">
              <li><strong>DM insulinodependente bem controlada:</strong> a partir de 32 semanas;</li>
              <li><strong>DM insulinodependente mal controlada:</strong> a partir de 26 semanas;</li>
              <li><strong>Gravidez prolongada sem comorbidades:</strong> a partir de 41 semanas.</li>
            </ul>
            <p class="pt-1 border-t border-slate-100 dark:border-slate-800">
              <strong>Monitorização Intraparto:</strong> Alto risco, indução do parto, prematuridade, presença de líquido meconial ou alterações na ausculta intermitente.
            </p>
          </div>
        </div>
      </div>

    </div>

    <!-- =========================================================================
         6. PERFIL BIOFÍSICO FETAL (PBF) + CONDUTA ZUGAIB 2020
         ========================================================================= -->
    <div class="space-y-6">
      <div class="flex items-center gap-3">
        <span class="w-8 h-8 rounded-xl bg-teal-600 text-white flex items-center justify-center font-black text-sm shadow-md">6</span>
        <div>
          <h3 class="text-lg sm:text-xl font-bold text-slate-900 dark:text-white">Perfil Biofísico Fetal (PBF): Parâmetros & Tabela de Conduta (Zugaib 2020)</h3>
          <p class="text-xs text-slate-500">Avaliação multivariável de 5 parâmetros integrando USG e CTG; redução do líquido amniótico como marcador crônico isolado</p>
        </div>
      </div>

      <!-- Tabela 100.2 de Rezende / Zugaib / SOGC 2007 -->
      <div class="p-5 rounded-3xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 shadow-sm space-y-3">
        <div class="flex items-center justify-between border-b border-slate-200 dark:border-slate-800 pb-2">
          <h4 class="font-bold text-sm text-slate-900 dark:text-white flex items-center gap-2">
            <i class="fa-solid fa-clipboard-check text-teal-500"></i> Tabela 100.2: Variáveis do Perfil Biofísico Fetal (Duração do Teste: 30 minutos)
          </h4>
          <span class="text-[10px] text-teal-600 dark:text-teal-400 font-bold">Presente = 2 pts | Ausente = 0 pts</span>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-5 gap-3 text-xs">
          <div class="p-3 rounded-xl bg-slate-50 dark:bg-slate-800/60 border border-slate-200 dark:border-slate-700">
            <span class="font-bold text-teal-600 dark:text-teal-400 block mb-1">1. FCF (Cardiotocografia)</span>
            <p class="text-slate-600 dark:text-slate-300 text-[11px]">2 ou mais acelerações transitórias ($\ge 15$ bpm por $\ge 15$s) associadas a movimentos.</p>
          </div>
          <div class="p-3 rounded-xl bg-slate-50 dark:bg-slate-800/60 border border-slate-200 dark:border-slate-700">
            <span class="font-bold text-teal-600 dark:text-teal-400 block mb-1">2. Movimento Respiratório</span>
            <p class="text-slate-600 dark:text-slate-300 text-[11px]">Pelo menos 1 episódio contínuo com $\ge 30$ segundos de movimentos respiratórios.</p>
          </div>
          <div class="p-3 rounded-xl bg-slate-50 dark:bg-slate-800/60 border border-slate-200 dark:border-slate-700">
            <span class="font-bold text-teal-600 dark:text-teal-400 block mb-1">3. Movimento Fetal</span>
            <p class="text-slate-600 dark:text-slate-300 text-[11px]">No mínimo 3 movimentos amplos do corpo ou membros em 30 minutos.</p>
          </div>
          <div class="p-3 rounded-xl bg-slate-50 dark:bg-slate-800/60 border border-slate-200 dark:border-slate-700">
            <span class="font-bold text-teal-600 dark:text-teal-400 block mb-1">4. Tônus Fetal</span>
            <p class="text-slate-600 dark:text-slate-300 text-[11px]">Pelo menos 1 episódio de extensão com flexão ativa de membros/tronco ou mão.</p>
          </div>
          <div class="p-3 rounded-xl bg-amber-50 dark:bg-amber-950/40 border border-amber-300 dark:border-amber-800">
            <span class="font-bold text-amber-700 dark:text-amber-300 block mb-1">5. Volume de Líquido Amniótico</span>
            <p class="text-slate-700 dark:text-slate-300 text-[11px]">Bolsão vertical $\ge 2$ cm (ou ILA &gt; 5,0 cm segundo Zugaib, 2020).</p>
            <span class="text-[9px] font-black text-rose-600 uppercase block mt-1">ÚNICO Marcador Crônico!</span>
          </div>
        </div>

        <div class="p-3 rounded-2xl bg-amber-50 dark:bg-amber-950/30 border border-amber-200 dark:border-amber-900 text-xs text-amber-900 dark:text-amber-200 flex items-center gap-3">
          <i class="fa-solid fa-triangle-exclamation text-amber-600 text-lg"></i>
          <div>
            <strong>Regra Áurea do PBF (Rezende / Zugaib):</strong> A redução do volume de líquido amniótico é o <strong>marcador exclusivo de sofrimento fetal crônico</strong>, decorrente da redistribuição de fluxo sanguíneo e vasoconstrição renal fetal (*brain sparing*). Os demais 4 parâmetros sofrem alteração aguda, regredindo na ordem inversa de sua diferenciação embriológica (1º FCF $\rightarrow$ 2º Respiração $\rightarrow$ 3º Movimento $\rightarrow$ 4º Tônus).
          </div>
        </div>
      </div>

      <!-- TABELA 4: CONDUTA DE ACORDO COM O PBF (ZUGAIB OBSTETRÍCIA 2020) -->
      <div class="p-5 rounded-3xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 shadow-sm space-y-3">
        <h4 class="font-bold text-sm text-slate-900 dark:text-white flex items-center gap-2">
          <i class="fa-solid fa-sitemap text-teal-500"></i> Tabela 4: Interpretação e Conduta de Acordo com o PBF (Zugaib Obstetrícia, 2020)
        </h4>

        <div class="overflow-x-auto">
          <table class="w-full text-left text-xs border-collapse">
            <thead>
              <tr class="bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-300">
                <th class="p-2.5 font-bold border-b border-slate-200 dark:border-slate-700">Índice do PBF</th>
                <th class="p-2.5 font-bold border-b border-slate-200 dark:border-slate-700">Interpretação Fisiopatológica</th>
                <th class="p-2.5 font-bold border-b border-slate-200 dark:border-slate-700">Conduta Obstétrica Oficial</th>
              </tr>
            </thead>
            <tbody class="divide-y divide-slate-100 dark:divide-slate-800 text-[11px] text-slate-700 dark:text-slate-300">
              <tr>
                <td class="p-2.5 font-bold text-emerald-600">8 ou 10 com ILA normal</td>
                <td class="p-2.5">Baixo risco para hipoxemia crônica e aguda.</td>
                <td class="p-2.5 font-semibold text-emerald-700 dark:text-emerald-300">Conduta Conservadora. Manter seguimento de pré-natal de rotina.</td>
              </tr>
              <tr>
                <td class="p-2.5 font-bold text-amber-600">8 com ILA $\le 5,0$ cm (Oligoâmnio)</td>
                <td class="p-2.5">Baixo risco para hipoxemia aguda; provável <strong>hipoxemia crônica</strong>.</td>
                <td class="p-2.5 space-y-0.5">
                  <p>Seguir protocolo de oligoâmnio por Idade Gestacional:</p>
                  <p>• <strong>&gt; 37 semanas:</strong> Resolução do parto;</p>
                  <p>• <strong>34 a 36,6 semanas:</strong> Resolução se associado a CIUR;</p>
                  <p>• <strong>25 a 34 semanas:</strong> Resolução se oligodramnia grave (ILA &lt; 3,0 cm).</p>
                </td>
              </tr>
              <tr>
                <td class="p-2.5 font-bold text-amber-600">6/10 com ILA normal</td>
                <td class="p-2.5">Possível hipoxemia aguda; baixo risco para hipoxemia crônica.</td>
                <td class="p-2.5">Considerar repetição do PBF em 6 horas. Se persistir PBF $\le 6$: indicação de parto na viabilidade.</td>
              </tr>
              <tr>
                <td class="p-2.5 font-bold text-rose-600">6/10 com ILA $\le 5,0$ cm</td>
                <td class="p-2.5">Provável hipoxemia crônica e aguda associadas.</td>
                <td class="p-2.5 font-semibold text-rose-600">Resolução da gravidez a partir da viabilidade fetal.</td>
              </tr>
              <tr class="bg-rose-50 dark:bg-rose-950/30">
                <td class="p-2.5 font-black text-rose-700 dark:text-rose-400">4/10, 2/10 ou 0/10</td>
                <td class="p-2.5 font-semibold text-rose-700 dark:text-rose-300">Asfixia fetal grave instalada; provável hipoxemia crônica (se ILA $\le 5$) e aguda severa.</td>
                <td class="p-2.5 font-black text-rose-800 dark:text-rose-200">Resolução imediata a partir da viabilidade fetal ($\ge 24-25$ semanas).</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <!-- CALCULADORA INTERATIVA EXPANDIDA DE PBF -->
      <div id="calculadora-pbf-expandida" class="p-6 rounded-3xl bg-teal-50/70 dark:bg-slate-900/90 border border-teal-300 dark:border-teal-800 space-y-4">
        <div class="flex items-center justify-between border-b border-teal-200 dark:border-teal-800 pb-3">
          <div>
            <span class="text-xs font-black uppercase tracking-wider text-teal-700 dark:text-teal-300">Ferramenta Clínica Integrada</span>
            <h4 class="text-lg font-bold text-slate-900 dark:text-white flex items-center gap-2">
              <i class="fa-solid fa-calculator text-teal-600"></i> Calculadora de PBF com Estratificação de Zugaib 2020
            </h4>
          </div>
          <span class="px-2.5 py-1 rounded-full text-xs font-bold bg-teal-600 text-white shadow">Algoritmo Inteligente</span>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-3 text-xs">
          <div>
            <label class="block font-bold text-slate-700 dark:text-slate-300 mb-1">Idade Gestacional (semanas):</label>
            <input type="number" id="pbf-ig" value="35" min="20" max="42" class="w-full p-2.5 rounded-xl border border-slate-300 dark:border-slate-700 bg-white dark:bg-slate-800">
          </div>
          <div>
            <label class="block font-bold text-slate-700 dark:text-slate-300 mb-1">Diagnóstico de CIUR associado?</label>
            <select id="pbf-tem-ciur" class="w-full p-2.5 rounded-xl border border-slate-300 dark:border-slate-700 bg-white dark:bg-slate-800">
              <option value="nao">Não (Crescimento fetal adequado)</option>
              <option value="sim">Sim (Restrição de Crescimento Fetal)</option>
            </select>
          </div>
          <div>
            <label class="block font-bold text-slate-700 dark:text-slate-300 mb-1">Volume de Líquido Amniótico (ILA):</label>
            <select id="pbf-ila-status" class="w-full p-2.5 rounded-xl border border-slate-300 dark:border-slate-700 bg-white dark:bg-slate-800">
              <option value="normal">Normal (Bolsão $\ge 2$ cm / ILA &gt; 5,0 cm) [2 pts]</option>
              <option value="oligo_moderado">Oligoâmnio (ILA 3,0 a 5,0 cm) [0 pts]</option>
              <option value="oligo_grave">Oligoâmnio Grave (ILA &lt; 3,0 cm) [0 pts]</option>
            </select>
          </div>
          <div>
            <label class="block font-bold text-slate-700 dark:text-slate-300 mb-1">Cardiotocografia (CTG Basal):</label>
            <select id="pbf-ctg-sel" class="w-full p-2.5 rounded-xl border border-slate-300 dark:border-slate-700 bg-white dark:bg-slate-800">
              <option value="2">Reativo ($\ge 2$ acelerações de 15bpm) [2 pts]</option>
              <option value="0">Não Reativo (&lt; 2 acelerações) [0 pts]</option>
            </select>
          </div>
          <div>
            <label class="block font-bold text-slate-700 dark:text-slate-300 mb-1">Movimentos Respiratórios:</label>
            <select id="pbf-resp-sel" class="w-full p-2.5 rounded-xl border border-slate-300 dark:border-slate-700 bg-white dark:bg-slate-800">
              <option value="2">Presente ($\ge 1$ episódio contínuo $\ge 30$s) [2 pts]</option>
              <option value="0">Ausente ou &lt; 30 segundos contínuos [0 pts]</option>
            </select>
          </div>
          <div>
            <label class="block font-bold text-slate-700 dark:text-slate-300 mb-1">Movimentos Corporais Fetais:</label>
            <select id="pbf-mov-sel" class="w-full p-2.5 rounded-xl border border-slate-300 dark:border-slate-700 bg-white dark:bg-slate-800">
              <option value="2">Normal ($\ge 3$ movimentos de corpo/membros) [2 pts]</option>
              <option value="0">Anormal (&lt; 3 movimentos corporais) [0 pts]</option>
            </select>
          </div>
          <div>
            <label class="block font-bold text-slate-700 dark:text-slate-300 mb-1">Tônus Fetal:</label>
            <select id="pbf-tonus-sel" class="w-full p-2.5 rounded-xl border border-slate-300 dark:border-slate-700 bg-white dark:bg-slate-800">
              <option value="2">Normal (extensão/flexão de membros/mãos) [2 pts]</option>
              <option value="0">Ausente ou flacidez sem retorno [0 pts]</option>
            </select>
          </div>
          <div class="flex items-end">
            <button onclick="calcularPBFExpandido()" class="w-full py-2.5 px-4 rounded-xl bg-teal-600 hover:bg-teal-700 text-white font-bold text-xs transition-all shadow">
              Calcular Conduta Zugaib
            </button>
          </div>
        </div>

        <div id="pbf-expandido-results" class="hidden p-4 rounded-2xl bg-white dark:bg-slate-800 border border-teal-200 dark:border-teal-800 space-y-3">
          <div class="flex items-center justify-between">
            <div>
              <span class="text-xs text-slate-500 block">Pontuação Total do PBF:</span>
              <span id="pbf-exp-score" class="text-2xl font-black text-teal-600">-- / 10</span>
            </div>
            <div id="pbf-exp-badge"></div>
          </div>
          <div id="pbf-exp-interpretacao" class="text-xs text-slate-700 dark:text-slate-300"></div>
          <div id="pbf-exp-conduta" class="p-3 rounded-xl bg-teal-50 dark:bg-slate-900 border border-teal-200 dark:border-slate-700 text-xs text-slate-800 dark:text-slate-200 font-semibold"></div>
        </div>
      </div>

    </div>

    <!-- =========================================================================
         7. SOFRIMENTO FETAL CRÔNICO & DOPPLERFLUXOMETRIA AVANÇADA
         ========================================================================= -->
    <div class="space-y-6">
      <div class="flex items-center gap-3">
        <span class="w-8 h-8 rounded-xl bg-teal-600 text-white flex items-center justify-center font-black text-sm shadow-md">7</span>
        <div>
          <h3 class="text-lg sm:text-xl font-bold text-slate-900 dark:text-white">Sofrimento Fetal Crônico & Estudo Doppler dos Territórios Vasculares</h3>
          <p class="text-xs text-slate-500">Avaliação hemodinâmica a partir de 24-26 semanas: Artérias Uterinas, Artéria Umbilical, ACM e Ducto Venoso</p>
        </div>
      </div>

      <!-- Fórmulas e Princípios Fisiológicos -->
      <div class="grid grid-cols-1 md:grid-cols-3 gap-4 text-xs">
        <div class="p-4 rounded-2xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 space-y-1.5 shadow-sm">
          <h4 class="font-bold text-teal-600 dark:text-teal-400 text-sm flex items-center gap-2">
            <i class="fa-solid fa-wave-square"></i> Índices Doppler
          </h4>
          <p class="text-slate-600 dark:text-slate-400">Mensuram a qualidade e resistência do fluxo ao longo do ciclo cardíaco:</p>
          <ul class="space-y-1 list-disc list-inside text-slate-700 dark:text-slate-300 font-mono text-[11px]">
            <li><strong>IP (Pulsatilidade):</strong> (Sístole - Diástole) / Velocidade Média</li>
            <li><strong>IR (Resistência):</strong> (Sístole - Diástole) / Sístole</li>
            <li><strong>Relação S/D:</strong> Velocidade Sistólica / Diastólica</li>
            <li><strong>RCP (Cérebro-Placentária):</strong> IP da ACM / IP Umbilical (Normal &gt; 1,0 ou &gt; p5)</li>
          </ul>
        </div>

        <div class="p-4 rounded-2xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 space-y-1.5 shadow-sm">
          <h4 class="font-bold text-slate-900 dark:text-white text-sm flex items-center gap-2">
            <i class="fa-solid fa-code-branch text-purple-500"></i> Fisiopatologia Vaso a Vaso
          </h4>
          <ul class="space-y-1.5 text-slate-700 dark:text-slate-300 text-[11px]">
            <li><strong>Artéria Uterina:</strong> Território materno. Avalia risco de pré-eclâmpsia e CIUR (incisura protodiastólica). <em>NÃO tem valor para avaliar sofrimento fetal agudo</em>!</li>
            <li><strong>Artéria Umbilical:</strong> Vaso periférico fetal. Sofre <strong>vasoconstrição</strong> (aumento do IP) na hipóxia crônica. Alterações no Doppler da umbilical <strong>antecedem</strong> PBF e CTG!</li>
            <li><strong>Artéria Cerebral Média (ACM):</strong> Sofre <strong>vasodilatação</strong> compensatória para preservação de órgãos nobres ("centralização fetal").</li>
          </ul>
        </div>

        <div class="p-4 rounded-2xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 space-y-1.5 shadow-sm">
          <h4 class="font-bold text-rose-600 dark:text-rose-400 text-sm flex items-center gap-2">
            <i class="fa-solid fa-heart text-rose-500"></i> Ducto Venoso (Função Miocárdica)
          </h4>
          <p class="text-slate-600 dark:text-slate-400 text-[11px]">
            Avalia a pré-carga e contratilidade cardíaca fetal (pressão retrógrada no átrio direito):
          </p>
          <div class="p-2.5 rounded-xl bg-rose-50 dark:bg-rose-950/30 border border-rose-200 dark:border-rose-900 text-rose-900 dark:text-rose-200 text-[11px] space-y-1">
            <p>• <strong>Onda A Positiva:</strong> Contração atrial normal em feto compensado.</p>
            <p>• <strong>Onda A Zero ou Reversa:</strong> Acidose fetal profunda, falência cardíaca e risco iminente de óbito intrauterino!</p>
            <p>• <strong>Utilidade Clínica:</strong> Permite prolongar a gestação em prematuros extremos com centralização fetal até 28-30 semanas.</p>
          </div>
        </div>
      </div>

      <!-- PAINEL VETORIAL NATIVO: CENTRALIZAÇÃO FETAL & DUCTO VENOSO -->
      <div class="grid grid-cols-1 md:grid-cols-2 gap-6 text-xs">
        
        <!-- CARD 1: CENTRALIZAÇÃO FETAL E INFOGRÁFICO HEMODINÂMICO NATIVO -->
        <div class="p-5 rounded-3xl bg-slate-900 text-white shadow-xl space-y-4 border border-slate-800">
          <div class="flex items-center justify-between border-b border-slate-800 pb-2">
            <span class="text-[10px] font-black uppercase text-teal-400 tracking-wider">Hemodinâmica Fetal • Rezende</span>
            <span class="px-2.5 py-0.5 rounded-full text-[10px] font-bold bg-teal-950 text-teal-300 border border-teal-800">Brain Sparing Effect</span>
          </div>
          <h4 class="font-bold text-sm text-white">Mecanismo da Centralização Fetal & Relação Cérebro-Placentária (RCP)</h4>
          
          <!-- Diagrama Vetorial Nativo de Centralização -->
          <div class="p-4 rounded-2xl bg-slate-950 border border-slate-800 space-y-3">
            <div class="grid grid-cols-2 gap-3 text-center">
              
              <!-- Órgãos Nobres -->
              <div class="p-3 rounded-xl bg-teal-950/50 border border-teal-500/40 space-y-1">
                <span class="text-teal-400 font-bold text-xs flex items-center justify-center gap-1.5">
                  <i class="fa-solid fa-brain"></i> Órgãos Nobres
                </span>
                <p class="text-[11px] text-teal-200 font-semibold">Cérebro, Coração, Suprarrenal</p>
                <div class="text-[10px] text-emerald-400 font-bold mt-1">
                  VASODILATAÇÃO REFLEXA<br>
                  $\downarrow$ Resistência / $\downarrow$ IP ACM (&lt; p5)
                </div>
              </div>

              <!-- Órgãos Periféricos -->
              <div class="p-3 rounded-xl bg-rose-950/50 border border-rose-500/40 space-y-1">
                <span class="text-rose-400 font-bold text-xs flex items-center justify-center gap-1.5">
                  <i class="fa-solid fa-lungs"></i> Órgãos Periféricos
                </span>
                <p class="text-[11px] text-rose-200 font-semibold">Rins, Pulmões, Esplâncnico</p>
                <div class="text-[10px] text-rose-400 font-bold mt-1">
                  VASOCONSTRIÇÃO COMPENSATÓRIA<br>
                  $\downarrow$ Diurese $\rightarrow$ <strong>Oligoâmnio</strong>
                </div>
              </div>

            </div>

            <!-- Fórmula de Ouro da RCP -->
            <div class="p-3 rounded-xl bg-slate-900 border border-slate-700 flex items-center justify-between text-xs">
              <span class="font-mono text-teal-300 font-bold">
                RCP = IP da ACM / IP da Umbilical
              </span>
              <span class="text-amber-400 font-black">
                Centralizado se &lt; 1,0 (ou &lt; p5)
              </span>
            </div>
          </div>

          <p class="text-[11px] text-slate-300 leading-relaxed">
            A centralização fetal é uma resposta hemodinâmica adaptativa que visa garantir o aporte de oxigênio ao cérebro e miocárdio em detrimento do território renal e esplâncnico. Na gestação a termo ($\ge 37$ semanas) ou com maturidade assegurada, <strong>a centralização fetal é indicação de parto</strong> pelo risco elevado de sofrimento fetal agudo no trabalho de parto.
          </p>
        </div>

        <!-- CARD 2: DOPPLER DO DUCTO VENOSO COM ONDAS NATIVAS EM SVG -->
        <div class="p-5 rounded-3xl bg-slate-900 text-white shadow-xl space-y-4 border border-slate-800">
          <div class="flex items-center justify-between border-b border-slate-800 pb-2">
            <span class="text-[10px] font-black uppercase text-rose-400 tracking-wider">Doppler Venoso • Rezende</span>
            <span class="px-2.5 py-0.5 rounded-full text-[10px] font-bold bg-rose-950 text-rose-300 border border-rose-800">Sobrecarga de VD</span>
          </div>
          <h4 class="font-bold text-sm text-white">Doppler do Ducto Venoso: Morfologia Normal vs Onda 'a' Reversa</h4>
          
          <!-- SVG Vetorial do Ducto Venoso -->
          <div class="rounded-2xl overflow-hidden border border-slate-800 bg-slate-950 p-2 shadow-inner">
            <svg viewBox="0 0 540 210" class="w-full h-auto select-none" xmlns="http://www.w3.org/2000/svg">
              <rect width="540" height="210" fill="#090d16" rx="12"/>
              
              <!-- LEFT: Normal -->
              <text x="25" y="24" fill="#10b981" font-size="11" font-family="sans-serif" font-weight="bold">
                PADRÃO NORMAL (IPDV &lt; p95)
              </text>
              <line x1="25" y1="140" x2="245" y2="140" stroke="#475569" stroke-width="1.5"/>
              <text x="210" y="135" fill="#64748b" font-size="8" font-family="monospace">Zero</text>
              
              <!-- Normal waveform: S, D, a > 0 -->
              <path d="M 30,140 Q 50,45 65,45 Q 80,55 90,95 Q 100,80 110,80 Q 120,95 130,118 Q 138,122 145,122 Q 152,138 158,140
                       Q 175,45 190,45 Q 205,55 215,95 Q 225,80 235,80 Q 242,100 248,120"
                    fill="none" stroke="#10b981" stroke-width="2.5" stroke-linecap="round"/>
              
              <text x="65" y="38" fill="#10b981" font-size="10" font-weight="bold" text-anchor="middle">S</text>
              <text x="110" y="72" fill="#34d399" font-size="10" font-weight="bold" text-anchor="middle">D</text>
              <text x="145" y="110" fill="#fbbf24" font-size="10" font-weight="bold" text-anchor="middle">Onda 'a' (+)</text>
              <circle cx="145" cy="120" r="3" fill="#fbbf24"/>
              
              <text x="25" y="165" fill="#94a3b8" font-size="9">Contração atrial com fluxo anterógrado.</text>
              <text x="25" y="180" fill="#10b981" font-size="9" font-weight="bold">Miocárdio fetal compensado.</text>
              
              <!-- Divider -->
              <line x1="265" y1="15" x2="265" y2="195" stroke="#1e293b" stroke-width="2"/>
              
              <!-- RIGHT: Reversa -->
              <text x="285" y="24" fill="#f43f5e" font-size="11" font-family="sans-serif" font-weight="bold">
                PADRÃO CRÍTICO: ONDA 'a' REVERSA
              </text>
              <line x1="285" y1="140" x2="515" y2="140" stroke="#475569" stroke-width="1.5"/>
              <text x="490" y="135" fill="#64748b" font-size="8" font-family="monospace">Zero</text>
              
              <!-- Abnormal waveform: a dips below 0 -->
              <path d="M 295,140 Q 312,50 325,50 Q 340,60 350,100 Q 360,85 370,85 Q 380,110 390,140 Q 398,175 405,175 Q 412,150 418,140
                       Q 435,50 450,50 Q 465,60 475,100 Q 485,85 495,85"
                    fill="none" stroke="#f43f5e" stroke-width="2.5" stroke-linecap="round"/>
              
              <text x="325" y="42" fill="#cbd5e1" font-size="10" font-weight="bold" text-anchor="middle">S</text>
              <text x="370" y="76" fill="#cbd5e1" font-size="10" font-weight="bold" text-anchor="middle">D</text>
              
              <circle cx="405" cy="175" r="4" fill="#f43f5e"/>
              <line x1="405" y1="140" x2="405" y2="175" stroke="#f43f5e" stroke-width="2" stroke-dasharray="2,2"/>
              <text x="405" y="195" fill="#f43f5e" font-size="9" font-weight="black" text-anchor="middle">Onda 'a' Reversa!</text>
              
              <text x="285" y="160" fill="#fca5a5" font-size="9" font-weight="bold">Refluxo diastólico para a veia umbilical.</text>
              <text x="285" y="175" fill="#f87171" font-size="9" font-weight="black">🚨 Acidose grave • Cesárea Imediata!</text>
            </svg>
          </div>

          <p class="text-[11px] text-slate-300 leading-relaxed">
            O ducto venoso é o parâmetro padrão-ouro para temporizar o parto em prematuros extremos com RCF grave. A presença de <strong>onda 'a' zero ou reversa</strong> traduz falência miocárdica e acidose metabólica avançada, sendo a <strong>indicação mandatória de parto imediato a partir da viabilidade fetal ($\ge 24-26$ semanas)</strong>.
          </p>
        </div>

      </div>
    </div>

    <!-- =========================================================================
         8. CRITÉRIOS DIAGNÓSTICOS DE RCIU - CONSENSO DELPHI 2016
         ========================================================================= -->
    <div class="space-y-6">
      <div class="flex items-center gap-3">
        <span class="w-8 h-8 rounded-xl bg-teal-600 text-white flex items-center justify-center font-black text-sm shadow-md">8</span>
        <div>
          <h3 class="text-lg sm:text-xl font-bold text-slate-900 dark:text-white">Critérios Diagnósticos de RCIU / CIUR (Consenso Delphi / Gordjin et al. 2016)</h3>
          <p class="text-xs text-slate-500">Definição internacional padronizada dividindo RCIU Precoce (&lt; 32 semanas) e RCIU Tardia (&ge; 32 semanas)</p>
        </div>
      </div>

      <div class="grid grid-cols-1 lg:grid-cols-2 gap-6 items-start text-xs">
        
        <!-- Matriz Comparativa Estruturada Delphi 2016 -->
        <div class="p-5 rounded-3xl bg-slate-900 text-white shadow-xl space-y-4 border border-slate-800">
          <div class="flex items-center justify-between border-b border-slate-800 pb-2">
            <span class="text-[10px] font-black uppercase text-teal-400 tracking-wider">Gordjin et al. • UOG 2016</span>
            <span class="px-2.5 py-0.5 rounded-full text-[10px] font-bold bg-teal-950 text-teal-300 border border-teal-800">Consenso Internacional</span>
          </div>

          <div class="space-y-3">
            
            <!-- RCF Precoce -->
            <div class="p-3.5 rounded-2xl bg-slate-800/80 border border-slate-700 space-y-2">
              <div class="flex items-center justify-between">
                <span class="font-bold text-rose-400 text-xs">RCF Precoce (&lt; 32 semanas)</span>
                <span class="text-[10px] px-2 py-0.5 rounded bg-rose-950 text-rose-300 border border-rose-800 font-bold">Fenótipo Placentário Grave</span>
              </div>
              <p class="text-slate-300 text-[11px]">
                <strong>Critério Maior Isolado:</strong> CA ou PFE &lt; p3 OU Artéria Umbilical com Diástole Zero.
              </p>
              <p class="text-slate-300 text-[11px]">
                <strong>Critérios Menores (exige $\ge 2$ combinados):</strong> PFE ou CA &lt; p10 associado a IP das Artérias Uterinas &gt; p95 e/ou IP da Artéria Umbilical &gt; p95.
              </p>
            </div>

            <!-- RCF Tardia -->
            <div class="p-3.5 rounded-2xl bg-slate-800/80 border border-slate-700 space-y-2">
              <div class="flex items-center justify-between">
                <span class="font-bold text-amber-400 text-xs">RCF Tardia (&ge; 32 semanas)</span>
                <span class="text-[10px] px-2 py-0.5 rounded bg-amber-950 text-amber-300 border border-amber-800 font-bold">Disfunção Sutil a Termo</span>
              </div>
              <p class="text-slate-300 text-[11px]">
                <strong>Critério Maior Isolado:</strong> CA ou PFE &lt; p3.
              </p>
              <p class="text-slate-300 text-[11px]">
                <strong>Critérios Menores (exige $\ge 2$ combinados):</strong> PFE ou CA &lt; p10 associado a Relação Cérebro-Placentária (RCP) &lt; p5, IP da Umbilical &gt; p95 ou queda do PFE &gt; 2 quartis na curva de crescimento.
              </p>
            </div>

            <!-- Feto PIG Constitucional -->
            <div class="p-3 rounded-2xl bg-teal-950/40 border border-teal-800/60 space-y-1">
              <span class="font-bold text-teal-400 text-xs">Diferencial: Feto PIG Constitucional</span>
              <p class="text-[11px] text-slate-300">
                PFE entre p3 e p10 com Doppler de Artéria Umbilical, Cerebral Média, Uterinas e Líquido Amniótico rigorosamente normais. Não é doença! Conduta conservadora ambulatorial.
              </p>
            </div>

          </div>
        </div>

        <!-- CLASSIFICADOR INTERATIVO DELPHI 2016 -->
        <div class="p-5 rounded-3xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 shadow-sm space-y-4">
          <div class="border-b border-slate-200 dark:border-slate-800 pb-2">
            <h4 class="font-bold text-sm text-slate-900 dark:text-white flex items-center gap-2">
              <i class="fa-solid fa-network-wired text-teal-500"></i> Classificador Interativo Delphi de RCIU
            </h4>
            <p class="text-[11px] text-slate-500">Selecione os parâmetros ultrassonográficos e Doppler observados:</p>
          </div>

          <div class="space-y-3">
            <div>
              <label class="block font-bold text-slate-700 dark:text-slate-300 mb-1">Idade Gestacional no Diagnóstico:</label>
              <select id="delphi-ig" class="w-full p-2.5 rounded-xl border border-slate-300 dark:border-slate-700 bg-slate-50 dark:bg-slate-800 text-xs">
                <option value="precoce">RCIU Precoce (&lt; 32 semanas de gestação)</option>
                <option value="tardia">RCIU Tardia (&ge; 32 semanas de gestação)</option>
              </select>
            </div>

            <!-- Critérios Maiores (Pelo menos 1) -->
            <div class="p-3 rounded-xl bg-rose-50 dark:bg-rose-950/30 border border-rose-200 dark:border-rose-900 space-y-1.5">
              <span class="font-black text-rose-800 dark:text-rose-200 text-[11px] uppercase tracking-wide">
                Critérios Maiores (Pelo menos 1 critério isolado confirma RCIU):
              </span>
              <div class="space-y-1 text-[11px]">
                <label class="flex items-center gap-2 cursor-pointer">
                  <input type="checkbox" id="delphi-ca-p3" class="rounded text-teal-600">
                  <span>Circunferência Abdominal (CA) &lt; percentil 3</span>
                </label>
                <label class="flex items-center gap-2 cursor-pointer">
                  <input type="checkbox" id="delphi-pfe-p3" class="rounded text-teal-600">
                  <span>Peso Fetal Estimado (PFE) &lt; percentil 3</span>
                </label>
                <label class="flex items-center gap-2 cursor-pointer" id="box-delphi-au-zero">
                  <input type="checkbox" id="delphi-au-zero" class="rounded text-teal-600">
                  <span>Artéria Umbilical com Diástole Zero (apenas para &lt; 32 sem)</span>
                </label>
              </div>
            </div>

            <!-- Critérios Menores (Pelo menos 2 combinados) -->
            <div class="p-3 rounded-xl bg-amber-50 dark:bg-amber-950/30 border border-amber-200 dark:border-amber-900 space-y-1.5">
              <span class="font-black text-amber-800 dark:text-amber-200 text-[11px] uppercase tracking-wide">
                Critérios Menores (Exigem pelo menos 2 combinados):
              </span>
              <div class="space-y-1 text-[11px]">
                <label class="flex items-center gap-2 cursor-pointer">
                  <input type="checkbox" id="delphi-pfe-p10" class="rounded text-teal-600">
                  <span>PFE ou CA &lt; percentil 10</span>
                </label>
                <label class="flex items-center gap-2 cursor-pointer">
                  <input type="checkbox" id="delphi-ip-ut" class="rounded text-teal-600">
                  <span>IP médio das Artérias Uterinas &gt; percentil 95</span>
                </label>
                <label class="flex items-center gap-2 cursor-pointer">
                  <input type="checkbox" id="delphi-ip-umb" class="rounded text-teal-600">
                  <span>IP da Artéria Umbilical &gt; percentil 95</span>
                </label>
                <label class="flex items-center gap-2 cursor-pointer" id="box-delphi-rcp">
                  <input type="checkbox" id="delphi-rcp" class="rounded text-teal-600">
                  <span>Relação Cérebro-Placentária (RCP) &lt; percentil 5 (tardia)</span>
                </label>
                <label class="flex items-center gap-2 cursor-pointer" id="box-delphi-queda">
                  <input type="checkbox" id="delphi-queda-quartis" class="rounded text-teal-600">
                  <span>Queda do PFE &gt; 2 quartis na curva de crescimento (tardia)</span>
                </label>
              </div>
            </div>

            <button onclick="avaliarDelphiRCIU()" class="w-full py-2.5 px-4 rounded-xl bg-teal-600 hover:bg-teal-700 text-white font-bold text-xs transition-colors shadow">
              Classificar RCIU pelo Consenso Delphi
            </button>
            <div id="delphi-result" class="hidden p-3 rounded-xl border text-xs"></div>
          </div>
        </div>

      </div>
    </div>

    <!-- =========================================================================
         9. ESTADIAMENTO DE RCF / CIUR & CONDUTA DE PARTO (EINSTEIN & MS 2022)
         ========================================================================= -->
    <div class="space-y-6">
      <div class="flex items-center gap-3">
        <span class="w-8 h-8 rounded-xl bg-teal-600 text-white flex items-center justify-center font-black text-sm shadow-md">9</span>
        <div>
          <h3 class="text-lg sm:text-xl font-bold text-slate-900 dark:text-white">Estadiamento de RCF, Risco de Óbito & Resolução Gestacional (Einstein / MS 2022)</h3>
          <p class="text-xs text-slate-500">Diretriz estratificada em 5 estágios hemodinâmicos cruzando vigilância de vitalidade e momento ideal de parto</p>
        </div>
      </div>

      <!-- Tabela Master de Estadiamento Einstein / MS 2022 -->
      <div class="p-5 rounded-3xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 shadow-sm space-y-4">
        <div class="overflow-x-auto">
          <table class="w-full text-left text-xs border-collapse">
            <thead>
              <tr class="bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-300">
                <th class="p-2.5 font-bold border-b border-slate-200 dark:border-slate-700">Estágio</th>
                <th class="p-2.5 font-bold border-b border-slate-200 dark:border-slate-700">Descrição & Achados Doppler</th>
                <th class="p-2.5 font-bold border-b border-slate-200 dark:border-slate-700">Risco de Óbito Fetal (OF)</th>
                <th class="p-2.5 font-bold border-b border-slate-200 dark:border-slate-700">Controle de Vitalidade</th>
                <th class="p-2.5 font-bold border-b border-slate-200 dark:border-slate-700">Momento do Parto (Einstein vs MS)</th>
              </tr>
            </thead>
            <tbody class="divide-y divide-slate-100 dark:divide-slate-800 text-[11px] text-slate-700 dark:text-slate-300">
              
              <!-- Feto PIG -->
              <tr>
                <td class="p-2.5 font-bold text-slate-800 dark:text-slate-200">Feto PIG</td>
                <td class="p-2.5">p3 &lt; PFE &lt; p10 com Doppler de Artérias Umbilicais e Cerebral Média normais.</td>
                <td class="p-2.5 text-emerald-600 font-semibold">Baixo</td>
                <td class="p-2.5">Doppler a cada 15 dias (semanal a partir de 36 sem); peso semanal; PBF/CTG 1-2x/sem.</td>
                <td class="p-2.5 font-bold text-slate-900 dark:text-white">Parto até 40 semanas (preferir preparo mecânico + ocitocina com vigilância).</td>
              </tr>

              <!-- Estágio 1 -->
              <tr>
                <td class="p-2.5 font-bold text-teal-600">Estágio 1</td>
                <td class="p-2.5">PFE &lt; p3 OU (p3 &gt; PFE &lt; p10 com IP médio de Art. Uterinas &gt; p95); Doppler fetal normal.</td>
                <td class="p-2.5 text-emerald-600 font-semibold">Baixo</td>
                <td class="p-2.5">Doppler semanal até 34 sem; 2x/sem a partir de 34 sem; peso semanal; PBF/CTG 1-2x/sem.</td>
                <td class="p-2.5 font-bold text-teal-700 dark:text-teal-300">Parto entre 37 e 38 semanas (indução obstétrica supervisionada).</td>
              </tr>

              <!-- Estágio 2 -->
              <tr>
                <td class="p-2.5 font-bold text-amber-600">Estágio 2</td>
                <td class="p-2.5">Doppler AU &gt; p95, ACM &lt; p5 ou Centralização de fluxo fetal (RCP &lt; p5).</td>
                <td class="p-2.5 text-amber-600 font-semibold">Baixo a curto prazo</td>
                <td class="p-2.5">Considerar internação e corticoterapia; Doppler 2-3x/sem (&lt; 34 sem) ou diário (&gt; 34 sem); CTG diária; PBF 2-3x/sem.</td>
                <td class="p-2.5 space-y-0.5">
                  <span class="font-bold text-amber-700 dark:text-amber-300 block">Einstein: Parto entre 34 e 37 semanas.</span>
                  <span class="text-[10px] text-slate-500 block">Manual MS 2022: Interrupção a partir de 37 semanas.</span>
                </td>
              </tr>

              <!-- Estágio 3 -->
              <tr class="bg-amber-50/50 dark:bg-amber-950/20">
                <td class="p-2.5 font-black text-orange-600">Estágio 3</td>
                <td class="p-2.5 font-semibold">RCF com Doppler de Artéria Umbilical com <strong>Diástole Zero (AEDV)</strong>.</td>
                <td class="p-2.5 text-orange-600 font-bold">Total 6,8% (OR 3,6). Com monitorização: 0 a 1%. Deterioração média: 5 dias.</td>
                <td class="p-2.5">Internação imediata, vitalidade diária, <strong>corticoterapia</strong>, Doppler diário com DV, CTG computadorizada diária, PBF diário, CTG convencional 2x/dia.</td>
                <td class="p-2.5 space-y-0.5">
                  <span class="font-bold text-orange-700 dark:text-orange-300 block">Einstein: Parto com 32 semanas por cesárea eletiva.</span>
                  <span class="text-[10px] text-slate-500 block">Manual MS 2022: Interrupção a partir de 34 semanas.</span>
                  <span class="text-[10px] text-rose-600 block">Adiantar parto se: estagnação ponderal ou alças intestinais hiperecogênicas.</span>
                </td>
              </tr>

              <!-- Estágio 4 -->
              <tr class="bg-rose-50/60 dark:bg-rose-950/30">
                <td class="p-2.5 font-black text-rose-600">Estágio 4</td>
                <td class="p-2.5 font-semibold"><strong>Diástole Reversa (REDV)</strong> na Artéria Umbilical OU <strong>IP do Ducto Venoso &gt; p95</strong>.</td>
                <td class="p-2.5 text-rose-600 font-black">Total 19% (OR 7,3). Com monitorização: 1 a 2%. Deterioração média: 2 dias!</td>
                <td class="p-2.5">Corticoterapia imediata + Parto. Se aguardar corticoide: Doppler diário, CTG computadorizada diária, PBF e CTG convencional 2x/dia.</td>
                <td class="p-2.5 space-y-0.5">
                  <span class="font-black text-rose-700 dark:text-rose-300 block">Cesárea Eletiva Imediata.</span>
                  <span class="text-[10px] text-slate-500 block">Manual MS 2022: Interrupção a partir de 30 semanas.</span>
                  <span class="text-[10px] text-slate-400 block">&lt; 26 semanas: individualizar com neonatologia.</span>
                </td>
              </tr>

              <!-- Estágio 5 -->
              <tr class="bg-red-100/60 dark:bg-red-950/40">
                <td class="p-2.5 font-black text-red-600">Estágio 5</td>
                <td class="p-2.5 font-black">Ducto Venoso com <strong>Onda A Zero ou Reversa</strong> OU STV na CTG &lt; 3 ms OU desacelerações espontâneas repetidas.</td>
                <td class="p-2.5 text-red-600 font-black">Total 20% (OR 11,6). Iminência de falência circulatória!</td>
                <td class="p-2.5 font-bold">Internação, corticoterapia de resgate e parto imediato.</td>
                <td class="p-2.5 font-black text-red-700 dark:text-red-300">
                  PARTO NA VIABILIDADE (a partir de 24-26 semanas) por Cesárea Eletiva Imediata!
                </td>
              </tr>

            </tbody>
          </table>
        </div>
      </div>

      <!-- BOX DE EMERGÊNCIA: INDICAÇÕES ABSOLUTAS DE PARTO INDEPENDENTE DA IG -->
      <div class="p-5 rounded-3xl bg-gradient-to-r from-rose-950/40 via-red-950/50 to-slate-900 border-2 border-red-500/50 text-white shadow-2xl space-y-3">
        <div class="flex items-center gap-2 text-red-400 font-black text-sm uppercase tracking-wider">
          <i class="fa-solid fa-triangle-exclamation text-lg animate-pulse"></i> 
          Indicações Absolutas de Parto Independente da Idade Gestacional (Hospital Einstein / Protocolo Oficial)
        </div>
        <p class="text-xs text-slate-300 leading-relaxed">
          Diante de qualquer um dos 4 critérios abaixo, o parto está indicado imediatamente, mesmo em prematuridade extrema, visando resgatar o concepto da asfixia letal ou salvar a vida materna:
        </p>
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-3 text-xs">
          <div class="p-3 rounded-2xl bg-white/5 border border-white/10 space-y-1">
            <span class="font-bold text-red-400 block">1. Indicação Materna Grave</span>
            <span class="text-slate-300 text-[11px]">Ex: Pré-Eclâmpsia com sinais de gravidade refratária, Síndrome HELLP, Eclâmpsia, DPP ou iminência de rotura uterina.</span>
          </div>
          <div class="p-3 rounded-2xl bg-white/5 border border-white/10 space-y-1">
            <span class="font-bold text-red-400 block">2. PBF $\le 4$</span>
            <span class="text-slate-300 text-[11px]">Escore 0 ou 2 mantido por 30 minutos, ou escore 4 mantido por 60 minutos de observação contínua.</span>
          </div>
          <div class="p-3 rounded-2xl bg-white/5 border border-white/10 space-y-1">
            <span class="font-bold text-red-400 block">3. CTG Patológica Crítica</span>
            <span class="text-slate-300 text-[11px]">Desacelerações tardias repetidas e imotivadas sem contração, bradicardia sustentada ou Padrão Sinusoidal verdadeiro.</span>
          </div>
          <div class="p-3 rounded-2xl bg-white/5 border border-white/10 space-y-1">
            <span class="font-bold text-red-400 block">4. Variação de Curto Prazo</span>
            <span class="text-slate-300 text-[11px]">STV (*Short-Term Variation*) &lt; 2,6 ms na Cardiotocografia computadorizada.</span>
          </div>
        </div>
      </div>

    </div>

    <!-- =========================================================================
         10. ARENA DE TREINAMENTO: CASOS REAIS DE CTG (PROF. PHELIPE BALBI)
         ========================================================================= -->
    <div class="space-y-6">
      <div class="flex items-center gap-3">
        <span class="w-8 h-8 rounded-xl bg-teal-600 text-white flex items-center justify-center font-black text-sm shadow-md">10</span>
        <div>
          <h3 class="text-lg sm:text-xl font-bold text-slate-900 dark:text-white">Para Treinar... Casos Práticos com Traçados Reais de CTG</h3>
          <p class="text-xs text-slate-500">Desafios baseados nas folhas reais de cardiotocografia apresentadas em aula pelo Prof. Phelipe Balbi</p>
        </div>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-6 text-xs">
        
        <!-- CASO PRÁTICO 1: DIP III DESFAVORÁVEL -->
        <div class="p-5 rounded-3xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 shadow-sm space-y-3">
          <div class="flex items-center justify-between">
            <span class="text-[10px] font-black uppercase text-rose-600 tracking-wider">Desafio Prático 01</span>
            <span class="px-2 py-0.5 rounded text-[10px] font-bold bg-rose-100 text-rose-900 dark:bg-rose-950 dark:text-rose-200">Caso 1</span>
          </div>
          <h4 class="font-bold text-sm text-slate-900 dark:text-white">Análise do Traçado: Paciente Tauane</h4>
          
          <!-- Monitor de Telemetria com Fita Limpa -->
          <div class="rounded-2xl overflow-hidden border border-slate-800 bg-slate-950 shadow-md">
            <div class="bg-slate-900 px-3 py-1.5 border-b border-slate-800 flex items-center justify-between text-[10px] text-slate-400">
              <span class="text-emerald-400 font-mono flex items-center gap-1.5">
                <span class="w-2 h-2 rounded-full bg-emerald-500 animate-pulse"></span> CANAL CTG #01
              </span>
              <span class="font-mono">Vel: 1 cm/min</span>
            </div>
            <div class="p-1 cursor-pointer" onclick="openLightbox('assets/img/ctg_strip_caso1.jpg', 'Caso 1: Fita de CTG Limpa', 'Analise a frequência das desacelerações, amplitude, morfologia e relação com as contrações.')">
              <img src="assets/img/ctg_strip_caso1.jpg" alt="Fita de CTG do Caso 1" class="w-full h-auto object-contain hover:scale-105 transition-transform duration-300 rounded-lg">
            </div>
          </div>
          
          <p class="text-slate-600 dark:text-slate-400 text-[11px]">
            Gestante em trabalho de parto ativo apresenta o traçado acima com quedas abruptas da FCF de grande amplitude.
          </p>

          <div class="space-y-1.5 pt-1">
            <label class="block font-bold text-slate-700 dark:text-slate-300 text-[11px]">Qual o diagnóstico cardiotocográfico?</label>
            <select id="ctg-quiz-1" class="w-full p-2 text-xs rounded-xl border border-slate-300 dark:border-slate-700 bg-slate-50 dark:bg-slate-800">
              <option value="">Selecione sua resposta...</option>
              <option value="dip1">DIP Tipo I (Cefálico / Fisiológico)</option>
              <option value="dip3_desfav">DIP Tipo III (Desaceleração Variável Desfavorável)</option>
              <option value="dip2">DIP Tipo II (Tardio / Placentário)</option>
              <option value="cat1">Traçado Categoria 1 Normal</option>
            </select>
            <button onclick="responderQuizCTG(1)" class="w-full py-2 px-3 rounded-xl bg-teal-600 hover:bg-teal-700 text-white font-bold text-xs transition-colors shadow">
              Conferir Análise do Professor
            </button>
            <div id="ctg-quiz-res-1" class="hidden p-3 rounded-xl border text-xs space-y-2"></div>
          </div>
        </div>

        <!-- CASO PRÁTICO 2: DIP I PRECOCE -->
        <div class="p-5 rounded-3xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 shadow-sm space-y-3">
          <div class="flex items-center justify-between">
            <span class="text-[10px] font-black uppercase text-emerald-600 tracking-wider">Desafio Prático 02</span>
            <span class="px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-100 text-emerald-900 dark:bg-emerald-950 dark:text-emerald-200">Caso 2</span>
          </div>
          <h4 class="font-bold text-sm text-slate-900 dark:text-white">Análise do Traçado: Paciente Jamile</h4>
          
          <!-- Monitor de Telemetria com Fita Limpa -->
          <div class="rounded-2xl overflow-hidden border border-slate-800 bg-slate-950 shadow-md">
            <div class="bg-slate-900 px-3 py-1.5 border-b border-slate-800 flex items-center justify-between text-[10px] text-slate-400">
              <span class="text-emerald-400 font-mono flex items-center gap-1.5">
                <span class="w-2 h-2 rounded-full bg-emerald-500 animate-pulse"></span> CANAL CTG #02
              </span>
              <span class="font-mono">Vel: 1 cm/min</span>
            </div>
            <div class="p-1 cursor-pointer" onclick="openLightbox('assets/img/ctg_strip_caso2.jpg', 'Caso 2: Fita de CTG Limpa', 'Observe a simultaneidade entre o início da contração e o início da desaceleração.')">
              <img src="assets/img/ctg_strip_caso2.jpg" alt="Fita de CTG do Caso 2" class="w-full h-auto object-contain hover:scale-105 transition-transform duration-300 rounded-lg">
            </div>
          </div>
          
          <p class="text-slate-600 dark:text-slate-400 text-[11px]">
            Parturiente com 6 cm de dilatação cervical; note que o nadir da desaceleração coincide exatamente com o acme da contração uterina.
          </p>

          <div class="space-y-1.5 pt-1">
            <label class="block font-bold text-slate-700 dark:text-slate-300 text-[11px]">Qual o diagnóstico e conduta?</label>
            <select id="ctg-quiz-2" class="w-full p-2 text-xs rounded-xl border border-slate-300 dark:border-slate-700 bg-slate-50 dark:bg-slate-800">
              <option value="">Selecione sua resposta...</option>
              <option value="dip1">DIP Tipo I (Precoce / Cefálica) - Conduta Expectante</option>
              <option value="dip2">DIP Tipo II (Tardia) - Cesárea de Emergência</option>
              <option value="dip3">DIP Tipo III Grave - Interromper Parto</option>
              <option value="sinusoidal">Padrão Sinusoidal - Transfusão Intrauterina</option>
            </select>
            <button onclick="responderQuizCTG(2)" class="w-full py-2 px-3 rounded-xl bg-teal-600 hover:bg-teal-700 text-white font-bold text-xs transition-colors shadow">
              Conferir Análise do Professor
            </button>
            <div id="ctg-quiz-res-2" class="hidden p-3 rounded-xl border text-xs space-y-2"></div>
          </div>
        </div>

        <!-- CASO PRÁTICO 3: CATEGORIA 1 NORMAL -->
        <div class="p-5 rounded-3xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 shadow-sm space-y-3">
          <div class="flex items-center justify-between">
            <span class="text-[10px] font-black uppercase text-teal-600 tracking-wider">Desafio Prático 03</span>
            <span class="px-2 py-0.5 rounded text-[10px] font-bold bg-teal-100 text-teal-900 dark:bg-teal-950 dark:text-teal-200">Caso 3</span>
          </div>
          <h4 class="font-bold text-sm text-slate-900 dark:text-white">Análise do Traçado: Classificação Geral</h4>
          
          <!-- Monitor de Telemetria com Fita Limpa -->
          <div class="rounded-2xl overflow-hidden border border-slate-800 bg-slate-950 shadow-md">
            <div class="bg-slate-900 px-3 py-1.5 border-b border-slate-800 flex items-center justify-between text-[10px] text-slate-400">
              <span class="text-emerald-400 font-mono flex items-center gap-1.5">
                <span class="w-2 h-2 rounded-full bg-emerald-500 animate-pulse"></span> CANAL CTG #03
              </span>
              <span class="font-mono">Vel: 1 cm/min</span>
            </div>
            <div class="p-1 cursor-pointer" onclick="openLightbox('assets/img/ctg_strip_caso3.jpg', 'Caso 3: Fita de CTG Limpa', 'Avalie a linha de base em torno de 135-140 bpm, variabilidade de 10-15 bpm e acelerações transitórias presentes.')">
              <img src="assets/img/ctg_strip_caso3.jpg" alt="Fita de CTG do Caso 3" class="w-full h-auto object-contain hover:scale-105 transition-transform duration-300 rounded-lg">
            </div>
          </div>
          
          <p class="text-slate-600 dark:text-slate-400 text-[11px]">
            Traçado com linha de base em 135-140 bpm, variabilidade moderada e acelerações espontâneas sem desacelerações patológicas.
          </p>

          <div class="space-y-1.5 pt-1">
            <label class="block font-bold text-slate-700 dark:text-slate-300 text-[11px]">Em qual categoria se enquadra?</label>
            <select id="ctg-quiz-3" class="w-full p-2 text-xs rounded-xl border border-slate-300 dark:border-slate-700 bg-slate-50 dark:bg-slate-800">
              <option value="">Selecione sua resposta...</option>
              <option value="cat1">Categoria 1 (Padrão Normal / Tranquilizador)</option>
              <option value="cat2">Categoria 2 (Indeterminado / Vigilância)</option>
              <option value="cat3">Categoria 3 (Anormal / Sofrimento Fetal)</option>
              <option value="sfa">Sofrimento Fetal Agudo Grave</option>
            </select>
            <button onclick="responderQuizCTG(3)" class="w-full py-2 px-3 rounded-xl bg-teal-600 hover:bg-teal-700 text-white font-bold text-xs transition-colors shadow">
              Conferir Análise do Professor
            </button>
            <div id="ctg-quiz-res-3" class="hidden p-3 rounded-xl border text-xs space-y-2"></div>
          </div>
        </div>

      </div>
    </div>

  </div>
</section>
'''

with open(comp_file, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Successfully wrote elevated modulo-6 component! Lines: {len(html_content.splitlines())}")
