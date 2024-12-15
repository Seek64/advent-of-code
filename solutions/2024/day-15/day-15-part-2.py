with open("input.txt", "r") as f:
    input_str = f.read()

field, commands = input_str.split("\n\n")
field = field.replace("#", "##")
field = field.replace("O", "[]")
field = field.replace(".", "..")
field = field.replace("@", "@.")
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
    elif field[next_pos] in "[]":
        non_box_pos = next_pos + direction
        # Push left / right
        if direction in (1, -1):
            while field[non_box_pos] in "[]":
                non_box_pos += direction
            if field[non_box_pos] == ".":
                while non_box_pos != next_pos:
                    field[non_box_pos] = field[non_box_pos - direction]
                    non_box_pos -= direction
                field[next_pos] = "@"
                field[pos] = "."
                pos = next_pos
        # Push up / down
        elif direction in (WIDTH, -WIDTH):
            affected_pos = [{next_pos}]
            if field[next_pos] == "[":
                affected_pos[0].add(next_pos + 1)
            else:
                affected_pos[0].add(next_pos - 1)
            while True:
                # Check whether any boxes hit a wall
                if any(field[p + direction] == "#" for p in affected_pos[-1]):
                    break
                # Push
                elif all(field[p + direction] == "." for p in affected_pos[-1]):
                    for row in affected_pos[::-1]:
                        for p_i in row:
                            field[p_i + direction] = field[p_i]
                            field[p_i] = "."
                    field[next_pos] = "@"
                    field[pos] = "."
                    pos = next_pos
                    break
                # Check affected boxes
                else:
                    new_aff_pos = set()
                    for aff_pos in affected_pos[-1]:
                        if field[aff_pos + direction] == "[":
                            new_aff_pos.add(aff_pos + direction)
                            new_aff_pos.add(aff_pos + direction + 1)
                        elif field[aff_pos + direction] == "]":
                            new_aff_pos.add(aff_pos + direction)
                            new_aff_pos.add(aff_pos + direction - 1)
                    affected_pos.append(new_aff_pos)

# print(HEIGHT * f"{"%c" * WIDTH}\n" % (*field,))

result = 0
for i, tile in enumerate(field):
    if tile == "[":
        result += i // WIDTH * 100 + i % WIDTH

print(result)
