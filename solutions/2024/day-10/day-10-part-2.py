with open("input.txt", "r") as f:
    input_str = f.read()

height_map = [[int(n) for n in row] for row in input_str.split("\n")]
WIDTH = len(height_map[0])
HEIGHT = len(height_map)
trailheads = [(i, j) for i, row in enumerate(height_map) for j, n in enumerate(row) if n == 0]

result = 0
for i, j in trailheads:
    curr_pos = {(i, j)}
    for next_height in range(1, 10):
        next_pos = set()
        for trail in curr_pos:
            x, y = trail[-2:]
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < HEIGHT and 0 <= ny < WIDTH and height_map[nx][ny] == next_height:
                    next_pos.add(trail + (nx, ny))
        curr_pos = next_pos
    result += len(curr_pos)

print(result)
