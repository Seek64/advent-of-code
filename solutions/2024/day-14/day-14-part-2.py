import re

with open("input.txt", "r") as f:
    input_str = f.read()

WIDTH = 101
HEIGHT = 103
N = 10000
robots = list()

for m in re.findall(r"p=(\d+),(\d+) v=(-?\d+),(-?\d+)", input_str):
    robots.append(list(map(int, m)))

N_ROBOTS = len(robots)
THRESHOLD = int(0.7 * N_ROBOTS)

for seconds in range(N):
    field = [[0] * WIDTH for row in range(HEIGHT)]
    for robot in robots:
        x, y, vx, vy = robot
        field[y][x] += 1
        robot[0] = (x + vx) % WIDTH
        robot[1] = (y + vy) % HEIGHT
    # Count connected robots
    connected = 0
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if field[y][x] == 0:
                continue
            cnt = 0
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1), (1, 1), (-1, 1), (1, -1), (-1, -1)]:
                nx, ny = (x + dx) % WIDTH, (y + dy) % HEIGHT
                cnt += field[ny][nx]
            if cnt:
                connected += field[y][x]
    if connected >= THRESHOLD:
        for row in field:
            print("".join(f" {n}"[n > 0] for n in row))
        print("-" * WIDTH)
        print(seconds)
