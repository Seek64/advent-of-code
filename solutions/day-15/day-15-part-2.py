from re import match

f = open("input.txt", "r")
input_str = f.read()
f.close()


def compute_hash(label_str):
    h = 0
    for c in label_str:
        h = (h + ord(c)) * 17 % 256
    return h


def focussing_power(box_number, box_list):
    fp = 0
    for i, (lens_label, lens_fl) in enumerate(box_list):
        fp += (box_number + 1) * (i + 1) * lens_fl
    return fp


boxes = {i: [] for i in range(256)}

for step in input_str.split(","):
    label, operation, focal_length = match(r"([a-zA-Z]*)([-=])(\d*)", step).groups()
    box = boxes[compute_hash(label)]
    # Not an ideal data structure, but sufficient for the given complexity
    if operation == "=":
        replaced = False
        for i, (l, f) in enumerate(box):
            if l == label:
                box[i] = (label, int(focal_length))
                replaced = True
        if not replaced:
            box.append((label, int(focal_length)))
    elif operation == "-":
        for i, (l, f) in enumerate(box):
            if l == label:
                box.pop(i)


result = sum(focussing_power(i, boxes[i]) for i in range(len(boxes)))

print(result)
