from re import findall

with open("input.txt", "r") as f:
    input_str = f.read()

left_list = []
right_list = []
result = 0

for a, b in findall(r"(\d+) +(\d+)", input_str):
    left_list.append(int(a))
    right_list.append(int(b))

for n in left_list:
    result += n * right_list.count(n)

print(result)
