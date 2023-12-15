from testcases import target_coord, convert_to_str, city_map
from succ_func import successor_func, State, manhat_heu
import timeit

start_states = []
for target in target_coord:
    start_states.extend(successor_func(State(target)))
start_state = min(start_states)

def astar(start_state, not_visited: list = target_coord.copy()):
    open_set = [start_state]
    closed_set = []

    while open_set:
        current_state = min(open_set)
        print(current_state.getInfo())
        open_set.remove(current_state)

        if current_state.getCurrent() in not_visited:
            not_visited.remove(current_state.getCurrent())
            if not_visited:
                best_next_target = min(not_visited, key=lambda target: manhat_heu(current_state.getCurrent(), target))
                current_state.setTarget(best_next_target)
            else:
                return current_state

        successor_states = successor_func(current_state)
        for successor_state in successor_states:
            succ_x, succ_y = successor_state.getCurrent()
            tentative_cost_val = current_state.getCostVal() + city_map[succ_x][succ_y]
            if successor_state in closed_set:
                continue

            if successor_state not in open_set:
                open_set.append(successor_state)
            else:
                if tentative_cost_val < successor_state.getCostVal():
                    successor_state.setCostVal(tentative_cost_val)
                    successor_state.setSteps(current_state.getSteps() + [current_state.getCurrent()])

        closed_set.append(current_state)

    return None


start_time = timeit.default_timer()
final_paths = astar(start_state)
end_time = timeit.default_timer()
total_time = f'{end_time - start_time} seconds'
print(final_paths.getInfo())