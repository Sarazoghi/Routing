from testcases import city_map, target_coord, rows, cols, convert_to_str
from succ_func import State, successor_func
import timeit
import math

def dfs_best_path(start_state, targets):
    visited = set()
    best_energy_path = []
    total_energy = 0
    elapsed_time = 0

    for target in targets:
        stack = [start_state]
        max_energy_path = []

        start_time = timeit.default_timer()

        while stack and target not in visited:
            current_state = stack.pop()

            if current_state.getCurrent() in visited:
                continue

            visited.add(current_state.getCurrent())

            print("Visited:", current_state.getCurrent())  # Print the visited cell

            if current_state.getCurrent() == target:
                targets.remove(target)  # Mark the target as visited

                if not max_energy_path or current_state.getEnergy() > max_energy_path[-1].getEnergy():
                    max_energy_path = current_state.getSteps() + [current_state.getCurrent()]

        end_time = timeit.default_timer()
        elapsed_time += end_time - start_time
        total_energy += max_energy_path[-1].getEnergy() if max_energy_path else 0

        best_energy_path += max_energy_path[:-1]  # Exclude the last cell, which is the target itself

        # Set the last visited target as the new starting point
        start_state = State(target=target)

    return best_energy_path, total_energy, elapsed_time


# Example usage:
start_state = State(target=(0, 0))  # Start from the first house
max_energy_path, total_energy, elapsed_time = dfs_best_path(start_state, target_coord)
optimal_path = convert_to_str(max_energy_path)
if max_energy_path:
    print(total_energy, optimal_path, elapsed_time, "seconds")
else:
    print("No solution found.")
