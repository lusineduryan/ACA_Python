# Compute i=01000ai, where a0=0, d=5 and ai=ai-1+(i % 3)*d

a_0 = 0
d = 5
a_1 = a_0 + 1 % 3 * d
a_2 = a_1 + 1 % 3 * d

d_1 = d_2 = 15
end_1 = a_1 + 333 * d_1 + 1
end_2 = a_2 + 332 * d_2 + 1

prog_1 = range(a_1, end_1, d_1)
prog_2 = range(a_2, end_2, d_2)

print(sum(prog_1) + 2 * sum(prog_2) + a_0)