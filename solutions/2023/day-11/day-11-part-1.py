f = open("input.txt", "r")
input_str = f.read()
f.close()

space = input_str.split("\n")
WIDTH = len(space[0])

empty_rows = [i for i, row in enumerate(space) if "#" not in row]
empty_columns = [i for i in range(WIDTH) if "#" not in "".join(row[i] for row in space)]

# expand space
for i in empty_rows[::-1]:
    space.insert(i, "." * WIDTH)
for j in empty_columns[::-1]:
    for i, row in enumerate(space):
        space[i] = row[:j] + "." + row[j:]
WIDTH = WIDTH + len(empty_columns)

galaxies = [(i, j) for i, row in enumerate(space) for j in range(WIDTH) if row[j] == "#"]

result = 0
for i, (x1, y1) in enumerate(galaxies[:-1]):
    for (x2, y2) in galaxies[i + 1:]:
        result += abs(x1 - x2) + abs(y1 - y2)

print(result)
