f = open("input.txt", "r")
input_str = f.read()
f.close()

UNFOLD_FACTOR = 5


# The solution uses dynamic programming to keep track of all the possibilities
# For each pair of substring and remaining number of groups, the number of possible ways to reach it are stored
def count_arrangements(field, groups):
    total_groups = len(groups)
    count_table = {field[i:]: {n: 0 for n in range(total_groups, 0, -1)} for i in range(len(field))}
    count_table[field][total_groups] = 1
    count = 0

    for sub_field in count_table:
        for groups_left in count_table[sub_field]:
            curr_mult = count_table[sub_field][groups_left]

            if sub_field[0] in ".?":
                if len(sub_field) > 1:
                    count_table[sub_field[1:]][groups_left] += curr_mult

            if sub_field[0] in "#?":
                curr_group = groups[total_groups - groups_left]
                groups_left -= 1

                if (not ("." in sub_field[:curr_group])
                        and not (len(sub_field) > curr_group and "#" == sub_field[curr_group])
                        and not curr_group > len(sub_field)):
                    new_sub_field = sub_field[curr_group + 1:]
                    if groups_left > 0 and len(new_sub_field) > 0:
                        count_table[new_sub_field][groups_left] += curr_mult
                    elif groups_left == 0:
                        count += 0 if "#" in new_sub_field else curr_mult

    return count


result = 0

for line in input_str.split("\n"):
    field_str, group_size_str = line.split()
    field_str_unfolded = "?".join(field_str for n in range(UNFOLD_FACTOR))
    group_size_list = [int(n) for n in group_size_str.split(",")] * UNFOLD_FACTOR
    result += count_arrangements(field_str_unfolded, group_size_list)

print(result)
