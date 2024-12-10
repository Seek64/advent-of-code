with open("input.txt", "r") as f:
    input_str = f.read()

mem = list()
is_file = True
file_id = 0

for n in map(int, input_str):
    if is_file:
        mem.extend(n * [file_id])
        file_id += 1
    else:
        mem.extend(n * [-1])
    is_file = not is_file

i = 0
while i < len(mem):
    if mem[i] >= 0:
        i += 1
    else:
        n = mem.pop(-1)
        if n >= 0:
            mem[i] = n
            i += 1

result = 0
for i, n in enumerate(mem):
    result += i * n

print(result)
