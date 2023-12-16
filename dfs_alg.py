from queue import LifoQueue
from testcases import *
from succ_func import *
import timeit

def dfs(start_state: State, targets: list = target_coord.copy()):
    visited = []
    stack = LifoQueue()
    stack.put(start_state)

    while not stack.empty():
        current_state = stack.get()

        if current_state not in visited:
            visited.append(current_state)
                
            if current_state.getCurrent() in targets:
                if current_state.getEnergy() != float('-inf'):
                    targets.remove(current_state.getCurrent())
                    if not targets:
                        return current_state
                    current_state.setHeuVal(targets)

            successor_states = successor_func(current_state)
            for state in successor_states:
                stack.put(state)

    return None

start_time = timeit.default_timer()

targets = target_coord.copy()

start_state = min(successor_func(State()))

final_state = dfs(start_state)

end_time = timeit.default_timer()

steps = convert_to_str(final_state.getSteps() + [final_state.getCurrent()])