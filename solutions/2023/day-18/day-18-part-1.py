from queue import Queue

f = open("input.txt", "r")
input_str = f.read()
f.close()

# This was a very educational task for me, learning how to calculate the area of a shape using coordinates.
# Therefore, part 2 shows a much better solution for this problem.

# compute size of the area
i = j = 0
min_i = max_i = min_j = max_j = 0
for instruction in input_str.split("\n"):
    d, l, c = instruction.split()
    if d == "U":
        i -= int(l)
        min_i = min(min_i, i)
    elif d == "R":
        j += int(l)
        max_j = max(max_j, j)
    elif d == "D":
        i += int(l)
        max_i = max(max_i, i)
    elif d == "L":
        j -= int(l)
        min_j = min(min_j, j)

WIDTH = 1 + max_j - min_j
HEIGHT = 1 + max_i - min_i

terrain = [["." for j in range(WIDTH)] for i in range(HEIGHT)]
i = -min_i
j = -min_j

# "dig" trench
for instruction in input_str.split("\n"):
    d, l, c = instruction.split()
    for _ in range(int(l)):
        if d == "U":
            i -= 1
        elif d == "R":
            j += 1
        elif d == "D":
            i += 1
        elif d == "L":
            j -= 1
        terrain[i][j] = "#"

# find tile in the interior
for j in range(WIDTH):
    if terrain[0][j] == "#" and terrain[1][j] == ".":
        break
i = 1

# "dig" out interior by propagating the found tile in all directions
# this method would not work if the trench had small passages of width 2
to_dig = Queue()
to_dig.put((i, j))
while not to_dig.empty():
    i, j = to_dig.get()
    if terrain[i][j] == ".":
        terrain[i][j] = "#"
        to_dig.put((i+1, j))
        to_dig.put((i-1, j))
        to_dig.put((i, j+1))
        to_dig.put((i, j-1))

result = sum("".join(row).count("#") for row in terrain)

print(result)
