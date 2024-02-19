from queue import Queue

f = open("input.txt", "r")
input_str = f.read()
f.close()

LOW = False
HIGH = True

ff_states = dict()
conj_states = dict()
out_connections = dict()

for module_str in input_str.split("\n"):
    name_str, output_str = module_str.split(" -> ")
    type_str = ""
    if name_str != "broadcaster":
        type_str = name_str[0]
        name_str = name_str[1:]
    out_connections[name_str] = output_str.split(", ")
    if type_str == "%":
        ff_states[name_str] = LOW
    elif type_str == "&":
        conj_states[name_str] = dict()

for start_module in out_connections:
    for target_module in out_connections[start_module]:
        if target_module in conj_states:
            conj_states[target_module][start_module] = LOW


def push_button():
    pulses = Queue()
    for tar in out_connections["broadcaster"]:
        pulses.put(("broadcaster", tar, LOW))

    while not pulses.empty():
        src, tar, pulse = pulses.get()

        if tar == "rx" and pulse == LOW:
            return True

        if tar in ff_states and pulse == LOW:
            new_ff_state = not ff_states[tar]
            ff_states[tar] = new_ff_state
            for next_tar in out_connections[tar]:
                pulses.put((tar, next_tar, new_ff_state))

        if tar in conj_states:
            conj_states[tar][src] = pulse
            if all(state == HIGH for state in conj_states[tar].values()):
                out_pulse = LOW
            else:
                out_pulse = HIGH
            for next_tar in out_connections[tar]:
                pulses.put((tar, next_tar, out_pulse))

    return False


# Brute forcing the solution is not feasible.
# The Flip-flops alone can traverse 2^48 states.
# A more efficient method is needed.
button_presses = 0
while not push_button():
    button_presses += 1

print(button_presses)
