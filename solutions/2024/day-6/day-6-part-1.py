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
x = y = x_next = y_next = 0
direction = UP
for i, row in enumerate(pat_map):
    if "^" in row:
        x = row.index("^")
        y = i

while True:
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
    if pat_map[y_next][x_next] == "#":
        direction = (direction + 1) % 4
    # Move
    else:
        pat_map[y][x] = "X"
        pat_map[y_next][x_next] = "^"
        x = x_next
        y = y_next

pat_map[y][x] = "X"

result = 0
for row in pat_map:
    result += row.count("X")

print(result)
