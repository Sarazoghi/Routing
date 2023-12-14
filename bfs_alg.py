# from testcases import target_coord,city_map,START_ENERGY;
# from succ_func import State, successor_func;
# from queue import Queue;
# import time;

# # Assuming START_ENERGY, city_map, and target_coord are defined
# # calculate the right answer
# def bfs(start_state, start_energy):
#     start_time = time.time()

#     visited = set()
#     queue = Queue()
#     queue.put(start_state)

#     max_energy = float('-inf')
#     optimal_path = []

#     while not queue.empty():
#         current_state = queue.get()

#         if current_state.getCurrent() in visited:
#             continue

#         visited.add(current_state.getCurrent())

#         # Calculate energy for the current state
#         energy = start_energy
#         path = reconstruct_path(current_state)
#         if path is None:
#             continue  # Skip if the path is None

#         for step in path:
#             if step is not None:  # Add this check to handle NoneType
#                 energy += city_map[step[0]][step[1]]

#         # Update max_energy and optimal_path when a valid path with finite energy is found
        
#         if ((energy < float('inf') and energy > float('-inf')) and energy > max_energy) :
#             max_energy = energy
#             optimal_path = path

#         # Generate successors with the desired order
#         successors = successor_func(current_state)
#         if successors is None:
#             continue  # Skip if the successors are None

#         successors.sort(key=lambda s: abs(s.getCurrent()[0] - target_coord[0][0]) + abs(s.getCurrent()[1] - target_coord[0][1]))

#         for successor in successors:
#             queue.put(successor)

#         if set(target_coord).issubset(set(visited)):
#             break
    
#     end_time = time.time()
#     elapsed_time = end_time - start_time

#     return {
#         'final_energy': max_energy,
#         'optimal_path': optimal_path,
#         'elapsed_time': elapsed_time
#     }

# def reconstruct_path(end_state):
#     path = []
#     current_state = end_state

#     while current_state is not None:
#         path.append(current_state.getCurrent())
#         current_state = current_state.getParent()

#     return list(reversed(path))

# # Creating the initial state
# start_state = State(target_coord[0], energy=START_ENERGY)
# # Running BFS
# result = bfs(start_state, START_ENERGY)
# print("Target Coordinates:", target_coord)
# # Displaying the results
# if result:
#     print("Final Energy:", result['final_energy'])
#     print("Optimal Path:", result['optimal_path'])
#     print("Elapsed Time:", result['elapsed_time'])
# else:
#     print("No valid path found.")

# Assuming START_ENERGY, city_map, and target_coord are defined
# calculate the right answer
from testcases import START_ENERGY, city_map, target_coord
from succ_func import State, successor_func,moves
from queue import Queue
import time

# Assuming START_ENERGY, city_map, and target_coord are defined
# calculate the right answer
def bfs(start_state, start_energy):
    start_time = time.time()

    visited = set()
    queue = Queue()
    queue.put(start_state)

    max_energy = float('-inf')
    optimal_path = None

    while not queue.empty():
        current_state = queue.get()

        if current_state.getCurrent() in visited:
            continue

        visited.add(current_state.getCurrent())

        # Calculate energy for the current state
        energy = start_energy
        path = reconstruct_path(current_state)
        if path is None:
            continue  # Skip if the path is None

        for move in moves:
            successors = successor_func(current_state, move)
            if successors is None:
                continue  # Skip if the successors are None

            for successor in successors:
                queue.put(successor)

        # Check if all targets are visited
        if all(target in visited for target in target_coord):
        # Update max_energy and optimal_path when all targets are visited with finite energy
            if (energy < float('inf') and energy > float('-inf')) and energy > max_energy:
                max_energy = energy
                optimal_path = path.copy() 

        print("Current State:", current_state.getInfo())
        # print("Visited Set:", visited)
        # print("Energy:", energy)
        # print("Path:", path)

    end_time = time.time()
    elapsed_time = end_time - start_time

    return {
        'final_energy': max_energy,
        'optimal_path': optimal_path,
        'elapsed_time': elapsed_time
    }

def reconstruct_path(end_state):
    path = []
    current_state = end_state

    while current_state is not None:
        current_cell = current_state.getCurrent()

        # Exclude cells with X from the path
        if current_cell and city_map[current_cell[0]][current_cell[1]] != float('-inf'):
            path.append(current_cell)

        current_state = current_state.getParent()

    return list((path))
# Creating the initial state
start_state = State(target_coord[0], energy=START_ENERGY)
# Running BFS
result = bfs(start_state, START_ENERGY)
print("Target Coordinates:", target_coord)
# Displaying the results
if result:
    print("Final Energy:", result['final_energy'])
    print("Optimal Path:", result['optimal_path'])
    print("Elapsed Time:", result['elapsed_time'])
else:
    print("No valid path found.")
