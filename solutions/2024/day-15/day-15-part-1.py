with open("input.txt", "r") as f:
    input_str = f.read()

field, commands = input_str.split("\n\n")
WIDTH = field.find("\n")
HEIGHT = len(field) // WIDTH
field = [*field.replace("\n", "")]
commands = commands.replace("\n", "")
pos = field.index("@")

for cmd in commands:
    direction = (1, -1, WIDTH, -WIDTH)["><v^".find(cmd)]
    next_pos = pos + direction
    if field[next_pos] == ".":
        field[next_pos] = "@"
        field[pos] = "."
        pos = next_pos
    elif field[next_pos] == "O":
        non_box_pos = next_pos + direction
        while field[non_box_pos] == "O":
            non_box_pos += direction
        if field[non_box_pos] == ".":
            field[non_box_pos] = "O"
            field[next_pos] = "@"
            field[pos] = "."
            pos = next_pos

# print(HEIGHT * f"{"%c" * WIDTH}\n" % (*field,))

result = 0
for i, tile in enumerate(field):
    if tile == "O":
        result += i // WIDTH * 100 + i % WIDTH

print(result)
