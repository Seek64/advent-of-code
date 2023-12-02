from re import findall

f = open("input.txt", "r")
input_str = f.read()
f.close()

RED_LIMIT = 12
GREEN_LIMIT = 13
BLUE_LIMIT = 14

result = 0

for game in input_str.split("\n"):
    game_id = int(findall(r"Game (\d*):", game)[0])
    red_max = max(int(n) for n in findall(r"(\d*) red", game))
    green_max = max(int(n) for n in findall(r"(\d*) green", game))
    blue_max = max(int(n) for n in findall(r"(\d*) blue", game))

    if red_max <= RED_LIMIT and green_max <= GREEN_LIMIT and blue_max <= BLUE_LIMIT:
        result += game_id

print(result)
