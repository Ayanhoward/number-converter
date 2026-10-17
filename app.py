import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Number System & Data Representation Converter",
    page_icon="💻",
    layout="wide",
)

# Embed the complete Cyber Architecture HTML/JS Web App
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
  
  <!-- Google Fonts: Inter & JetBrains Mono -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=JetBrains+Mono:ital,wght@0,400;0,600;0,700;0,800;1,400&display=swap" rel="stylesheet">
  
  <!-- Font Awesome Icons -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">

  <script>
    tailwind.config = {
      theme: {
        extend: {
          fontFamily: {
            sans: ['Inter', 'sans-serif'],
            mono: ['JetBrains Mono', 'monospace'],
          },
          colors: {
            cyber: {
              dark: '#030712',
              card: 'rgba(11, 15, 25, 0.75)',
              border: 'rgba(56, 189, 248, 0.25)',
              cyan: '#38bdf8',
              magenta: '#f43f5e',
              purple: '#a855f7',
              neonGreen: '#10b981',
              gold: '#f59e0b',
            }
          }
        }
      }
    }
  </script>

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
      25% { text-shadow: -2px 0 #f43f5e, 2px 0 #38bdf8; }
      50% { text-shadow: 2px -1px #a855f7, -2px 1px #10b981; }
      75% { text-shadow: -1px 2px #f43f5e, 1px -2px #38bdf8; }
      100% { text-shadow: 2px 0 #f43f5e, -2px 0 #38bdf8; }
    }
    .glitch-text { animation: glitch 3s infinite alternate ease-in-out; }

    @keyframes rgb-border-rotate {
      0% { border-color: rgba(56, 189, 248, 0.5); box-shadow: 0 0 15px rgba(56, 189, 248, 0.2); }
      33% { border-color: rgba(168, 85, 247, 0.5); box-shadow: 0 0 18px rgba(168, 85, 247, 0.25); }
      66% { border-color: rgba(244, 63, 94, 0.5); box-shadow: 0 0 18px rgba(244, 63, 94, 0.25); }
      100% { border-color: rgba(56, 189, 248, 0.5); box-shadow: 0 0 15px rgba(56, 189, 248, 0.2); }
    }

    .cyber-card {
      background: rgba(11, 15, 25, 0.78);
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      border: 1px solid rgba(56, 189, 248, 0.3);
      animation: rgb-border-rotate 8s infinite linear;
      transition: transform 0.25s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.25s ease;
    }
    .cyber-card:hover {
      transform: translateY(-2px);
      box-shadow: 0 0 25px rgba(56, 189, 248, 0.4) !important;
    }

    .bit-box {
      transition: all 0.2s cubic-bezier(0.34, 1.56, 0.64, 1);
      cursor: pointer; user-select: none;
    }
    .bit-box.active {
      background: linear-gradient(135deg, #0284c7, #0d9488);
      color: #ffffff; border-color: #38bdf8;
      box-shadow: 0 0 12px rgba(56, 189, 248, 0.7), inset 0 0 6px rgba(255, 255, 255, 0.4);
    }
    .bit-box.inactive {
      background: rgba(15, 23, 42, 0.8);
      color: #64748b; border-color: #1e293b;
    }
    .bit-box:hover { transform: scale(1.12); border-color: #a855f7; }

    @keyframes value-pop {
      0% { transform: scale(0.96); opacity: 0.7; }
      50% { transform: scale(1.03); color: #38bdf8; }
      100% { transform: scale(1); opacity: 1; }
    }
    .animate-pop { animation: value-pop 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275); }
    .cyber-input:focus { box-shadow: 0 0 15px rgba(56, 189, 248, 0.4); }
  </style>
</head>
<body class="bg-[#030712] text-slate-100 font-sans min-h-screen relative overflow-x-hidden p-4">

  <canvas id="supernova-canvas"></canvas>

  <div class="max-w-7xl mx-auto relative z-10">

    <header class="mb-6 flex flex-col lg:flex-row lg:items-center justify-between gap-4 border-b border-slate-800/80 pb-5 backdrop-blur-md bg-slate-950/40 p-4 rounded-2xl border">
      <div class="flex items-center gap-4">
        <div class="w-12 h-12 rounded-2xl bg-gradient-to-tr from-sky-500 via-purple-500 to-pink-500 p-0.5 flex items-center justify-center shadow-lg shadow-sky-500/20">
          <div class="w-full h-full bg-slate-950 rounded-[14px] flex items-center justify-center">
            <i class="fa-solid fa-atom text-2xl text-sky-400 animate-spin" style="animation-duration: 10s;"></i>
          </div>
        </div>
        <div>
          <span class="text-xs font-mono font-bold tracking-widest text-sky-400 uppercase bg-sky-950/80 px-2 py-0.5 rounded border border-sky-800/50">
            ARCHITECTURE & ORGANIZATION
          </span>
          <h1 class="text-2xl sm:text-3xl font-black tracking-tight text-white mt-0.5 glitch-text">
            NUMBER SYSTEM CONVERTER
          </h1>
        </div>
      </div>

      <div class="flex flex-wrap items-center gap-2">
        <button onclick="triggerSupernovaPulse()" class="px-3.5 py-2 rounded-xl bg-gradient-to-r from-sky-500/20 to-purple-500/20 border border-sky-500/40 text-xs font-mono font-bold text-sky-300 hover:text-white hover:border-sky-400 transition-all flex items-center gap-2 shadow-lg group">
          <i class="fa-solid fa-wand-magic-sparkles text-amber-400 group-hover:rotate-12 transition-transform"></i>
          PULSE ANIMATION
        </button>
        <div class="px-3 py-2 rounded-xl bg-slate-900/80 border border-slate-800 text-xs font-mono text-slate-400 flex items-center gap-2">
          <span class="w-2 h-2 rounded-full bg-emerald-400 animate-ping"></span>
          ENGINE ACTIVE
        </div>
      </div>
    </header>

    <div class="grid grid-cols-1 lg:grid-cols-12 gap-6">

      <!-- LEFT COLUMN -->
      <div class="lg:col-span-5 space-y-6">
        <div class="cyber-card rounded-2xl p-6 shadow-2xl relative overflow-hidden">
          <div class="flex items-center justify-between mb-5 border-b border-slate-800 pb-3">
            <h2 class="text-base font-bold text-sky-400 uppercase tracking-wider flex items-center gap-2">
              <i class="fa-solid fa-sliders text-purple-400"></i> Conversion Parameters
            </h2>
            <span id="bit-mode-badge" class="text-xs font-mono text-purple-300 bg-purple-950/80 px-2.5 py-1 rounded-full border border-purple-800/60">
              8-BIT WORD
            </span>
          </div>

          <div class="space-y-4">
            <div>
              <label class="block text-xs font-bold uppercase tracking-wider text-slate-300 mb-2">Select Input Base</label>
              <select id="input-base" class="w-full bg-slate-900/90 border border-slate-700/80 focus:border-sky-400 focus:ring-2 focus:ring-sky-400/20 text-slate-100 rounded-xl px-4 py-3 text-sm font-semibold transition-all outline-none">
                <option value="Decimal">Decimal (Base 10)</option>
                <option value="Binary">Binary (Base 2)</option>
                <option value="Hexadecimal">Hexadecimal (Base 16)</option>
                <option value="Octal">Octal (Base 8)</option>
              </select>
            </div>

            <div>
              <label class="block text-xs font-bold uppercase tracking-wider text-slate-300 mb-2">Word Size (Bit Width)</label>
              <div class="grid grid-cols-3 gap-2">
                <button type="button" onclick="setBitWidth(8)" id="btn-bit-8" class="bit-width-btn active bg-sky-600 border border-sky-400 text-white font-mono font-bold text-xs py-2.5 rounded-xl shadow-lg shadow-sky-600/30 transition-all">8-Bit</button>
                <button type="button" onclick="setBitWidth(16)" id="btn-bit-16" class="bit-width-btn bg-slate-900/80 border border-slate-800 text-slate-400 hover:text-slate-200 font-mono font-bold text-xs py-2.5 rounded-xl transition-all">16-Bit</button>
                <button type="button" onclick="setBitWidth(32)" id="btn-bit-32" class="bit-width-btn bg-slate-900/80 border border-slate-800 text-slate-400 hover:text-slate-200 font-mono font-bold text-xs py-2.5 rounded-xl transition-all">32-Bit</button>
              </div>
            </div>

            <div>
              <div class="flex justify-between items-center mb-2">
                <label class="block text-xs font-bold uppercase tracking-wider text-slate-300">Enter Input Value</label>
                <button onclick="clearInput()" class="text-[11px] text-slate-400 hover:text-sky-400 font-mono transition-colors">
                  <i class="fa-solid fa-rotate-left"></i> Reset
                </button>
              </div>
              <div class="relative">
                <input type="text" id="input-value" value="12" placeholder="Enter value..." class="cyber-input w-full bg-slate-900/90 border border-slate-700/80 focus:border-sky-400 text-slate-100 font-mono text-lg font-bold rounded-xl pl-4 pr-10 py-3 transition-all outline-none">
              </div>
              <p id="error-message" class="text-xs text-rose-400 mt-2 font-medium hidden flex items-center gap-1.5">
                <i class="fa-solid fa-triangle-exclamation"></i> Invalid input for selected number base!
              </p>
            </div>

            <div>
              <label class="block text-[11px] font-bold uppercase tracking-wider text-slate-400 mb-2">Quick Preset Benchmarks</label>
              <div class="flex flex-wrap gap-1.5">
                <button onclick="applyPreset('MAX_UNSIGNED')" class="px-2.5 py-1.5 rounded-lg bg-slate-900 border border-slate-800 text-[11px] font-mono text-slate-300 hover:text-sky-300 hover:border-sky-500/50 transition-all">Max Unsigned</button>
                <button onclick="applyPreset('MIN_SIGNED')" class="px-2.5 py-1.5 rounded-lg bg-slate-900 border border-slate-800 text-[11px] font-mono text-slate-300 hover:text-sky-300 hover:border-sky-500/50 transition-all">Min Signed</button>
                <button onclick="applyPreset('ALL_ONES')" class="px-2.5 py-1.5 rounded-lg bg-slate-900 border border-slate-800 text-[11px] font-mono text-slate-300 hover:text-sky-300 hover:border-sky-500/50 transition-all">All 1s</button>
                <button onclick="applyPreset('ZERO')" class="px-2.5 py-1.5 rounded-lg bg-slate-900 border border-slate-800 text-[11px] font-mono text-slate-300 hover:text-sky-300 hover:border-sky-500/50 transition-all">Zero</button>
              </div>
            </div>
          </div>
        </div>

        <div class="cyber-card rounded-2xl p-6 shadow-2xl">
          <div class="flex items-center justify-between mb-4 border-b border-slate-800 pb-3">
            <h3 class="text-xs font-bold uppercase tracking-wider text-purple-400 flex items-center gap-2">
              <i class="fa-solid fa-microchip text-purple-400"></i> Interactive Bit Flip Matrix
            </h3>
            <span class="text-[10px] text-slate-400 font-mono bg-slate-900 px-2 py-0.5 rounded border border-slate-800">Click bit to toggle</span>
          </div>
          <div id="bit-grid" class="flex flex-wrap gap-2 justify-center max-h-56 overflow-y-auto p-1"></div>
        </div>
      </div>

      <!-- RIGHT COLUMN -->
      <div class="lg:col-span-7 space-y-6">
        <div class="flex items-center justify-between">
          <h2 class="text-base font-bold text-slate-100 uppercase tracking-wider flex items-center gap-2">
            <i class="fa-solid fa-bolt text-amber-400 animate-pulse"></i> Converted Base Outputs
          </h2>
          <span class="text-xs text-slate-400 font-mono">Live Hardware Alignment</span>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
          <div class="cyber-card rounded-2xl p-5 relative group">
            <div class="flex justify-between items-start mb-2">
              <span class="text-xs font-bold uppercase tracking-wider text-sky-400">Decimal (Base 10)</span>
              <button onclick="copyToClipboard('out-decimal', 'Decimal')" class="text-slate-500 hover:text-sky-400 text-xs"><i class="fa-regular fa-copy"></i></button>
            </div>
            <div id="out-decimal" class="text-2xl font-mono font-extrabold text-white animate-pop">0</div>
          </div>

          <div class="cyber-card rounded-2xl p-5 relative group">
            <div class="flex justify-between items-start mb-2">
              <span class="text-xs font-bold uppercase tracking-wider text-purple-400">Hexadecimal (Base 16)</span>
              <button onclick="copyToClipboard('out-hex', 'Hexadecimal')" class="text-slate-500 hover:text-purple-400 text-xs"><i class="fa-regular fa-copy"></i></button>
            </div>
            <div id="out-hex" class="text-2xl font-mono font-extrabold text-white animate-pop">0x00</div>
          </div>

          <div class="cyber-card rounded-2xl p-5 relative group">
            <div class="flex justify-between items-start mb-2">
              <span class="text-xs font-bold uppercase tracking-wider text-pink-400">Binary (Base 2)</span>
              <button onclick="copyToClipboard('out-binary', 'Binary')" class="text-slate-500 hover:text-pink-400 text-xs"><i class="fa-regular fa-copy"></i></button>
            </div>
            <div id="out-binary" class="text-xl font-mono font-extrabold text-white animate-pop">00000000</div>
          </div>

          <div class="cyber-card rounded-2xl p-5 relative group">
            <div class="flex justify-between items-start mb-2">
              <span class="text-xs font-bold uppercase tracking-wider text-emerald-400">Octal (Base 8)</span>
              <button onclick="copyToClipboard('out-octal', 'Octal')" class="text-slate-500 hover:text-emerald-400 text-xs"><i class="fa-regular fa-copy"></i></button>
            </div>
            <div id="out-octal" class="text-2xl font-mono font-extrabold text-white animate-pop">0o000</div>
          </div>
        </div>

        <div class="cyber-card rounded-2xl p-6 shadow-2xl space-y-4">
          <div class="flex items-center justify-between border-b border-slate-800 pb-3">
            <h3 class="text-sm font-bold uppercase tracking-wider text-amber-400">Architecture Signed Formats</h3>
            <span id="range-badge" class="text-[11px] font-mono text-slate-300 bg-slate-900 px-3 py-1 rounded-lg border border-slate-800">Range: -128 to +127</span>
          </div>

          <div class="space-y-3 font-mono text-sm">
            <div class="bg-slate-950/80 p-4 rounded-xl border border-slate-800 flex justify-between items-center">
              <div>
                <div class="text-xs text-sky-400 font-bold uppercase">Signed 2's Complement</div>
                <div id="out-twos-comp" class="text-base font-extrabold text-white mt-1">00000000</div>
              </div>
              <button onclick="copyToClipboard('out-twos-comp', '2\'s Complement')" class="px-3 py-1.5 rounded-lg bg-slate-900 border border-slate-800 text-xs text-slate-400 hover:text-sky-300">Copy</button>
            </div>

            <div class="bg-slate-950/80 p-4 rounded-xl border border-slate-800 flex justify-between items-center">
              <div>
                <div class="text-xs text-purple-400 font-bold uppercase">Sign-Magnitude</div>
                <div id="out-sign-mag" class="text-base font-extrabold text-white mt-1">00000000</div>
              </div>
              <button onclick="copyToClipboard('out-sign-mag', 'Sign-Magnitude')" class="px-3 py-1.5 rounded-lg bg-slate-900 border border-slate-800 text-xs text-slate-400 hover:text-purple-300">Copy</button>
            </div>
          </div>
        </div>

      </div>

    </div>

    <div id="toast" class="fixed bottom-6 right-6 bg-slate-900/90 text-sky-300 border border-sky-500/50 backdrop-blur-lg font-mono font-bold text-xs px-5 py-3.5 rounded-2xl shadow-2xl opacity-0 pointer-events-none transition-all duration-300 flex items-center gap-3 z-50">
      <div class="w-2.5 h-2.5 rounded-full bg-sky-400 animate-ping"></div>
      <span id="toast-text">Copied!</span>
    </div>

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
      updateConversion();
    };

    function setupEventListeners() {
      inputBaseSelect.addEventListener('change', (e) => { currentBase = e.target.value; updateConversion(); });
      inputValueInput.addEventListener('input', () => { updateConversion(); });
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

      const stars = Array.from({ length: 80 }, () => ({
        x: Math.random() * width, y: Math.random() * height,
        radius: Math.random() * 1.5 + 0.3, alpha: Math.random() * 0.8 + 0.2,
        speed: Math.random() * 0.2 + 0.05, color: ['#38bdf8', '#a855f7', '#f43f5e'][Math.floor(Math.random() * 3)]
      }));

      function renderFrame() {
        ctx.clearRect(0, 0, width, height);
        stars.forEach(star => {
          star.y -= star.speed;
          if (star.y < 0) { star.y = height; star.x = Math.random() * width; }
          ctx.beginPath(); ctx.arc(star.x, star.y, star.radius, 0, Math.PI * 2);
          ctx.fillStyle = star.color; ctx.globalAlpha = star.alpha; ctx.fill(); ctx.globalAlpha = 1.0;
        });

        for (let i = shockwavePulses.length - 1; i >= 0; i--) {
          const p = shockwavePulses[i];
          p.radius += p.speed; p.alpha -= 0.02;
          if (p.alpha <= 0) { shockwavePulses.splice(i, 1); continue; }
          ctx.beginPath(); ctx.arc(p.x, p.y, p.radius, 0, Math.PI * 2);
          ctx.strokeStyle = p.color; ctx.lineWidth = p.lineWidth; ctx.globalAlpha = p.alpha; ctx.stroke(); ctx.globalAlpha = 1.0;
        }
        requestAnimationFrame(renderFrame);
      }
      renderFrame();
    }

    function triggerSupernovaPulse() {
      shockwavePulses.push({ x: window.innerWidth / 2, y: window.innerHeight / 3, radius: 10, speed: 6, alpha: 0.8, lineWidth: 2, color: '#38bdf8' });
    }

    function setBitWidth(bits) {
      currentBitWidth = bits;
      document.querySelectorAll('.bit-width-btn').forEach(btn => {
        btn.classList.remove('bg-sky-600', 'border-sky-400', 'text-white', 'shadow-lg');
        btn.classList.add('bg-slate-900/80', 'border-slate-800', 'text-slate-400');
      });
      const activeBtn = document.getElementById(`btn-bit-${bits}`);
      if (activeBtn) {
        activeBtn.classList.remove('bg-slate-900/80', 'border-slate-800', 'text-slate-400');
        activeBtn.classList.add('bg-sky-600', 'border-sky-400', 'text-white', 'shadow-lg');
      }
      document.getElementById('bit-mode-badge').textContent = `${bits}-BIT WORD`;
      triggerSupernovaPulse();
      updateConversion();
    }

    function clearInput() { inputValueInput.value = ''; updateConversion(); }

    function applyPreset(type) {
      inputBaseSelect.value = 'Decimal'; currentBase = 'Decimal';
      if (type === 'MAX_UNSIGNED') inputValueInput.value = Math.pow(2, currentBitWidth) - 1;
      else if (type === 'MIN_SIGNED') inputValueInput.value = -Math.pow(2, currentBitWidth - 1);
      else if (type === 'ALL_ONES') { inputBaseSelect.value = 'Binary'; currentBase = 'Binary'; inputValueInput.value = "1".repeat(currentBitWidth); }
      else if (type === 'ZERO') inputValueInput.value = '0';
      updateConversion(); triggerSupernovaPulse();
    }

    function updateConversion() {
      const raw = inputValueInput.value.trim();
      errorMessage.classList.add('hidden');
      if (raw === "") { renderZeros(); return; }

      let decimalVal = 0, isValid = true;
      try {
        if (currentBase === 'Decimal') decimalVal = parseInt(raw, 10);
        else if (currentBase === 'Binary') decimalVal = parseInt(raw, 2);
        else if (currentBase === 'Hexadecimal') decimalVal = parseInt(raw.replace(/^0x/i, ''), 16);
        else if (currentBase === 'Octal') decimalVal = parseInt(raw.replace(/^0o/i, ''), 8);
      } catch (err) { isValid = false; }

      if (!isValid || isNaN(decimalVal)) { errorMessage.classList.remove('hidden'); renderZeros(); return; }
      renderOutputs(decimalVal);
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

    function renderZeros() {
      const zeros = "0".repeat(currentBitWidth);
      updateElementText('out-decimal', "0");
      updateElementText('out-hex', "0x00");
      updateElementText('out-binary', zeros);
      updateElementText('out-octal', "0o0");
      updateElementText('out-twos-comp', zeros);
      updateElementText('out-sign-mag', zeros);
      renderBitGrid(zeros);
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
        bitBox.className = `bit-box font-mono font-extrabold text-xs w-8 h-10 rounded-xl flex flex-col items-center justify-center border ${bit === '1' ? 'active' : 'inactive'}`;
        bitBox.innerHTML = `<span>${bit}</span><span class="text-[8px] opacity-60">b${binStr.length - 1 - idx}</span>`;
        bitBox.onclick = () => {
          let arr = binStr.split('');
          arr[idx] = arr[idx] === '1' ? '0' : '1';
          inputBaseSelect.value = 'Binary'; currentBase = 'Binary';
          inputValueInput.value = arr.join('');
          updateConversion(); triggerSupernovaPulse();
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
      toast.classList.remove('opacity-0', 'pointer-events-none');
      toast.classList.add('opacity-100');
      setTimeout(() => { toast.classList.remove('opacity-100'); toast.classList.add('opacity-0', 'pointer-events-none'); }, 2000);
    }
  </script>
</body>
</html>
""",
    height=850,
    scrolling=True,
)