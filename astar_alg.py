from testcases import target_coord, city_map
from succ_func import successor_func, State, manhat_heu

start_states = []
for target in target_coord:
    start_states.extend(successor_func(State(target)))
start_state = min(start_states)

def astar(state: State, not_visited: list = target_coord.copy()):
    print(state.getInfo())
    best_next_move = min(successor_func(state))
    if state.getCurrent() == state.getTarget():
        not_visited.remove(state.getCurrent())
        if not_visited:
            best_next_target = min(not_visited, key=lambda target: manhat_heu(state.getCurrent(), target))
            best_next_move.target = best_next_target
            astar(best_next_move, not_visited)
    else:
        astar(best_next_move, not_visited)
        
astar(start_state)