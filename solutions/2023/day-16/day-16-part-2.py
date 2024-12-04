import queue

f = open("input.txt", "r")
input_str = f.read()
f.close()

NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3
HEIGHT = len(input_str.split("\n"))
WIDTH = len(input_str.split("\n")[0])


class Tile:
    def __init__(self, tile_type):
        self.type = tile_type
        self.in_dir = set()
        self.out_dir = set()

    def is_energized(self):
        return len(self.in_dir) > 0

    def add_input_beam(self, new_in_dir):

        old_out_dirs = set(d for d in self.out_dir)

        if new_in_dir not in self.in_dir:
            self.in_dir.add(new_in_dir)
            self._propagate(new_in_dir)

        # return only new propagations
        return self.out_dir - old_out_dirs

    def _propagate(self, new_in_dir):

        if self.type == ".":
            if new_in_dir == NORTH:
                self.out_dir.add(SOUTH)
            elif new_in_dir == EAST:
                self.out_dir.add(WEST)
            elif new_in_dir == SOUTH:
                self.out_dir.add(NORTH)
            elif new_in_dir == WEST:
                self.out_dir.add(EAST)

        elif self.type == "/":
            if new_in_dir == NORTH:
                self.out_dir.add(WEST)
            elif new_in_dir == EAST:
                self.out_dir.add(SOUTH)
            elif new_in_dir == SOUTH:
                self.out_dir.add(EAST)
            elif new_in_dir == WEST:
                self.out_dir.add(NORTH)

        elif self.type == "\\":
            if new_in_dir == NORTH:
                self.out_dir.add(EAST)
            elif new_in_dir == EAST:
                self.out_dir.add(NORTH)
            elif new_in_dir == SOUTH:
                self.out_dir.add(WEST)
            elif new_in_dir == WEST:
                self.out_dir.add(SOUTH)

        elif self.type == "|":
            if new_in_dir == NORTH:
                self.out_dir.add(SOUTH)
            elif new_in_dir == SOUTH:
                self.out_dir.add(NORTH)
            elif new_in_dir == EAST or new_in_dir == WEST:
                self.out_dir.add(NORTH)
                self.out_dir.add(SOUTH)

        elif self.type == "-":
            if new_in_dir == EAST:
                self.out_dir.add(WEST)
            elif new_in_dir == WEST:
                self.out_dir.add(EAST)
            elif new_in_dir == NORTH or new_in_dir == SOUTH:
                self.out_dir.add(EAST)
                self.out_dir.add(WEST)


def energize_field(field_str, start_i, start_j, start_in_dir):
    field = [[Tile(tile_char) for tile_char in row] for row in field_str.split("\n")]

    new_propagations = queue.Queue()
    new_propagations.put((start_i, start_j, start_in_dir))

    while not new_propagations.empty():
        i, j, in_prop = new_propagations.get()
        new_out_prop = field[i][j].add_input_beam(in_prop)

        for p in new_out_prop:
            p_inv = (p + 2) % 4
            if p == NORTH and i > 0:
                new_propagations.put((i-1, j, p_inv))
            elif p == EAST and j < WIDTH - 1:
                new_propagations.put((i, j+1, p_inv))
            elif p == SOUTH and i < HEIGHT - 1:
                new_propagations.put((i+1, j, p_inv))
            elif p == WEST and j > 0:
                new_propagations.put((i, j-1, p_inv))

    return sum(sum(tile.is_energized() for tile in row) for row in field)


result = 0

for start_col in range(WIDTH):
    result = max(result, energize_field(input_str, 0, start_col, NORTH))
    result = max(result, energize_field(input_str, HEIGHT-1, start_col, SOUTH))

for start_row in range(HEIGHT):
    result = max(result, energize_field(input_str, start_row, 0, WEST))
    result = max(result, energize_field(input_str, start_row, WIDTH-1, EAST))

print(result)
