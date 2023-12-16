from testcases import *
from succ_func import *
import timeit
import math

def bestHeuVal(first: State, second: State):
    if sum(first.getHeuVal()) <= sum(second.getHeuVal()):
        return first
    else:
        return second
    
def greedy(start_state: State, targets: list = target_coord.copy()):
    if start_state.getEnergy() < most_cost:
        return None
    else:
        if start_state.getCurrent() in targets:
            targets.remove(start_state.getCurrent())
            if not targets:
                return start_state
            start_state.setHeuVal(targets)
            return greedy(start_state, targets)
        else:
            successor_states = successor_func(start_state)
            best_next_state = successor_states[0]
            for state in successor_states[1:]:
                best_next_state = bestHeuVal(best_next_state, state)
            return greedy(best_next_state)

start_time = timeit.default_timer()

targets = target_coord.copy()

start_state = min(successor_func(State()))

final_state = greedy(start_state)

end_time = timeit.default_timer()

if final_state and final_state.getEnergy() != float('-inf'):
    total_time = f'{end_time - start_time} seconds'
    print(f"Steps: {convert_to_str(final_state.getSteps())} \nEnergy: {final_state.getEnergy()} \nTime: {total_time}")
else:
    print('No route found!')