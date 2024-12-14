import re

with open("input.txt", "r") as f:
    input_str = f.read()

WIDTH = 101
HEIGHT = 103
N = 100
q1 = q2 = q3 = q4 = 0

for m in re.findall(r"p=(\d+),(\d+) v=(-?\d+),(-?\d+)", input_str):
    x, y, vx, vy = map(int, m)
    x = (x + N * vx) % WIDTH
    y = (y + N * vy) % HEIGHT
    if x < WIDTH // 2 and y < HEIGHT // 2:
        q1 += 1
    elif x > WIDTH // 2 and y < HEIGHT // 2:
        q2 += 1
    elif x < WIDTH // 2 and y > HEIGHT // 2:
        q3 += 1
    elif x > WIDTH // 2 and y > HEIGHT // 2:
        q4 += 1

print(q1 * q2 * q3 * q4)
