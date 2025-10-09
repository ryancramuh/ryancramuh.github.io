---
title: 523 Homework 2
parent: 523 Homework
nav_order: 2
---

# Homework 2

**Due:** Thursday by 11:59 PM  
**Points:** 100  
**Submission Type:** File Upload  

---

## Technology Information

For all problems, assume the following technology parameters based on **45 nm CMOS process**:

- $\lambda = 22.5\text{ nm}$ (half the minimum gate length)  
- Minimum transistor length: $L_{min} = 2\lambda = 45\text{ nm}$  
- $V_{DD} = 1.0\text{ V}$  
- $C_{ox} = 2.5 \, \text{fF}/\mu\text{m}^2$ (oxide capacitance per unit area)  
- $C_{diff} = 0.5 \, \text{fF}/\mu\text{m}$ (diffusion capacitance per unit length)  
- $R_{unit} = 6.5\text{ k}\Omega/\mu\text{m}$ (unit transistor resistance at minimum length)  
- $T_{clk} = 1\text{ ns}$ (1 GHz clock frequency)  
- Wires are assumed to have length $L_{wire} = 200\lambda = 4.5\text{ µm}$.  
- All transistors are of minimum length unless otherwise specified.

For sizing or capacitance calculations, assume the following approximations:

- $C_{wire} = 0.2 \, \text{fF}/\mu\text{m}$  
- $E = \alpha \, C_{load} \, V_{DD}^2$  
- $P_{avg} = E / T_{clk}$  

---

## 1. Gate Design

Implement the following Boolean functions using a **single CMOS gate** (transistor-level schematic).  
Assume all inputs and their complements are available.

a) $F_1 = \overline{(A + \overline{B})}$  
b) $F_2 = \overline{(A \, B + \overline{C})}$

**Tasks:**
- Draw the full **transistor-level CMOS circuit** for each function.  
- Indicate all **pull-up and pull-down networks (PUN/PDN)** clearly.  
- Label transistor widths (in λ) and ensure logic symmetry.

---

## 2. Energy and Power Calculation

Consider the **combinational logic block** shown below.  
This circuit operates inside a sequential system with a **1 GHz clock (1 ns cycle time)**.  
We will analyze its **energy consumption** over **four clock cycles**.

All gate sizes are labeled on the schematic.  
The notation **N:4** indicates that each NMOS in that gate has **width 4λ**.  

The input waveforms $X(t)$ and $Y(t)$ are provided;  
each **vertical gridline** represents **one full clock cycle**.  
The clock period is long enough for all input changes to propagate through the circuit.

### Tasks

a) Draw the waveforms for the remaining nodes labeled **A, B, C, and F**.  

b) Calculate the **total number of transitions** and **activity factor** for each node:

$$
\alpha_i = \frac{\text{Number of transitions at node } i}{\text{Number of clock cycles}}
$$

for $i \in \{X, Y, A, B, C, F\}$ over 4 cycles.

c) Compute the **energy per cycle** and **average power dissipation** for each node:

$$
E_i = \alpha_i \, C_i \, V_{DD}^2
$$

$$
P_i = \frac{E_i}{T_{clk}}
$$

### Capacitance Model

For each node, total capacitance is given by:

$$
C_i = C_{diff,i} + C_{gate,load} + C_{wire}
$$

where:
- $C_{diff,i}$ = diffusion capacitance of the driving transistor(s)  
- $C_{gate,load}$ = sum of input gate capacitances of fanout gates  
- $C_{wire}$ = wire capacitance (based on 200λ interconnect length)

Assume all interconnects are 200λ long.  
Ignore any capacitance external to this circuit.

---

## 3. Transistor Sizing

For each gate shown below, determine transistor **widths (in λ)** such that the **worst-case pull-up and pull-down resistances** are each equal to **2.6 kΩ**.

### Guidelines

- Some circuits have series-connected devices; there are multiple ways to achieve total $R = 2.6\text{ k}\Omega$.  
- Choose transistor widths that **minimize total gate capacitance** while maintaining balanced input loading.  
- In general, try to equalize the resistance of series transistors.

Use the approximate relationship:

$$
R_{eq} = \frac{R_{unit} \cdot L}{W}
$$

and size transistors accordingly to meet $R_{eq,total} = 2.6\text{ k}\Omega$.

---

## 4. Ring Oscillator

Consider the **N-stage ring oscillator** shown below (typically 3 or 5 inverters).

### Tasks

a) Derive the **RC delay** of a single inverter:

$$
\tau_{inv} = R_p C_{load} + R_n C_{par}
$$

Identify and compute contributions from:
- **Fanout delay:** $R C_{load}$  
- **Parasitic delay:** $R C_{par}$  

b) Determine the **oscillation period**:

$$
T_{osc} = 2 N \tau_{inv}
$$

where $N$ is the number of inverters.

c) Compute the **oscillation frequency**:

$$
f_{osc} = \frac{1}{T_{osc}}
$$

---

## 5. Static Timing Analysis

Consider the logic network defined by the following **structural Verilog** description:

```verilog
inv   ginv1  (k, a);
or    gor1   (e, k, b);
nor   gnor1  (g, b, c);
and   gand1  (f, a, g);
and   gand2  (h, a, b);
xnor  gxnor1 (i, f, d);
or    gor2   (j, d, s);
xor   gxor1  (x, e, i);
or    gor3   (y, j, h);
