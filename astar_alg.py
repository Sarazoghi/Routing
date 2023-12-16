from testcases import *
from succ_func import *
import timeit

def astar(start_state: State, targets: list = target_coord.copy()):
    open_set = [start_state]
    closed_set = []

    while open_set:
        current_state = min(open_set)
        open_set.remove(current_state)

        if current_state.getCurrent() in targets:
            targets.remove(current_state.getCurrent())
            if not targets:
                return current_state
            current_state.setHeuVal(targets)

        successor_states = successor_func(current_state)
        for successor_state in successor_states:
            succ_x, succ_y = successor_state.getCurrent()
            tentative_cost_val = current_state.getCostVal() + city_map[succ_x][succ_y]
            if successor_state not in closed_set:
                if successor_state not in open_set:
                    open_set.append(successor_state)
                else:
                    if tentative_cost_val < successor_state.getCostVal():
                        successor_state.setCostVal(tentative_cost_val)
                        successor_state.setSteps(current_state.getSteps() + [current_state.getCurrent()])

        closed_set.append(current_state)

    return None

start_time = timeit.default_timer()

targets = target_coord.copy()

start_state = min(successor_func(State()))
final_state = astar(start_state)

end_time = timeit.default_timer()

if final_state.getEnergy() != float('-inf'):
    total_time = f'{end_time - start_time} seconds'
    curr_x, curr_y = final_state.getCurrent()
    print(f"Steps: {convert_to_str(final_state.getSteps() + [final_state.getCurrent()])} \nEnergy: {final_state.getEnergy()} \nTime: {total_time}")
else:
    print('No route found!')