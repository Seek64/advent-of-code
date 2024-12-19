with open("input.txt", "r") as f:
    input_str = f.read()

towels, _, *designs = input_str.split("\n")
towels = towels.split(", ")

total_comb = 0
for design in designs:
    to_check = {design}
    comb = {design: 1, "": 0}
    while to_check:
        rest_design = to_check.pop()
        curr_comb = comb[rest_design]
        for towel in towels:
            if rest_design == towel:
                comb[""] += curr_comb
            elif rest_design.startswith(towel):
                new_rest = rest_design[len(towel):]
                comb[new_rest] = curr_comb + comb.get(new_rest, 0)
                to_check.add(new_rest)
            comb[rest_design] = 0
    total_comb += comb.get("", 0)

print(total_comb)
