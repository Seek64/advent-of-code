import re

with open("input.txt", "r") as f:
    input_str = f.read()

computers = dict()
for pc_a, pc_b in re.findall(r"(\w+)-(\w+)", input_str):
    computers[pc_a] = computers.get(pc_a, set()) | {pc_b}
    computers[pc_b] = computers.get(pc_b, set()) | {pc_a}


# Maximum clique problem
# Solution could probably be more efficient...
connected_tuples = set()
for pc_a in computers:
    for pc_b in computers[pc_a]:
        connected_tuples.add(tuple(sorted([pc_a, pc_b])))
print(2, len(connected_tuples))

i = 3
while len(connected_tuples) > 1:
    next_tuples = set()
    for t in connected_tuples:
        for comp in computers:
            if comp in t:
                continue
            if all(comp in computers[c] for c in t):
                next_tuples.add(tuple(sorted([*t, comp])))
    connected_tuples = next_tuples
    print(i, len(connected_tuples))
    i += 1

for final_set in connected_tuples:
    print(",".join(final_set))
