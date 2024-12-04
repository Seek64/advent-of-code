from re import findall

with open("input.txt", "r") as f:
    input_str = f.read()

result = 0
enabled = True
for cmd in findall(r"mul\(\d+,\d+\)|do\(\)|don\'t\(\)", input_str):
    if cmd == "do()":
        enabled = True
    elif cmd == "don't()":
        enabled = False
    elif enabled:
        a, b = findall(r"\d+", cmd)
        result += int(a) * int(b)

print(result)
