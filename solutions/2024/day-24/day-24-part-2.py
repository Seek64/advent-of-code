import re
from collections import deque

with open("input.txt", "r") as f:
    input_str = f.read()

# The circuit implements a ripple-carry adder made of a single half-adder and 44 full-adders
#
# Half Adder:
# z00 = x00 ^ y00
# c00 = x00 * y00
#
# Full Adder:
# z01 = x01 ^ y01 ^ c00
# c01 = x01 * y01 + (x01 ^ y01) * c00 = x01 * y01 + x01 * c00 + y01 * c00
#
# We check when these connection rules are violated

inputs = list()
for gate in re.findall(r"([a-z0-9]+): [0-1]", input_str):
    inputs.append(gate)

gates = dict()
gate_fan_out = dict()
outputs = list()
pattern = re.compile(r"([a-z0-9]+) (AND|OR|XOR) ([a-z0-9]+) -> ([a-z0-9]+)")
for rs1, op, rs2, rd in re.findall(pattern, input_str):
    if rs1[0] == "y":
        rs1, rs2 = rs2, rs1
    gates[rd] = (rs1, op, rs2)
    gate_fan_out[rs1] = gate_fan_out.get(rs1, list()) + [op]
    gate_fan_out[rs2] = gate_fan_out.get(rs2, list()) + [op]
    if rd[0] == "z":
        outputs.append(rd)

wrong_outputs = set()
for rd, (rs1, op, rs2) in gates.items():
    if op == "AND":
        # AND gates are always connected to OR gates (except for the half adder x00 * y00)
        if set(gate_fan_out.get(rd, [])) != {"OR"} and rs1 != "x00":
            wrong_outputs.add(rd)
            # print("%s %s %s -> %s" % (rs1, op, rs2, rd), gate_fan_out.get(rd, []))
    elif op == "OR":
        # OR gates (carry out) are always connected to an AND and an XOR gate (except for the last output)
        if set(gate_fan_out.get(rd, [])) != {"AND", "XOR"} and rd != "z45":
            wrong_outputs.add(rd)
            # print("%s %s %s -> %s" % (rs1, op, rs2, rd), gate_fan_out.get(rd, []))
    elif op == "XOR":
        # XOR gates are always connected to an AND and an XOR gate, or are outputs
        if set(gate_fan_out.get(rd, [])) != {"AND", "XOR"} and rd not in outputs:
            wrong_outputs.add(rd)
            # print("%s %s %s -> %s" % (rs1, op, rs2, rd), gate_fan_out.get(rd, []))
        elif set(gate_fan_out.get(rd, [])) == {"AND", "XOR"} and rs1 not in inputs:
            wrong_outputs.add(rd)
            # print("%s %s %s -> %s" % (rs1, op, rs2, rd), gate_fan_out.get(rd, []))

print(*sorted(wrong_outputs), sep=",")

# x05 AND y05 -> svm ['XOR', 'AND']
# fsp AND bdr -> z39 []
# dkk OR pbd -> z15 []
# bdr XOR fsp -> fnr ['OR']
# x05 XOR y05 -> nbc ['OR']
# x23 AND y23 -> z23 []
# kph XOR hpw -> cgq ['OR']
# fwr XOR cpv -> kqk ['XOR', 'AND']

# x05 AND y05 -> fnr/nbc/cgq
# x23 AND y23 -> fnr/nbc/cgq
# fsp AND bdr -> fnr/nbc/cgq
# dkk  OR pbd -> kqk
# x05 XOR y05 -> svm
# bdr XOR fsp -> z39
# kph XOR hpw -> z23
# cpv XOR fwr -> z15

# cgq,fnr,kqk,nbc,svm,z15,z23,z39
