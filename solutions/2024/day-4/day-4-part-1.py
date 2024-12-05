with open("input.txt", "r") as f:
    input_str = f.read()

WIDTH = input_str.find("\n") + 1

result = 0

for i in range(len(input_str)):
    if input_str[i] == "X":
        if input_str[i:][:4] == "XMAS":
            result += 1
        if input_str[i::WIDTH + 1][:4] == "XMAS":
            result += 1
        if input_str[i::WIDTH][:4] == "XMAS":
            result += 1
        if input_str[i::WIDTH - 1][:4] == "XMAS":
            result += 1
        if input_str[i::-1][:4] == "XMAS":
            result += 1
        if input_str[i::-WIDTH - 1][:4] == "XMAS":
            result += 1
        if input_str[i::-WIDTH][:4] == "XMAS":
            result += 1
        if input_str[i::-WIDTH + 1][:4] == "XMAS":
            result += 1

print(result)
