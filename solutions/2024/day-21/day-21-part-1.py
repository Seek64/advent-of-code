with open("input.txt", "r") as f:
    input_str = f.read()

# Sequences like "<v<" should never produce a shorter result than "<<v" or "v<<" and are thus omitted
button_transitions_numeric = {
    "AA": ["A"],
    "A0": ["<A"],
    "A1": ["^<<A"],
    "A2": ["<^A", "^<A"],
    "A3": ["^A"],
    "A4": ["^^<<A"],
    "A5": ["<^^A", "^^<A"],
    "A6": ["^^A"],
    "A7": ["^^^<<A"],
    "A8": ["<^^^A", "^^^<A"],
    "A9": ["^^^A"],
    "0A": [">A"],
    "00": ["A"],
    "01": ["^<A"],
    "02": ["^A"],
    "03": [">^A", "^>A"],
    "04": ["^^<A"],
    "05": ["^^A"],
    "06": [">^^A", "^^>A"],
    "07": ["^^^<A"],
    "08": ["^^^A"],
    "09": [">^^^A", "^^^>A"],
    "1A": [">>vA"],
    "10": [">vA"],
    "11": ["A"],
    "12": [">A"],
    "13": [">>A"],
    "14": ["^A"],
    "15": [">^A", "^>A"],
    "16": [">>^A", "^>>A"],
    "17": ["^^A"],
    "18": [">^^A", "^^>A"],
    "19": [">>^^A", "^^>>A"],
    "2A": [">vA", "v>A"],
    "20": ["vA"],
    "21": ["<A"],
    "22": ["A"],
    "23": [">A"],
    "24": ["<^A", "^<A"],
    "25": ["^A"],
    "26": [">^A", "^>A"],
    "27": ["<^^A", "^^<A"],
    "28": ["^^A"],
    "29": [">^^A", "^^>A"],
    "3A": ["vA"],
    "30": ["<vA", "v<A"],
    "31": ["<<A"],
    "32": ["<A"],
    "33": ["A"],
    "34": ["<<^A", "^<<A"],
    "35": ["<^A", "^<A"],
    "36": ["^A"],
    "37": ["<<^^A", "^^<<A"],
    "38": ["<^^A", "^^<A"],
    "39": ["^^A"],
    "4A": [">>vvA"],
    "40": [">vvA"],
    "41": ["vA"],
    "42": [">vA", "v>A"],
    "43": [">>vA", "v>>A"],
    "44": ["A"],
    "45": [">A"],
    "46": [">>A"],
    "47": ["^A"],
    "48": [">^A", "^>A"],
    "49": [">>^A", "^>>A"],
    "5A": [">vvA", "vv>A"],
    "50": ["vvA"],
    "51": ["<vA", "v<A"],
    "52": ["vA"],
    "53": [">vA", "v>A"],
    "54": ["<A"],
    "55": ["A"],
    "56": [">A"],
    "57": ["<<^A", "^<<A"],
    "58": ["^A"],
    "59": [">^A", "^>A"],
    "6A": ["vvA"],
    "60": ["<vvA", "vv<A"],
    "61": ["<<vA", "v<<A"],
    "62": ["<vA", "v<A"],
    "63": ["vA"],
    "64": ["<<A"],
    "65": ["<A"],
    "66": ["A"],
    "67": ["<<^A", "^<<A"],
    "68": ["<^A", "^<A"],
    "69": ["^A"],
    "7A": [">>vvvA"],
    "70": [">vvvA"],
    "71": ["vvA"],
    "72": [">vvA", "vv>A"],
    "73": [">>vvA", "vv>>A"],
    "74": ["vA"],
    "75": [">vA", "v>A"],
    "76": [">>vA", "v>>A"],
    "77": ["A"],
    "78": [">A"],
    "79": [">>A"],
    "8A": [">vvvA", "vvv>A"],
    "80": ["vvvA"],
    "81": ["<vvA", "vv<A"],
    "82": ["vvA"],
    "83": [">vvA", "vv>A"],
    "84": ["<vA", "v<A"],
    "85": ["vA"],
    "86": [">vA", "v>A"],
    "87": ["<A"],
    "88": ["A"],
    "89": [">A"],
    "9A": ["vvvA"],
    "90": ["<vvvA", "vvv<A"],
    "91": ["<<vvA", "vv<<A"],
    "92": ["<vvA", "vv<A"],
    "93": ["vvA"],
    "94": ["<<vA", "v<<A"],
    "95": ["<vA", "v<A"],
    "96": ["vA"],
    "97": ["<<A"],
    "98": ["<A"],
    "99": ["A"],
}

button_transitions_directional = {
    "AA": ["A"],
    "A^": ["<A"],
    "A<": ["v<<A", "<v<A"],
    "Av": ["<vA", "v<A"],
    "A>": ["vA"],
    "^A": [">A"],
    "^^": ["A"],
    "^<": ["v<A"],
    "^v": ["vA"],
    "^>": [">vA", "v>A"],
    "<A": [">>^A"],
    "<^": [">^A"],
    "<<": ["A"],
    "<v": [">A"],
    "<>": [">>A"],
    "vA": [">^A", "^>A"],
    "v^": ["^A"],
    "v<": ["<A"],
    "vv": ["A"],
    "v>": [">A"],
    ">A": ["^A"],
    ">^": ["<^A", "^<A"],
    "><": ["<<A"],
    ">v": ["<A"],
    ">>": ["A"],
}

result = 0
for seq in input_str.split("\n"):
    d1_sequences = [""]
    for a, b in zip("A" + seq, seq):
        num_trans = a + b
        new_dir_sequences = []
        for bt in button_transitions_numeric[num_trans]:
            for ds in d1_sequences:
                new_dir_sequences.append(ds + bt)
        d1_sequences = new_dir_sequences

    d2_sequences = []
    for d1_seq in d1_sequences:
        d2_sequences_tmp = [""]
        for a, b in zip("A" + d1_seq, d1_seq):
            dir_trans = a + b
            new_dir_sequences = []
            for bt in button_transitions_directional[dir_trans]:
                for ds in d2_sequences_tmp:
                    new_dir_sequences.append(ds + bt)
            d2_sequences_tmp = new_dir_sequences
        d2_sequences.extend(d2_sequences_tmp)

    d3_sequences = []
    for d2_seq in d2_sequences:
        d3_sequences_tmp = [""]
        for a, b in zip("A" + d2_seq, d2_seq):
            dir_trans = a + b
            new_dir_sequences = []
            for bt in button_transitions_directional[dir_trans]:
                for ds in d3_sequences_tmp:
                    new_dir_sequences.append(ds + bt)
            d3_sequences_tmp = new_dir_sequences
        d3_sequences.extend(d3_sequences_tmp)

    seq_len = len(min(d3_sequences, key=len))
    num_value = int(seq[:-1])
    result += seq_len * num_value

print(result)
