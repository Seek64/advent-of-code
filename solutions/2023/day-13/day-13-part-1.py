f = open("input.txt", "r")
input_str = f.read()
f.close()


def find_horizontal_split(matrix):
    for i in range(1, len(matrix)):
        upper_part = "".join(matrix[:i][::-1])
        lower_part = "".join(matrix[i:])
        overlap_len = min(len(upper_part), len(lower_part))
        if upper_part[:overlap_len] == lower_part[:overlap_len]:
            return i
    return 0


result = 0

for mat_str in input_str.split("\n\n"):
    mat = mat_str.split("\n")
    horizontal_split = find_horizontal_split(mat)
    if horizontal_split:
        result += 100 * horizontal_split
    else:
        mat_trans = ["".join(row[i] for row in mat) for i in range(len(mat[0]))]
        result += find_horizontal_split(mat_trans)

print(result)
