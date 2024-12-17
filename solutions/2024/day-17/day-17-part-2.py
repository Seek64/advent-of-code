import re

with open("input.txt", "r") as f:
    input_str = f.read()

reg_a_init, reg_b_init, reg_c_init, *i_mem = map(int, re.findall(r"\d+", input_str))


# Brute force is not feasible.
# Since the program only consists of 8 instructions, I de-assembled and analyzed it manually.
#
# Input Program:
# 2, 4
# 1, 1
# 7, 5
# 1, 5
# 4, 3
# 0, 3
# 5, 5
# 3, 0
#
# while a > 0:
#  b = a % 8
#  b = b ^ 1
#  c = a >> b
#  b = b ^ 5
#  b = b ^ c
#  a = a >> 3
#  out <- b % 8

# 16 iterations (i.e., outputs) required: 2**45 <= a < 2**48

def single_it(a: int) -> int:
    b = a % 8
    b = b ^ 1
    c = a >> b
    b = b ^ 5
    b = b ^ c
    return b % 8


# Analyze the program backwards to determine digits of a required to produce the desired result
curr_a = {0}
for target_output in i_mem[::-1]:
    next_a = set()
    for ca in curr_a:
        for i in range(8):
            if single_it((ca << 3) + i) == target_output:
                next_a.add((ca << 3) + i)
    curr_a = next_a

print(min(curr_a))
