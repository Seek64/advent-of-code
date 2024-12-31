from itertools import combinations

with open("input.txt", "r") as f:
    input_str = f.read()

keys = list()
for raw_key in input_str.split("\n\n"):
    keys.append(int(raw_key.translate({ord("\n"): "", ord("#"): "1", ord("."): "0"}), 2))

result = 0
for key_a, key_b in combinations(keys, 2):
    if key_a & key_b == 0:
        result += 1

print(result)
