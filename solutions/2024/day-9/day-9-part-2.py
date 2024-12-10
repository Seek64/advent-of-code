with open("input.txt", "r") as f:
    input_str = f.read()

# Save memory blocks as tuples (start_index, width) by ID
mem = dict()
free_space = list()
is_file = True
file_id = 0
i = 0
for n in map(int, input_str):
    if is_file:
        mem[file_id] = (i, n)
        file_id += 1
    else:
        free_space.append((i, n))
    i += n
    is_file = not is_file

while file_id:
    file_id -= 1
    file_index, file_width = mem[file_id]
    for i, (free_index, free_width) in enumerate(free_space):
        if file_width <= free_width and free_index < file_index:
            mem[file_id] = (free_index, file_width)
            free_index = free_index + file_width
            free_width = free_width - file_width
            if free_width > 0:
                free_space[i] = (free_index, free_width)
            else:
                del free_space[i]
            break

result = 0
for file_id in mem:
    file_index, file_width = mem[file_id]
    result += file_id * int(file_width / 2 * (2 * file_index + file_width - 1))

print(result)
