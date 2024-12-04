f = open("input.txt", "r")
input_str = f.read()
f.close()

card_strings = input_str.split("\n")

cards = {card_id: 1 for card_id in range(1, len(card_strings) + 1)}

card_id = 1

for card in card_strings:

    # input is nicely formatted, so we can slice to remove "Card X:"
    win_nr_str, my_nr_str = card[10:].split(" | ")
    win_nr = {int(n) for n in win_nr_str.split()}
    my_nr = {int(n) for n in my_nr_str.split()}
    matches = len(win_nr & my_nr)

    curr_mult = cards[card_id]

    for i in range(card_id + 1, card_id + 1 + matches):
        cards[i] += curr_mult

    card_id += 1

result = sum(cards.values())

print(result)
