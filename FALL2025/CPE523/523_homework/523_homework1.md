---
title: 523 Homework 1
parent: 523 Homework
nav_order: 1
---
    
## Homework 1: Multi-Core Processor Tradeoffs

Recently, micro-processor manufacturers have started putting multiple processors on the same die rather than building a larger, faster single processor. The reason for this shift is that processor designs follow a non-linear performance vs. energy design curve. In modern processor designs, four mediocre processor cores can deliver better performance at lower power than a single well-designed core. This problem will explore some of the trade-offs in multi-core designs.

## Q1

The Intel Pentium microprocessor was manufactured in a $ 0.25\mu m $ process, had a $ 3.3V $ power supply, ran at a frequency of up to $ 200 MHz $ and consumed $ 15.5W $ of power. The Intel Pentium 4 chip was manufactured in a $ 65nm $ process, had a $ 1.2V $ power supply, consumed $ 86W $ of power and run at $ 3.6Ghz $.  If the Intel Pentium design was directly ported to a $ 65nm $ process with $ V_{dd} $ , what frequency and power consumption would you expect it to have?

Hint: Power is given by $ P = C_{eff}V_{dd}^{2}f $.
For the sake of this problem, assume that capacitance decreases linearly with process size, and that frequency increases linearly with process size.

## Q2 

Using the results from part a, how many 65nm Pentium cores would be needed to achieve the same performance as a single Pentium 4 chip? For this problem, assume that the Pentium 4 produces 1.5 times more useful work per cycle than the Pentium chip.  Also assume that all programs are fully parallelizable (i.e. two Pentium cores deliver twice the performance of a single Pentium core).  How much power would these Pentium cores require?  If you were an engineer working at Intel, would you recommend using a multi-core Pentium design or the single Pentium 4?  Why?
