---
title: Home
nav_order: 1
---

<section class="chip-hero">
  <div class="chip-hero__prompt">ryan@silicon:~$ whoami<span class="blink">▊</span></div>
  <h1>Ryan Cramer</h1>
  <p class="chip-hero__role">B.S. Computer Engineering · Cal Poly SLO</p>
  <p>
    My work sits at the intersection of digital design, computer architecture, FPGA
    development, and ASIC design. Across coursework, internships, and student-led research
    I've built projects spanning autonomous vehicle software, hardware diagnostics, embedded
    systems, RISC-V processors, and full ASIC design flows. I founded and served as president
    of CARP — the Computer Architecture Research Project at Cal Poly — a student organization
    helping students build the skills to enter the semiconductor industry. I'm driven to build
    silicon-based devices that change the world for the better.
  </p>
  <div class="chip-hero__meta">
    <span class="chip-tag" data-cat="rtl">RTL</span>
    <span class="chip-tag" data-cat="pd">Physical Design</span>
    <span class="chip-tag" data-cat="asic">ASIC Flow</span>
    <span class="chip-tag" data-cat="arch">Computer Architecture</span>
    <span class="chip-tag" data-cat="verif">Verification</span>
  </div>
</section>

<div class="chip-eyebrow">modules // start here</div>

<div class="chip-grid">
  <a class="chip-card" href="{{ '/dashboard.html' | relative_url }}">
    <div class="chip-card__kicker">taskboard</div>
    <div class="chip-card__title">Weekly Study Dashboard</div>
    <div class="chip-card__desc">Rotating queue of RTL / PD / ASIC topics to study, with progress tracked in-browser.</div>
    <div class="chip-card__tags"><span class="chip-tag" data-cat="asic">checklists</span><span class="chip-tag" data-cat="pd">progress</span></div>
  </a>
  <a class="chip-card" href="{{ '/events.html' | relative_url }}">
    <div class="chip-card__kicker">calendar</div>
    <div class="chip-card__title">Industry Events</div>
    <div class="chip-card__desc">Upcoming semiconductor / EDA events — online or within an hour of San Jose.</div>
    <div class="chip-card__tags"><span class="chip-tag" data-cat="arch">conferences</span><span class="chip-tag" data-cat="eda">webinars</span></div>
  </a>
  <a class="chip-card" href="{{ '/schedule.html' | relative_url }}">
    <div class="chip-card__kicker">schedule</div>
    <div class="chip-card__title">My Calendar</div>
    <div class="chip-card__desc">Live class &amp; work schedule pulled from Google Calendar.</div>
    <div class="chip-card__tags"><span class="chip-tag">weekly</span></div>
  </a>
</div>

<div class="chip-eyebrow">projects // silicon &amp; systems</div>

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
    <div class="chip-card__desc">Wafer mask design, the KLA tour, and SEMICON Japan — the physical layer up close.</div>
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
    <div class="chip-card__desc">Computer Architecture Research Project — the student research group I lead at Cal Poly.</div>
    <div class="chip-card__tags"><span class="chip-tag" data-cat="arch">architecture</span></div>
  </a>
  <a class="chip-card" href="{{ '/eva.html' | relative_url }}">
    <div class="chip-card__kicker">research</div>
    <div class="chip-card__title">EVA</div>
    <div class="chip-card__desc">Environmental Vibration Analyzer — mixed-signal sensing with neuromorphic computation.</div>
    <div class="chip-card__tags"><span class="chip-tag" data-cat="dsp">mixed-signal</span></div>
  </a>
</div>

<div class="chip-eyebrow">coursework // quarters</div>

<div class="chip-grid">
  <a class="chip-card" href="{{ '/FALL2025/Fall_2025.html' | relative_url }}">
    <div class="chip-card__kicker">2025</div>
    <div class="chip-card__title">Fall Quarter</div>
    <div class="chip-card__desc">CPE 523, EE 431, PHYS 425 + Capstone notes.</div>
  </a>
  <a class="chip-card" href="{{ '/WINTER2026/Winter_2026.html' | relative_url }}">
    <div class="chip-card__kicker">2026</div>
    <div class="chip-card__title">Winter Quarter</div>
    <div class="chip-card__desc">CPE 426, CSC 453, EE 529, EE 531.</div>
  </a>
  <a class="chip-card" href="{{ '/SPRING2026/Spring_2026.html' | relative_url }}">
    <div class="chip-card__kicker">2026</div>
    <div class="chip-card__title">Spring Quarter</div>
    <div class="chip-card__desc">CPE 400 (HLS), CPE 439, CPE 464.</div>
  </a>
</div>

<div class="chip-eyebrow">schedule // this week</div>

<div class="chip-panel chip-cal">
  <iframe src="https://calendar.google.com/calendar/embed?src=ngc9dfl0qm68j5cfmkcugkabjb8ra03k%40import.calendar.google.com&ctz=America%2FLos_Angeles" style="border:0" width="800" height="600" frameborder="0" scrolling="no"></iframe>
</div>
