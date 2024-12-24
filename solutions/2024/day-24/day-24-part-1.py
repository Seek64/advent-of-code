import re
from collections import deque

with open("input.txt", "r") as f:
    input_str = f.read()

evaluated_gates = dict()
for gate, init_value in re.findall(r"([a-z0-9]+): ([0-1])", input_str):
    evaluated_gates[gate] = init_value == "1"

instructions = deque()
pattern = re.compile(r"([a-z0-9]+) (AND|OR|XOR) ([a-z0-9]+) -> ([a-z0-9]+)")
for rs1, op, rs2, rd in re.findall(pattern, input_str):
    instructions.append((rs1, op, rs2, rd))

while instructions:
    rs1, op, rs2, rd = instructions.popleft()
    if rs1 in evaluated_gates and rs2 in evaluated_gates:
        if op == "AND":
            evaluated_gates[rd] = evaluated_gates[rs1] & evaluated_gates[rs2]
        elif op == "OR":
            evaluated_gates[rd] = evaluated_gates[rs1] | evaluated_gates[rs2]
        elif op == "XOR":
            evaluated_gates[rd] = evaluated_gates[rs1] ^ evaluated_gates[rs2]
    else:
        instructions.append((rs1, op, rs2, rd))

outputs = sorted(gate for gate in evaluated_gates if gate.startswith("z"))[::-1]
print(int("".join("1" if evaluated_gates[o] else "0" for o in outputs), 2))
