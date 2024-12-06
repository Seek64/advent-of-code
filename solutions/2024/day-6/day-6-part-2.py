with open("input.txt", "r") as f:
    input_str = f.read()

pat_map = [[*line] for line in input_str.split("\n")]
HEIGHT = len(pat_map)
WIDTH = len(pat_map[0])
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

# Find guard
x_start = y_start = x_next = y_next = 0
direction = UP
for i, row in enumerate(pat_map):
    if "^" in row:
        x_start = row.index("^")
        y_start = i

result = 0

# For performance, one could add a check that only inserts at positions actually traversed by the guard
for y_add in range(HEIGHT):
    for x_add in range(WIDTH):

        if pat_map[y_add][x_add] != ".":
            continue

        pat_map_ins = [[i for i in row] for row in pat_map]
        pat_map_ins[y_add][x_add] = "#"

        visited = set()
        x, y = x_start, y_start
        direction = UP

        while True:

            pos = (x, y, direction)
            if pos in visited:
                result += 1
                break

            visited.add(pos)

            if direction == UP:
                x_next = x
                y_next = y - 1
            elif direction == RIGHT:
                x_next = x + 1
                y_next = y
            elif direction == DOWN:
                x_next = x
                y_next = y + 1
            elif direction == LEFT:
                x_next = x - 1
                y_next = y

            if x_next < 0 or x_next >= WIDTH or y_next < 0 or y_next >= HEIGHT:
                break

            # Turn
            if pat_map_ins[y_next][x_next] == "#":
                direction = (direction + 1) % 4
            # Move
            else:
                x = x_next
                y = y_next

print(result)
