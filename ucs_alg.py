from queue import PriorityQueue
from succ_func import *
from testcases import *
import timeit

start_time = timeit.default_timer()

def ucs(start_state: State, targets: list = target_coord.copy()):
    visited = []
    priority_queue = PriorityQueue()
    priority_queue.put((start_state.getCostVal(), start_state))

    while not priority_queue.empty():
        current_state = priority_queue.get()[1]
        
        if current_state not in visited:
            visited.append(current_state)

            if current_state.getCurrent() in targets:
                return current_state

            successor_state = successor_func(current_state)
            for state in successor_state:
                priority_queue.put((state.getCostVal(), state))
    
    return None

targets = target_coord.copy()

final_state = min(successor_func(State()))

while targets:
    final_state = ucs(final_state, targets)
    targets.remove(final_state.getCurrent())

end_time = timeit.default_timer()

steps = convert_to_str(final_state.getSteps() + [final_state.getCurrent()])