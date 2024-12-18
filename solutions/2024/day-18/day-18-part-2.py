from collections import deque

with open("input.txt", "r") as f:
    input_str = f.read()

corrupted_bytes = [tuple(map(int, c.split(","))) for c in input_str.split("\n")]
WIDTH = HEIGHT = 71
min_corr = 0
max_corr = len(corrupted_bytes)

# Binary search
while min_corr + 1 < max_corr:
    n_corr = (min_corr + max_corr) // 2

    shortest_path = {(0, 0) : 0}
    to_check = deque()
    to_check.append((0, 0))
    while to_check:
        x, y = to_check.popleft()
        # Could remove the cost comparison from part 1 since we're only concerned about reachability
        cost = shortest_path[(x, y)]
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < WIDTH and 0 <= ny < HEIGHT and (nx, ny) not in corrupted_bytes[:n_corr]:
                next_cost = shortest_path.get((nx, ny), -1)
                if next_cost < 0 or cost + 1 < next_cost:
                    shortest_path[(nx, ny)] = cost + 1
                    to_check.append((nx, ny))

    if (WIDTH - 1, HEIGHT - 1) in shortest_path:
        min_corr = n_corr
    else:
        max_corr = n_corr

print("%d,%d" % corrupted_bytes[min_corr])
