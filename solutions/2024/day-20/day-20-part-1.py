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

# Find cheats (shortcuts) - order does not matter
time_saves = dict()
for x, y in path_costs:
    for dx, dy in [(2, 0), (1, 1), (0, 2), (-1, 1), (-2, 0), (-1, -1), (0, -2), (1, -1)]:
        nx, ny = x + dx, y + dy
        if (nx, ny) in path_costs and path_costs[(nx, ny)] > path_costs[(x, y)] + 2:
            time_save = path_costs[(nx, ny)] - path_costs[(x, y)] - 2
            time_saves[time_save] = time_saves.get(time_save, 0) + 1

result = 0
for time_save, n in time_saves.items():
    if time_save >= 100:
        result += n
print(result)
