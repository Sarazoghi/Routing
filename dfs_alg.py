from queue import LifoQueue
from testcases import *
from succ_func import *
import timeit

def dfs(start_state: State, targets):
    visited = set()
    stack = LifoQueue()
    stack.put(start_state)

    while not stack.empty() and targets:
        current_state = stack.get()

        # Check if the current state is already in the path
        if current_state.getCurrent() in current_state.getSteps():
            continue

        visited.add(current_state.getCurrent())

        print("Visited:", current_state.getCurrent())  # Print the visited cell
        print("Energy:", current_state.getEnergy())  # Print the current energy level

        if current_state.getCurrent() in targets:
            targets.remove(current_state.getCurrent())  # Mark the target as visited

            # Check if all targets are visited after marking the current target
            if not targets:
                return current_state

        successor_states = successor_func(current_state)

        # Push successor states with updated energy in reverse order for DFS
        for state in reversed(successor_states):
            print(state.getInfo())
            
            # Update the steps by adding the current state's position to it
            updated_steps = current_state.getSteps() + [current_state.getCurrent()]

            if state.getEnergy() >= 0 and set(state.getTargets()) == set(targets):
                state_energy = state.getEnergy() + city_map[state.getCurrent()[0]][state.getCurrent()[1]]
                updated_state = State(targets, state.getCurrent(), state_energy, updated_steps)
                stack.put(updated_state)

    return None

start_time = timeit.default_timer()

targets = target_coord.copy()

start_state = State(targets, None, START_ENERGY, [])

final_state = dfs(start_state, targets)

end_time = timeit.default_timer()

if final_state and final_state.getEnergy() != float('-inf'):
    total_time = f'{end_time - start_time} seconds'
    print(f"Steps: {(final_state.getSteps())} \nEnergy: {final_state.getEnergy()} \nTime: {total_time}")
else:
    print('No route found!')
