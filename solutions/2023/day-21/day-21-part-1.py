f = open("input.txt", "r")
input_str = f.read()
f.close()

field = input_str.split("\n")
HEIGHT = len(field)
WIDTH = len(field[0])
STEPS = 64

walks = [[0] * WIDTH for i in range(HEIGHT)]
for i in range(HEIGHT):
    for j in range(WIDTH):
        if field[i][j] == "#":
            walks[i][j] = -2
        elif field[i][j] == ".":
            walks[i][j] = -1

for step in range(STEPS):
    for i in range(HEIGHT):
        for j in range(WIDTH):
            if walks[i][j] == step:
                if i > 0 and walks[i-1][j] > -2:
                    walks[i-1][j] = step + 1
                if j > 0 and walks[i][j-1] > -2:
                    walks[i][j-1] = step + 1
                if i < HEIGHT - 1 and walks[i+1][j] > -2:
                    walks[i+1][j] = step + 1
                if j < WIDTH - 1 and walks[i][j+1] > -2:
                    walks[i][j+1] = step + 1

result = 0
for row in walks:
    result += row.count(STEPS)

print(result)
