from collections import deque

with open("input.txt", "r") as f:
    input_str = f.read()

corrupted_bytes = [tuple(map(int, c.split(","))) for c in input_str.split("\n")]
WIDTH = HEIGHT = 71
N_CORR = 1024
shortest_path = {(0, 0) : 0}
to_check = deque()
to_check.append((0, 0))

while to_check:
    x, y = to_check.popleft()
    cost = shortest_path[(x, y)]
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < WIDTH and 0 <= ny < HEIGHT and (nx, ny) not in corrupted_bytes[:N_CORR]:
            next_cost = shortest_path.get((nx, ny), -1)
            if next_cost < 0 or cost + 1 < next_cost:
                shortest_path[(nx, ny)] = cost + 1
                to_check.append((nx, ny))

print(shortest_path[(WIDTH - 1, HEIGHT - 1)])
