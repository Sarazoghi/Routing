from queue import Queue
from testcases import *
from succ_func import *
import timeit

def bfs(start_state: State, targets: list = target_coord.copy()):
    visited = set()
    queue = Queue()
    queue.put(start_state)

    while not queue.empty():
        current_state = queue.get()
        state_tuple = (current_state.getCurrent(), current_state.getEnergy(), tuple(current_state.getHeuVal()))

        if state_tuple not in visited:
            visited.add(state_tuple)
                
            if current_state.getCurrent() in targets:
                if current_state.getEnergy() != float('-inf'):
                    targets.remove(current_state.getCurrent())
                    if not targets:
                        return current_state
                    current_state.setHeuVal(targets)

            successor_states = successor_func(current_state)
            for state in successor_states:
                queue.put(state)

    return None

start_time = timeit.default_timer()

targets = target_coord.copy()

start_state = min(successor_func(State()))

final_state = bfs(start_state)

end_time = timeit.default_timer()

if final_state.getEnergy() != float('-inf'):
    total_time = f'{end_time - start_time} seconds'
    print(f"Steps: {convert_to_str(final_state.getSteps() + [final_state.getCurrent()])} \nEnergy: {final_state.getEnergy()} \nTime: {total_time}")
else:
    print('No route found!')
