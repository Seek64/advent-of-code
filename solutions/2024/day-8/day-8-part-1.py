import itertools
import re

with open("input.txt", "r") as f:
    input_str = f.read()

antennas = dict()

for m in re.finditer(r"[a-zA-Z0-9]", input_str):
    if m.group() in antennas:
        antennas[m.group()].append(m.start())
    else:
        antennas[m.group()] = [m.start()]

roof = [c for c in input_str]
for pos_list in antennas.values():
    for i, j in itertools.combinations(pos_list, 2):
        # i < j since we don't change the order
        d = j - i
        y_dist = roof[i:j].count("\n")
        if i - d >= 0 and roof[i - d:i].count("\n") == y_dist and roof[i - d] != "\n":
            roof[i - d] = "#"
        if j + d < len(roof) and roof[j:j + d + 1].count("\n") == y_dist and roof[j + d] != "\n":
            roof[j + d] = "#"

result = roof.count("#")
print(result)
