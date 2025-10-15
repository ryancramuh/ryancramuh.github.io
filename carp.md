---
title: CARP Project
nav_order: 4
---

# CARP Project (President)

The **Computer Architecture Research Project (CARP)** at **Cal Poly San Luis Obispo** is a student-led research initiative that I founded and lead.  
CARP’s mission is to **bridge digital design education and real-world silicon development**, giving students the opportunity to take a custom **RISC-V SoC** from RTL to GDSII using fully open-source ASIC tools.

**Websites:**
- [calpolycarp.org](https://calpolycarp.org) — main project site and outreach portal  
- [cal-poly-ramp.github.io](https://cal-poly-ramp.github.io) — internal documentation and technical wiki  

---

## Leadership and Vision

- **Founder & Lead of CARP** — Established the project to empower Cal Poly students with real industry-relevant ASIC and FPGA experience.  
- **Defined the organizational structure** for Frontend (RTL/ISA), Backend (Verification & Synthesis), and Layout (PDK/Physical Design) teams.  
- Built a framework for **sustained multi-quarter collaboration**, enabling continuity beyond a single academic term.  
- Guided the team toward a **tapeout-ready open-source RISC-V SoC**, emphasizing documentation, verification, and reproducibility.

---

## Documentation and Infrastructure

I built and maintained CARP’s documentation ecosystem to ensure professional-level clarity and onboarding ease.

- Created the **CARP Documentation Hub** using **GitHub Pages** (`cal-poly-ramp.github.io`) with a **"Read the Docs"**-style structure.  
- Authored and maintained reStructuredText and Markdown-based content for:
  - **Meeting notes** (`meeting-1.rst` through `meeting-8.rst`)
  - **Technical reports**, such as the multiplier/divider verification, pipeline hazard integration, and OpenLane layout readiness.
  - **Team guides**, including Docker setup, GitHub workflow, branch policies, and RISC-V testbench integration.
- Built the `_static/pdf/meeting-slides/` section and embedded interactive PDFs directly in RST via `<iframe>` tags for visual documentation.
- Managed visual consistency through `_config.yml` and SCSS theme customization for CARP’s GitHub Pages.

---

## System Setup and Tooling

To support cross-disciplinary collaboration, I designed a reproducible **Docker environment** integrating all required ASIC tools:

- **OpenLane**, **Yosys**, **Magic**, **KLayout**, **Netgen**, **Verilator**, and **Icarus Verilog** — packaged into a unified CARP Docker image.
- Added **RISC-V GNU toolchain**, **Spike**, and **FreeRTOS** support for embedded testing.
- Wrote comprehensive setup scripts (`install.sh`, `run.sh`, and `carp-tools/entrypoint.sh`) to simplify environment bootstrapping.
- Ensured compatibility between student laptops, lab machines, and remote build servers using containerized workflows.
- Deployed a custom **CARP Tools Docker image**, forked from IIC-OSIC-TOOLS and extended for RISC-V verification and ASIC synthesis.

---

## Advocacy and Recognition

CARP’s impact extends beyond the lab — I’ve led outreach and advocacy to secure recognition and support from Cal Poly and the broader academic community.

- **Advocated for official recognition** as a **Cal Poly Research Organization**, coordinating with faculty advisor  **Professor James (Bryan) Mealy**.  
- Collaborated with **EE and CPE departments** to align CARP’s roadmap with VLSI and digital systems coursework.  
- Drafted **bylaws and proposal documents** for recognition under both RSO and IRA pathways.  
- Presented CARP’s mission and progress to faculty and peers, earning strong institutional support and academic acknowledgment.

---

## Reports and Progress Deliverables

I created and organized formal documentation across multiple project phases:

- **CARP Meeting Slides**: Designed RST/Markdown-based presentation decks summarizing milestones, verification progress, and design status.  
- **Verification Reports**: Authored detailed analyses on:
  - RV32IM pipeline integration
  - Multiplier/divider unit test results
  - Hazard detection and forwarding coverage
  - Layout and DRC/LVS verification summaries
- **Milestone Documents**: Transition points (e.g., from design to verification) formally recorded and published on the documentation site.

---

## Outreach and Team Culture

- Developed CARP’s **visual identity**: logo, branding, and CARP-themed slides and documentation styling.  
- Organized weekly meetings and technical review sessions.  
- Onboarded and mentored new members in Verilog, SystemVerilog, and ASIC flow fundamentals.  
- Fostered an open-source, collaborative culture emphasizing learning and ownership.

---

## Summary

Through CARP, I’ve established a **comprehensive student research ecosystem** that blends:
- Advanced technical design (RTL → GDSII),
- Clear documentation and public transparency,
- Departmental advocacy, and long-term sustainability through infrastructure and mentorship.

CARP now stands as one of the first open-source ASIC research projects at Cal Poly — a community of engineers pushing the boundaries of what’s possible in undergraduate chip design.

---

**Links:**  
- [calpolycarp.org](https://calpolycarp.org)  
- [cal-poly-ramp.github.io](https://cal-poly-ramp.github.io)
