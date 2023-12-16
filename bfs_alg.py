from testcases import city_map, target_coord, rows, cols, convert_to_str
from succ_func import State, successor_func
import heapq
import timeit
import math

def bfs_all_targets(start_state, targets):
    visited_cells = set()
    queue = [start_state]
    max_energy_path = []
    energy = 0;

    start_time = timeit.default_timer()

    while queue and set(targets) - visited_cells:
        current_state = queue.pop(0)

        if current_state.getCurrent() in visited_cells:
            continue

        visited_cells.add(current_state.getCurrent())

        print("Visited:", current_state.getCurrent())  # Print the visited cell

        if current_state.getCurrent() in targets:
            targets.remove(current_state.getCurrent())  # Mark the target as visited

            # Check if all targets are visited after marking the current target
            if not (set(targets) - visited_cells):

                if not max_energy_path or current_state.getEnergy() > max_energy_path[-1].getEnergy():
                    max_energy_path = current_state.getSteps() + [current_state.getCurrent()]
                    energy = current_state.getEnergy()

        successor_states = successor_func(current_state)

        # Sort the successor states to prioritize left-to-right, top-to-bottom order
        successor_states.sort(key=lambda state: (state.getCurrent()[0], state.getCurrent()[1]))

        for successor_state in successor_states:
            next_x, next_y = successor_state.getCurrent()

            # Check if the cell has a valid value (not -inf)
            if not math.isinf(city_map[next_x][next_y]):
                queue.append(successor_state)

    end_time = timeit.default_timer()
    elapsed_time = end_time - start_time

    return max_energy_path, energy, elapsed_time  # Return the path with maximum energy and all targets


# Example usage:
start_state = State(target=(rows - 1, cols - 1))
max_energy_path, total_energy, elapsed_time = bfs_all_targets(start_state, set(target_coord))
optimal_path = convert_to_str(max_energy_path)
if max_energy_path:
    print(total_energy, optimal_path, elapsed_time, "seconds")
    for state in max_energy_path:
        print(state)
else:
    print("No solution found.")
