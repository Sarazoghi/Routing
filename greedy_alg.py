from testcases import *
from succ_func import *
import timeit
import math

def bestHeuVal(first: State, second: State):
    if first.getHeuVal() != second.getHeuVal():
        if first.getHeuVal() < second.getHeuVal():
            return first
        else:
            return second
    else:
        return first
    
def greedy(start_state: State):
    if start_state.getCurrent() == start_state.getTarget():
        return start_state
    else:
        successor_states = successor_func(start_state)
        best_next_state = None
        for first, second in zip(successor_states, successor_states[1:]):
            best_next_state = bestHeuVal(first, second)
        print(start_state.getInfo(), best_next_state.getInfo())
        if best_next_state.getHeuVal() > start_state.getHeuVal():
            return None
        return greedy(best_next_state)

start_time = timeit.default_timer()

targets = target_coord.copy()
start_states = []
for target in target_coord:
    start_states.extend(successor_func(State(target)))

final_state = min(start_states)
while targets and final_state:
    best_next_target = min(targets, key=lambda target: manhat_heu(final_state.getCurrent(), target))
    final_state.setTarget(best_next_target)
    final_state = greedy(final_state)
    targets.remove(best_next_target)

end_time = timeit.default_timer()

if final_state:
    total_time = f'{end_time - start_time} seconds'
    print(f"Steps: {convert_to_str(final_state.getSteps())} \nEnergy: {final_state.getEnergy()} \nTime: {total_time}")
else:
    print('No route found!')