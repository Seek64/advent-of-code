from re import findall
from math import lcm

f = open("input.txt", "r")
input_str = f.read()
f.close()

instructions = input_str.split("\n")[0]
network = {s[0]: (s[1], s[2]) for s in findall(r"(\w+) = \((\w+), (\w+)\)", input_str)}
states = [state for state in network if state[2] == "A"]

cycle_lengths = []

# paths from A to Z states are periodical without an offset
# thus, we can compute the cycle lengths and calculate their least common multiple
for state in states:
    transitions = 0
    i = 0
    while state[2] != "Z":
        decision = 0 if instructions[i] == "L" else 1
        state = network[state][decision]
        i = (i + 1) % len(instructions)
        transitions += 1

    cycle_lengths.append(transitions)

result = lcm(*cycle_lengths)

print(result)
