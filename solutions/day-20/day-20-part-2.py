from queue import Queue
from math import lcm

f = open("input.txt", "r")
input_str = f.read()
f.close()

# This was a challenging one.
# Brute forcing the solution by simulating the entire network is not feasible.
# However, the network is divided into four sub-networks which leaf to the "mf" conjunction.
# Therefore, we can calculate the periods for each sub-network and compute the smallest common multiple.

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


sub_networks = []
for candidate in out_connections["broadcaster"]:
    new_sub_network = [candidate]
    i = 0
    while i < len(new_sub_network):
        src = new_sub_network[i]
        i += 1
        if src == "mf":
            continue
        for tar in out_connections[src]:
            if tar not in new_sub_network:
                new_sub_network.append(tar)
    new_sub_network = [x for x in new_sub_network if x in ff_states]
    sub_networks.append(new_sub_network)

cnt = 0
periods = [0] * len(sub_networks)
while 0 in periods:
    push_button()
    cnt += 1
    for i in range(len(sub_networks)):
        if len(sub_networks[i]) == len([x for x in sub_networks[i] if ff_states[x] == LOW]):
            periods[i] = cnt

# The required outputs are only set correctly if all flip-flops are LOW.
# Therefore, we can simply calculate the LCM of the period lengths.
result = lcm(*periods)
print(result)
