f = open("input.txt", "r")
input_str = f.read()
f.close()

result = 0

for card in input_str.split("\n"):

    # input is nicely formatted, so we can slice to remove "Card X:"
    win_nr_str, my_nr_str = card[10:].split(" | ")
    win_nr = {int(n) for n in win_nr_str.split()}
    my_nr = {int(n) for n in my_nr_str.split()}

    matches = len(win_nr & my_nr)

    if matches > 0:
        result += 2 ** (matches - 1)

print(result)
