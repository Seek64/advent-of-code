with open("input.txt", "r") as f:
    input_str = f.read()

result = 0

for report_str in input_str.split("\n"):
    report = list(map(int, report_str.split()))
    report_safe = (all(0 < l2 - l1 < 4 for l1, l2 in zip(report, report[1:]))
                   or all(0 > l2 - l1 > -4 for l1, l2 in zip(report, report[1:])))
    if report_safe:
        result += 1

print(result)
