from testcases import target_coord, convert_to_str
from succ_func import successor_func, State, manhat_heu
import timeit

start_states = []
for target in target_coord:
    start_states.extend(successor_func(State(target)))
start_state = min(start_states)

def astar(state: State, not_visited: list = target_coord.copy()):
    if state.getCurrent() == state.getTarget():
        not_visited.remove(state.getCurrent())
        if not_visited:
            best_next_target = min(not_visited, key=lambda target: manhat_heu(state.getCurrent(), target))
            state.target = best_next_target
            state.heu_val = manhat_heu(state.getCurrent(), state.getTarget())
            state.total_val = state.getHeuVal() + state.getCostVal()
            best_next_move = min(successor_func(state))
            return astar(best_next_move, not_visited)
        else:
            return state
    else:
        best_next_move = min(successor_func(state))
        return astar(best_next_move, not_visited)

start_time = timeit.default_timer()
final_path = astar(start_state)
end_time = timeit.default_timer()
total_time = f'{end_time - start_time} seconds'
print(f"{convert_to_str(final_path.getSteps())}, {total_time}")