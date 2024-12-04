from re import finditer

f = open("input.txt", "r")
input_str = f.read()
f.close()

WIDTH = input_str.find("\n") + 1

result = 0

# reduce to 1D to make indexing easier
for m in finditer(r"\*", input_str):
    i = m.start()
    # no additional check as there are no gears at the border
    border = {i-WIDTH-1, i-WIDTH, i-WIDTH+1, i-1, i+1, i+WIDTH-1, i+WIDTH, i+WIDTH+1}
    gear_numbers = []

    # not very efficient but does the job
    for n in finditer(r"\d+", input_str):
        if set(range(n.start(), n.end())) & border:
            gear_numbers.append(int(n.group(0)))

    if len(gear_numbers) == 2:
        result += gear_numbers[0] * gear_numbers[1]

print(result)
