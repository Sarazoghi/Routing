from queue import Queue
from testcases import *
from succ_func import *
import timeit

targets = target_coord.copy()

def bfs(start_state: State):
    visited = []
    queue = Queue()
    queue.put(start_state)

    while not queue.empty():
        current_state = queue.get()

        if current_state not in visited:
            visited.append(current_state)
                
            if current_state.getCurrent() in targets:
                if current_state.getEnergy() != float('-inf'):
                    targets.remove(current_state.getCurrent())
                    current_state.setHeuVal(targets)
                    return current_state

            successor_states = successor_func(current_state)
            for state in successor_states:
                queue.put(state)

    return None

start_time = timeit.default_timer()

final_state = min(successor_func(State()))

while targets:
    final_state = bfs(final_state)
    
end_time = timeit.default_timer()

steps = convert_to_str(final_state.getSteps() + [final_state.getCurrent()])