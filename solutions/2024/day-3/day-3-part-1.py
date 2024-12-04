from re import findall

with open("input.txt", "r") as f:
    input_str = f.read()

result = 0
for a, b in findall(r"mul\((\d+),(\d+)\)", input_str):
    result += int(a) * int(b)

print(result)
