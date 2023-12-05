from re import findall

f = open("input.txt", "r")
input_str = f.read()
f.close()

_, seed_str, *map_str = input_str.split(":")

seeds = [int(s) for s in findall(r"\d+", seed_str)]

for m in map_str:
    ranges = list()
    for range_str in findall(r"\d+ \d+ \d+", m):
        ranges.append(tuple(int(n) for n in range_str.split()))

    for i, seed in enumerate(seeds):
        for d_start, s_start, l_range in ranges:
            if s_start <= seed < s_start + l_range:
                seeds[i] = d_start + (seed - s_start)

result = min(seeds)

print(result)
