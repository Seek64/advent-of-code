from re import findall

with open("input.txt", "r") as f:
    input_str = f.read()

left_list = []
right_list = []
result = 0

for a, b in findall(r"(\d+) +(\d+)", input_str):
    left_list.append(int(a))
    right_list.append(int(b))

left_list.sort()
right_list.sort()

for i in range(len(left_list)):
    result += abs(right_list[i] - left_list[i])

print(result)
