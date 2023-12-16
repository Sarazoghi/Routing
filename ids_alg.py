from queue import LifoQueue
from testcases import *
from succ_func import *
import timeit

def ids(start_state: State, all_targets: list, depth_limit: int):
    visited = []
    stack = LifoQueue()
    stack.put((start_state, 0, all_targets))  

    while not stack.empty():
        current_state, current_depth, targets = stack.get()

        if current_state not in visited:
            visited.append(current_state)

            if current_state.getCurrent() in targets:
                if current_state.getEnergy() != float('-inf'):
                    targets.remove(current_state.getCurrent())
                    if not targets:
                        return current_state

            if current_depth < depth_limit:
                successor_states = successor_func(current_state)
                for state in successor_states:
                    stack.put((state, current_depth + 1, targets.copy()))

    return None

start_time = timeit.default_timer()

all_targets = target_coord.copy()
start_state = min(successor_func(State()))

depth_limit = 0
while True:
    final_state = ids(start_state, all_targets.copy(), depth_limit)
    if final_state is not None:
        break
    depth_limit += 1

end_time = timeit.default_timer()

if final_state.getEnergy() != float('-inf'):
    total_time = f'{end_time - start_time} seconds'
    curr_x, curr_y = final_state.getCurrent()
    print(f"Steps: {convert_to_str(final_state.getSteps() + [final_state.getCurrent()])} \nEnergy: {final_state.getEnergy()} \nTime: {total_time}")
else:
    print('No route found!')



