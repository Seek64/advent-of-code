import re

with open("input.txt", "r") as f:
    input_str = f.read()

pattern = r"Button A: X\+(\d+), Y\+(\d+)\nButton B: X\+(\d+), Y\+(\d+)\nPrize: X=(\d+), Y=(\d+)"

N = 10000000000000
result = 0
for m in re.findall(pattern, input_str):
    x1, y1, x2, y2, x_target, y_target = map(int, m)
    x_target += N
    y_target += N
    nb = (y1 * x_target - x1 * y_target) / (x2 * y1 - x1 * y2)
    na = (x_target - x2 * nb) / x1
    if na.is_integer() and nb.is_integer() and (na >= 0 or nb >= 0):
        result += 3 * int(na) + int(nb)

print(result)
