from re import findall

f = open("input.txt", "r")
input_str = f.read()
f.close()

race_time, threshold = [int(n) for n in findall(r"\d+", input_str.replace(" ", ""))]

result = 0

# brute force still works in a few seconds...
# a more efficient approach would be to binary search the start and end of the margin that beats the threshold
for acc_time in range(1, race_time):
    distance = (race_time - acc_time) * acc_time
    if distance > threshold:
        result += 1

print(result)
