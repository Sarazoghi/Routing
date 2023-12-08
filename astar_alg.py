from testcases import target_coord

def manhat_heu(state: tuple, target: tuple):
    state_x, state_y = state
    target_x, target_y = target
    return abs(state_x - target_x) + abs(state_y - target_y)