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
            up_edges = set()
            right_edges = set()
            down_edges = set()
            left_edges = set()
            area = 1
            sides = 0
            field_type = field[i][j]
            fields_to_check = queue.Queue()
            fields_to_check.put((i, j))
            checked[i][j] = True
            while not fields_to_check.empty():
                ci, cj = fields_to_check.get()
                for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    check_side = False
                    ni, nj = ci + di, cj + dj
                    if 0 <= ni < HEIGHT and 0 <= nj < WIDTH:
                        if field[ni][nj] == field_type and not checked[ni][nj]:
                            area += 1
                            checked[ni][nj] = True
                            fields_to_check.put((ni, nj))
                        elif field[ni][nj] != field_type:
                            check_side = True
                    else:
                        check_side = True
                    # Not a good way of doing it.
                    # Sides can get added twice due to the way the fields are traversed.
                    # Below shows a minimal example how this could happen. The lowest edge is added twice since we only check whether neighboring edges are already found.
                    # A better way would probably be to first collect all edges of the same direction and then connect them.
                    #
                    # .X.
                    # XXX
                    # X.X
                    # XXX
                    # ^ ^
                    if check_side:
                        if di == 1 and dj == 0:
                            down_edges.add((ni, nj))
                            if ((ni, nj - 1) not in down_edges) and ((ni, nj + 1) not in down_edges):
                                sides += 1
                            if ((ni, nj - 1) in down_edges) and ((ni, nj + 1) in down_edges):
                                sides -= 1
                        if di == -1 and dj == 0:
                            up_edges.add((ni, nj))
                            if ((ni, nj - 1) not in up_edges) and ((ni, nj + 1) not in up_edges):
                                sides += 1
                            if ((ni, nj - 1) in up_edges) and ((ni, nj + 1) in up_edges):
                                sides -= 1
                        if di == 0 and dj == 1:
                            right_edges.add((ni, nj))
                            if ((ni - 1, nj) not in right_edges) and ((ni + 1, nj) not in right_edges):
                                sides += 1
                            if ((ni - 1, nj) in right_edges) and ((ni + 1, nj) in right_edges):
                                sides -= 1
                        if di == 0 and dj == -1:
                            left_edges.add((ni, nj))
                            if ((ni - 1, nj) not in left_edges) and ((ni + 1, nj) not in left_edges):
                                sides += 1
                            if ((ni - 1, nj) in left_edges) and ((ni + 1, nj) in left_edges):
                                sides -= 1
            result += area * sides

print(result)
