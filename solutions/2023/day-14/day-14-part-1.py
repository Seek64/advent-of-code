f = open("input.txt", "r")
input_str = f.read()
f.close()


def tilt_north(mat):
    done = False
    while not done:
        done = True
        for i, row in enumerate(mat[:-1]):
            for j, tile in enumerate(row):
                if tile == "." and mat[i+1][j] == "O":
                    mat[i][j] = "O"
                    mat[i+1][j] = "."
                    done = False
    return mat


def count_weight(mat):
    return sum((i + 1) * row.count("O") for i, row in enumerate(mat[::-1]))


rock_matrix = [[j for j in i] for i in input_str.split("\n")]
tilted_rock_matrix = tilt_north(rock_matrix)
result = count_weight(tilted_rock_matrix)

print(result)
