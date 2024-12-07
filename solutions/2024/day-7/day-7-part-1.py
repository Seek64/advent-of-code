import re

with open("input.txt", "r") as f:
    input_str = f.read()


def find_combination(tgt: int, intermediate_result: int, op: list[int]) -> bool:
    if not op:
        return intermediate_result == tgt
    n, *op = op
    return find_combination(tgt, intermediate_result + n, op) or find_combination(tgt, intermediate_result * n, op)


result = 0
for equation_str in input_str.split("\n"):
    target, *operands = map(int, re.findall(r"\d+", equation_str))
    if find_combination(target, operands[0], operands[1:]):
        result += target

print(result)
