with open("input.txt", "r") as f:
    input_str = f.read()

WIDTH = input_str.find("\n") + 1

result = 0

for i in range(len(input_str)):
    if input_str[i] == "A":
        if (input_str[i - WIDTH - 1:i + WIDTH + 2:WIDTH + 1] in ("MAS", "SAM") and
            input_str[i - WIDTH + 1:i + WIDTH    :WIDTH - 1] in ("MAS", "SAM")):
            result += 1

print(result)
