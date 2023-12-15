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


# Step 1: Find all the loop tiles
curr_pos = input_str.find("S")
direction = RIGHT
next_pos = curr_pos + move[direction]
loop_tiles = {curr_pos}

while input_str[next_pos] != "S":
    curr_pos = next_pos
    loop_tiles.add(curr_pos)
    direction = dir_change(input_str[curr_pos], direction)
    next_pos = curr_pos + move[direction]

# Step 2: Traverse the loop again and collect unconnected tiles left and right of it
#         We treat the line breaks as unconnected tiles
curr_pos = input_str.find("S")
direction = RIGHT
next_pos = curr_pos + move[direction]
right_tiles = set()
left_tiles = set()

while input_str[next_pos] != "S":
    curr_pos = next_pos
    new_direction = dir_change(input_str[curr_pos], direction)

    back_dir = (direction + 2) % 4
    look_dir = new_direction
    add_to_right_tiles = True
    for _ in range(3):
        # turn right
        look_dir = (look_dir + 1) % 4
        if look_dir == back_dir:
            add_to_right_tiles = False
        else:
            new_tile = curr_pos + move[look_dir]
            if 0 <= new_tile < len(input_str) and new_tile not in loop_tiles:
                if add_to_right_tiles:
                    right_tiles.add(new_tile)
                else:
                    left_tiles.add(new_tile)

    direction = new_direction
    next_pos = curr_pos + move[direction]


# Step 3: Extend unconnected fields as much as possible
new_tiles = {0}
while new_tiles:
    new_tiles = set()
    covered_tiles = loop_tiles | right_tiles
    for tile in right_tiles:
        up_tile = tile - WIDTH
        if up_tile >= 0 and up_tile not in covered_tiles:
            new_tiles.add(up_tile)
        left_tile = tile - 1
        if left_tile >= 0 and left_tile not in covered_tiles:
            new_tiles.add(left_tile)
        down_tile = tile + WIDTH
        if down_tile < len(input_str) and down_tile not in covered_tiles:
            new_tiles.add(down_tile)
        right_tile = tile + 1
        if right_tile < len(input_str) and right_tile not in covered_tiles:
            new_tiles.add(right_tile)
    right_tiles = right_tiles | new_tiles

new_tiles = {0}
while new_tiles:
    new_tiles = set()
    covered_tiles = loop_tiles | left_tiles
    for tile in left_tiles:
        up_tile = tile - WIDTH
        if up_tile >= 0 and up_tile not in covered_tiles:
            new_tiles.add(up_tile)
        left_tile = tile - 1
        if left_tile >= 0 and left_tile not in covered_tiles:
            new_tiles.add(left_tile)
        down_tile = tile + WIDTH
        if down_tile < len(input_str) and down_tile not in covered_tiles:
            new_tiles.add(down_tile)
        right_tile = tile + 1
        if right_tile < len(input_str) and right_tile not in covered_tiles:
            new_tiles.add(right_tile)
    left_tiles = left_tiles | new_tiles

# Step 4: Check whether the left or right of the loop is the inside, i.e., does not contain index 2
result = len(right_tiles) if 2 in left_tiles else len(left_tiles)

print(result)
