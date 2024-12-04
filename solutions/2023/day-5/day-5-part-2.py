from re import findall

f = open("input.txt", "r")
input_str = f.read()
f.close()

_, seed_str, *map_str = input_str.split(":")

seeds = [tuple(map(int, s.split())) for s in findall(r"\d+ \d+", seed_str)]

for m in map_str:
    ranges = list()
    for range_str in findall(r"\d+ \d+ \d+", m):
        ranges.append(tuple(int(n) for n in range_str.split()))

    new_seeds = list()

    for seed_start, seed_range in seeds:
        seed_processed = False
        for dst_start, src_start, map_range in ranges:
            seed_end = seed_start + seed_range - 1
            src_end = src_start + map_range - 1

            overlap_start = max(seed_start, src_start)
            overlap_end = min(seed_end, src_end)
            overlap_range = overlap_end - overlap_start + 1

            if overlap_range > 0:

                new_seeds.append((dst_start + (overlap_start - src_start), overlap_range))

                if seed_start < overlap_start:
                    seeds.append((seed_start, overlap_start - seed_start))
                if seed_end > overlap_end:
                    seeds.append((overlap_end + 1, seed_end - overlap_end))

                seed_processed = True

        # seed is not mapped at all and keeps its value range
        if not seed_processed:
            new_seeds.append((seed_start, seed_range))

    seeds = new_seeds

result = min(s for s, _ in seeds)

print(result)
