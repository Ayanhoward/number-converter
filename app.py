import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Number System & Data Representation Converter",
    page_icon="💻",
    layout="wide",
)

# Embed the complete Cyber Architecture HTML/JS Web App with Sequential Page Transitions
st.components.v1.html(
    """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Number System & Data Representation Converter</title>
  
  <!-- Tailwind CSS -->
  <script src="https://cdn.tailwindcss.com"></script>
  
  <!-- Google Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=JetBrains+Mono:ital,wght@0,400;0,600;0,700;0,800;1,400&display=swap" rel="stylesheet">
  
  <!-- Font Awesome Icons -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">

  <style>
    ::-webkit-scrollbar { width: 6px; height: 6px; }
    ::-webkit-scrollbar-track { background: #030712; }
    ::-webkit-scrollbar-thumb { background: #1e293b; border-radius: 4px; }
    ::-webkit-scrollbar-thumb:hover { background: #38bdf8; }

    #supernova-canvas {
      position: fixed;
      top: 0; left: 0;
      width: 100vw; height: 100vh;
      z-index: 0; pointer-events: none;
    }

    @keyframes glitch {
      0% { text-shadow: 2px 0 #f43f5e, -2px 0 #38bdf8; }
      50% { text-shadow: 2px -1px #10b981, -2px 1px #a855f7; }
      100% { text-shadow: 2px 0 #f43f5e, -2px 0 #38bdf8; }
    }
    .glitch-text { animation: glitch 3s infinite alternate ease-in-out; }

    .cyber-grid-bg {
      background-image: linear-gradient(to right, rgba(56, 189, 248, 0.04) 1px, transparent 1px),
                        linear-gradient(to bottom, rgba(56, 189, 248, 0.04) 1px, transparent 1px);
      background-size: 30px 30px;
    }

    @keyframes rgb-border {
      0% { border-color: rgba(244, 63, 94, 0.6); box-shadow: 0 0 25px rgba(244, 63, 94, 0.25); }
      50% { border-color: rgba(56, 189, 248, 0.6); box-shadow: 0 0 25px rgba(56, 189, 248, 0.25); }
      100% { border-color: rgba(244, 63, 94, 0.6); box-shadow: 0 0 25px rgba(244, 63, 94, 0.25); }
    }

    .cyber-card {
      background: rgba(11, 15, 25, 0.88);
      backdrop-filter: blur(20px);
      -webkit-backdrop-filter: blur(20px);
      border: 2px solid rgba(244, 63, 94, 0.4);
      animation: rgb-border 8s infinite linear;
      transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    .cyber-card:hover {
      box-shadow: 0 0 35px rgba(56, 189, 248, 0.5) !important;
    }

    .bit-box {
      transition: all 0.2s cubic-bezier(0.34, 1.56, 0.64, 1);
      cursor: pointer; user-select: none;
    }
    .bit-box.active {
      background: linear-gradient(135deg, #0284c7, #9333ea);
      color: #ffffff; border-color: #38bdf8;
      box-shadow: 0 0 15px rgba(56, 189, 248, 0.8);
    }
    .bit-box.inactive {
      background: rgba(15, 23, 42, 0.9);
      color: #64748b; border-color: #1e293b;
    }
    .bit-box:hover { transform: scale(1.15); border-color: #f43f5e; }

    @keyframes value-pop {
      0% { transform: scale(0.92); opacity: 0.5; }
      50% { transform: scale(1.05); color: #38bdf8; }
      100% { transform: scale(1); opacity: 1; }
    }
    .animate-pop { animation: value-pop 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275); }
    
    .page-transition { transition: opacity 0.4s ease, transform 0.4s ease; }
  </style>
</head>
<body class="bg-[#030712] text-slate-100 font-sans min-h-screen relative overflow-x-hidden p-6 cyber-grid-bg">

  <canvas id="supernova-canvas"></canvas>

  <!-- STAGE 1: CONVERSION PARAMETERS INPUT SCREEN -->
  <div class="max-w-xl mx-auto relative z-10 py-12 page-transition" id="input-screen">
    <div class="cyber-card rounded-3xl p-8 sm:p-10 shadow-2xl space-y-6">
      
      <div class="text-center space-y-2">
        <span class="text-xs font-mono font-bold tracking-widest text-sky-400 uppercase bg-sky-950/80 px-3 py-1 rounded-full border border-sky-800/60">
          ARCHITECTURE & ORGANIZATION
        </span>
        <h1 class="text-2xl sm:text-3xl font-black tracking-tight text-white glitch-text mt-2">
          Number System Converter
        </h1>
        <p class="text-xs text-slate-400">Configure parameters and press Enter to generate output HUD</p>
      </div>

      <div class="space-y-4 pt-2">
        <div>
          <label class="block text-xs font-bold uppercase tracking-wider text-slate-300 mb-2">Select Input Base</label>
          <select id="input-base" class="w-full bg-slate-900/95 border border-slate-700 focus:border-sky-400 text-slate-100 rounded-2xl px-4 py-3.5 text-sm font-semibold outline-none transition-all">
            <option value="Decimal">Decimal (Base 10)</option>
            <option value="Binary">Binary (Base 2)</option>
            <option value="Hexadecimal">Hexadecimal (Base 16)</option>
            <option value="Octal">Octal (Base 8)</option>
          </select>
        </div>

        <div>
          <label class="block text-xs font-bold uppercase tracking-wider text-slate-300 mb-2">Word Size (Bit Width)</label>
          <div class="grid grid-cols-3 gap-2">
            <button type="button" onclick="setBitWidth(8)" id="btn-bit-8" class="bit-width-btn active bg-sky-600 border border-sky-400 text-white font-mono font-bold text-xs py-3 rounded-2xl shadow-lg transition-all">8-Bit</button>
            <button type="button" onclick="setBitWidth(16)" id="btn-bit-16" class="bit-width-btn bg-slate-900/90 border border-slate-800 text-slate-400 font-mono font-bold text-xs py-3 rounded-2xl transition-all">16-Bit</button>
            <button type="button" onclick="setBitWidth(32)" id="btn-bit-32" class="bit-width-btn bg-slate-900/90 border border-slate-800 text-slate-400 font-mono font-bold text-xs py-3 rounded-2xl transition-all">32-Bit</button>
          </div>
        </div>

        <div>
          <div class="flex justify-between items-center mb-2">
            <label class="block text-xs font-bold uppercase tracking-wider text-slate-300">Enter Value & Press Enter ↵</label>
            <button onclick="clearInput()" class="text-[11px] text-slate-400 hover:text-sky-400 font-mono">
              <i class="fa-solid fa-rotate-left"></i> Reset
            </button>
          </div>
          <div class="relative">
            <input type="text" id="input-value" value="12" placeholder="Type value & press Enter..." class="cyber-input w-full bg-slate-900/95 border border-slate-700 text-slate-100 font-mono text-lg font-bold rounded-2xl pl-4 pr-10 py-4 outline-none transition-all shadow-inner">
          </div>
          <p id="error-message" class="text-xs text-rose-400 mt-2 font-medium hidden flex items-center gap-1.5">
            <i class="fa-solid fa-triangle-exclamation"></i> Invalid input for selected number base!
          </p>
        </div>

        <div>
          <label class="block text-[11px] font-bold uppercase tracking-wider text-slate-400 mb-2">Quick Preset Benchmarks</label>
          <div class="flex flex-wrap gap-1.5">
            <button onclick="applyPreset('MAX_UNSIGNED')" class="px-3 py-1.5 rounded-xl bg-slate-900 border border-slate-800 text-[11px] font-mono text-slate-300 hover:text-sky-300 transition-all">Max Unsigned</button>
            <button onclick="applyPreset('MIN_SIGNED')" class="px-3 py-1.5 rounded-xl bg-slate-900 border border-slate-800 text-[11px] font-mono text-slate-300 hover:text-sky-300 transition-all">Min Signed</button>
            <button onclick="applyPreset('ALL_ONES')" class="px-3 py-1.5 rounded-xl bg-slate-900 border border-slate-800 text-[11px] font-mono text-slate-300 hover:text-sky-300 transition-all">All 1s</button>
            <button onclick="applyPreset('ZERO')" class="px-3 py-1.5 rounded-xl bg-slate-900 border border-slate-800 text-[11px] font-mono text-slate-300 hover:text-sky-300 transition-all">Zero</button>
          </div>
        </div>
      </div>

    </div>
  </div>

  <!-- STAGE 2: OUTPUT HUD DASHBOARD (Initially Hidden) -->
  <div class="max-w-7xl mx-auto relative z-10 hidden opacity-0 page-transition" id="output-screen">

    <!-- Header Bar -->
    <header class="mb-6 flex flex-col lg:flex-row lg:items-center justify-between gap-4 border border-slate-800 pb-5 backdrop-blur-xl bg-slate-950/60 p-5 rounded-3xl shadow-2xl">
      <div class="flex items-center gap-4">
        <button onclick="returnToInput()" class="px-4 py-2.5 rounded-2xl bg-slate-900 border border-slate-700 text-xs font-mono font-bold text-sky-300 hover:text-white hover:border-sky-400 transition-all flex items-center gap-2 shadow-lg">
          <i class="fa-solid fa-arrow-left"></i> Change Parameters
        </button>
        <div>
          <span id="active-param-badge" class="text-[11px] font-mono font-bold tracking-widest text-purple-400 uppercase bg-purple-950/90 px-2.5 py-1 rounded-md border border-purple-800/60">
            DECIMAL (12) • 8-BIT WORD
          </span>
        </div>
      </div>

      <div class="flex flex-wrap items-center gap-3">
        <button onclick="triggerPulseWave()" class="px-4 py-2.5 rounded-2xl bg-gradient-to-r from-sky-500/20 to-pink-500/20 border border-sky-400/50 text-xs font-mono font-bold text-sky-300 hover:text-white transition-all flex items-center gap-2">
          <i class="fa-solid fa-wand-magic-sparkles text-amber-400"></i> TRIGGER PULSE
        </button>
      </div>
    </header>

    <!-- Content Grid -->
    <div class="grid grid-cols-1 lg:grid-cols-12 gap-6">

      <!-- LEFT COLUMN: Bit Matrix -->
      <div class="lg:col-span-5 space-y-6">
        <div class="cyber-card rounded-3xl p-6 shadow-2xl">
          <div class="flex items-center justify-between mb-4 border-b border-slate-800 pb-3">
            <h3 class="text-xs font-bold uppercase tracking-wider text-purple-400 flex items-center gap-2">
              <i class="fa-solid fa-microchip text-purple-400"></i> Interactive Bit Flip Matrix
            </h3>
            <span class="text-[10px] text-slate-400 font-mono bg-slate-900 px-2.5 py-1 rounded-md border border-slate-800">Click bit to toggle</span>
          </div>
          <div id="bit-grid" class="flex flex-wrap gap-2 justify-center max-h-56 overflow-y-auto p-2"></div>
        </div>
      </div>

      <!-- RIGHT COLUMN: Converted Base Outputs -->
      <div class="lg:col-span-7 space-y-6">
        <div class="flex items-center justify-between">
          <h2 class="text-base font-bold text-slate-100 uppercase tracking-wider flex items-center gap-2">
            <i class="fa-solid fa-bolt text-amber-400 animate-pulse"></i> Converted Base Outputs
          </h2>
          <span class="text-xs text-slate-400 font-mono bg-slate-900 px-3 py-1 rounded-lg border border-slate-800">Hardware Verified</span>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
          <div class="cyber-card rounded-3xl p-5 relative group">
            <div class="flex justify-between items-start mb-2">
              <span class="text-xs font-bold uppercase tracking-wider text-sky-400">Decimal (Base 10)</span>
              <button onclick="copyToClipboard('out-decimal', 'Decimal')" class="text-slate-500 hover:text-sky-400 text-xs p-1"><i class="fa-regular fa-copy"></i></button>
            </div>
            <div id="out-decimal" class="text-2xl font-mono font-extrabold text-white animate-pop">0</div>
          </div>

          <div class="cyber-card rounded-3xl p-5 relative group">
            <div class="flex justify-between items-start mb-2">
              <span class="text-xs font-bold uppercase tracking-wider text-purple-400">Hexadecimal (Base 16)</span>
              <button onclick="copyToClipboard('out-hex', 'Hexadecimal')" class="text-slate-500 hover:text-purple-400 text-xs p-1"><i class="fa-regular fa-copy"></i></button>
            </div>
            <div id="out-hex" class="text-2xl font-mono font-extrabold text-white animate-pop">0x00</div>
          </div>

          <div class="cyber-card rounded-3xl p-5 relative group">
            <div class="flex justify-between items-start mb-2">
              <span class="text-xs font-bold uppercase tracking-wider text-pink-400">Binary (Base 2)</span>
              <button onclick="copyToClipboard('out-binary', 'Binary')" class="text-slate-500 hover:text-pink-400 text-xs p-1"><i class="fa-regular fa-copy"></i></button>
            </div>
            <div id="out-binary" class="text-xl font-mono font-extrabold text-white animate-pop">00000000</div>
          </div>

          <div class="cyber-card rounded-3xl p-5 relative group">
            <div class="flex justify-between items-start mb-2">
              <span class="text-xs font-bold uppercase tracking-wider text-emerald-400">Octal (Base 8)</span>
              <button onclick="copyToClipboard('out-octal', 'Octal')" class="text-slate-500 hover:text-emerald-400 text-xs p-1"><i class="fa-regular fa-copy"></i></button>
            </div>
            <div id="out-octal" class="text-2xl font-mono font-extrabold text-white animate-pop">0o000</div>
          </div>
        </div>

        <div class="cyber-card rounded-3xl p-6 shadow-2xl space-y-4">
          <div class="flex items-center justify-between border-b border-slate-800 pb-3">
            <h3 class="text-sm font-bold uppercase tracking-wider text-amber-400 flex items-center gap-2">
              <i class="fa-solid fa-layer-group"></i> Architecture Signed Formats
            </h3>
            <span id="range-badge" class="text-[11px] font-mono text-slate-300 bg-slate-900 px-3 py-1 rounded-lg border border-slate-800">Range: -128 to +127</span>
          </div>

          <div class="space-y-3 font-mono text-sm">
            <div class="bg-slate-950/90 p-4 rounded-2xl border border-slate-800 flex justify-between items-center">
              <div>
                <div class="text-xs text-sky-400 font-bold uppercase">Signed 2's Complement</div>
                <div id="out-twos-comp" class="text-base font-extrabold text-white mt-1 animate-pop">00000000</div>
              </div>
              <button onclick="copyToClipboard('out-twos-comp', '2\'s Complement')" class="px-3.5 py-2 rounded-xl bg-slate-900 border border-slate-800 text-xs text-slate-400 hover:text-sky-300">Copy</button>
            </div>

            <div class="bg-slate-950/90 p-4 rounded-2xl border border-slate-800 flex justify-between items-center">
              <div>
                <div class="text-xs text-purple-400 font-bold uppercase">Sign-Magnitude</div>
                <div id="out-sign-mag" class="text-base font-extrabold text-white mt-1 animate-pop">00000000</div>
              </div>
              <button onclick="copyToClipboard('out-sign-mag', 'Sign-Magnitude')" class="px-3.5 py-2 rounded-xl bg-slate-900 border border-slate-800 text-xs text-slate-400 hover:text-purple-300">Copy</button>
            </div>
          </div>
        </div>

      </div>

    </div>

  </div>

  <!-- Toast Alert -->
  <div id="toast" class="fixed bottom-6 right-6 bg-slate-900/95 text-sky-300 border border-sky-500/60 backdrop-blur-xl font-mono font-bold text-xs px-5 py-3.5 rounded-2xl shadow-2xl opacity-0 pointer-events-none transition-all duration-300 flex items-center gap-3 z-50 transform translate-y-4">
    <div class="w-2.5 h-2.5 rounded-full bg-sky-400 animate-ping"></div>
    <span id="toast-text">Copied!</span>
  </div>

  <script>
    let currentBitWidth = 8;
    let currentBase = "Decimal";
    let shockwavePulses = [];

    const inputBaseSelect = document.getElementById('input-base');
    const inputValueInput = document.getElementById('input-value');
    const errorMessage = document.getElementById('error-message');
    const bitGrid = document.getElementById('bit-grid');

    window.onload = function() {
      setupCanvasAnimation();
      setupEventListeners();
    };

    function setupEventListeners() {
      inputValueInput.addEventListener('keydown', (e) => {
        if (e.key === 'Enter') {
          processAndTransitionToHUD();
        }
      });
    }

    function processAndTransitionToHUD() {
      const raw = inputValueInput.value.trim();
      errorMessage.classList.add('hidden');
      if (raw === "") {
        errorMessage.classList.remove('hidden');
        return;
      }

      let decimalVal = 0, isValid = true;
      currentBase = inputBaseSelect.value;

      try {
        if (currentBase === 'Decimal') decimalVal = parseInt(raw, 10);
        else if (currentBase === 'Binary') decimalVal = parseInt(raw, 2);
        else if (currentBase === 'Hexadecimal') decimalVal = parseInt(raw.replace(/^0x/i, ''), 16);
        else if (currentBase === 'Octal') decimalVal = parseInt(raw.replace(/^0o/i, ''), 8);
      } catch (err) { isValid = false; }

      if (!isValid || isNaN(decimalVal)) {
        errorMessage.classList.remove('hidden');
        return;
      }

      // Render Outputs
      renderOutputs(decimalVal);

      // Update Header Badge
      document.getElementById('active-param-badge').textContent = `${currentBase.toUpperCase()} (${raw}) • ${currentBitWidth}-BIT WORD`;

      // Transition to Output HUD Screen
      const inputScreen = document.getElementById('input-screen');
      const outputScreen = document.getElementById('output-screen');

      inputScreen.style.opacity = '0';
      inputScreen.style.transform = 'scale(0.95)';

      setTimeout(() => {
        inputScreen.style.display = 'none';
        outputScreen.classList.remove('hidden');
        setTimeout(() => {
          outputScreen.classList.remove('opacity-0');
          triggerPulseWave();
        }, 50);
      }, 400);
    }

    function returnToInput() {
      const inputScreen = document.getElementById('input-screen');
      const outputScreen = document.getElementById('output-screen');

      outputScreen.style.opacity = '0';
      outputScreen.style.transform = 'scale(0.95)';

      setTimeout(() => {
        outputScreen.classList.add('hidden');
        outputScreen.style.opacity = '1';
        outputScreen.style.transform = 'scale(1)';

        inputScreen.style.display = 'block';
        setTimeout(() => {
          inputScreen.style.opacity = '1';
          inputScreen.style.transform = 'scale(1)';
          inputValueInput.focus();
        }, 50);
      }, 400);
    }

    function setupCanvasAnimation() {
      const canvas = document.getElementById('supernova-canvas');
      const ctx = canvas.getContext('2d');
      let width = (canvas.width = window.innerWidth);
      let height = (canvas.height = window.innerHeight);

      window.addEventListener('resize', () => {
        width = canvas.width = window.innerWidth;
        height = canvas.height = window.innerHeight;
      });

      const stars = Array.from({ length: 85 }, () => ({
        x: Math.random() * width, y: Math.random() * height,
        radius: Math.random() * 1.6 + 0.3, alpha: Math.random() * 0.8 + 0.2,
        speed: Math.random() * 0.25 + 0.05, color: ['#38bdf8', '#a855f7', '#f43f5e', '#38bdf8'][Math.floor(Math.random() * 4)]
      }));

      function renderFrame() {
        ctx.clearRect(0, 0, width, height);
        stars.forEach(star => {
          star.y -= star.speed;
          if (star.y < 0) { star.y = height; star.x = Math.random() * width; }
          ctx.beginPath(); ctx.arc(star.x, star.y, star.radius, 0, Math.PI * 2);
          ctx.fillStyle = star.color; ctx.globalAlpha = star.alpha;
          ctx.shadowBlur = 8; ctx.shadowColor = star.color;
          ctx.fill(); ctx.shadowBlur = 0; ctx.globalAlpha = 1.0;
        });

        for (let i = shockwavePulses.length - 1; i >= 0; i--) {
          const p = shockwavePulses[i];
          p.radius += p.speed; p.alpha -= 0.018;
          if (p.alpha <= 0) { shockwavePulses.splice(i, 1); continue; }
          ctx.beginPath(); ctx.arc(p.x, p.y, p.radius, 0, Math.PI * 2);
          ctx.strokeStyle = p.color; ctx.lineWidth = p.lineWidth;
          ctx.globalAlpha = p.alpha; ctx.stroke(); ctx.globalAlpha = 1.0;
        }
        requestAnimationFrame(renderFrame);
      }
      renderFrame();
    }

    function triggerPulseWave() {
      shockwavePulses.push({
        x: window.innerWidth / 2, y: window.innerHeight / 3,
        radius: 10, speed: 7, alpha: 0.85, lineWidth: 2.5, color: '#38bdf8'
      });
    }

    function setBitWidth(bits) {
      currentBitWidth = bits;
      document.querySelectorAll('.bit-width-btn').forEach(btn => {
        btn.classList.remove('bg-sky-600', 'border-sky-400', 'text-white', 'shadow-lg');
        btn.classList.add('bg-slate-900/90', 'border-slate-800', 'text-slate-400');
      });
      const activeBtn = document.getElementById(`btn-bit-${bits}`);
      if (activeBtn) {
        activeBtn.classList.remove('bg-slate-900/90', 'border-slate-800', 'text-slate-400');
        activeBtn.classList.add('bg-sky-600', 'border-sky-400', 'text-white', 'shadow-lg');
      }
    }

    function clearInput() { inputValueInput.value = ''; }

    function applyPreset(type) {
      inputBaseSelect.value = 'Decimal'; currentBase = 'Decimal';
      if (type === 'MAX_UNSIGNED') inputValueInput.value = Math.pow(2, currentBitWidth) - 1;
      else if (type === 'MIN_SIGNED') inputValueInput.value = -Math.pow(2, currentBitWidth - 1);
      else if (type === 'ALL_ONES') { inputBaseSelect.value = 'Binary'; currentBase = 'Binary'; inputValueInput.value = "1".repeat(currentBitWidth); }
      else if (type === 'ZERO') inputValueInput.value = '0';
    }

    function renderOutputs(decVal) {
      const bits = currentBitWidth;
      const mask = (1 << bits) - 1;
      let binStr = decVal < 0 ? (Math.pow(2, bits) + decVal).toString(2).padStart(bits, '0').slice(-bits) : (decVal & mask).toString(2).padStart(bits, '0');
      
      const hexStr = "0x" + (parseInt(binStr, 2) >>> 0).toString(16).toUpperCase().padStart(Math.ceil(bits / 4), '0');
      const octStr = "0o" + (parseInt(binStr, 2) >>> 0).toString(8).padStart(Math.ceil(bits / 3), '0');
      const maxMag = Math.pow(2, bits - 1) - 1;
      const signMagStr = (decVal < 0 ? "1" : "0") + (Math.abs(decVal) & maxMag).toString(2).padStart(bits - 1, '0');

      updateElementText('out-decimal', decVal.toString());
      updateElementText('out-hex', hexStr);
      updateElementText('out-binary', binStr);
      updateElementText('out-octal', octStr);
      updateElementText('out-twos-comp', binStr);
      updateElementText('out-sign-mag', signMagStr);

      document.getElementById('range-badge').textContent = `Range: ${-Math.pow(2, bits - 1)} to +${Math.pow(2, bits - 1) - 1}`;
      renderBitGrid(binStr);
    }

    function updateElementText(id, text) {
      const el = document.getElementById(id);
      if (el && el.textContent !== text) {
        el.textContent = text;
        el.classList.remove('animate-pop');
        void el.offsetWidth;
        el.classList.add('animate-pop');
      }
    }

    function renderBitGrid(binStr) {
      bitGrid.innerHTML = '';
      binStr.split('').forEach((bit, idx) => {
        const bitBox = document.createElement('div');
        bitBox.className = `bit-box font-mono font-extrabold text-xs w-9 h-11 rounded-2xl flex flex-col items-center justify-center border ${bit === '1' ? 'active' : 'inactive'}`;
        bitBox.innerHTML = `<span>${bit}</span><span class="text-[8px] opacity-60">b${binStr.length - 1 - idx}</span>`;
        bitBox.onclick = () => {
          let arr = binStr.split('');
          arr[idx] = arr[idx] === '1' ? '0' : '1';
          const newBin = arr.join('');
          const newDec = parseInt(newBin, 2);
          renderOutputs(newDec);
          triggerPulseWave();
        };
        bitGrid.appendChild(bitBox);
      });
    }

    function copyToClipboard(id, label) {
      const text = document.getElementById(id).textContent;
      navigator.clipboard.writeText(text);
      showToast(`Copied ${label}: ${text}`);
    }

    function showToast(msg) {
      const toast = document.getElementById('toast');
      document.getElementById('toast-text').textContent = msg;
      toast.classList.remove('opacity-0', 'pointer-events-none', 'translate-y-4');
      toast.classList.add('opacity-100', 'translate-y-0');
      setTimeout(() => {
        toast.classList.remove('opacity-100', 'translate-y-0');
        toast.classList.add('opacity-0', 'pointer-events-none', 'translate-y-4');
      }, 2200);
    }
  </script>
</body>
</html>
""",
    height=900,
    scrolling=True,
)