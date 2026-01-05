---
title: 523 Homework 3
parent: 523 Homework
nav_order: 3
---
    
## Homework 3 

Today most people write Verilog/VHDL and use synthesis programs to decide on the best boolean function for implementing the circuit. Since the circuits fabricated today contain tens of millions of gates, it makes sense to automate the majority of circuit design and rely on a Verilog/VHDL abstraction to speed up the process. In this homework, we will explore (on a much smaller scale) how gate sizing is done manually, and we will look at what Verilog and synthesis tools can do for us. 

### For all the problems, please use the following values where needed (based on 45 nm tech.)
 * $ \lambda = 0.0225 {\mu}m $
 * $ R_{sqp} = 26 kOhm/\square $
 * $ R_{sqn} = 12 kOhm/\square $
 * $ C_{gate} = 1.2 fF/{\mu}m$ of $W$
 * $ C_{d} = 1.2 fF/{\mu}m$ of $W$
 * $ V_{DD} = 1.0 V $
 * All the transistors have minimum length $2{\lambda}$
 * All the transistors have minimum width $4{\lambda}$

 ### 1. Gate Sizing 

 Your first task is to find the best logical implementation (with respect to delay) of an 8-input AND gate which drives a fanout of 100, and an 8-input AND gate which drivesa fanout of 10,000. You have only the gates provided in Table 1 available to you. You have been provided the parasitic delay of NAND, NOR, and interter gates. For logical effort calculations, assume equal rise and fall drive resistances. 

 Remember: Delay* = $(LE_{gate} \times FO) + P_{gate}$  

 Where Delay* is the delay of the gate normalized to 
 $\tau _{inv}$ and $$P_{gate}$$ is the parasitic delay of the gate also normalized to $\tau _{inv}$ 


| Circuit Element | 1 Input        | 2 Inputs        | 3 Inputs        | 4 Inputs        |
|-----------------|----------------|-----------------|-----------------|-----------------|
| Inverter        | $P_{inv}$ = 1       | —               | —               | —               |
| NAND            | —              | $2 {\times} P_{inv}$         | $3 {\times} P_{inv}$          | $4 {\times} P_{inv}$          |
| NOR             | —              | $3 {\times} P_{inv}$          | $4.5 {\times} P_{inv}$       | $6 {\times} P_{inv}$          |


While a good rule of thumb for a fast design is a fanout of 4, we will see in this problem that, for real circuits, the question of fastest fanout is a little more complex. As we change the number of stages, and the logic needed per stage, we are changing both the parasitic delay and the effort delay. The best topology minimizes the total delay and depends on the relationship between parasitic delay changes and fanout. For the fanout of 100 case, you will need to consider a few options to solve the problem. 

A. Please describe (sketch) two topologies that you think might be optimal for the FO=100 case, and how you selected them. Then calculate the delay for each of the designs, and find out which is best. Is there a FO value that would cause you to switch between the two? If so, what is it? 

B. Repeat 1.A for a fanout of 10,000. Do you still need to consider two topologies, or is there a clear design choice? 

C. Now that you have sketched the design on paper, it's time to see how it would be done in Verilog. Implement your AND gate structurally and verify that it works. 

D. Based on this exercise, can you explain why the industry jargon typically refers to a design having a clockspeed of $N \times FO4$ (i.e., "This circuit is designed for 5 logic levels in each clock cycle" or "5 FO4 per clock cycle")? Why would FO4 be a better way to compare designs than the actual frequency? 

### 2. How technology affects optimal circuit motifs

Because of leakage issues, many research groups are looking for a new type of switching element. The search is hard because leakage is fundamental for any device that modulates current by changing an energy barrier. One promising candidate is a nano relay - a device where the gate electrode is electro-statically attracted to another electrode and physically moves. This movement shorts the source and the drain terminals. This device acts like a transistor (capacitave input, resistance driven between source and drain), except it takes time to physically switch when the input arrives. Assume that the device takes 1ns to switch, and after switching its $C_{g} * R = 0.2ps$. Also assume that the device comes in pMOS and nMOS versions (these are made by changign the voltage of the counter electrode) and they have the same time constant (unlike CMOS where pMOS are 2x the resistance).

A. Draw a delay vs. fanout plot for an Inverter and 2-input NAND and NOR gates. Remember, as long as the delay is liner, one can use logical effort to represent the gate. Do these gates obey this rule? If so, what is the logical effort compared to a CMOS inverter? How do you deal with the switching time delay that does not depend on fanout/fanin? 

B. Using these transistors, should we design our circuits differently? If Logical Effort works for these cells, please use it to explain how we should change the way we design circuits. If Logical Effort does not work for these cells, explain how we should think about sizing, fanin, and fanout of these gates. To make the problem more concrete, think about how you should construct a circuit that compares two 64 bit numbers, or a 200 input AND? 

C. Follow the derivation of the optimal fanout from the class slides and find the optimal fanout for this technology. (The optimal fanout should be found numerically using an excel/matlab tool)

### 3. Delay and Energy Optimizations

The figure below shows a buffer chain of 4 inverters driving a wire load of 518fF. 

![inverter_circuit](hw_3_2.jpg) 

A. Size the final 3 inverters (in terms of $\lambda$) to minimize the delay from IN to $C_{load}$. Find the total delay from Input to Output in normalized unit delay and in picoseconds. 

B. We have seen in class that there is a tradeoff between energy consumed in the circuit and delay of the circuit. In this subpart, we will take a closer look at this tradeoff. We decide to tradeoff 15 percent of the delay for lower energy consumption. Change the fanout of the final stage and re-optimize the inverter chain so that the new delay is 15% greater than the optimized delay. 

Before you write some optimization script and let some program do the problem for you, please think of how the delay will change when you change the size of the final inverter. Will the delay of the first three gates change by much? Why? What about the delaly of the final stage? Those answers should make it much easier to check the answers from your program.

What is the saved energy (in percentage)? Assume that the input goes through a cycle of 0 -> 1 -> 0 transistions for the energy calculations 

C. Submit energy versus delay plot (energy in y-axis and delay in x-axis) for various values of fanout of the last inverter. (Hint: pick a fanout for the last inverter, find the nergy and dealy of the re-optimized chain for that fanout and plot it in the graph. Use a tool like Excel or Matlab to repeat the process for many fanout values). 

### 4. Verilog Debugging 

A 3-bit majority gate is a gate in which the output is high if two or more inputs are high. 

A. Write the boolean equation for this gate. Use A, B, and C for the inputs and F for the output. 

B. Complete a Boolean implementation and testbench for this circuit. 