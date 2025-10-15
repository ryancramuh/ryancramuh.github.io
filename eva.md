---
title: EVA
nav_order: 5
---

# Ryan Cramer — Work with EVA (Environmental Vibration Analyzer)

The **Environmental Vibration Analyzer (EVA)** is a mixed-signal embedded research project I designed to analyze real-world vibration patterns and interpret them through **neuromorphic computation**.  
Built around an **STM32L476RGT6 microcontroller**, EVA combines **sensor acquisition**, **analog preprocessing**, and **on-board signal analysis** with the long-term goal of enabling **spiking neural network (SNN)**-based vibration classification for predictive maintenance.

---

## Project Overview

EVA began as a proof-of-concept system capable of generating, capturing, and transforming analog signals in real time.  
The early prototype demonstrated:
- **Waveform generation** through the STM32 DAC (sine, triangle, sawtooth).  
- **Signal sampling** through the ADC with 1 MHz acquisition rate.  
- **Real-time FFT computation** using ARM’s CMSIS-DSP library.  
- **UART command interface** for interactive frequency tuning and FFT output visualization.  

This initial phase served as a testbed for the analog front-end and DSP chain.  
The final system eliminates the DAC and transitions toward **physical vibration sensing and neuromorphic analysis**.

---

## Final System Architecture

### Hardware Overview

| Subsystem | Description |
|------------|-------------|
| **Microcontroller** | STM32L476RGT6 (Cortex-M4F, single-precision FPU, FreeRTOS-compatible) |
| **Sensor Input** | ADXL1002 high-bandwidth accelerometer (via analog input) |
| **Analog Front-End** | Custom **BJT amplifier** and **active filter** chain to condition the accelerometer output before digitization |
| **Data Acquisition** | 12-bit ADC triggered by TIM2 at up to 1 MHz sample rate |
| **Neural Processing** | Future integration of **Leaky Integrate-and-Fire (LIF)** neural network layer to detect vibration signatures |
| **Communication** | UART terminal interface for system monitoring and debug output |

### System Flow


The **FFT stage** computes frequency-domain energy distributions, which feed into the **LIF neuron array**, acting as an adaptive classifier that recognizes vibration signatures associated with specific mechanical states or anomalies.

---

## Technical Accomplishments

### 1. Embedded DSP Implementation
- Implemented a **real-time FFT engine** using the CMSIS-DSP library (`arm_math.h`).
- Supported variable point sizes (e.g., 256–2048) and dynamic frequency domain analysis.
- Validated FFT magnitude accuracy with MATLAB reference scripts.

### 2. DAC-Based Signal Generation (Testing Phase)
- Generated stable **DAC-driven sine waves** synchronized with timer interrupts.
- Allowed user frequency control via UART commands (`f <freq>`).  
- Verified FFT spectral alignment of generated tones, confirming ADC–DAC synchronization.

### 3. Analog Signal Chain Development
- Designed **BJT amplifier stages** to bring micro-g accelerometer signals into the ADC’s measurable range.
- Incorporated **active bandpass filtering** (anti-aliasing and noise suppression) prior to digitization.
- Simulated the analog front-end in LTspice for bandwidth, noise floor, and phase response analysis.

### 4. Transition to Neuromorphic Processing
- Designing a **Leaky Integrate-and-Fire (LIF)** neural model to replace conventional FFT-only processing.  
- The LIF network will learn to identify vibration modes through time-domain spiking activity, enabling **event-driven inference**.  
- Planned implementation on STM32 or a custom RISC-V SoC (eventually within the CARP ecosystem).

---

## Goals and Future Development

- [ ] Integrate analog accelerometer input and replace DAC simulation.  
- [ ] Implement multi-channel sampling for 3-axis vibration sensing.  
- [ ] Port fixed-point LIF neural network to STM32 FreeRTOS framework.  
- [ ] Create UART-based visualization of spiking activity and frequency response.  
- [ ] Log spectral signatures for dataset generation and offline neural training.

---

## Broader Context and Vision

EVA is a stepping stone toward **hardware-level machine perception** — a fusion of analog electronics, embedded DSP, and neuromorphic computation.  
By translating real-world vibrations into spiking neuron dynamics, EVA lays the groundwork for **predictive maintenance systems** that can autonomously detect imbalance, wear, or resonance patterns in vehicles and industrial equipment.

The long-term vision is to integrate EVA into a **hardware neuromorphic sensor node** that learns from its environment without cloud dependency or external computation.

---

**Related Work:**  
- **CARP (Computer Architecture Research Project):** [calpolycarp.org](https://calpolycarp.org)  
- **CARP Documentation Hub:** [cal-poly-ramp.github.io](https://cal-poly-ramp.github.io)
