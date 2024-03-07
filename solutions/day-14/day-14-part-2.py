f = open("input.txt", "r")
input_str = f.read()
f.close()

N = 1000000000


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


def tilt_west(mat):
    done = False
    while not done:
        done = True
        for i, row in enumerate(mat):
            for j, tile in enumerate(row[:-1]):
                if tile == "." and mat[i][j+1] == "O":
                    mat[i][j] = "O"
                    mat[i][j+1] = "."
                    done = False


def tilt_south(mat):
    done = False
    while not done:
        done = True
        for i, row in enumerate(mat[:-1]):
            for j, tile in enumerate(row):
                if tile == "O" and mat[i+1][j] == ".":
                    mat[i][j] = "."
                    mat[i+1][j] = "O"
                    done = False


def tilt_east(mat):
    done = False
    while not done:
        done = True
        for i, row in enumerate(mat):
            for j, tile in enumerate(row[:-1]):
                if tile == "O" and mat[i][j+1] == ".":
                    mat[i][j] = "."
                    mat[i][j+1] = "O"
                    done = False


def full_rotation(mat):
    tilt_north(mat)
    tilt_west(mat)
    tilt_south(mat)
    tilt_east(mat)


def print_matrix(mat):
    for row in mat:
        print("".join(row))
    print()


def count_weight(mat):
    return sum((i + 1) * row.count("O") for i, row in enumerate(mat[::-1]))


rock_matrix = [[j for j in i] for i in input_str.split("\n")]

# Rotate until the current configuration has been encountered before
# For a simple comparison, we transform the matrix into a single string
# Could be more efficient by using some unique hash for a configuration, but still sufficient for this problem
field_configs = dict()
config_weights = []
curr_field_str = "".join("".join(row) for row in rock_matrix)
rot_count = 0
while curr_field_str not in field_configs:
    field_configs[curr_field_str] = rot_count
    config_weights.append(count_weight(rock_matrix))
    full_rotation(rock_matrix)
    rot_count += 1
    curr_field_str = "".join("".join(row) for row in rock_matrix)

period_start = field_configs[curr_field_str]
period_length = rot_count - period_start
final_config_nr = (N - period_start) % period_length + period_start

result = config_weights[final_config_nr]
print(result)
