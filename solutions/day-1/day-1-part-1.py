from re import findall

f = open("input.txt", "r")
input_str = f.read()
f.close()

result = 0

for value in input_str.split():
    digits = findall(r"\d", value)
    result += int(digits[0] + digits[-1])

print(result)
