---
title: Home
layout: default
---

<section class="hero" id="intro">
  <div class="hero__prompt anim">ryan@silicon:~$ whoami<span class="blink">▊</span></div>
  <h1 class="hero__name anim">Ryan Cramer</h1>
  <p class="hero__role anim">B.S. Computer Engineering &middot; Cal Poly SLO</p>
  <p class="hero__blurb anim">
    I work at the intersection of digital design, computer architecture, FPGA development,
    and ASIC design. Across coursework, internships, and student-led research I have built
    RISC-V processors, embedded and motor-control systems, hardware diagnostics, and full
    ASIC design flows. I founded and lead CARP, the Computer Architecture Research Project
    at Cal Poly. I want to build silicon that changes the world for the better.
  </p>
  <div class="hero__meta anim">
    <span class="chip-tag" data-cat="rtl">RTL</span>
    <span class="chip-tag" data-cat="pd">Physical Design</span>
    <span class="chip-tag" data-cat="asic">ASIC Flow</span>
    <span class="chip-tag" data-cat="arch">Computer Architecture</span>
    <span class="chip-tag" data-cat="verif">Verification</span>
  </div>
  <div class="hero__cta anim">
    <a class="btn btn--primary" href="https://github.com/ryancramuh" target="_blank" rel="noopener"><span class="btn__i">◆</span> View my GitHub</a>
    <a class="btn" href="#projects">Browse projects</a>
    <a class="btn" href="{{ '/dashboard.html' | relative_url }}">Study dashboard</a>
  </div>
</section>

<section class="section reveal" id="github">
  <div class="gh">
    <div class="gh__top">
      <div class="gh__head">
        <div class="chip-eyebrow">source // github</div>
        <div class="gh__title">
          <svg viewBox="0 0 16 16" aria-hidden="true"><path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.01 8.01 0 0 0 16 8c0-4.42-3.58-8-8-8z"/></svg>
          <span>@<span class="gh__handle">ryancramuh</span></span>
        </div>
        <p class="gh__lead">
          RTL, embedded firmware, formal verification, and open-source ASIC flows.
          Everything below is public. The highlights:
        </p>
      </div>
      <div class="gh__actions">
        <a class="btn btn--primary" href="https://github.com/ryancramuh" target="_blank" rel="noopener">Follow on GitHub</a>
      </div>
    </div>

    <div class="gh__repos">
      <a class="repo" href="https://github.com/ryancramuh/EEL" target="_blank" rel="noopener">
        <div class="repo__name">EEL</div>
        <div class="repo__desc">EEL-32, a pipelined 32-bit RV32I processor built to be hardened into a drop-in ASIC block.</div>
        <div class="repo__meta"><span class="repo__lang"><span class="repo__dot" style="--_l:#dae1c2"></span>SystemVerilog</span></div>
      </a>
      <a class="repo" href="https://github.com/ryancramuh/SVPWM-STM32-Motor-Project" target="_blank" rel="noopener">
        <div class="repo__name">SVPWM-STM32-Motor-Project</div>
        <div class="repo__desc">Space-vector PWM drive for a 3-phase BLDC motor on the STM32L476RGT6.</div>
        <div class="repo__meta"><span class="repo__lang"><span class="repo__dot" style="--_l:#555"></span>C</span></div>
      </a>
      <a class="repo" href="https://github.com/ryancramuh/common-hdl" target="_blank" rel="noopener">
        <div class="repo__name">common-hdl</div>
        <div class="repo__desc">A reusable SystemVerilog HDL library of building blocks for larger designs.</div>
        <div class="repo__meta"><span class="repo__lang"><span class="repo__dot" style="--_l:#dae1c2"></span>SystemVerilog</span></div>
      </a>
      <a class="repo" href="https://github.com/ryancramuh/ttsky-verilog-calpoly-slo" target="_blank" rel="noopener">
        <div class="repo__name">ttsky-verilog-calpoly-slo</div>
        <div class="repo__desc">A Tiny Tapeout Sky130 design, taped out through the open-source flow.</div>
        <div class="repo__meta"><span class="repo__lang"><span class="repo__dot" style="--_l:#dae1c2"></span>SystemVerilog</span></div>
      </a>
      <a class="repo" href="https://github.com/ryancramuh/RTOS-Projects" target="_blank" rel="noopener">
        <div class="repo__name">RTOS-Projects</div>
        <div class="repo__desc">A collection of real-time operating system projects and FreeRTOS experiments.</div>
        <div class="repo__meta"><span class="repo__lang"><span class="repo__dot" style="--_l:#555"></span>C</span></div>
      </a>
      <a class="repo" href="https://github.com/ryancramuh/BareMetalRISCV" target="_blank" rel="noopener">
        <div class="repo__name">BareMetalRISCV</div>
        <div class="repo__desc">Bare-metal RISC-V bring-up and low-level firmware experiments.</div>
        <div class="repo__meta"><span class="repo__lang"><span class="repo__dot" style="--_l:#555"></span>C</span></div>
      </a>
    </div>
  </div>
</section>

