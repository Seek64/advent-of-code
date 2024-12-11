with open("input.txt", "r") as f:
    input_str = f.read()

stone_line = list(map(int, input_str.split()))


def blink(stones: list[int]) -> list[int]:
    update_stones = list()
    for stone in stones:
        if stone == 0:
            update_stones.append(1)
        elif len(str(stone)) % 2 == 0:
            half = len(str(stone)) // 2
            update_stones.append(int(str(stone)[:half]))
            update_stones.append(int(str(stone)[half:]))
        else:
            update_stones.append(stone * 2024)
    return update_stones


for i in range(25):
    stone_line = blink(stone_line)

result = len(stone_line)

print(result)
