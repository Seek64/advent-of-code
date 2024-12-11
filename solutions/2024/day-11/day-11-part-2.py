with open("input.txt", "r") as f:
    input_str = f.read()

initial_stones = list(map(int, input_str.split()))
stone_count = {s: initial_stones.count(s) for s in initial_stones}


def blink(stones: dict[int, int]) -> dict[int, int]:
    update_stones = {}
    for stone, cnt in stones.items():
        if stone == 0:
            update_stones[1] = update_stones.get(1, 0) + cnt
        elif (length := len(str(stone))) % 2 == 0:
            half = length // 2
            s1, s2 = divmod(stone, 10 ** half)
            update_stones[s1] = update_stones.get(s1, 0) + cnt
            update_stones[s2] = update_stones.get(s2, 0) + cnt
        else:
            s1 = stone * 2024
            update_stones[s1] = update_stones.get(s1, 0) + cnt
    return update_stones


for i in range(75):
    stone_count = blink(stone_count)

print(sum(stone_count.values()))
