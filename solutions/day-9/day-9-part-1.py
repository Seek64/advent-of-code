def extrapolate(input_seq):
    sequences = [input_seq]
    while set(sequences[-1]) != {0}:
        curr_seq = sequences[-1]
        sequences.append([curr_seq[i] - curr_seq[i - 1] for i in range(1, len(curr_seq))])

    sequences[-1].append(0)

    for i in range(len(sequences) - 2, -1, -1):
        sequences[i].append(sequences[i][-1] + sequences[i + 1][-1])

    return sequences[0][-1]


f = open("input.txt", "r")
input_str = f.read()
f.close()

input_seq_list = [[int(n) for n in s.split()] for s in input_str.split("\n")]
result = 0

for seq in input_seq_list:
    result += extrapolate(seq)

print(result)
