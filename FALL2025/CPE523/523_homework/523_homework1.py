# CPE 523 - Homework #1
# Ryan Cramer

p_nm = 250e-9
p_v = 3.3
p_f = 200e6
p_w = 15.5

p4_nm = 65e-9
p4_v = 1.2
p4_f = 3.6e9
p4_w = 86

# Since P = C_eff * (V_dd)^2 * f 
# C_eff = P/((V_dd)^2 * f)

p_c_eff = p_w/((p_v**2) * p_f)
p4_c_eff = p4_w/((p4_v**2) * p4_f)
print("P1\n")
print(f"C_EFF for the Pentium is {p_c_eff:.02e}")
print(f"C_EFF for the Pentium 4 is {p4_c_eff:.02e}")

c_new = p_c_eff * (p4_nm/p_nm)
f_new = p_f * (p_nm/p4_nm)

p_new = c_new * (1.2**2) * f_new

print(f"The power consumption would be {p_new:.02f} Watts")
print(f"Thew new frequency would be {f_new:.02f} Hz")

print("\nP2\n")

# Using the results from P1

perf_p4 = 1.5 * p4_f
perf_p = 1.0 * f_new

num_p_65_cores = (int) (perf_p4/perf_p)
rem = perf_p4 % perf_p
if (rem != 0):
    num_p_65_cores = num_p_65_cores + 1

w_total = num_p_65_cores * p_new

print(f"Number of Pentium 65nm cores needed: {num_p_65_cores} ")
print(f"The power for 8 cores: {w_total:.02f} Watts")

if(w_total < p4_w):
    print("\nIf I was an engineer working at Intel,")
    print("I would recommend using a multi-core Pentium design")
    print("because it offers equal performance for less power overall")
    print(f"The Pentium 4 requires {p4_w-w_total} more watts for equal performance")
else:
    print("\nIf I was an engineer working at Intel,")
    print("I would recommend using the single Pentium 4 for the design")
    print("because it offers equal performance for less power overall")
    print(f"The Pentium 65nm require {w_total-p4_w} more watts for equal performance")
