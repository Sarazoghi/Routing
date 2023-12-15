from testcases import target_coord ,rows , cols
from succ_func import State, successor_func
import heapq
import time


def bfs_all_targets(start_state, targets):
    visited = set()
    priority_queue = [start_state]
    max_energy_path = []
    energy = 0;
    
    start_time = time.time();
    
    while priority_queue and set(targets) - visited:
        current_state = heapq.heappop(priority_queue)

        if current_state.getCurrent() in visited:
            continue

        visited.add(current_state.getCurrent())

        if current_state.getCurrent() in targets:
            targets.remove(current_state.getCurrent())  # Mark the target as visited

            # Check if all targets are visited after marking the current target
            if not (set(targets) - visited):
                
                if not max_energy_path or current_state.getEnergy() > max_energy_path[-1].getEnergy():
                    max_energy_path = current_state.getSteps() + [current_state.getCurrent()]
                    energy = current_state.getEnergy()
        successor_states = successor_func(current_state)
        for successor_state in successor_states:
            heapq.heappush(priority_queue, successor_state)
            
    end_time = time.time()
    elapsed_time = end_time - start_time
    
    return max_energy_path , energy , elapsed_time # Return the path with maximum energy and all targets


# Example usage:
start_state = State(target=(rows - 1, cols - 1))
max_energy_path , total_energy , elapsed_time = bfs_all_targets(start_state, target_coord)

if max_energy_path:
    print("Final Energy : " ,total_energy)  
    for step in max_energy_path :
        print("Step :", step) 
        
    print("Elapsed Time:", elapsed_time, "seconds")
else:
    print("No solution found.")