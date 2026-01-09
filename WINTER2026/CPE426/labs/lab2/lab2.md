---
title: CPE 426 Lab 2
parent: CPE 426 Labs
nav_order: 2
--- 

# Lab 2 - Ring-Oscillator Based TRNG 

### Introduction 
In the last lab we explored using ring oscillators as a source of per-device randomness. We designed the circuits in lab 1 so that per-device randomness would be the dominant factor in determining the output, providing us with a useful PUF implementation. In this lab, however, we’re going to try designing our circuits so that stochastic (random) noise sources determine the output. Specifically, we’re trying to measure “jitter” or random fluctuations in the period of a ring oscillator to generate true random numbers.


Our implementation for this lab is based off of the circuit described in:
Kohlbrenner, Paul, and Kris Gaj. "An embedded true random number generator for FPGAs." Proceedings of the 2004 ACM/SIGDA 12th international symposium on Field programmable gate arrays. ACM, 2004. 

This time, you need to find and download the paper. You will probably want to log into and use the [Cal Poly Library website](https://lib.calpoly.edu/).

### Lab Products 

1. An answer to all questions in the questions section of the lab

2. A description of approaches taken, problems encountered, and techniques used to overcome these challenges.

3. A working Ring-Oscillator based random number generator based off of the architecture in Figure 2 of Kohlbrenner et. al with either an XOR or a Von Neumann corrector to improve bias. Use the 7-segment display from last lab to show a new 16-bit random number each time a button is pressed.

4. An analysis of the behavior of your random number generator both with and without your corrector. 

    1. Measure 100 bits of your RNG without corrector, what percent of bits are 1 vs. 0? What is the longest streak of 1 number (take the max of the length of the longest string of 1s and the longest string of 0s)

    2. Measure 100 bits of your RNG with corrector, what percent of bits are 1 vs. 0? What is the longest streak of 1 number (take the max of the length of the longest string of 1s and the longest string of 0s)
 
    3. (If we make it work) During Lab Demo day, provide your outputs from A and B to the software teams to measure using their statistical tests.

### Potential Problems 

Since we’re still using ring-oscillators, many of the potential problems from the last lab apply to this one. Remember to set "keep" and "dont_touch" attributes on your ring oscillator signals so Vivado doesn’t optimize pairs of inverters or transparent latches away. Also, remember to allow combinatorial nets in your constraints file. 

### Questions 

1. How did you modify your TRNG to generate 16-bit random numbers?

2. In this lab and the previous lab we used Ring Oscillators to capture different aspects of randomness- device-to-device vs. stochastic. What allows the ring oscillators in this lab to capture stochastic randomness?

3. There are many different ways to generate random numbers on FPGA, including other circuit topologies that rely on ring oscillators. Find a peer-reviewed paper that describes a method for random number generation and summarize how that random number generator works here. Be
sure to cite the paper you use. 