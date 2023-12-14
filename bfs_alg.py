from testcases import START_ENERGY, city_map, target_coord
from succ_func import State, successor_func
from queue import Queue
from collections import deque

def bfs_best_paths(start, targets):
    best_paths = {}  # Dictionary to store the best path from start to each target
    best_energy_to_targets = float('-inf')

    for target in targets:
        print(f"Finding path to target {target}:")

        queue = deque([start])
        visited = set()

        while queue:
            current_state = queue.popleft()

            visited.add(current_state.getCurrent())

            if current_state.getCurrent() == target:
                path_energy = START_ENERGY
                for cell in current_state.getSteps():
                    cell_energy = city_map[cell[0]][cell[1]]
                    path_energy += cell_energy 
                if path_energy > best_energy_to_targets:
                    best_paths[target] = current_state.getSteps()
                    best_energy_to_targets = path_energy
                break  # Stop exploring once the target is reached

            successors = successor_func(current_state)
            for successor in successors:
                cell_value = city_map[successor.getCurrent()[0]][successor.getCurrent()[1]]
                if cell_value != float('-inf') and successor.getCurrent() not in visited:
                    queue.append(successor)
                    visited.add(successor.getCurrent())  # Add the current position to visited

            print(f"Current state: {current_state.getCurrent()}")
            print(f"Current path: {current_state.getSteps()}")

        print(f"Best path to target {target}: {best_paths.get(target, 'No valid path found')}")
        print(f"Best energy to target {target}: {best_energy_to_targets}")
        print("\n")

    return best_paths

# Example usage:
start_state = State(target_coord[0])
best_paths = bfs_best_paths(start_state, target_coord)

print("Best Paths to Targets:")
for target, path in best_paths.items():
    path_energy = START_ENERGY
    for cell in path:
        cell_energy = city_map[cell[0]][cell[1]]
        path_energy += cell_energy
    print(f"Target {target}: {path + [target]}, Energy: {path_energy}")

# Find the overall best path among targets
if best_paths:
    max_energy_path = max(best_paths.values(), key=lambda path: sum(city_map[x][y] for x, y in path))
    overall_best_path_energy = START_ENERGY
    for cell in max_energy_path:
        cell_energy = city_map[cell[0]][cell[1]]
        overall_best_path_energy += cell_energy
    print("Overall Best Path:", max_energy_path + [target_coord[0]])
    print("Overall Best Path Energy:", overall_best_path_energy)
else:
    print("No valid paths found.")
