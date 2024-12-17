import re

with open("input.txt", "r") as f:
    input_str = f.read()


class Opcodes:
    ADV = 0
    BXL = 1
    BST = 2
    JNZ = 3
    BXC = 4
    OUT = 5
    BDV = 6
    CDV = 7


reg_a, reg_b, reg_c, *i_mem = map(int, re.findall(r"\d+", input_str))
pc = 0
output = list()


def get_combo_op(rs1: int) -> int:
    if 0 <= rs1 <= 3:
        return rs1
    elif rs1 == 4:
        return reg_a
    elif rs1 == 5:
        return reg_b
    elif rs1 == 6:
        return reg_c
    else:
        raise "Invalid operand specified!"


while pc < len(i_mem):
    literal_op = i_mem[pc + 1]
    combo_op = get_combo_op(literal_op)
    opcode = i_mem[pc]
    pc += 2
    match opcode:
        case Opcodes.ADV:
            # Division by 2 ** combo_op is the same as shifting
            reg_a = reg_a >> combo_op
        case Opcodes.BXL:
            reg_b = reg_b ^ literal_op
        case Opcodes.BST:
            reg_b = combo_op % 8
        case Opcodes.JNZ:
            if reg_a != 0:
                pc = literal_op
        case Opcodes.BXC:
            reg_b = reg_b ^ reg_c
        case Opcodes.OUT:
            output.append(combo_op % 8)
        case Opcodes.BDV:
            reg_b = reg_a >> combo_op
        case Opcodes.CDV:
            reg_c = reg_a >> combo_op
        case _:
            raise "Invalid opcode specified!"

print(*output, sep=",")
