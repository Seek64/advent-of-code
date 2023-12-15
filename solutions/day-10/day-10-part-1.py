f = open("input.txt", "r")
input_str = f.read()
f.close()

WIDTH = input_str.find("\n") + 1
RIGHT = 0
DOWN = 1
LEFT = 2
UP = 3

move = {
    RIGHT: 1,
    DOWN: WIDTH,
    LEFT: -1,
    UP: -WIDTH
}


def dir_change(tile_p, dir_p):
    if tile_p == "|":
        return dir_p
    elif tile_p == "-":
        return dir_p
    elif tile_p == "L":
        return RIGHT if dir_p == DOWN else UP
    elif tile_p == "J":
        return UP if dir_p == RIGHT else LEFT
    elif tile_p == "7":
        return DOWN if dir_p == RIGHT else LEFT
    elif tile_p == "F":
        return DOWN if dir_p == LEFT else RIGHT


curr_pos = input_str.find("S")
direction = RIGHT
next_pos = curr_pos + move[direction]
steps = 0

while input_str[next_pos] != "S":
    curr_pos = next_pos
    steps += 1
    direction = dir_change(input_str[curr_pos], direction)
    next_pos = curr_pos + move[direction]

result = (steps + 1) // 2

print(result)
