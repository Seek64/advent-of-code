from itertools import combinations

with open("input.txt", "r") as f:
    input_str = f.read()

field = input_str.split("\n")
WIDTH = len(field[0])
HEIGHT = len(field)
start = end = (-1, -1)

for i, row in enumerate(field):
    for j, tile in enumerate(row):
        if tile == "S":
            start = (j, i)
        elif tile == "E":
            end = (j, i)

# Find regular (unique) path
x, y = start
path_costs = {(x, y): 0}
while (x, y) != end:
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nx, ny = x + dx, y + dy
        if field[ny][nx] in ".E" and (nx, ny) not in path_costs:
            path_costs[(nx, ny)] = path_costs[(x, y)] + 1
            x, y = nx, ny
            break

time_saves = dict()
for (x1, y1), (x2, y2) in combinations(path_costs, 2):
    dist = abs(x2 - x1) + abs(y2 - y1)
    time_save = path_costs[(x2, y2)] - path_costs[(x1, y1)] - dist
    if 0 < dist <= 20 and time_save > 0:
        time_saves[time_save] = time_saves.get(time_save, 0) + 1

result = 0
for time_save, n in time_saves.items():
    if time_save >= 100:
        result += n
print(result)
