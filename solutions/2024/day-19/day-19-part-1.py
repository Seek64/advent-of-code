with open("input.txt", "r") as f:
    input_str = f.read()

towels, _, *designs = input_str.split("\n")
towels = towels.split(", ")

possible_designs = 0
for design in designs:
    to_check = set()
    to_check.add(design)
    is_possible = False
    while to_check and not is_possible:
        rest_design = to_check.pop()
        for towel in towels:
            if towel == rest_design:
                is_possible = True
                break
            elif rest_design.startswith(towel):
                to_check.add(rest_design[len(towel):])
    if is_possible:
        possible_designs += 1

print(possible_designs)
