from re import findall

f = open("input.txt", "r")
input_str = f.read()
f.close()

instructions = input_str.split("\n")[0]
network = {s[0]: (s[1], s[2]) for s in findall(r"(\w+) = \((\w+), (\w+)\)", input_str)}

state = "AAA"
transitions = 0
i = 0

while state != "ZZZ":
    decision = instructions[i]
    if decision == "L":
        state = network[state][0]
    elif decision == "R":
        state = network[state][1]

    i = (i + 1) % len(instructions)
    transitions += 1

print(transitions)
