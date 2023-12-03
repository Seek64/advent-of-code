from re import finditer

f = open("input.txt", "r")
input_str = f.read()
f.close()

engine = input_str.split()
WIDTH = len(engine[0])
HEIGHT = len(engine)

result = 0

for i, row in enumerate(engine):
    for match in finditer(r"\d+", row):
        n_str = match.group(0)
        left = match.start() - 1 if match.start() > 0 else match.start()
        right = match.end() + 1 if match.end() < WIDTH else match.end()
        frame = engine[i][left:right]
        if i > 0:
            frame += engine[i-1][left:right]
        if i < HEIGHT - 1:
            frame += engine[i+1][left:right]

        # check if there are more symbols than the number and '.'
        if set(frame) - set(n_str) - set('.'):
            result += int(n_str)

print(result)
