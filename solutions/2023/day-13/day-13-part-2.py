f = open("input.txt", "r")
input_str = f.read()
f.close()


def hamming_distance(str1, str2):
    return sum(c1 != c2 for c1, c2 in zip(str1, str2))


# Same approach, but now we search for a hamming distance of 1 instead of 0
def find_horizontal_split_smudge(matrix):
    for i in range(1, len(matrix)):
        upper_part = "".join(matrix[:i][::-1])
        lower_part = "".join(matrix[i:])
        if hamming_distance(upper_part, lower_part) == 1:
            return i
    return 0


result = 0

for mat_str in input_str.split("\n\n"):
    mat = mat_str.split("\n")
    horizontal_split = find_horizontal_split_smudge(mat)
    if horizontal_split:
        result += 100 * horizontal_split
    else:
        mat_trans = ["".join(row[i] for row in mat) for i in range(len(mat[0]))]
        result += find_horizontal_split_smudge(mat_trans)

print(result)