<section class="section reveal" id="projects">
  <div class="chip-eyebrow">projects // silicon &amp; systems</div>
  <h2 class="section__title">Selected work</h2>
  <p class="section__lead">Deeper write-ups, photos, and notes for the projects I am most proud of.</p>

  <div class="chip-grid">
    <a class="chip-card" href="{{ '/EEL/EEL.html' | relative_url }}">
      <div class="chip-card__kicker">RV32I core</div>
      <div class="chip-card__title">EEL Processor</div>
      <div class="chip-card__desc">A pipelined 32-bit RISC-V core built to be hardened into a drop-in ASIC block.</div>
      <div class="chip-card__tags"><span class="chip-tag" data-cat="rtl">RTL</span><span class="chip-tag" data-cat="arch">RISC-V</span></div>
    </a>
    <a class="chip-card" href="{{ '/SVPWM_Project/SVPWM_MOTOR.html' | relative_url }}">
      <div class="chip-card__kicker">mixed-signal</div>
      <div class="chip-card__title">SVPWM BLDC ESC</div>
      <div class="chip-card__desc">Space-vector PWM motor controller on an STM32 driving a 3-phase BLDC via H-bridges.</div>
      <div class="chip-card__tags"><span class="chip-tag" data-cat="dsp">DSP</span><span class="chip-tag">embedded</span></div>
    </a>
    <a class="chip-card" href="{{ '/MST/mst.html' | relative_url }}">
      <div class="chip-card__kicker">device / fab</div>
      <div class="chip-card__title">MicroFab &amp; MST</div>
      <div class="chip-card__desc">Wafer mask design, the KLA tour, and SEMICON Japan. The physical layer up close.</div>
      <div class="chip-card__tags"><span class="chip-tag" data-cat="asic">fabrication</span><span class="chip-tag" data-cat="pd">devices</span></div>
    </a>
    <a class="chip-card" href="{{ '/Stanford_VLSI/stanford_vlsi.html' | relative_url }}">
      <div class="chip-card__kicker">reading room</div>
      <div class="chip-card__title">Stanford VLSI Library</div>
      <div class="chip-card__desc">Curated lecture sets and a deep archive of high-performance adder papers.</div>
      <div class="chip-card__tags"><span class="chip-tag" data-cat="papers">papers</span><span class="chip-tag" data-cat="arch">VLSI</span></div>
    </a>
    <a class="chip-card" href="{{ '/carp.html' | relative_url }}">
      <div class="chip-card__kicker">leadership</div>
      <div class="chip-card__title">CARP (Founder / President)</div>
      <div class="chip-card__desc">Computer Architecture Research Project, the student research group I lead at Cal Poly.</div>
      <div class="chip-card__tags"><span class="chip-tag" data-cat="arch">architecture</span></div>
    </a>
    <a class="chip-card" href="{{ '/eva.html' | relative_url }}">
      <div class="chip-card__kicker">research</div>
      <div class="chip-card__title">EVA</div>
      <div class="chip-card__desc">Environmental Vibration Analyzer, mixed-signal sensing with neuromorphic computation.</div>
      <div class="chip-card__tags"><span class="chip-tag" data-cat="dsp">mixed-signal</span></div>
    </a>
  </div>
</section>

<section class="section reveal" id="tools">
  <div class="chip-eyebrow">live // tools &amp; feeds</div>
  <h2 class="section__title">What I am tracking now</h2>
  <p class="section__lead">Self-updating dashboards I keep for staying sharp and plugged into the industry.</p>

  <div class="chip-grid">
    <a class="chip-card" href="{{ '/dashboard.html' | relative_url }}">
      <div class="chip-card__kicker">taskboard</div>
      <div class="chip-card__title">Weekly Study Dashboard</div>
      <div class="chip-card__desc">A rotating queue of RTL, PD, and ASIC topics, with progress tracked in-browser.</div>
      <div class="chip-card__tags"><span class="chip-tag" data-cat="asic">checklists</span><span class="chip-tag" data-cat="pd">progress</span></div>
    </a>
    <a class="chip-card" href="{{ '/events.html' | relative_url }}">
      <div class="chip-card__kicker">calendar</div>
      <div class="chip-card__title">Industry Events</div>
      <div class="chip-card__desc">A weekly feed of semiconductor and EDA meetups, webinars, and conferences, online or near San Jose.</div>
      <div class="chip-card__tags"><span class="chip-tag" data-cat="eda">weekly</span><span class="chip-tag" data-cat="arch">meetups</span></div>
    </a>
    <a class="chip-card" href="{{ '/schedule.html' | relative_url }}">
      <div class="chip-card__kicker">schedule</div>
      <div class="chip-card__title">My Calendar</div>
      <div class="chip-card__desc">Live class and work schedule pulled from Google Calendar.</div>
      <div class="chip-card__tags"><span class="chip-tag">weekly</span></div>
    </a>
  </div>
</section>

<section class="section section--tight reveal" id="archive">
  <a class="chip-panel" href="{{ '/archive.html' | relative_url }}" style="display:flex;align-items:center;gap:1rem;flex-wrap:wrap;text-decoration:none;">
    <div style="flex:1 1 300px;min-width:0;">
      <div class="chip-eyebrow">archive // coursework</div>
      <div style="color:var(--chip-heading);font-size:1.15rem;font-weight:600;">School &amp; coursework archive</div>
      <div style="color:var(--chip-muted);font-size:.9rem;margin-top:.25rem;">Every quarter at Cal Poly: notes, labs, syllabi, and reference material, kept out of the way but always here.</div>
    </div>
    <span class="btn">Open archive →</span>
  </a>
</section>
