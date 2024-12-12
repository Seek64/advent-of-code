import queue

with open("input.txt", "r") as f:
    input_str = f.read()

field = [list(row) for row in input_str.split("\n")]
WIDTH = len(field[0])
HEIGHT = len(field)
checked = [[False] * WIDTH for h in range(HEIGHT)]

result = 0
for i in range(HEIGHT):
    for j in range(WIDTH):
        if not checked[i][j]:
            area = 1
            perimeter = 0
            field_type = field[i][j]
            fields_to_check = queue.Queue()
            fields_to_check.put((i, j))
            checked[i][j] = True
            while not fields_to_check.empty():
                ci, cj = fields_to_check.get()
                for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    ni, nj = ci + di, cj + dj
                    if 0 <= ni < HEIGHT and 0 <= nj < WIDTH:
                        if field[ni][nj] == field_type and not checked[ni][nj]:
                            area += 1
                            checked[ni][nj] = True
                            fields_to_check.put((ni, nj))
                        elif field[ni][nj] != field_type:
                            perimeter += 1
                    else:
                        perimeter += 1
            result += area * perimeter

print(result)
