f = open("input.txt", "r")
input_str = f.read()
f.close()


# recursive function that calls itself twice for both possibilities of "?"
def count_arrangements(field, group_sizes):

    # terminate if remaining groups can't fit anymore
    if sum(group_sizes) + len(group_sizes) - 1 > len(field):
        return 0

    # terminate if all groups are handled
    if not group_sizes:
        return 0 if "#" in field else 1

    if field[0] == ".":
        return count_arrangements(field[1:], group_sizes)
    elif field[0] == "#":
        curr_group_size, *group_sizes = group_sizes
        if "." in field[:curr_group_size]:
            return 0
        elif len(field) > curr_group_size and "#" == field[curr_group_size]:
            return 0
        else:
            return count_arrangements(field[curr_group_size + 1:], group_sizes)
    elif field[0] == "?":
        return count_arrangements("." + field[1:], group_sizes) + count_arrangements("#" + field[1:], group_sizes)
    else:
        return 0


result = 0

for line in input_str.split("\n"):
    field_str, group_size_str = line.split()
    group_size_list = [int(n) for n in group_size_str.split(",")]
    result += count_arrangements(field_str, group_size_list)

print(result)
