"""
build_site.py - Gerador do Portal Interativo de Ginecologia Geral (Parte 5)
Compatível com GitHub Pages • Padrão USMLE Step 2 CK / FEBRASGO / SUS / ACOG / FIGO / ESHRE
"""

import os

BASE_DIR = r"c:\Users\Admin\Downloads\INTERNATO GO\site_ginecologia_geral"
OUTPUT_HTML = os.path.join(BASE_DIR, "index.html")

def generate_html():
    html = """<!DOCTYPE html>
<html lang="pt-BR" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Ginecologia Geral | Portal Médico Interativo</title>
  <meta name="description" content="Guia Completo e Interativo de Ginecologia Geral (Parte 5). USMLE Step 2 CK, Residência Médica, FEBRASGO, Ministério da Saúde / SUS, FIGO e ESHRE.">

  <!-- Previne Flash of Unstyled Content (FOUC) ao carregar tema escuro -->
  <script>
    (function() {
      try {
        const saved = localStorage.getItem('theme');
        const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
        if (saved === 'dark' || (!saved && prefersDark)) {
          document.documentElement.classList.add('dark');
        } else {
          document.documentElement.classList.remove('dark');
        }
      } catch (e) {}
    })();
  </script>

  <!-- Tailwind CSS CDN -->
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {
      darkMode: 'class',
      theme: {
        extend: {
          screens: {
            'xs': '480px'
          },
          colors: {
            sus: {
              blue: '#0284c7',
              navy: '#0f172a',
              sky: '#38bdf8',
              emerald: '#059669',
              amber: '#d97706',
              rose: '#e11d48'
            }
          }
        }
      }
    }
  </script>

  <!-- Lucide Icons -->
  <script src="https://unpkg.com/lucide@latest"></script>

  <!-- Custom CSS -->
  <link rel="stylesheet" href="assets/css/custom.css">
</head>
<body class="bg-slate-50 dark:bg-slate-950 text-slate-800 dark:text-slate-100 min-h-screen flex flex-col antialiased transition-colors duration-200">

  <!-- ======================================================================
       HEADER / NAVBAR COM DESIGN MULTI-NÍVEL RESPONSIVO & ELEGANTE
       ====================================================================== -->
  <header class="sticky top-0 z-40 glass-nav border-b border-slate-200/80 dark:border-slate-800/80 transition-colors">
    <!-- Nível 1: Barra Principal -->
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex items-center justify-between h-16 gap-3 lg:gap-4">
        
        <!-- Logo e Título com Identidade Visual SUS / FEBRASGO / FIGO / ESHRE -->
        <a href="#" class="flex items-center gap-3 flex-shrink-0 group" title="Ir para o início">
          <div class="w-10 h-10 rounded-xl bg-gradient-to-tr from-rose-600 via-pink-500 to-indigo-600 flex items-center justify-center text-white shadow-md shadow-rose-500/20 group-hover:scale-105 transition-transform flex-shrink-0">
            <i data-lucide="flower-2" class="w-5 h-5"></i>
          </div>
          <div>
            <div class="flex items-center gap-2">
              <span class="font-extrabold text-sm sm:text-base tracking-tight text-slate-900 dark:text-white">Ginecologia Geral</span>
              <span class="text-[10px] uppercase font-bold tracking-wider px-1.5 py-0.5 rounded bg-rose-100 text-rose-800 dark:bg-rose-950 dark:text-rose-300 border border-rose-200 dark:border-rose-800 hidden xs:inline-block">PCDT / SUS</span>
            </div>
            <span class="text-[11px] text-slate-500 dark:text-slate-400 font-medium hidden sm:block">USMLE Step 2 CK • Residência Médica • FEBRASGO • FIGO</span>
          </div>
        </a>

        <!-- Barra de Busca Global Inteligente (Desktop & Tablet) -->
        <div class="hidden md:flex items-center flex-1 max-w-sm lg:max-w-md mx-2 lg:mx-4">
          <div class="relative w-full">
            <i data-lucide="search" class="w-4 h-4 absolute left-3 top-1/2 -translate-y-1/2 text-slate-400"></i>
            <input type="text" id="global-search" placeholder="Buscar módulos, condutas (ex: PALM-COEIN, SOP, Miomas, ESHRE...)" 
              class="w-full pl-9 pr-14 py-2 text-xs rounded-xl bg-slate-100/90 dark:bg-slate-900/90 border border-slate-200 dark:border-slate-800 focus:outline-none focus:ring-2 focus:ring-rose-500 text-slate-800 dark:text-slate-200 placeholder-slate-400 transition-all">
            <kbd class="hidden lg:inline-flex items-center absolute right-2.5 top-1/2 -translate-y-1/2 px-1.5 py-0.5 text-[10px] font-semibold text-slate-400 dark:text-slate-500 bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 rounded shadow-sm">Ctrl K</kbd>
          </div>
        </div>

        <!-- Ações Rápidas de Estudo, Botão de Tema e Menu Mobile -->
        <div class="flex items-center gap-1.5 sm:gap-2">
          <!-- Atalho Calculadoras -->
          <a href="#ferramentas-clinicas" class="hidden xl:inline-flex items-center gap-1.5 px-3 py-1.5 text-xs font-bold rounded-lg text-rose-700 dark:text-rose-300 bg-rose-50 dark:bg-rose-950/60 border border-rose-200 dark:border-rose-800 hover:bg-rose-100 transition-colors">
            <i data-lucide="calculator" class="w-3.5 h-3.5"></i>
            <span>Calculadoras</span>
          </a>

          <!-- Atalho Flashcards -->
          <a href="#estudo-ativo" class="hidden xl:inline-flex items-center gap-1.5 px-3 py-1.5 text-xs font-bold rounded-lg text-indigo-700 dark:text-indigo-300 bg-indigo-50 dark:bg-indigo-950/60 border border-indigo-200 dark:border-indigo-800 hover:bg-indigo-100 transition-colors">
            <i data-lucide="layers" class="w-3.5 h-3.5"></i>
            <span>Flashcards</span>
          </a>

          <!-- Atalho Simulado -->
          <a href="#simulado-clinico" class="hidden xl:inline-flex items-center gap-1.5 px-3 py-1.5 text-xs font-bold rounded-lg text-emerald-700 dark:text-emerald-300 bg-emerald-50 dark:bg-emerald-950/60 border border-emerald-200 dark:border-emerald-800 hover:bg-emerald-100 transition-colors">
            <i data-lucide="check-circle-2" class="w-3.5 h-3.5"></i>
            <span>Simulado (15Q)</span>
          </a>

          <!-- Botão Modo Claro / Escuro -->
          <button type="button" id="theme-toggle" class="p-2 rounded-xl text-slate-600 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-800 transition-colors border border-transparent hover:border-slate-200 dark:hover:border-slate-700" title="Alternar tema">
            <i data-lucide="moon" class="w-4 h-4 icon-moon"></i>
            <i data-lucide="sun" class="w-4 h-4 icon-sun"></i>
          </button>

          <!-- Botão Menu Mobile -->
          <button type="button" id="mobile-menu-toggle" class="p-2 rounded-xl text-slate-600 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-800 transition-colors border border-transparent md:hidden" aria-label="Abrir menu" aria-expanded="false">
            <i data-lucide="menu" id="mobile-menu-icon" class="w-5 h-5"></i>
          </button>
        </div>
      </div>
    </div>

    <!-- Nível 2: Faixa de Navegação Rápida entre Módulos (Subnav Ribbon) -->
    <div class="border-t border-slate-200/60 dark:border-slate-800/60 bg-slate-50/70 dark:bg-slate-900/70 overflow-x-auto no-scrollbar">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <nav class="flex items-center gap-1 py-1.5 text-xs font-semibold whitespace-nowrap min-w-max">
          <a href="#modulo-40" class="px-2.5 py-1 rounded-md text-slate-600 dark:text-slate-300 hover:text-rose-600 dark:hover:text-rose-400 hover:bg-slate-200/60 dark:hover:bg-slate-800 transition-colors">M40: Ciclo Menstrual</a>
          <span class="text-slate-300 dark:text-slate-700">•</span>
          <a href="#modulo-41" class="px-2.5 py-1 rounded-md text-slate-600 dark:text-slate-300 hover:text-rose-600 dark:hover:text-rose-400 hover:bg-slate-200/60 dark:hover:bg-slate-800 transition-colors">M41: SUA (PALM-COEIN)</a>
          <span class="text-slate-300 dark:text-slate-700">•</span>
          <a href="#modulo-41-sop" class="px-2.5 py-1 rounded-md text-slate-600 dark:text-slate-300 hover:text-rose-600 dark:hover:text-rose-400 hover:bg-slate-200/60 dark:hover:bg-slate-800 transition-colors">M41.8: SOP (Rotterdam)</a>
          <span class="text-slate-300 dark:text-slate-700">•</span>
          <a href="#modulo-42" class="px-2.5 py-1 rounded-md text-slate-600 dark:text-slate-300 hover:text-rose-600 dark:hover:text-rose-400 hover:bg-slate-200/60 dark:hover:bg-slate-800 transition-colors">M42: Miomas (FIGO 0-8)</a>
          <span class="text-slate-300 dark:text-slate-700">•</span>
          <a href="#modulo-43" class="px-2.5 py-1 rounded-md text-slate-600 dark:text-slate-300 hover:text-rose-600 dark:hover:text-rose-400 hover:bg-slate-200/60 dark:hover:bg-slate-800 transition-colors">M43: Adenomiose</a>
          <span class="text-slate-300 dark:text-slate-700">•</span>
          <a href="#modulo-44" class="px-2.5 py-1 rounded-md text-slate-600 dark:text-slate-300 hover:text-rose-600 dark:hover:text-rose-400 hover:bg-slate-200/60 dark:hover:bg-slate-800 transition-colors">M44: Endometriose</a>
          <span class="text-slate-300 dark:text-slate-700">•</span>
          <a href="#modulo-45" class="px-2.5 py-1 rounded-md text-slate-600 dark:text-slate-300 hover:text-rose-600 dark:hover:text-rose-400 hover:bg-slate-200/60 dark:hover:bg-slate-800 transition-colors">M45: Massas Anexiais</a>
          <span class="text-slate-300 dark:text-slate-700">•</span>
          <a href="#modulo-46" class="px-2.5 py-1 rounded-md text-slate-600 dark:text-slate-300 hover:text-rose-600 dark:hover:text-rose-400 hover:bg-slate-200/60 dark:hover:bg-slate-800 transition-colors">M46: Dor Pélvica & DPC</a>
          <span class="text-slate-300 dark:text-slate-700">•</span>
          <a href="#modulo-47" class="px-2.5 py-1 rounded-md text-slate-600 dark:text-slate-300 hover:text-rose-600 dark:hover:text-rose-400 hover:bg-slate-200/60 dark:hover:bg-slate-800 transition-colors">M47: Menopausa & TH</a>
          <span class="text-slate-300 dark:text-slate-700">•</span>
          <a href="#modulo-48" class="px-2.5 py-1 rounded-md text-slate-600 dark:text-slate-300 hover:text-rose-600 dark:hover:text-rose-400 hover:bg-slate-200/60 dark:hover:bg-slate-800 transition-colors">M48: Amenorreias</a>
          <span class="text-slate-300 dark:text-slate-700">•</span>
          <a href="#modulo-49" class="px-2.5 py-1 rounded-md text-slate-600 dark:text-slate-300 hover:text-rose-600 dark:hover:text-rose-400 hover:bg-slate-200/60 dark:hover:bg-slate-800 transition-colors">M49: Infertilidade</a>
          <span class="text-slate-300 dark:text-slate-700">•</span>
          <a href="#ferramentas-clinicas" class="px-2.5 py-1 rounded-md text-rose-600 dark:text-rose-400 font-bold hover:bg-rose-50 dark:hover:bg-rose-950 transition-colors">🧮 Calculadoras</a>
          <span class="text-slate-300 dark:text-slate-700">•</span>
          <a href="#estudo-ativo" class="px-2.5 py-1 rounded-md text-indigo-600 dark:text-indigo-400 font-bold hover:bg-indigo-50 dark:hover:bg-indigo-950 transition-colors">🃏 Flashcards</a>
          <span class="text-slate-300 dark:text-slate-700">•</span>
          <a href="#simulado-clinico" class="px-2.5 py-1 rounded-md text-emerald-600 dark:text-emerald-400 font-bold hover:bg-emerald-50 dark:hover:bg-emerald-950 transition-colors">📝 Simulado</a>
        </nav>
      </div>
    </div>
  </header>

  <!-- Gaveta Mobile (Drawer) -->
  <div id="mobile-menu-drawer" class="hidden md:hidden fixed inset-x-0 top-24 bottom-0 z-30 bg-slate-900/60 backdrop-blur-sm p-4 overflow-y-auto">
    <div class="bg-white dark:bg-slate-900 rounded-2xl p-4 shadow-xl border border-slate-200 dark:border-slate-800 space-y-4">
      <div class="relative">
        <i data-lucide="search" class="w-4 h-4 absolute left-3 top-1/2 -translate-y-1/2 text-slate-400"></i>
        <input type="text" id="mobile-search" placeholder="Buscar no guia..." 
          class="w-full pl-9 pr-3 py-2 text-xs rounded-xl bg-slate-100 dark:bg-slate-800 border border-slate-200 dark:border-slate-700 focus:outline-none focus:ring-2 focus:ring-rose-500 text-slate-800 dark:text-slate-200">
      </div>
      <div class="grid grid-cols-2 gap-2 text-xs font-semibold">
        <a href="#modulo-40" class="p-2.5 rounded-xl bg-slate-50 dark:bg-slate-800 hover:bg-rose-50 dark:hover:bg-rose-950">M40: Ciclo Menstrual</a>
        <a href="#modulo-41" class="p-2.5 rounded-xl bg-slate-50 dark:bg-slate-800 hover:bg-rose-50 dark:hover:bg-rose-950">M41: SUA (PALM-COEIN)</a>
        <a href="#modulo-41-sop" class="p-2.5 rounded-xl bg-slate-50 dark:bg-slate-800 hover:bg-rose-50 dark:hover:bg-rose-950">M41.8: SOP (Rotterdam)</a>
        <a href="#modulo-42" class="p-2.5 rounded-xl bg-slate-50 dark:bg-slate-800 hover:bg-rose-50 dark:hover:bg-rose-950">M42: Miomas (FIGO)</a>
        <a href="#modulo-43" class="p-2.5 rounded-xl bg-slate-50 dark:bg-slate-800 hover:bg-rose-50 dark:hover:bg-rose-950">M43: Adenomiose</a>
        <a href="#modulo-44" class="p-2.5 rounded-xl bg-slate-50 dark:bg-slate-800 hover:bg-rose-50 dark:hover:bg-rose-950">M44: Endometriose</a>
        <a href="#modulo-45" class="p-2.5 rounded-xl bg-slate-50 dark:bg-slate-800 hover:bg-rose-50 dark:hover:bg-rose-950">M45: Massas Anexiais</a>
        <a href="#modulo-46" class="p-2.5 rounded-xl bg-slate-50 dark:bg-slate-800 hover:bg-rose-50 dark:hover:bg-rose-950">M46: Dor Pélvica & DPC</a>
        <a href="#modulo-47" class="p-2.5 rounded-xl bg-slate-50 dark:bg-slate-800 hover:bg-rose-50 dark:hover:bg-rose-950">M47: Menopausa & TH</a>
        <a href="#modulo-48" class="p-2.5 rounded-xl bg-slate-50 dark:bg-slate-800 hover:bg-rose-50 dark:hover:bg-rose-950">M48: Amenorreias</a>
        <a href="#modulo-49" class="p-2.5 rounded-xl bg-slate-50 dark:bg-slate-800 hover:bg-rose-50 dark:hover:bg-rose-950">M49: Infertilidade</a>
        <a href="#ferramentas-clinicas" class="p-2.5 rounded-xl bg-rose-50 dark:bg-rose-950 text-rose-700 dark:text-rose-300 font-bold">🧮 Calculadoras</a>
        <a href="#estudo-ativo" class="p-2.5 rounded-xl bg-indigo-50 dark:bg-indigo-950 text-indigo-700 dark:text-indigo-300 font-bold">🃏 Flashcards</a>
        <a href="#simulado-clinico" class="p-2.5 rounded-xl bg-emerald-50 dark:bg-emerald-950 text-emerald-700 dark:text-emerald-300 font-bold">📝 Simulado (15Q)</a>
      </div>
    </div>
  </div>

  <!-- ======================================================================
       HERO BANNER COM IDENTIDADE VISUAL E REGRAS DE OURO
       ====================================================================== -->
  <section class="relative overflow-hidden bg-gradient-to-b from-rose-50 via-slate-50 to-white dark:from-slate-900 dark:via-slate-950 dark:to-slate-950 border-b border-slate-200 dark:border-slate-800 py-12 lg:py-16">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
      <div class="text-center max-w-3xl mx-auto space-y-4">
        <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-rose-100 dark:bg-rose-950 text-rose-800 dark:text-rose-300 text-xs font-bold border border-rose-200 dark:border-rose-800">
          <i data-lucide="shield-check" class="w-3.5 h-3.5"></i>
          <span>Guia Completo de Obstetrícia & Ginecologia • Parte 5: Ginecologia Geral</span>
        </div>
        <h1 class="text-3xl sm:text-4xl lg:text-5xl font-black tracking-tight text-slate-900 dark:text-white leading-tight">
          Portal Interativo de <span class="bg-gradient-to-r from-rose-600 via-pink-600 to-indigo-600 bg-clip-text text-transparent">Ginecologia Geral</span>
        </h1>
        <p class="text-sm sm:text-base text-slate-600 dark:text-slate-300 leading-relaxed font-normal">
          Da neuroendocrinologia do ciclo menstrual à medicina reprodutiva avançada. Dominância prática para <strong>USMLE Step 2 CK / Step 3</strong>, <strong>Provas de Título FEBRASGO</strong>, <strong>Residência Médica</strong> e <strong>PCDT / SUS</strong>.
        </p>

        <!-- Banner Regra nº 1 -->
        <div class="mt-6 p-4 rounded-2xl bg-amber-50 dark:bg-amber-950/40 border-2 border-amber-300 dark:border-amber-800 text-amber-950 dark:text-amber-200 text-xs sm:text-sm font-semibold max-w-2xl mx-auto flex items-center justify-center gap-3 shadow-sm">
          <i data-lucide="alert-triangle" class="w-5 h-5 text-amber-600 shrink-0"></i>
          <span><strong>Regra nº 1 de toda a ginecologia:</strong> Em qualquer mulher em idade reprodutiva com sangramento anormal, dor pélvica ou amenorreia, <u>o primeiro exame é sempre o β-hCG</u>!</span>
        </div>
      </div>
    </div>
  </section>

  <!-- Alerta de "Nenhum resultado" na busca -->
  <div id="search-no-results" class="hidden max-w-md mx-auto my-6 p-4 rounded-2xl bg-amber-50 dark:bg-amber-950 text-amber-900 dark:text-amber-200 text-xs text-center border border-amber-200 dark:border-amber-800">
    <i data-lucide="alert-circle" class="w-5 h-5 mx-auto mb-1 text-amber-600"></i>
    Nenhum módulo encontrado para o termo pesquisado. Tente termos como "PALM", "SOP", "Mioma", "ESHRE", "O-RADS" ou "Menopausa".
  </div>

  <!-- ======================================================================
       CONTEÚDO PRINCIPAL: MÓDULOS M40 AO M49
       ====================================================================== -->
  <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 space-y-16 flex-1">

    <!-- ====================================================================
         MÓDULO 40: O CICLO MENSTRUAL EM 1 MINUTO
         ==================================================================== -->
    <section id="modulo-40" class="module-card space-y-6 scroll-mt-28">
      <div class="border-b border-slate-200 dark:border-slate-800 pb-4 flex items-center justify-between flex-wrap gap-2">
        <div class="flex items-center gap-3">
          <span class="w-10 h-10 rounded-xl bg-rose-600 text-white font-black text-lg flex items-center justify-center shadow-md">40</span>
          <div>
            <h2 class="text-xl sm:text-2xl font-black text-slate-900 dark:text-white">O Ciclo Menstrual em 1 Minuto</h2>
            <p class="text-xs sm:text-sm text-slate-500 dark:text-slate-400">A Base Fisiológica Central: Eixo Hipotálamo-Hipófise-Ovário & Parâmetros FIGO</p>
          </div>
        </div>
        <span class="px-2.5 py-1 text-xs font-bold rounded-full bg-rose-100 text-rose-800 dark:bg-rose-950 dark:text-rose-300">Fisiologia Geral</span>
      </div>

      <!-- Analogia Didática -->
      <div class="p-4 rounded-2xl bg-amber-50 dark:bg-amber-950/40 border border-amber-200 dark:border-amber-800 text-xs sm:text-sm leading-relaxed text-amber-900 dark:text-amber-200">
        <span class="font-bold text-amber-800 dark:text-amber-300">🎈 Analogia Didática:</span> O ciclo é uma <strong>orquestra</strong> com um maestro (<strong>hipotálamo</strong>, pulsos de GnRH), um spalla (<strong>hipófise</strong>, FSH e LH), os músicos (<strong>ovários</strong>, que produzem estrogênio e progesterona) e o palco (<strong>endométrio</strong>).
        <ul class="list-disc list-inside mt-2 space-y-1">
          <li><strong>1ª metade (fase folicular):</strong> O <strong>estrogênio</strong> é o "adubo" que faz o endométrio crescer.</li>
          <li><strong>Ovulação:</strong> O <strong>pico de LH</strong> solta o óvulo (36h após o início do surto).</li>
          <li><strong>2ª metade (fase lútea):</strong> A <strong>progesterona</strong> é o "cimento" que deixa o endométrio firme e organizado.</li>
          <li><strong>Sem gravidez:</strong> O corpo lúteo involui &rarr; a progesterona despenca &rarr; o endométrio desaba de forma organizada = <strong>menstruação</strong>.</li>
        </ul>
      </div>

      <!-- Imagem Infográfica M40 -->
      <div class="rounded-2xl overflow-hidden border border-slate-200 dark:border-slate-800 shadow-md group relative">
        <img src="assets/img/ciclo_menstrual_eixo_hho.jpg" alt="Fisiologia do Ciclo Menstrual & Eixo HHO" class="w-full h-auto cursor-pointer zoomable-image group-hover:scale-[1.01] transition-transform">
        <div class="p-3 bg-white/90 dark:bg-slate-900/90 text-xs text-slate-500 dark:text-slate-400 flex items-center justify-between">
          <span>Figura 40.1: Fisiologia Integrada do Ciclo Menstrual, Eixo HHO e Parâmetros FIGO</span>
          <span class="text-rose-600 dark:text-rose-400 font-bold flex items-center gap-1"><i data-lucide="zoom-in" class="w-3.5 h-3.5"></i> Clique para ampliar</span>
        </div>
      </div>
    </section>

    <!-- ====================================================================
         MÓDULO 41: SANGRAMENTO UTERINO ANORMAL (SUA) & PALM-COEIN
         ==================================================================== -->
    <section id="modulo-41" class="module-card space-y-6 scroll-mt-28">
      <div class="border-b border-slate-200 dark:border-slate-800 pb-4 flex items-center justify-between flex-wrap gap-2">
        <div class="flex items-center gap-3">
          <span class="w-10 h-10 rounded-xl bg-rose-600 text-white font-black text-lg flex items-center justify-center shadow-md">41</span>
          <div>
            <h2 class="text-xl sm:text-2xl font-black text-slate-900 dark:text-white">Sangramento Uterino Anormal (SUA)</h2>
            <p class="text-xs sm:text-sm text-slate-500 dark:text-slate-400">Classificação PALM-COEIN FIGO, Triagem de Coagulopatias & Algoritmo de Biópsia</p>
          </div>
        </div>
        <span class="px-2.5 py-1 text-xs font-bold rounded-full bg-blue-100 text-blue-800 dark:bg-blue-950 dark:text-blue-300">FIGO 2018</span>
      </div>

      <!-- Analogia PALM-COEIN -->
      <div class="p-4 rounded-2xl bg-amber-50 dark:bg-amber-950/40 border border-amber-200 dark:border-amber-800 text-xs sm:text-sm leading-relaxed text-amber-900 dark:text-amber-200">
        <span class="font-bold text-amber-800 dark:text-amber-300">🎈 Analogia:</span> <strong>PALM</strong> são alterações que <strong>dá para ver ou palpar</strong> (estruturais, como uma 'palmeira'). <strong>COEIN</strong> são alterações <strong>invisíveis aos olhos</strong> (distúrbios funcionais, sistêmicos ou de hemostasia local).
      </div>

      <!-- Classificador Interativo PALM-COEIN -->
      <div class="p-5 rounded-2xl border border-slate-200 dark:border-slate-800 bg-slate-50/80 dark:bg-slate-900/60 space-y-4">
        <div class="flex items-center justify-between flex-wrap gap-2">
          <h3 class="font-extrabold text-sm sm:text-base text-slate-900 dark:text-white flex items-center gap-2">
            <i data-lucide="layers" class="w-4 h-4 text-rose-600"></i>
            Navegador Interativo PALM-COEIN (Clique na letra para explorar)
          </h3>
          <span class="text-xs text-slate-500">Selecione uma categoria</span>
        </div>

        <div class="flex flex-wrap gap-2">
          <button type="button" data-letter="P" class="palm-btn px-3 py-1.5 rounded-xl border border-rose-300 dark:border-rose-800 bg-white dark:bg-slate-800 text-xs font-bold hover:bg-rose-50 transition-all">P - Pólipo</button>
          <button type="button" data-letter="A" class="palm-btn px-3 py-1.5 rounded-xl border border-rose-300 dark:border-rose-800 bg-white dark:bg-slate-800 text-xs font-bold hover:bg-rose-50 transition-all">A - Adenomiose</button>
          <button type="button" data-letter="L" class="palm-btn px-3 py-1.5 rounded-xl border border-rose-300 dark:border-rose-800 bg-white dark:bg-slate-800 text-xs font-bold hover:bg-rose-50 transition-all">L - Leiomioma</button>
          <button type="button" data-letter="M" class="palm-btn px-3 py-1.5 rounded-xl border border-rose-300 dark:border-rose-800 bg-white dark:bg-slate-800 text-xs font-bold hover:bg-rose-50 transition-all">M - Malignidade</button>
          <button type="button" data-letter="C" class="palm-btn px-3 py-1.5 rounded-xl border border-blue-300 dark:border-blue-800 bg-white dark:bg-slate-800 text-xs font-bold hover:bg-blue-50 transition-all">C - Coagulopatia</button>
          <button type="button" data-letter="O" class="palm-btn px-3 py-1.5 rounded-xl border border-blue-300 dark:border-blue-800 bg-white dark:bg-slate-800 text-xs font-bold hover:bg-blue-50 transition-all">O - Ovulatória</button>
          <button type="button" data-letter="E" class="palm-btn px-3 py-1.5 rounded-xl border border-blue-300 dark:border-blue-800 bg-white dark:bg-slate-800 text-xs font-bold hover:bg-blue-50 transition-all">E - Endometrial</button>
          <button type="button" data-letter="I" class="palm-btn px-3 py-1.5 rounded-xl border border-blue-300 dark:border-blue-800 bg-white dark:bg-slate-800 text-xs font-bold hover:bg-blue-50 transition-all">I - Iatrogênica</button>
          <button type="button" data-letter="N" class="palm-btn px-3 py-1.5 rounded-xl border border-blue-300 dark:border-blue-800 bg-white dark:bg-slate-800 text-xs font-bold hover:bg-blue-50 transition-all">N - Não Classificada</button>
        </div>

        <div id="palm-details" class="transition-all"></div>
      </div>

      <!-- Imagem Infográfica M41 -->
      <div class="rounded-2xl overflow-hidden border border-slate-200 dark:border-slate-800 shadow-md group relative">
        <img src="assets/img/sangramento_uterino_palm_coein.jpg" alt="Classificação PALM-COEIN FIGO e Algoritmo de Biópsia" class="w-full h-auto cursor-pointer zoomable-image group-hover:scale-[1.01] transition-transform">
        <div class="p-3 bg-white/90 dark:bg-slate-900/90 text-xs text-slate-500 dark:text-slate-400 flex items-center justify-between">
          <span>Figura 41.1: Mapeamento PALM-COEIN, Sangramento Pós-Menopausa e Hiperplasia Endometrial OMS 2020</span>
          <span class="text-rose-600 dark:text-rose-400 font-bold flex items-center gap-1"><i data-lucide="zoom-in" class="w-3.5 h-3.5"></i> Clique para ampliar</span>
        </div>
      </div>
    </section>

    <!-- ====================================================================
         MÓDULO 41.8: SÍNDROME DOS OVÁRIOS POLICÍSTICOS (SOP)
         ==================================================================== -->
    <section id="modulo-41-sop" class="module-card space-y-6 scroll-mt-28">
      <div class="border-b border-slate-200 dark:border-slate-800 pb-4 flex items-center justify-between flex-wrap gap-2">
        <div class="flex items-center gap-3">
          <span class="w-10 h-10 rounded-xl bg-pink-600 text-white font-black text-lg flex items-center justify-center shadow-md">41.8</span>
          <div>
            <h2 class="text-xl sm:text-2xl font-black text-slate-900 dark:text-white">Síndrome dos Ovários Policísticos (SOP)</h2>
            <p class="text-xs sm:text-sm text-slate-500 dark:text-slate-400">Diretriz Internacional 2023, Fisiopatologia da Resistência à Insulina & Indução com Letrozol</p>
          </div>
        </div>
        <span class="px-2.5 py-1 text-xs font-bold rounded-full bg-pink-100 text-pink-800 dark:bg-pink-950 dark:text-pink-300">Rotterdam 2023</span>
      </div>

      <!-- Analogia Didática SOP -->
      <div class="p-4 rounded-2xl bg-amber-50 dark:bg-amber-950/40 border border-amber-200 dark:border-amber-800 text-xs sm:text-sm leading-relaxed text-amber-900 dark:text-amber-200">
        <span class="font-bold text-amber-800 dark:text-amber-300">🎈 Analogia:</span> Na SOP, os ovários estão cheios de <strong>'ovinhos que começam a crescer mas nunca terminam'</strong> (folículos paralisados em 2 a 9 mm). Como não há ovulação, <strong>não há progesterona</strong>, o endométrio cresce desordenadamente e a mulher sangra de forma irregular. Ao mesmo tempo, o excesso de insulina faz as células da teca fabricarem <strong>hormônio masculino em excesso</strong> (acne, espinhas, pelos).
      </div>

      <!-- Calculadora de SOP Rotterdam -->
      <div class="p-5 rounded-2xl border border-slate-200 dark:border-slate-800 bg-white/80 dark:bg-slate-900/60 shadow-sm space-y-4">
        <h3 class="font-extrabold text-sm sm:text-base text-slate-900 dark:text-white flex items-center gap-2">
          <i data-lucide="check-square" class="w-4 h-4 text-pink-600"></i>
          Avaliador Diagnóstico de SOP (Critérios de Rotterdam 2023)
        </h3>
        <p class="text-xs text-slate-500 dark:text-slate-400">Marque os achados presentes na paciente (necessários 2 de 3 após exclusão obrigatória):</p>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs">
          <label class="flex items-start gap-2.5 p-3 rounded-xl border border-slate-200 dark:border-slate-700 hover:bg-slate-50 dark:hover:bg-slate-800 cursor-pointer">
            <input type="checkbox" id="sop-anov" class="mt-0.5 rounded text-pink-600 focus:ring-pink-500" checked>
            <div>
              <strong class="text-slate-900 dark:text-white">1. Oligo ou Anovulação</strong>
              <span class="block text-slate-500 dark:text-slate-400 text-[11px]">Ciclos > 35 dias ou < 8 ciclos no último ano.</span>
            </div>
          </label>

          <label class="flex items-start gap-2.5 p-3 rounded-xl border border-slate-200 dark:border-slate-700 hover:bg-slate-50 dark:hover:bg-slate-800 cursor-pointer">
            <input type="checkbox" id="sop-hyper" class="mt-0.5 rounded text-pink-600 focus:ring-pink-500" checked>
            <div>
              <strong class="text-slate-900 dark:text-white">2. Hiperandrogenismo</strong>
              <span class="block text-slate-500 dark:text-slate-400 text-[11px]">Hirsutismo, acne, alopecia OU testosterona livre/total elevada.</span>
            </div>
          </label>

          <label class="flex items-start gap-2.5 p-3 rounded-xl border border-slate-200 dark:border-slate-700 hover:bg-slate-50 dark:hover:bg-slate-800 cursor-pointer">
            <input type="checkbox" id="sop-usg" class="mt-0.5 rounded text-pink-600 focus:ring-pink-500">
            <div>
              <strong class="text-slate-900 dark:text-white">3. Morfologia Ovariana Policística ao USG / AMH</strong>
              <span class="block text-slate-500 dark:text-slate-400 text-[11px]">&ge; 20 folículos por ovário OU volume &ge; 10 mL (ou AMH alto).</span>
            </div>
          </label>

          <label class="flex items-start gap-2.5 p-3 rounded-xl border border-amber-300 dark:border-amber-800 bg-amber-50/50 dark:bg-amber-950/20 cursor-pointer">
            <input type="checkbox" id="sop-excl" class="mt-0.5 rounded text-amber-600 focus:ring-amber-500" checked>
            <div>
              <strong class="text-amber-900 dark:text-amber-200">Exclusões Realizadas (Mandatório)</strong>
              <span class="block text-amber-700 dark:text-amber-300 text-[11px]">&beta;-hCG, TSH, Prolactina e 17-OH-Progesterona normais.</span>
            </div>
          </label>
        </div>

        <div class="pt-2">
          <label class="inline-flex items-center gap-2 text-xs font-bold text-slate-700 dark:text-slate-300 cursor-pointer">
            <input type="checkbox" id="sop-fertility" class="rounded text-pink-600 focus:ring-pink-500">
            <span>Paciente deseja engravidar ativamente neste momento?</span>
          </label>
        </div>

        <div id="sop-result" class="transition-all"></div>
      </div>

      <!-- Imagem Infográfica M41.8 SOP -->
      <div class="rounded-2xl overflow-hidden border border-slate-200 dark:border-slate-800 shadow-md group relative">
        <img src="assets/img/sop_rotterdam_fisiopatologia.jpg" alt="Síndrome dos Ovários Policísticos Rotterdam 2023" class="w-full h-auto cursor-pointer zoomable-image group-hover:scale-[1.01] transition-transform">
        <div class="p-3 bg-white/90 dark:bg-slate-900/90 text-xs text-slate-500 dark:text-slate-400 flex items-center justify-between">
          <span>Figura 41.2: Fisiopatologia da Resistência à Insulina, Critérios de Rotterdam e Algoritmo Terapêutico</span>
          <span class="text-rose-600 dark:text-rose-400 font-bold flex items-center gap-1"><i data-lucide="zoom-in" class="w-3.5 h-3.5"></i> Clique para ampliar</span>
        </div>
      </div>
    </section>

    <!-- ====================================================================
         MÓDULO 42: MIOMATOSE UTERINA (LEIOMIOMAS)
         ==================================================================== -->
    <section id="modulo-42" class="module-card space-y-6 scroll-mt-28">
      <div class="border-b border-slate-200 dark:border-slate-800 pb-4 flex items-center justify-between flex-wrap gap-2">
        <div class="flex items-center gap-3">
          <span class="w-10 h-10 rounded-xl bg-rose-600 text-white font-black text-lg flex items-center justify-center shadow-md">42</span>
          <div>
            <h2 class="text-xl sm:text-2xl font-black text-slate-900 dark:text-white">Miomatose Uterina (Leiomiomas)</h2>
            <p class="text-xs sm:text-sm text-slate-500 dark:text-slate-400">Classificação FIGO 0 a 8, Degeneração Rubra Gestacional & Miomectomia</p>
          </div>
        </div>
        <span class="px-2.5 py-1 text-xs font-bold rounded-full bg-rose-100 text-rose-800 dark:bg-rose-950 dark:text-rose-300">Tumor Benigno Mais Comum</span>
      </div>

      <!-- Mapeador FIGO Interativo -->
      <div class="p-5 rounded-2xl border border-slate-200 dark:border-slate-800 bg-white/80 dark:bg-slate-900/60 shadow-sm space-y-4">
        <div class="flex items-center justify-between flex-wrap gap-2">
          <h3 class="font-extrabold text-sm sm:text-base text-slate-900 dark:text-white flex items-center gap-2">
            <i data-lucide="target" class="w-4 h-4 text-rose-600"></i>
            Mapeador e Estadiador de Miomas FIGO (Subtipos 0 a 8)
          </h3>
          <span class="text-xs text-slate-500">Selecione o tipo anatômico</span>
        </div>

        <div class="max-w-md">
          <label for="figo-select" class="block text-xs font-bold text-slate-700 dark:text-slate-300 mb-1">Selecione o Subtipo FIGO:</label>
          <select id="figo-select" class="w-full p-2.5 text-xs rounded-xl border border-slate-300 dark:border-slate-700 bg-slate-50 dark:bg-slate-800 text-slate-900 dark:text-white font-semibold">
            <option value="0">FIGO 0: Submucoso pediculado 100% intracavitário</option>
            <option value="1">FIGO 1: Submucoso com invasão intramural < 50%</option>
            <option value="2">FIGO 2: Submucoso com invasão intramural >= 50%</option>
            <option value="3">FIGO 3: Intramural que contata o endométrio (100% intramural)</option>
            <option value="4">FIGO 4: Intramural puro (sem contato com endométrio nem serosa)</option>
            <option value="5">FIGO 5: Subseroso com componente intramural >= 50%</option>
            <option value="6">FIGO 6: Subseroso com componente intramural < 50%</option>
            <option value="7">FIGO 7: Subseroso pediculado (Risco de Torção Aguda)</option>
            <option value="8">FIGO 8: Outros (Cervical, Parasita no ligamento largo)</option>
          </select>
        </div>

        <div id="figo-output" class="transition-all"></div>
      </div>

      <!-- Imagem Infográfica M42 Miomas -->
      <div class="rounded-2xl overflow-hidden border border-slate-200 dark:border-slate-800 shadow-md group relative">
        <img src="assets/img/miomatose_uterina_figo_classificacao.jpg" alt="Classificação FIGO dos Leiomiomas Uterinos" class="w-full h-auto cursor-pointer zoomable-image group-hover:scale-[1.01] transition-transform">
        <div class="p-3 bg-white/90 dark:bg-slate-900/90 text-xs text-slate-500 dark:text-slate-400 flex items-center justify-between">
          <span>Figura 42.1: Classificação Topográfica FIGO 0 a 8, Degenerações e Decisão Cirúrgica</span>
          <span class="text-rose-600 dark:text-rose-400 font-bold flex items-center gap-1"><i data-lucide="zoom-in" class="w-3.5 h-3.5"></i> Clique para ampliar</span>
        </div>
      </div>
    </section>

    <!-- ====================================================================
         MÓDULO 43 & 44: ADENOMIOSE & ENDOMETRIOSE (ESHRE 2022)
         ==================================================================== -->
    <section id="modulo-43" class="module-card space-y-6 scroll-mt-28">
      <div class="border-b border-slate-200 dark:border-slate-800 pb-4 flex items-center justify-between flex-wrap gap-2">
        <div class="flex items-center gap-3">
          <span class="w-10 h-10 rounded-xl bg-blue-600 text-white font-black text-lg flex items-center justify-center shadow-md">43</span>
          <div>
            <h2 class="text-xl sm:text-2xl font-black text-slate-900 dark:text-white">Adenomiose & Endometriose</h2>
            <p class="text-xs sm:text-sm text-slate-500 dark:text-slate-400">Critérios MUSA de Adenomiose, Os '4 Ds' da Endometriose & Diretriz ESHRE 2022</p>
          </div>
        </div>
        <span class="px-2.5 py-1 text-xs font-bold rounded-full bg-blue-100 text-blue-800 dark:bg-blue-950 dark:text-blue-300">ESHRE 2022</span>
      </div>

      <!-- Guia ESHRE Interativo -->
      <div id="modulo-44" class="p-5 rounded-2xl border border-slate-200 dark:border-slate-800 bg-white/80 dark:bg-slate-900/60 shadow-sm space-y-4 scroll-mt-28">
        <h3 class="font-extrabold text-sm sm:text-base text-slate-900 dark:text-white flex items-center gap-2">
          <i data-lucide="git-branch" class="w-4 h-4 text-blue-600"></i>
          Guia de Decisão Clínica na Endometriose (Diretriz ESHRE 2022)
        </h3>

        <div class="grid grid-cols-1 sm:grid-cols-3 gap-3 text-xs">
          <div>
            <label for="endo-pain-level" class="block font-bold text-slate-700 dark:text-slate-300 mb-1">Intensidade da Dor Pélvica:</label>
            <select id="endo-pain-level" class="w-full p-2.5 rounded-xl border border-slate-300 dark:border-slate-700 bg-slate-50 dark:bg-slate-800">
              <option value="mild">Dor Leve a Moderada (Dismenorreia)</option>
              <option value="severe">Dor Incapacitante / 4 Ds Presentes</option>
            </select>
          </div>

          <div class="flex items-center pt-5">
            <label class="inline-flex items-center gap-2 font-bold text-slate-700 dark:text-slate-300 cursor-pointer">
              <input type="checkbox" id="endo-deep-usg" class="rounded text-blue-600 focus:ring-blue-500">
              <span>Mapeamento USG com Preparo Intestinal Positivo?</span>
            </label>
          </div>

          <div class="flex items-center pt-5">
            <label class="inline-flex items-center gap-2 font-bold text-slate-700 dark:text-slate-300 cursor-pointer">
              <input type="checkbox" id="endo-fertility" class="rounded text-blue-600 focus:ring-blue-500">
              <span>Desejo de Gravidez Imediata?</span>
            </label>
          </div>
        </div>

        <div id="endo-result" class="transition-all"></div>
      </div>

      <!-- Imagem Infográfica M43 e M44 -->
      <div class="rounded-2xl overflow-hidden border border-slate-200 dark:border-slate-800 shadow-md group relative">
        <img src="assets/img/adenomiose_vs_endometriose.jpg" alt="Adenomiose vs Endometriose Comparativo Completo" class="w-full h-auto cursor-pointer zoomable-image group-hover:scale-[1.01] transition-transform">
        <div class="p-3 bg-white/90 dark:bg-slate-900/90 text-xs text-slate-500 dark:text-slate-400 flex items-center justify-between">
          <span>Figura 43.1: Comparativo Adenomiose (MUSA / RM) vs Endometriose (4 Ds / ESHRE 2022)</span>
          <span class="text-rose-600 dark:text-rose-400 font-bold flex items-center gap-1"><i data-lucide="zoom-in" class="w-3.5 h-3.5"></i> Clique para ampliar</span>
        </div>
      </div>
    </section>

    <!-- ====================================================================
         MÓDULO 45: CISTOS E MASSAS ANEXIAIS
         ==================================================================== -->
    <section id="modulo-45" class="module-card space-y-6 scroll-mt-28">
      <div class="border-b border-slate-200 dark:border-slate-800 pb-4 flex items-center justify-between flex-wrap gap-2">
        <div class="flex items-center gap-3">
          <span class="w-10 h-10 rounded-xl bg-amber-600 text-white font-black text-lg flex items-center justify-center shadow-md">45</span>
          <div>
            <h2 class="text-xl sm:text-2xl font-black text-slate-900 dark:text-white">Cistos e Massas Anexiais</h2>
            <p class="text-xs sm:text-sm text-slate-500 dark:text-slate-400">Regras IOTA, Classificação ACR O-RADS US 1 a 5 & Emergência da Torção</p>
          </div>
        </div>
        <span class="px-2.5 py-1 text-xs font-bold rounded-full bg-amber-100 text-amber-800 dark:bg-amber-950 dark:text-amber-300">O-RADS 2022</span>
      </div>

      <!-- Calculadora O-RADS -->
      <div class="p-5 rounded-2xl border border-slate-200 dark:border-slate-800 bg-white/80 dark:bg-slate-900/60 shadow-sm space-y-4">
        <h3 class="font-extrabold text-sm sm:text-base text-slate-900 dark:text-white flex items-center gap-2">
          <i data-lucide="shield-alert" class="w-4 h-4 text-amber-600"></i>
          Estratificador de Risco de Malignidade O-RADS US (ACR 2022)
        </h3>

        <div class="grid grid-cols-1 sm:grid-cols-3 gap-3 text-xs">
          <div>
            <label for="orads-score" class="block font-bold text-slate-700 dark:text-slate-300 mb-1">Categoria O-RADS Atribuída:</label>
            <select id="orads-score" class="w-full p-2.5 rounded-xl border border-slate-300 dark:border-slate-700 bg-slate-50 dark:bg-slate-800">
              <option value="1">O-RADS 1: Normal fisiológico (folículo <= 3 cm)</option>
              <option value="2" selected>O-RADS 2: Quase certamente benigno (< 1% risco)</option>
              <option value="3">O-RADS 3: Baixo risco de malignidade (1 a < 10%)</option>
              <option value="4">O-RADS 4: Risco intermediário (10 a < 50%)</option>
              <option value="5">O-RADS 5: Alto risco de malignidade (&ge; 50%)</option>
            </select>
          </div>

          <div>
            <label for="orads-ca125" class="block font-bold text-slate-700 dark:text-slate-300 mb-1">CA-125 Sérico (U/mL):</label>
            <input type="number" id="orads-ca125" value="25" min="0" max="5000" class="w-full p-2.5 rounded-xl border border-slate-300 dark:border-slate-700 bg-slate-50 dark:bg-slate-800">
          </div>

          <div class="flex items-center pt-5">
            <label class="inline-flex items-center gap-2 font-bold text-slate-700 dark:text-slate-300 cursor-pointer">
              <input type="checkbox" id="orads-postmeno" class="rounded text-amber-600 focus:ring-amber-500">
              <span>Paciente na Pós-Menopausa?</span>
            </label>
          </div>
        </div>

        <div id="orads-result" class="transition-all"></div>
      </div>

      <!-- Imagem Infográfica M45 Massas Anexiais -->
      <div class="rounded-2xl overflow-hidden border border-slate-200 dark:border-slate-800 shadow-md group relative">
        <img src="assets/img/massas_anexiais_orads_iota.jpg" alt="Massas Anexiais O-RADS e Torção Ovariana" class="w-full h-auto cursor-pointer zoomable-image group-hover:scale-[1.01] transition-transform">
        <div class="p-3 bg-white/90 dark:bg-slate-900/90 text-xs text-slate-500 dark:text-slate-400 flex items-center justify-between">
          <span>Figura 45.1: Regras Simples IOTA, Categorias O-RADS e Emergência da Torção de Ovário</span>
          <span class="text-rose-600 dark:text-rose-400 font-bold flex items-center gap-1"><i data-lucide="zoom-in" class="w-3.5 h-3.5"></i> Clique para ampliar</span>
        </div>
      </div>
    </section>

    <!-- ====================================================================
         MÓDULO 46: DOR PÉLVICA AGUDA & CRÔNICA
         ==================================================================== -->
    <section id="modulo-46" class="module-card space-y-6 scroll-mt-28">
      <div class="border-b border-slate-200 dark:border-slate-800 pb-4 flex items-center justify-between flex-wrap gap-2">
        <div class="flex items-center gap-3">
          <span class="w-10 h-10 rounded-xl bg-rose-600 text-white font-black text-lg flex items-center justify-center shadow-md">46</span>
          <div>
            <h2 class="text-xl sm:text-2xl font-black text-slate-900 dark:text-white">Dor Pélvica</h2>
            <p class="text-xs sm:text-sm text-slate-500 dark:text-slate-400">Algoritmo da Dor Aguda com &beta;-hCG, Dismenorreia & Dor Pélvica Crônica (DPC &ge; 6 Meses)</p>
          </div>
        </div>
        <span class="px-2.5 py-1 text-xs font-bold rounded-full bg-rose-100 text-rose-800 dark:bg-rose-950 dark:text-rose-300">Raciocínio Clínico</span>
      </div>

      <!-- Imagem Infográfica M46 Dor Pélvica -->
      <div class="rounded-2xl overflow-hidden border border-slate-200 dark:border-slate-800 shadow-md group relative">
        <img src="assets/img/dor_pelvica_aguda_cronica.jpg" alt="Algoritmo da Dor Pélvica Aguda e Crônica" class="w-full h-auto cursor-pointer zoomable-image group-hover:scale-[1.01] transition-transform">
        <div class="p-3 bg-white/90 dark:bg-slate-900/90 text-xs text-slate-500 dark:text-slate-400 flex items-center justify-between">
          <span>Figura 46.1: Algoritmo da Dor Pélvica Aguda, Diagnóstico Diferencial e Abordagem da DPC</span>
          <span class="text-rose-600 dark:text-rose-400 font-bold flex items-center gap-1"><i data-lucide="zoom-in" class="w-3.5 h-3.5"></i> Clique para ampliar</span>
        </div>
      </div>
    </section>

    <!-- ====================================================================
         MÓDULO 47: CLIMATÉRIO, MENOPAUSA & TERAPIA HORMONAL (TH)
         ==================================================================== -->
    <section id="modulo-47" class="module-card space-y-6 scroll-mt-28">
      <div class="border-b border-slate-200 dark:border-slate-800 pb-4 flex items-center justify-between flex-wrap gap-2">
        <div class="flex items-center gap-3">
          <span class="w-10 h-10 rounded-xl bg-indigo-600 text-white font-black text-lg flex items-center justify-center shadow-md">47</span>
          <div>
            <h2 class="text-xl sm:text-2xl font-black text-slate-900 dark:text-white">Climatério e Menopausa</h2>
            <p class="text-xs sm:text-sm text-slate-500 dark:text-slate-400">Janela de Oportunidade da TH, Síndrome Geniturinária (SGM) & Prevenção da Osteoporose</p>
          </div>
        </div>
        <span class="px-2.5 py-1 text-xs font-bold rounded-full bg-indigo-100 text-indigo-800 dark:bg-indigo-950 dark:text-indigo-300">NAMS / IMS 2022</span>
      </div>

      <!-- Avaliador de TH Interativo -->
      <div class="p-5 rounded-2xl border border-slate-200 dark:border-slate-800 bg-white/80 dark:bg-slate-900/60 shadow-sm space-y-4">
        <h3 class="font-extrabold text-sm sm:text-base text-slate-900 dark:text-white flex items-center gap-2">
          <i data-lucide="heart-pulse" class="w-4 h-4 text-indigo-600"></i>
          Avaliador de Elegibilidade e Esquema de Terapia Hormonal (TH)
        </h3>

        <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-3 text-xs">
          <div>
            <label for="ht-age" class="block font-bold text-slate-700 dark:text-slate-300 mb-1">Idade da Mulher (anos):</label>
            <input type="number" id="ht-age" value="52" min="35" max="85" class="w-full p-2.5 rounded-xl border border-slate-300 dark:border-slate-700 bg-slate-50 dark:bg-slate-800">
          </div>

          <div>
            <label for="ht-years" class="block font-bold text-slate-700 dark:text-slate-300 mb-1">Anos Desde a Menopausa:</label>
            <input type="number" id="ht-years" value="2" min="0" max="30" class="w-full p-2.5 rounded-xl border border-slate-300 dark:border-slate-700 bg-slate-50 dark:bg-slate-800">
          </div>

          <div class="flex items-center pt-5">
            <label class="inline-flex items-center gap-2 font-bold text-slate-700 dark:text-slate-300 cursor-pointer">
              <input type="checkbox" id="ht-uterus" class="rounded text-indigo-600 focus:ring-indigo-500" checked>
              <span>Útero Presente (Intacto)?</span>
            </label>
          </div>

          <div class="flex items-center pt-5">
            <label class="inline-flex items-center gap-2 font-bold text-slate-700 dark:text-slate-300 cursor-pointer">
              <input type="checkbox" id="ht-vte" class="rounded text-indigo-600 focus:ring-indigo-500">
              <span>Risco TEV / Obesidade / HAS?</span>
            </label>
          </div>
        </div>

        <div>
          <label class="inline-flex items-center gap-2 text-xs font-bold text-rose-700 dark:text-rose-300 cursor-pointer">
            <input type="checkbox" id="ht-breast" class="rounded text-rose-600 focus:ring-rose-500">
            <span>Histórico Prévio/Atual de Câncer de Mama ou Lesão Neoplásica Estrogênio-Dependente?</span>
          </label>
        </div>

        <div id="ht-result" class="transition-all"></div>
      </div>

      <!-- Imagem Infográfica M47 Menopausa -->
      <div class="rounded-2xl overflow-hidden border border-slate-200 dark:border-slate-800 shadow-md group relative">
        <img src="assets/img/climaterio_menopausa_th.jpg" alt="Climatério, Menopausa e Terapia Hormonal" class="w-full h-auto cursor-pointer zoomable-image group-hover:scale-[1.01] transition-transform">
        <div class="p-3 bg-white/90 dark:bg-slate-900/90 text-xs text-slate-500 dark:text-slate-400 flex items-center justify-between">
          <span>Figura 47.1: Janela de Oportunidade da TH, Alternativas Não Hormonais e Manejo da SGM</span>
          <span class="text-rose-600 dark:text-rose-400 font-bold flex items-center gap-1"><i data-lucide="zoom-in" class="w-3.5 h-3.5"></i> Clique para ampliar</span>
        </div>
      </div>
    </section>

    <!-- ====================================================================
         MÓDULO 48: AMENORREIAS (PRIMÁRIA & SECUNDÁRIA)
         ==================================================================== -->
    <section id="modulo-48" class="module-card space-y-6 scroll-mt-28">
      <div class="border-b border-slate-200 dark:border-slate-800 pb-4 flex items-center justify-between flex-wrap gap-2">
        <div class="flex items-center gap-3">
          <span class="w-10 h-10 rounded-xl bg-purple-600 text-white font-black text-lg flex items-center justify-center shadow-md">48</span>
          <div>
            <h2 class="text-xl sm:text-2xl font-black text-slate-900 dark:text-white">Investigação das Amenorreias</h2>
            <p class="text-xs sm:text-sm text-slate-500 dark:text-slate-400">Os 4 Compartimentos, Teste da Progesterona & Diferencial MRKH (46,XX) vs Morris (46,XY)</p>
          </div>
        </div>
        <span class="px-2.5 py-1 text-xs font-bold rounded-full bg-purple-100 text-purple-800 dark:bg-purple-950 dark:text-purple-300">4 Compartimentos</span>
      </div>

      <!-- Simulador de Amenorreias -->
      <div class="p-5 rounded-2xl border border-slate-200 dark:border-slate-800 bg-white/80 dark:bg-slate-900/60 shadow-sm space-y-4">
        <div class="flex items-center justify-between flex-wrap gap-2">
          <h3 class="font-extrabold text-sm sm:text-base text-slate-900 dark:text-white flex items-center gap-2">
            <i data-lucide="help-circle" class="w-4 h-4 text-purple-600"></i>
            Árvore de Decisão Diagnóstica das Amenorreias
          </h3>
          <div class="w-48">
            <select id="amen-type" class="w-full p-2 text-xs rounded-xl border border-slate-300 dark:border-slate-700 bg-slate-50 dark:bg-slate-800 font-bold">
              <option value="primary">Amenorreia Primária</option>
              <option value="secondary" selected>Amenorreia Secundária</option>
            </select>
          </div>
        </div>

        <div id="amen-steps" class="transition-all"></div>
      </div>

      <!-- Imagem Infográfica M48 Amenorreias -->
      <div class="rounded-2xl overflow-hidden border border-slate-200 dark:border-slate-800 shadow-md group relative">
        <img src="assets/img/amenorreias_4_compartimentos.jpg" alt="Investigação dos 4 Compartimentos das Amenorreias" class="w-full h-auto cursor-pointer zoomable-image group-hover:scale-[1.01] transition-transform">
        <div class="p-3 bg-white/90 dark:bg-slate-900/90 text-xs text-slate-500 dark:text-slate-400 flex items-center justify-between">
          <span>Figura 48.1: Os 4 Compartimentos, Testes de Privação Hormonal e Diferenciação MRKH vs Morris</span>
          <span class="text-rose-600 dark:text-rose-400 font-bold flex items-center gap-1"><i data-lucide="zoom-in" class="w-3.5 h-3.5"></i> Clique para ampliar</span>
        </div>
      </div>
    </section>

    <!-- ====================================================================
         MÓDULO 49: INFERTILIDADE CONJUGAL BÁSICA
         ==================================================================== -->
    <section id="modulo-49" class="module-card space-y-6 scroll-mt-28">
      <div class="border-b border-slate-200 dark:border-slate-800 pb-4 flex items-center justify-between flex-wrap gap-2">
        <div class="flex items-center gap-3">
          <span class="w-10 h-10 rounded-xl bg-emerald-600 text-white font-black text-lg flex items-center justify-center shadow-md">49</span>
          <div>
            <h2 class="text-xl sm:text-2xl font-black text-slate-900 dark:text-white">Infertilidade Básica</h2>
            <p class="text-xs sm:text-sm text-slate-500 dark:text-slate-400">Abordagem Simultânea do Casal, Espermograma OMS 2021 & Indução com Letrozol</p>
          </div>
        </div>
        <span class="px-2.5 py-1 text-xs font-bold rounded-full bg-emerald-100 text-emerald-800 dark:bg-emerald-950 dark:text-emerald-300">OMS 2021 (6ª Ed)</span>
      </div>

      <!-- Calculadora de Espermograma OMS 2021 -->
      <div class="p-5 rounded-2xl border border-slate-200 dark:border-slate-800 bg-white/80 dark:bg-slate-900/60 shadow-sm space-y-4">
        <h3 class="font-extrabold text-sm sm:text-base text-slate-900 dark:text-white flex items-center gap-2">
          <i data-lucide="activity" class="w-4 h-4 text-emerald-600"></i>
          Calculadora de Parâmetros Seminais (Critérios OMS 2021)
        </h3>

        <div class="grid grid-cols-1 sm:grid-cols-3 gap-3 text-xs">
          <div>
            <label for="semen-conc" class="block font-bold text-slate-700 dark:text-slate-300 mb-1">Concentração (Milhões / mL):</label>
            <input type="number" id="semen-conc" value="25" min="0" max="250" class="w-full p-2.5 rounded-xl border border-slate-300 dark:border-slate-700 bg-slate-50 dark:bg-slate-800">
            <span class="text-[10px] text-slate-400">Valor de corte OMS: &ge; 16 M/mL</span>
          </div>

          <div>
            <label for="semen-mot" class="block font-bold text-slate-700 dark:text-slate-300 mb-1">Motilidade Progressiva (%):</label>
            <input type="number" id="semen-mot" value="45" min="0" max="100" class="w-full p-2.5 rounded-xl border border-slate-300 dark:border-slate-700 bg-slate-50 dark:bg-slate-800">
            <span class="text-[10px] text-slate-400">Valor de corte OMS: &ge; 30%</span>
          </div>

          <div>
            <label for="semen-morph" class="block font-bold text-slate-700 dark:text-slate-300 mb-1">Morfologia Normal Kruger (%):</label>
            <input type="number" id="semen-morph" value="6" min="0" max="100" class="w-full p-2.5 rounded-xl border border-slate-300 dark:border-slate-700 bg-slate-50 dark:bg-slate-800">
            <span class="text-[10px] text-slate-400">Valor de corte OMS: &ge; 4%</span>
          </div>
        </div>

        <div id="semen-result" class="transition-all"></div>
      </div>

      <!-- Imagem Infográfica M49 Infertilidade -->
      <div class="rounded-2xl overflow-hidden border border-slate-200 dark:border-slate-800 shadow-md group relative">
        <img src="assets/img/infertilidade_casal_investigacao.jpg" alt="Investigação Básica do Casal Infértil" class="w-full h-auto cursor-pointer zoomable-image group-hover:scale-[1.01] transition-transform">
        <div class="p-3 bg-white/90 dark:bg-slate-900/90 text-xs text-slate-500 dark:text-slate-400 flex items-center justify-between">
          <span>Figura 49.1: Abordagem Simultânea do Casal, Espermograma OMS 2021 e Tratamentos Guiados</span>
          <span class="text-rose-600 dark:text-rose-400 font-bold flex items-center gap-1"><i data-lucide="zoom-in" class="w-3.5 h-3.5"></i> Clique para ampliar</span>
        </div>
      </div>
    </section>

    <!-- ====================================================================
         CENTRAL DE CALCULADORAS & DECISÃO CLÍNICA
         ==================================================================== -->
    <section id="ferramentas-clinicas" class="space-y-6 pt-8 border-t border-slate-200 dark:border-slate-800 scroll-mt-28">
      <div class="text-center max-w-2xl mx-auto space-y-2">
        <span class="px-3 py-1 rounded-full bg-rose-100 dark:bg-rose-950 text-rose-800 dark:text-rose-300 text-xs font-bold border border-rose-200 dark:border-rose-800">Prática Baseada em Evidências</span>
        <h2 class="text-2xl sm:text-3xl font-black text-slate-900 dark:text-white">Central de Decisão Clínica Rápida</h2>
        <p class="text-xs sm:text-sm text-slate-500 dark:text-slate-400">Calculadora de Risco de Biópsia Endometrial, Classificador FIGO, SOP e Avaliação de Terapia Hormonal.</p>
      </div>

      <!-- Calculadora de Biópsia Endometrial ACOG -->
      <div id="calc-biopsia" class="p-6 rounded-2xl border border-slate-200 dark:border-slate-800 bg-white/80 dark:bg-slate-900/60 shadow-md space-y-4">
        <div class="flex items-center justify-between flex-wrap gap-2">
          <div class="flex items-center gap-3">
            <div class="w-9 h-9 rounded-xl bg-rose-600 text-white flex items-center justify-center font-bold">
              <i data-lucide="microscope" class="w-5 h-5"></i>
            </div>
            <div>
              <h3 class="text-base sm:text-lg font-black text-slate-900 dark:text-white">Calculadora de Risco e Indicação de Biópsia Endometrial</h3>
              <p class="text-xs text-slate-500 dark:text-slate-400">Critérios ACOG / FIGO para Investigação Histopatológica no SUA</p>
            </div>
          </div>
          <span class="px-2.5 py-0.5 rounded-full text-xs font-bold bg-rose-100 text-rose-800 dark:bg-rose-950 dark:text-rose-300">ACOG Guideline</span>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-3 gap-3 text-xs">
          <div>
            <label for="bx-age" class="block font-bold text-slate-700 dark:text-slate-300 mb-1">Idade da Paciente (anos):</label>
            <input type="number" id="bx-age" value="38" min="12" max="95" class="w-full p-2.5 rounded-xl border border-slate-300 dark:border-slate-700 bg-slate-50 dark:bg-slate-800">
            <span class="text-[10px] text-slate-400">Ponto de corte ACOG: &ge; 45 anos</span>
          </div>

          <div>
            <label for="bx-thickness" class="block font-bold text-slate-700 dark:text-slate-300 mb-1">Espessura Endometrial (mm):</label>
            <input type="number" id="bx-thickness" value="6" min="0" max="40" step="0.5" class="w-full p-2.5 rounded-xl border border-slate-300 dark:border-slate-700 bg-slate-50 dark:bg-slate-800">
            <span class="text-[10px] text-slate-400">Ponto de corte pós-menopausa: > 4 mm</span>
          </div>

          <div class="flex items-center pt-5">
            <label class="inline-flex items-center gap-2 font-bold text-slate-700 dark:text-slate-300 cursor-pointer">
              <input type="checkbox" id="bx-postmeno" class="rounded text-rose-600 focus:ring-rose-500">
              <span>Paciente na Pós-Menopausa?</span>
            </label>
          </div>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-3 gap-2 text-xs">
          <label class="inline-flex items-center gap-2 font-semibold text-slate-700 dark:text-slate-300 cursor-pointer">
            <input type="checkbox" id="bx-unopposed" class="rounded text-rose-600 focus:ring-rose-500">
            <span>Estrogênio sem oposição (SOP / Obesidade)?</span>
          </label>
          <label class="inline-flex items-center gap-2 font-semibold text-slate-700 dark:text-slate-300 cursor-pointer">
            <input type="checkbox" id="bx-lynch" class="rounded text-rose-600 focus:ring-rose-500">
            <span>Síndrome de Lynch (risco 40-60%)?</span>
          </label>
          <label class="inline-flex items-center gap-2 font-semibold text-slate-700 dark:text-slate-300 cursor-pointer">
            <input type="checkbox" id="bx-tamoxifen" class="rounded text-rose-600 focus:ring-rose-500">
            <span>Uso atual de Tamoxifeno?</span>
          </label>
        </div>

        <div id="bx-result" class="transition-all"></div>
      </div>
    </section>

    <!-- ====================================================================
         HIGH-YIELD REVIEW: TOP 35 PÉROLAS DE GINECOLOGIA GERAL
         ==================================================================== -->
    <section id="high-yield-review" class="space-y-6 pt-8 border-t border-slate-200 dark:border-slate-800 scroll-mt-28">
      <div class="text-center max-w-2xl mx-auto space-y-2">
        <span class="px-3 py-1 rounded-full bg-amber-100 dark:bg-amber-950 text-amber-800 dark:text-amber-300 text-xs font-bold border border-amber-200 dark:border-amber-800">Memorização Rápida</span>
        <h2 class="text-2xl sm:text-3xl font-black text-slate-900 dark:text-white">High-Yield Review: Top 35 Pérolas</h2>
        <p class="text-xs sm:text-sm text-slate-500 dark:text-slate-400">Conceitos com altíssima taxa de cobrança nas bancas de Residência Médica e USMLE Step 2 CK.</p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-3 text-xs">
        <div class="p-3.5 rounded-xl border border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900 shadow-sm">
          <strong class="text-rose-600 dark:text-rose-400 block mb-1">Regra Universal:</strong>
          Qualquer sangramento, dor ou atraso em idade fértil &rarr; <strong>&beta;-hCG SEMPRE PRIMEIRO!</strong>
        </div>
        <div class="p-3.5 rounded-xl border border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900 shadow-sm">
          <strong class="text-rose-600 dark:text-rose-400 block mb-1">Adolescente com Menorragia:</strong>
          Sangramento intenso desde a menarca &rarr; <strong>Pesquisar Doença de von Willebrand</strong>.
        </div>
        <div class="p-3.5 rounded-xl border border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900 shadow-sm">
          <strong class="text-rose-600 dark:text-rose-400 block mb-1">SUA &ge; 45 Anos:</strong>
          Indicação formal de <strong>Biópsia Endometrial</strong> ambulatorial (Pipelle).
        </div>
        <div class="p-3.5 rounded-xl border border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900 shadow-sm">
          <strong class="text-rose-600 dark:text-rose-400 block mb-1">Pós-Menopausa e Sangramento:</strong>
          Endométrio &le; 4 mm = Atrofia (baixo risco); <strong>Endométrio > 4 mm = Biópsia mandatória</strong>!
        </div>
        <div class="p-3.5 rounded-xl border border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900 shadow-sm">
          <strong class="text-rose-600 dark:text-rose-400 block mb-1">Tamoxifeno & Endométrio:</strong>
          Causa espessamento cístico estromal &rarr; <strong>O corte de 4 mm NÃO se aplica</strong>!
        </div>
        <div class="p-3.5 rounded-xl border border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900 shadow-sm">
          <strong class="text-rose-600 dark:text-rose-400 block mb-1">Hiperplasia com Atipia (NIE):</strong>
          Risco de câncer concomitante de até 40% &rarr; <strong>Histerectomia Total</strong> sem morcelamento.
        </div>
        <div class="p-3.5 rounded-xl border border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900 shadow-sm">
          <strong class="text-rose-600 dark:text-rose-400 block mb-1">Tratamento Clínico do SUA:</strong>
          <strong>DIU de Levonorgestrel 52 mg</strong> é o método clínico mais eficaz (redução de 70-90%).
        </div>
        <div class="p-3.5 rounded-xl border border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900 shadow-sm">
          <strong class="text-rose-600 dark:text-rose-400 block mb-1">SOP & Indução da Ovulação:</strong>
          <strong>Letrozol</strong> é a primeira linha formal (superior ao clomifeno em nascidos vivos).
        </div>
        <div class="p-3.5 rounded-xl border border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900 shadow-sm">
          <strong class="text-rose-600 dark:text-rose-400 block mb-1">Mioma Submucoso FIGO 0:</strong>
          Sintomático com desejo gestacional &rarr; <strong>Miomectomia histeroscópica</strong>.
        </div>
        <div class="p-3.5 rounded-xl border border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900 shadow-sm">
          <strong class="text-rose-600 dark:text-rose-400 block mb-1">Degeneração Rubra de Mioma:</strong>
          Dor aguda + febre baixa na gestação &rarr; <strong>Tratamento CONSERVADOR</strong> (analgesia + AINE curto).
        </div>
        <div class="p-3.5 rounded-xl border border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900 shadow-sm">
          <strong class="text-rose-600 dark:text-rose-400 block mb-1">Útero Boggy e Doloroso:</strong>
          Útero globoso amolecido simétrico + menorragia + dismenorreia &rarr; <strong>Adenomiose</strong>.
        </div>
        <div class="p-3.5 rounded-xl border border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900 shadow-sm">
          <strong class="text-rose-600 dark:text-rose-400 block mb-1">Endometriose (ESHRE 2022):</strong>
          Laparoscopia NÃO é obrigatória &rarr; <strong>Tratamento empírico inicial</strong> com AINE + Dienogeste.
        </div>
        <div class="p-3.5 rounded-xl border border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900 shadow-sm">
          <strong class="text-rose-600 dark:text-rose-400 block mb-1">Endometrioma ao USG:</strong>
          Cisto com conteúdo homogêneo hipoecoico <strong>'em vidro fosco'</strong> (ground-glass).
        </div>
        <div class="p-3.5 rounded-xl border border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900 shadow-sm">
          <strong class="text-rose-600 dark:text-rose-400 block mb-1">Teratoma Dermoide Maduro:</strong>
          Nódulo de Rokitansky, dentes/cabelo &rarr; <strong>Maior risco de torção ovariana</strong>.
        </div>
        <div class="p-3.5 rounded-xl border border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900 shadow-sm">
          <strong class="text-rose-600 dark:text-rose-400 block mb-1">Síndrome de Meigs:</strong>
          <strong>Fibroma ovariano benigno + Ascite + Derrame pleural</strong> (que regridem pós-ressecção).
        </div>
        <div class="p-3.5 rounded-xl border border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900 shadow-sm">
          <strong class="text-rose-600 dark:text-rose-400 block mb-1">Torção de Ovário:</strong>
          Fluxo ao Doppler NÃO exclui &rarr; <strong>Laparoscopia urgente: DESTORCER E PRESERVAR!</strong>
        </div>
        <div class="p-3.5 rounded-xl border border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900 shadow-sm">
          <strong class="text-rose-600 dark:text-rose-400 block mb-1">Massa em Criança/Jovem:</strong>
          Suspeita de tumor de células germinativas &rarr; <strong>Dosar AFP, &beta;-hCG e LDH</strong>.
        </div>
        <div class="p-3.5 rounded-xl border border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900 shadow-sm">
          <strong class="text-rose-600 dark:text-rose-400 block mb-1">Janela de Oportunidade TH:</strong>
          Idade < 60 anos ou < 10 anos pós-menopausa &rarr; <strong>Benefício cardiovascular supera o risco</strong>.
        </div>
        <div class="p-3.5 rounded-xl border border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900 shadow-sm">
          <strong class="text-rose-600 dark:text-rose-400 block mb-1">TH em Mulher com Útero:</strong>
          Exige <strong>Estrogênio + Progestagênio</strong> para prevenir câncer de endométrio.
        </div>
        <div class="p-3.5 rounded-xl border border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900 shadow-sm">
          <strong class="text-rose-600 dark:text-rose-400 block mb-1">Interação Tamoxifeno:</strong>
          <strong>Evitar Paroxetina e Fluoxetina</strong> (inibem CYP2D6 e anulam a ação antineoplásica).
        </div>
        <div class="p-3.5 rounded-xl border border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900 shadow-sm">
          <strong class="text-rose-600 dark:text-rose-400 block mb-1">Síndrome de Asherman:</strong>
          Amenorreia secundária pós-curetagem que não sangra com E+P &rarr; <strong>Lise por Histeroscopia</strong>.
        </div>
        <div class="p-3.5 rounded-xl border border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900 shadow-sm">
          <strong class="text-rose-600 dark:text-rose-400 block mb-1">Síndrome de Kallmann:</strong>
          Amenorreia primária + <strong>Anosmia / Hiposmia</strong> (falha na migração dos neurônios GnRH).
        </div>
        <div class="p-3.5 rounded-xl border border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900 shadow-sm">
          <strong class="text-rose-600 dark:text-rose-400 block mb-1">Síndrome de Sheehan:</strong>
          Necrose hipofisária após hemorragia pós-parto grave &rarr; <strong>Primeiro sinal: Agalactia</strong>.
        </div>
        <div class="p-3.5 rounded-xl border border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900 shadow-sm">
          <strong class="text-rose-600 dark:text-rose-400 block mb-1">MRKH vs Morris:</strong>
          Em MRKH (46,XX) os pelos são normais; <strong>Em Morris (46,XY) os pelos são escassos/ausentes</strong>!
        </div>
        <div class="p-3.5 rounded-xl border border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900 shadow-sm">
          <strong class="text-rose-600 dark:text-rose-400 block mb-1">Síndrome de Turner (45,X):</strong>
          Pescoço alado, baixa estatura, FSH alto &rarr; <strong>Solicitar Ecocardiograma (coarctação de aorta)</strong>.
        </div>
        <div class="p-3.5 rounded-xl border border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900 shadow-sm">
          <strong class="text-rose-600 dark:text-rose-400 block mb-1">Hidrossalpinge antes de FIV:</strong>
          Líquido tóxico ao concepto &rarr; <strong>Salpingectomia prévia dobra a taxa de gravidez</strong>!
        </div>
        <div class="p-3.5 rounded-xl border border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900 shadow-sm">
          <strong class="text-rose-600 dark:text-rose-400 block mb-1">Investigação de Infertilidade:</strong>
          SEMPRE SIMULTÂNEA NO CASAL &rarr; <strong>O fator masculino responde por até 50% dos casos</strong>.
        </div>
      </div>
    </section>

    <!-- ====================================================================
         ESTUDO ATIVO: FLASHCARDS 3D INTERATIVOS
         ==================================================================== -->
    <section id="estudo-ativo" class="space-y-6 pt-8 border-t border-slate-200 dark:border-slate-800 scroll-mt-28">
      <div class="text-center max-w-2xl mx-auto space-y-2">
        <span class="px-3 py-1 rounded-full bg-indigo-100 dark:bg-indigo-950 text-indigo-800 dark:text-indigo-300 text-xs font-bold border border-indigo-200 dark:border-indigo-800">Memorização Espaçada</span>
        <h2 class="text-2xl sm:text-3xl font-black text-slate-900 dark:text-white">Flashcards 3D Interativos</h2>
        <p class="text-xs sm:text-sm text-slate-500 dark:text-slate-400">Clique no cartão para virar e conferir a resposta baseada em evidências.</p>
      </div>

      <div class="max-w-xl mx-auto">
        <!-- Container do Flashcard com Efeito 3D -->
        <div class="perspective-1000 h-72 sm:h-80 w-full cursor-pointer" id="flashcard">
          <div class="card-inner">
            <!-- Frente -->
            <div class="card-front p-6 sm:p-8 border-2 border-indigo-300 dark:border-indigo-800 bg-gradient-to-tr from-white to-indigo-50/60 dark:from-slate-900 dark:to-indigo-950/40 shadow-xl flex flex-col justify-between">
              <div>
                <div class="flex items-center justify-between">
                  <span id="fc-category" class="px-2.5 py-0.5 rounded-full text-xs font-black tracking-wider uppercase bg-indigo-100 text-indigo-800 dark:bg-indigo-900 dark:text-indigo-200">Módulo</span>
                  <span class="text-xs text-slate-400 font-semibold flex items-center gap-1"><i data-lucide="rotate-cw" class="w-3.5 h-3.5"></i> Clique para virar</span>
                </div>
                <h4 class="text-base sm:text-lg font-bold text-slate-900 dark:text-white mt-6 leading-relaxed" id="fc-question">Pergunta</h4>
              </div>
              <div class="flex items-center justify-between text-xs text-slate-400 border-t border-indigo-100 dark:border-indigo-900/60 pt-3">
                <span id="fc-counter">1 de 15</span>
                <span class="font-bold text-indigo-600 dark:text-indigo-400">Ver Resposta &rarr;</span>
              </div>
            </div>

            <!-- Verso -->
            <div class="card-back p-6 sm:p-8 border-2 border-emerald-400 dark:border-emerald-700 bg-gradient-to-tr from-emerald-50/80 to-white dark:from-emerald-950/60 dark:to-slate-900 shadow-xl flex flex-col justify-between">
              <div>
                <div class="flex items-center justify-between">
                  <span class="px-2.5 py-0.5 rounded-full text-xs font-black tracking-wider uppercase bg-emerald-100 text-emerald-800 dark:bg-emerald-900 dark:text-emerald-200">Resposta Correta</span>
                  <span class="text-xs text-slate-400 font-semibold flex items-center gap-1"><i data-lucide="check" class="w-3.5 h-3.5 text-emerald-600"></i> FEBRASGO / USMLE</span>
                </div>
                <div class="text-xs sm:text-sm text-slate-800 dark:text-slate-100 font-semibold mt-4 leading-relaxed overflow-y-auto max-h-48" id="fc-answer">Resposta</div>
              </div>
              <div class="flex items-center justify-between text-xs text-slate-400 border-t border-emerald-200 dark:border-emerald-900/60 pt-3">
                <span>Clique para virar novamente</span>
                <span class="font-bold text-emerald-600 dark:text-emerald-400">Gabarito Consolidado</span>
              </div>
            </div>
          </div>
        </div>

        <!-- Controles dos Flashcards -->
        <div class="flex items-center justify-center gap-3 mt-4">
          <button type="button" id="fc-prev" class="px-4 py-2 rounded-xl border border-slate-300 dark:border-slate-700 bg-white dark:bg-slate-800 text-xs font-bold hover:bg-slate-100 dark:hover:bg-slate-700 transition-colors flex items-center gap-1">
            <i data-lucide="chevron-left" class="w-4 h-4"></i> Anterior
          </button>
          <button type="button" id="fc-flip" class="px-4 py-2 rounded-xl bg-indigo-600 hover:bg-indigo-700 text-white text-xs font-bold transition-colors flex items-center gap-1 shadow-sm">
            <i data-lucide="refresh-cw" class="w-3.5 h-3.5"></i> Virar Cartão
          </button>
          <button type="button" id="fc-next" class="px-4 py-2 rounded-xl border border-slate-300 dark:border-slate-700 bg-white dark:bg-slate-800 text-xs font-bold hover:bg-slate-100 dark:hover:bg-slate-700 transition-colors flex items-center gap-1">
            Próximo <i data-lucide="chevron-right" class="w-4 h-4"></i>
          </button>
        </div>
      </div>
    </section>

    <!-- ====================================================================
         SIMULADO CLÍNICO: 15 VINHETAS ESTILO USMLE STEP 2 CK
         ==================================================================== -->
    <section id="simulado-clinico" class="space-y-6 pt-8 border-t border-slate-200 dark:border-slate-800 scroll-mt-28">
      <div class="text-center max-w-2xl mx-auto space-y-2">
        <span class="px-3 py-1 rounded-full bg-emerald-100 dark:bg-emerald-950 text-emerald-800 dark:text-emerald-300 text-xs font-bold border border-emerald-200 dark:border-emerald-800">Avaliação de Desempenho</span>
        <h2 class="text-2xl sm:text-3xl font-black text-slate-900 dark:text-white">Simulado Clínico (15 Vinhetas)</h2>
        <p class="text-xs sm:text-sm text-slate-500 dark:text-slate-400">Casos clínicos completos estilo USMLE Step 2 CK e Provas de Residência Médica com gabarito imediato e pontuação em tempo real.</p>
        <div class="flex items-center justify-center gap-3 pt-2">
          <span id="quiz-score-display" class="text-xs font-extrabold px-3 py-1 rounded-lg bg-slate-200 dark:bg-slate-800 text-slate-800 dark:text-slate-200">Pontuação: 0 de 15 respondidas</span>
          <button type="button" id="quiz-reset-btn" class="text-xs font-bold text-rose-600 dark:text-rose-400 hover:underline flex items-center gap-1">
            <i data-lucide="rotate-ccw" class="w-3.5 h-3.5"></i> Reiniciar
          </button>
        </div>
      </div>

      <div id="quiz-container" class="space-y-4 max-w-3xl mx-auto"></div>
    </section>

  </main>

  <!-- ======================================================================
       FOOTER ELEGANTE & BADGES DE DIRETRIZES
       ====================================================================== -->
  <footer class="mt-20 border-t border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900 text-slate-600 dark:text-slate-400 py-10 text-xs">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 space-y-6 text-center sm:text-left sm:flex sm:items-center sm:justify-between">
      <div class="space-y-2">
        <div class="flex items-center justify-center sm:justify-start gap-2">
          <div class="w-6 h-6 rounded-lg bg-rose-600 text-white flex items-center justify-center font-bold text-xs">
            <i data-lucide="flower-2" class="w-3.5 h-3.5"></i>
          </div>
          <span class="font-extrabold text-sm text-slate-900 dark:text-white">Ginecologia Geral • Portal Médico Interativo</span>
        </div>
        <p class="text-slate-500 dark:text-slate-400 max-w-xl text-[11px] leading-relaxed">
          Baseado no Guia Completo de Obstetrícia e Ginecologia (Parte 5). Conteúdo estruturado para o Internato Médico, Residência em GO, Prova de Título (TEGO/FEBRASGO) e USMLE Step 2 CK/Step 3.
        </p>
      </div>

      <div class="flex flex-col sm:items-end gap-2">
        <div class="flex items-center justify-center sm:justify-end gap-1.5 flex-wrap">
          <span class="px-2 py-0.5 rounded bg-slate-100 dark:bg-slate-800 text-[10px] font-bold border border-slate-200 dark:border-slate-700">FEBRASGO</span>
          <span class="px-2 py-0.5 rounded bg-slate-100 dark:bg-slate-800 text-[10px] font-bold border border-slate-200 dark:border-slate-700">PCDT / SUS</span>
          <span class="px-2 py-0.5 rounded bg-slate-100 dark:bg-slate-800 text-[10px] font-bold border border-slate-200 dark:border-slate-700">FIGO 2018</span>
          <span class="px-2 py-0.5 rounded bg-slate-100 dark:bg-slate-800 text-[10px] font-bold border border-slate-200 dark:border-slate-700">ESHRE 2022</span>
          <span class="px-2 py-0.5 rounded bg-slate-100 dark:bg-slate-800 text-[10px] font-bold border border-slate-200 dark:border-slate-700">ACOG</span>
          <span class="px-2 py-0.5 rounded bg-slate-100 dark:bg-slate-800 text-[10px] font-bold border border-slate-200 dark:border-slate-700">OMS 2021</span>
        </div>
        <span class="text-[10px] text-slate-400">100% Compatível com GitHub Pages • Pronto para Deploy Estático</span>
      </div>
    </div>
  </footer>

  <!-- ======================================================================
       HD LIGHTBOX MODAL FULLSCREEN (COM ZOOM & ARRASTAR)
       ====================================================================== -->
  <div id="lightbox-modal" class="hidden fixed inset-0 z-50 bg-slate-950/95 backdrop-blur-md items-center justify-center flex-col p-2 sm:p-4 select-none">
    <!-- Barra Superior de Controle do Lightbox -->
    <div class="w-full max-w-6xl flex items-center justify-between text-white py-2 px-4 mb-1">
      <span id="lightbox-caption" class="text-xs sm:text-sm font-bold truncate max-w-md sm:max-w-xl text-slate-200"></span>
      <div class="flex items-center gap-2">
        <button type="button" id="lightbox-zoom-out" class="p-2 rounded-lg bg-slate-800/80 hover:bg-slate-700 text-white text-xs flex items-center justify-center transition-colors" title="Diminuir zoom">
          <i data-lucide="zoom-out" class="w-4 h-4"></i>
        </button>
        <button type="button" id="lightbox-reset" class="p-2 rounded-lg bg-slate-800/80 hover:bg-slate-700 text-white text-xs flex items-center justify-center transition-colors" title="Restaurar tamanho">
          <i data-lucide="rotate-ccw" class="w-4 h-4"></i>
        </button>
        <button type="button" id="lightbox-zoom-in" class="p-2 rounded-lg bg-slate-800/80 hover:bg-slate-700 text-white text-xs flex items-center justify-center transition-colors" title="Aumentar zoom">
          <i data-lucide="zoom-in" class="w-4 h-4"></i>
        </button>
        <button type="button" id="lightbox-close" class="p-2 rounded-lg bg-rose-600 hover:bg-rose-700 text-white text-xs flex items-center justify-center transition-colors ml-2" title="Fechar (Esc)">
          <i data-lucide="x" class="w-5 h-5"></i>
        </button>
      </div>
    </div>

    <!-- Área de Exibição da Imagem com Zoom/Pan -->
    <div class="relative w-full max-w-6xl flex-1 flex items-center justify-center overflow-hidden rounded-xl border border-slate-800 bg-slate-900/50">
      <img id="lightbox-img" src="" alt="Infográfico em alta resolução" class="max-w-full max-h-[82vh] object-contain transition-transform user-select-none">
    </div>
  </div>

  <!-- Scripts do App -->
  <script src="assets/js/app.js"></script>
  <script>
    // Inicializa Lucide Icons
    if (window.lucide) {
      lucide.createIcons();
    }
  </script>
</body>
</html>
"""
    with open(OUTPUT_HTML, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Sucesso: index.html gerado com {len(html):,} caracteres em {OUTPUT_HTML}")

if __name__ == "__main__":
    generate_html()
