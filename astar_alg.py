from testcases import *
from succ_func import *
import timeit

def astar(start_state: State, target: tuple):
    open_set = [start_state]
    closed_set = []

    while open_set:
        current_state = min(open_set)
        open_set.remove(current_state)

        if current_state.getCurrent() == target:
            return current_state

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

start_states = []
for target in target_coord:
    start_states.extend(successor_func(State(target)))

not_visited = target_coord.copy()
final_state = min(start_states)
while not_visited:
    best_next_target = min(not_visited, key=lambda target: manhat_heu(final_state.getCurrent(), target))
    final_state.setTarget(best_next_target)
    final_state = astar(final_state, best_next_target)
    not_visited.remove(best_next_target)

end_time = timeit.default_timer()

if final_state.getEnergy() != float('-inf'):
    total_time = f'{end_time - start_time} seconds'
    print(f"Steps: {convert_to_str(final_state.getSteps())} \nEnergy: {final_state.getEnergy()} \nTime: {total_time}")
else:
    print('No route found!')