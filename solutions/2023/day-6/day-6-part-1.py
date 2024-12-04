from re import findall

f = open("input.txt", "r")
input_str = f.read()
f.close()

time_str, distance_str, *_ = input_str.split("\n")
times = [int(n) for n in findall(r"(\d+)", time_str)]
distances = [int(n) for n in findall(r"(\d+)", distance_str)]

result = 1

for race_time, threshold in zip(times, distances):
    margin = 0
    for acc_time in range(1, race_time):
        distance = (race_time - acc_time) * acc_time
        if distance > threshold:
            margin += 1
    result *= margin

print(result)
