f = open("input.txt", "r")
input_str = f.read()
f.close()

hand_to_bid = {hand_bid_str[:5]: int(hand_bid_str[6:]) for hand_bid_str in input_str.split("\n")}

pairs_to_type = {
    "5": "7",
    "14": "6",
    "23": "5",
    "113": "4",
    "122": "3",
    "1112": "2",
    "11111": "1"
}

card_to_hex_value = {
    "A": "E",
    "K": "D",
    "Q": "C",
    "J": "B",
    "T": "A",
    "9": "9",
    "8": "8",
    "7": "7",
    "6": "6",
    "5": "5",
    "4": "4",
    "3": "3",
    "2": "2"
}


# function maps each hand to a unique integer score
def eval_hand(hand_p):
    pairs = "".join(str(p) for p in sorted(hand_p.count(card) for card in set(hand_p)))
    type_value = pairs_to_type[pairs]
    value_str = type_value + "".join(card_to_hex_value[card] for card in hand_p)
    return int(value_str, 16)


score_to_hand = {eval_hand(hand): hand for hand in hand_to_bid}

result = 0
mul = 1

for score in sorted(score_to_hand):
    result += mul * hand_to_bid[score_to_hand[score]]
    mul += 1

print(result)
