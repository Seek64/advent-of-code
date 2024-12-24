import re

with open("input.txt", "r") as f:
    input_str = f.read()

computers = dict()
for pc_a, pc_b in re.findall(r"(\w+)-(\w+)", input_str):
    computers[pc_a] = computers.get(pc_a, set()) | {pc_b}
    computers[pc_b] = computers.get(pc_b, set()) | {pc_a}

connected_triples = set()
for pc_a in computers:
    if not pc_a.startswith("t"):
        continue
    for pc_b in computers[pc_a]:
        for pc_c in computers[pc_b]:
            if pc_a in computers[pc_c]:
                triple = tuple(sorted([pc_a, pc_b, pc_c]))
                connected_triples.add(triple)

print(len(connected_triples))
