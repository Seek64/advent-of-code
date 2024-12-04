f = open("input.txt", "r")
input_str = f.read()
f.close()

# The formula for the area A described by a set of points (A, B, C, .., Z) is
# A = 0.5 * [(A_x * B_y - A_y * B_x) + (B_x * C_y - B_y * C_x) + ... + (Z_x * A_y - Z_y * A_x)]

# Since we need the outline of the trench as coordinates, we have to distinguish left and right turns

R, D, L, U = 0, 1, 2, 3

instructions = []
for line in input_str.split("\n"):
    instr_dir = int(line[-2])
    instr_len = int(line[-7:-2], 16)
    instructions.append((instr_dir, instr_len))


x = y = next_x = next_y = 0
area = 0

last_turn_right = False
dig_dir = instructions[-1][0]
next_dig_dir = instructions[0][0]
if next_dig_dir == R:
    last_turn_right = dig_dir == U
elif next_dig_dir == D:
    last_turn_right = dig_dir == R
elif next_dig_dir == L:
    last_turn_right = dig_dir == D
elif next_dig_dir == U:
    last_turn_right = dig_dir == L

for i, instruction in enumerate(instructions[:-1]):
    dig_dir, length = instruction
    next_dig_dir = instructions[i+1][0]
    length = int(length)
    if dig_dir == U:

        if next_dig_dir == R:
            if last_turn_right:
                length += 1
            last_turn_right = True
        else:
            if not last_turn_right:
                length -= 1
            last_turn_right = False

        next_x = x
        next_y = y + length
    elif dig_dir == R:

        if next_dig_dir == D:
            if last_turn_right:
                length += 1
            last_turn_right = True
        else:
            if not last_turn_right:
                length -= 1
            last_turn_right = False

        next_x = x + length
        next_y = y
    elif dig_dir == D:

        if next_dig_dir == L:
            if last_turn_right:
                length += 1
            last_turn_right = True
        else:
            if not last_turn_right:
                length -= 1
            last_turn_right = False

        next_x = x
        next_y = y - length
    elif dig_dir == L:

        if next_dig_dir == U:
            if last_turn_right:
                length += 1
            last_turn_right = True
        else:
            if not last_turn_right:
                length -= 1
            last_turn_right = False

        next_x = x - length
        next_y = y
    area += x * next_y - next_x * y
    x, y = next_x, next_y

area = abs(area) // 2

print(area)
