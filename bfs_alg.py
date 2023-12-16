from queue import Queue
from testcases import *
from succ_func import *
import timeit

def bfs(start_state: State, targets):
    visited = set()
    queue = Queue()
    queue.put(start_state)

    while not queue.empty() and targets:
        current_state = queue.get()

        if current_state.getCurrent() in visited:
            continue

        visited.add(current_state.getCurrent())

        print("Visited:", current_state.getCurrent())  # Print the visited cell

        if current_state.getCurrent() in targets:
            targets.remove(current_state.getCurrent())  # Mark the target as visited

            # Check if all targets are visited after marking the current target
            if not targets:
                return current_state

        successor_states = successor_func(current_state)

        # Enqueue successor states with updated energy
        for state in successor_states:
            if state.getCurrent() not in visited and state.getEnergy() >= 0:
                state_energy = state.getEnergy() + city_map[state.getCurrent()[0]][state.getCurrent()[1]]
                updated_steps = current_state.getSteps() + [state.getCurrent()]  # Include the new step
                updated_state = State(state.getTargets(), state.getCurrent(), state_energy, updated_steps)
                queue.put(updated_state)

    return None

start_time = timeit.default_timer()

targets = target_coord.copy()

# Assuming the initial state is at the starting point (0, 0)
start_state = State(targets, None, 500, [])

final_state = bfs(start_state, targets)

end_time = timeit.default_timer()

if final_state and final_state.getEnergy() != float('-inf'):
    total_time = f'{end_time - start_time} seconds'
    print(f"Steps: {convert_to_str(final_state.getSteps() + [final_state.getCurrent()])} \nEnergy: {final_state.getEnergy()} \nTime: {total_time}")
else:
    print('No route found!')
