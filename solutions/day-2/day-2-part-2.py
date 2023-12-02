from re import findall

f = open("input.txt", "r")
input_str = f.read()
f.close()

result = 0

for game in input_str.split("\n"):
    red_max = max(int(n) for n in findall(r"(\d*) red", game))
    green_max = max(int(n) for n in findall(r"(\d*) green", game))
    blue_max = max(int(n) for n in findall(r"(\d*) blue", game))

    result += red_max * green_max * blue_max

print(result)
