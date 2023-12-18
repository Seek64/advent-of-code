f = open("input.txt", "r")
input_str = f.read()
f.close()

space = input_str.split("\n")
WIDTH = len(space[0])
EX_FACTOR = 1000000

empty_rows = [i for i, row in enumerate(space) if "#" not in row]
empty_columns = [i for i in range(WIDTH) if "#" not in "".join(row[i] for row in space)]
galaxies = [(i, j) for i, row in enumerate(space) for j in range(WIDTH) if row[j] == "#"]

# don't expand space but count the empy rows/cols between galaxies and add their multiple
result = 0
for i, (x1, y1) in enumerate(galaxies[:-1]):
    for (x2, y2) in galaxies[i + 1:]:
        result += abs(x1 - x2) + abs(y1 - y2)
        result += (EX_FACTOR - 1) * len([j for j in empty_rows if x1 < j < x2 or x2 < j < x1])
        result += (EX_FACTOR - 1) * len([j for j in empty_columns if y1 < j < y2 or y2 < j < y1])

print(result)
