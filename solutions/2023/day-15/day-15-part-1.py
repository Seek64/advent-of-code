f = open("input.txt", "r")
input_str = f.read()
f.close()


def compute_hash(step_str):
    h = 0
    for c in step_str:
        h = (h + ord(c)) * 17 % 256
    return h


result = sum(compute_hash(s) for s in input_str.split(","))

print(result)
