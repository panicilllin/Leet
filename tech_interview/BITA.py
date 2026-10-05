def cal_steps(ladder, max_steps):
    # print(f"ladder={ladder}, steps={max_steps}")
    res = []
    if ladder == 1:
        return [[1]]
    if max_steps == 0:
        return [[]]
    if ladder == max_steps:
        res.append([max_steps])
    max_step_this_round = min(max_steps, ladder)
    for i in range(max_step_this_round, 0, -1):
        # print(i)
        future_res = cal_steps(ladder - i, max_steps)
        # print(future_res)
        res_this_round = [[i] + j for j in future_res]
        res.extend(res_this_round)
    return res
