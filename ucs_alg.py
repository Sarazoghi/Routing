from queue import PriorityQueue
from succ_func import *
from testcases import *
import timeit

start_time = timeit.default_timer()

targets = target_coord.copy()

def ucs(start_state: State):
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
    final_state = ucs(final_state)
    targets.remove(final_state.getCurrent())

end_time = timeit.default_timer()

if final_state.getEnergy() != float('-inf'):
    total_time = f'{end_time - start_time} seconds'
    curr_x, curr_y = final_state.getCurrent()
    print(f"Steps: {convert_to_str(final_state.getSteps() + [final_state.getCurrent()])} \nEnergy: {final_state.getEnergy()} \nTime: {total_time}")
else:
    print('No route found!')