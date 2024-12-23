with open("input.txt", "r") as f:
    input_str = f.read()

seeds = list(map(int, input_str.split("\n")))
# 16777216 = 2 ** 24
PRUNE = 2 ** 24 - 1
N = 2000


def compute_change_seq(n: int) -> list[int]:
    change_seq = list()
    prev_d = n % 10
    for _ in range(N):
        n = ((n << 6) ^ n) & PRUNE
        n = ((n >> 5) ^ n) & PRUNE
        n = ((n << 11) ^ n) & PRUNE
        d = n % 10
        change_seq.append(d - prev_d)
        prev_d = d
    return change_seq


seq_values = dict()
for seed in seeds:
    diff_seq = compute_change_seq(seed)
    sell_price = seed % 10 + sum(diff_seq[:3])
    curr_seq_values = dict()
    for i in range(3, N):
        sell_price += diff_seq[i]
        curr_seq = tuple(diff_seq[i - 3:i + 1])
        if curr_seq not in curr_seq_values:
            curr_seq_values[curr_seq] = sell_price
    for seq in curr_seq_values:
        seq_values[seq] = seq_values.get(seq, 0) + curr_seq_values[seq]

best_seq = max(seq_values, key=seq_values.get)
print(seq_values[best_seq])
