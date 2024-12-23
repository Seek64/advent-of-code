with open("input.txt", "r") as f:
    input_str = f.read()

seeds = list(map(int, input_str.split("\n")))
# 16777216 = 2 ** 24
PRUNE = 2 ** 24 - 1

result = 0
for seed in seeds:
    n = seed
    for _ in range(2000):
        n = ((n << 6) ^ n) & PRUNE
        n = ((n >> 5) ^ n) & PRUNE
        n = ((n << 11) ^ n) & PRUNE
    result += n
print(result)
