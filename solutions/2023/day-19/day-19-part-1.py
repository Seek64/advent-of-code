from re import findall

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
        wf_steps.append((cond[0], cond[1:], next_wf))
    wf_steps.append(wf_str.split(",")[-1])
    workflows[wf_name] = wf_steps

parts = findall(r"\{x=(\d*),m=(\d*),a=(\d*),s=(\d*)}", input_str)


def evaluate_workflow(part_tuple, wf_id):
    workflow = workflows[wf_id]

    for wf_step in workflow[:-1]:
        part_val = part_tuple[category_to_index[wf_step[0]]]
        if eval(part_val + wf_step[1]):
            return wf_step[2]

    return workflow[-1]


result = 0

for part in parts:
    curr_wf = "in"
    done = False
    while not done:
        curr_wf = evaluate_workflow(part, curr_wf)
        if curr_wf == "A":
            result += sum(map(int, part))
            done = True
        elif curr_wf == "R":
            done = True

print(result)
