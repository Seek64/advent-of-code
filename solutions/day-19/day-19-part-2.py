from re import findall
from queue import Queue

f = open("input.txt", "r")
input_str = f.read()
f.close()

category_to_index = {
    "x": 0,
    "m": 1,
    "a": 2,
    "s": 3
}

workflows = dict()
workflow_matches = findall(r"([a-z]+)\{(.*)}", input_str)
for wf_name, wf_str in workflow_matches:
    wf_steps = list()
    for step in wf_str.split(",")[:-1]:
        cond, next_wf = step.split(":")
        wf_steps.append((cond[0], cond[1], cond[2:], next_wf))
    wf_steps.append(wf_str.split(",")[-1])
    workflows[wf_name] = wf_steps

# We reason over ranges now
result = 0
wf_queue = Queue()
wf_queue.put(("in", [(1, 4000), (1, 4000), (1, 4000), (1, 4000)]))

while not wf_queue.empty():
    wf_id, parts = wf_queue.get()
    if wf_id == "A":
        int_result = 1
        for cat in parts:
            int_result *= (cat[1] - cat[0] + 1)
        result += int_result
    elif not wf_id == "R":
        curr_wf = workflows[wf_id]
        for step in curr_wf[:-1]:
            i = category_to_index[step[0]]
            threshold = int(step[2])
            if parts[i][0] < threshold < parts[i][1]:
                branch_parts = [part for part in parts]
                if step[1] == "<":
                    branch_parts[i] = (parts[i][0], threshold - 1)
                    parts[i] = (threshold, parts[i][1])
                elif step[1] == ">":
                    branch_parts[i] = (threshold + 1, parts[i][1])
                    parts[i] = (parts[i][0], threshold)
                wf_queue.put((step[3], branch_parts))
        wf_queue.put((curr_wf[-1], parts))

print(result)
