from queue import Queue
from testcases import *
from succ_func import *
import timeit

def bfs(start_state: State):
    visited = set()
    queue = Queue()
    queue.put(start_state)

    while not queue.empty():
        current_state = queue.get()

        # Process the current state (you can add your own logic here)
        print("Visiting:", current_state.getCurrent())

        # Mark the current state as visited
        visited.add(current_state.getCurrent())

        # Generate successor states using successor_func
        successor_states = successor_func(current_state)

        for state in successor_states:
            if state.getCurrent() not in visited:
                queue.put(state)

    print("BFS traversal completed.")

# Example usage:
start_time = timeit.default_timer()

# Assuming you have some logic to initialize the start_state properly
start_state = State(targets=target_coord.copy(), current=(0, 0), energy=START_ENERGY)

bfs(start_state)

end_time = timeit.default_timer()
total_time = f'{end_time - start_time} seconds'
print(f"Time: {total_time}")
