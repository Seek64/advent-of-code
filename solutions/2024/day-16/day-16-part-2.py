from collections import deque

with open("input.txt", "r") as f:
    input_str = f.read()

WIDTH = input_str.find("\n")
HEIGHT = len(input_str) // WIDTH
field = [c for c in input_str if c != "\n"]

start = field.index("S")
end_pos = field.index("E")
RIGHT, DOWN, LEFT, UP = 1, WIDTH, -1, -WIDTH

MAX_COST = 10**9
lowest_cost = dict()
to_check = deque()
to_check.append((start, RIGHT, 0))

while to_check:
    pos, direction, cost = to_check.popleft()
    curr_lowest = lowest_cost.get((pos, direction), MAX_COST)
    if cost < curr_lowest:
        lowest_cost[(pos, direction)] = cost
        if field[pos + direction] in ".SE":
            to_check.append((pos + direction, direction, cost + 1))
        if direction == RIGHT or direction == LEFT:
            to_check.append((pos, UP, cost + 1000))
            to_check.append((pos, DOWN, cost + 1000))
        elif direction == UP or direction == DOWN:
            to_check.append((pos, LEFT, cost + 1000))
            to_check.append((pos, RIGHT, cost + 1000))

# Bellman-Ford Algorithm
end_cost = min(lowest_cost[(p,d)] for p,d in lowest_cost if p == end_pos)
end_dir = UP
for p, d in lowest_cost:
    if lowest_cost[(p, d)] == end_cost:
        end_dir = d
backwards_cost = dict()
end_cost = max(lowest_cost[(end_pos, UP)], lowest_cost[(end_pos, DOWN)], lowest_cost[(end_pos, LEFT)], lowest_cost[(end_pos, RIGHT)])
to_check.append((end_pos, end_dir, end_cost))

while to_check:
    pos, direction, cost = to_check.popleft()
    curr_highest = backwards_cost.get((pos, direction), -MAX_COST)
    if cost > curr_highest:
        backwards_cost[(pos, direction)] = cost
        if field[pos - direction] in ".SE":
            to_check.append((pos - direction, direction, cost - 1))
        if direction == RIGHT or direction == LEFT:
            to_check.append((pos, UP, cost - 1000))
            to_check.append((pos, DOWN, cost - 1000))
        elif direction == UP or direction == DOWN:
            to_check.append((pos, LEFT, cost - 1000))
            to_check.append((pos, RIGHT, cost - 1000))

result = len({p for p, d in lowest_cost if backwards_cost[(p, d)] - lowest_cost[(p, d)] == 0})
print(result)
