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
        roof[i] = "#"
        roof[j] = "#"
        # i < j since we don't change the order
        d = j - i
        y_dist = roof[i:j].count("\n")
        k = i - d
        while k >= 0 and roof[k:k + d].count("\n") == y_dist and roof[k] != "\n":
            roof[k] = "#"
            k -= d
        k = j + d
        while k < len(roof) and roof[k - d:k + 1].count("\n") == y_dist and roof[k] != "\n":
            roof[k] = "#"
            k += d

result = roof.count("#")
print(result)
