---
title: EEL Processor
nav_order: 4
---
# EEL Processor
## [EEL Github Repo](https://github.com/ryancramuh/EEL) 


The EEL-32I is a pipelined 32-bit RV32I processor. The goal of the EEL is to be the basis for a later, ASIC hardened drop-in core. 
## Background 
### *EEL: Evolved Execution Logic* 
Based on the CPE 333 OTTER, the EEL is a highly parameterized, clean RISC-V integer implementation, with extensions for multiplication/division, as well as compressed instructions. Because the 333 OTTER only had a static branch predictor with no interrupts, we hope to create reduced gate expressions for the Hazard Unit (make it purely combinational), and drop in a CSR-based interrupt system, along with dynamic branch predictor. 
## ISA Extensions
The EEL will target being the base for several new extensions:
<br>Zifencei
<br>Zicsr
<br>M - multiply/divide
<br>A - atomic
<br>C - compressed

## Design Goals
Though many iterations of the OTTER exist, no accessible version has been developed usign Design-for-Test (DFT) or extended to this extent. The basic OTTER many are familiar with simply implements a set of arithmetic operations, control-transfer operations, and memory/register read/write operations. With DFT principles in mind, the EEL will be developed using parameterizable modules, with well defined net names. Much care will be taken in developing the Hazard Unit and the Branch Predictor, to try to get all instructions within 1.5 cycles per instruction. A CSR-based interrupt/trap system will be implemented, as well as multiplication/division, and a decompression unit to support compressed instrcutions.  

## Current Modules (Verified):
- 4 to 1 MUX (n-bit)
- 2 to 1 MUX (n-bit)
- Program Counter (n-bit)
- Instruction Memory (configurable, set to 64kB)
- Data Memory (configurable, set to 64kB)
- Register File (32 x 32)
- Instruction Decoder 
- Immediate Extender
- Arithmetic Logic Unit

## Current Status:
- As of 10/9/2025, multiplier and divider are being implemented to the core.
- Verification for the M extension has begun, and the next phase is implementing the Jump/Branch prediction. 

## Original Schematic
<img src="./images/EEL_DIAGRAM.svg" alt="Project logo" width="2000">

## Hazard Forwarding Schematic 
<img src="./images/EEL_DIAGRAM_HAZsvg.svg" alt="Project logo" width="2000">
