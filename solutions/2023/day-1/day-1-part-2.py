from re import search

f = open("input.txt", "r")
input_str = f.read()
f.close()

digit_map = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

result = 0

for value in input_str.split():
    digit_1 = search(r"\d|" + "|".join(digit_map), value)[0]
    if digit_1 in digit_map:
        digit_1 = digit_map[digit_1]
    # search from the back to avoid overlapping numbers
    digit_2 = search(r"\d|" + "|".join(d[::-1] for d in digit_map), value[::-1])[0][::-1]
    if digit_2 in digit_map:
        digit_2 = digit_map[digit_2]
    result += int(digit_1 + digit_2)

print(result)
