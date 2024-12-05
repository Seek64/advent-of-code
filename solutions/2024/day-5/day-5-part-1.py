import re

with open("input.txt", "r") as f:
    input_str = f.read()


def ordering_correct(pages: list[int], rules: dict[int: int]) -> bool:
    for i, page in enumerate(pages):
        if page in rules:
            for page_rule in rules[page]:
                if page_rule in pages[:i]:
                    return False
    return True


ordering_rules = dict()
for a, b in re.findall(r"(\d+)\|(\d+)", input_str):
    a = int(a)
    b = int(b)
    if a in ordering_rules:
        ordering_rules[a].append(b)
    else:
        ordering_rules[a] = [b]

result = 0

for page_matches in re.findall(r"(\d+(,\d+)+)", input_str):
    page_list = list(map(int, page_matches[0].split(",")))
    if ordering_correct(page_list, ordering_rules):
        result += page_list[len(page_list) // 2]

print(result)
