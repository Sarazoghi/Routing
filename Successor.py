import time

def successor(state, city_map):
    x, y, energy = state
    successors = []
    rows, cols = len(city_map), len(city_map[0])

    # Define the possible moves
    moves = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}

    for action, (dx, dy) in moves.items():
        new_x, new_y = x + dx, y + dy

        # Check if the new position is within the allowed range
        if 0 <= new_x < rows and 0 <= new_y < cols:
            cell_value = city_map[new_x][new_y]

            # Calculate the energy cost based on the cell value
            first_letter = cell_value[0]
            second_letter = cell_value[1]
            
            energy_cost = int(first_letter)

            if second_letter == 'T':
                energy_cost   # No additional energy cost for targets
            elif second_letter == 'C':
                energy_cost = 10 - energy_cost  # Replenish energy at the cafe
            elif second_letter == 'B':
                energy_cost = 5 - energy_cost  # Replenish energy at the B ysquiit
            elif second_letter == 'I':
                energy_cost = 12 - energy_cost  # Energy cost for using the fast 12 yen street

            # Check if Ali can afford the energy cost
            if energy - energy_cost >= 0:
                # Update the energy after the move
                new_energy = energy - energy_cost
                # Append the successor state to the list
                successors.append((new_x, new_y, new_energy))

    return successors

def find_optimal_route(initial_state, city_map):
    start_time = time.time()
    
    # Initialize variables
    final_energy = 500
    current_state = initial_state
    movements_used = []
    
    # Flatten the city_map to check for targets in the entire map
    targets_exist = 'T' in [cell[1] for row in city_map for cell in row]

    # Perform movements until reaching all targets
    while targets_exist:
        successors = successor(current_state, city_map)

        # If no successors are available, there is no route
        if not successors:
            print("There is no route.")
            return

        # Choose the successor with the maximum energy gain
        best_successor = max(successors, key=lambda x: x[2])

        # Update variables
        current_state = (best_successor[0], best_successor[1], best_successor[2])
        final_energy = best_successor[2]
        movements_used.append(best_successor[3])

        # Check for targets in the entire city_map
        targets_exist = 'T' in [cell[1] for row in city_map for cell in row]

    end_time = time.time()

    # Print the results
    print(f"{final_energy}")
    print(f"{''.join(movements_used)}")
    print(f"{end_time - start_time:.4f}")

# Example usage:
city_map = [
    ['1R', '1', '1', '5', '5', '4', '2C', '1', '15', '1B'],
    ['1', '1', '5', '3', '5', '5', '4', '5', 'X', 'X'],
    ['5', '1I', '1', '6', '2', '2', '2', '1', '1', '1T'],
    ['X', 'X', '1', '6', '5', '5', '2', '1', '1', 'X'],
    ['X', 'X', '1', 'X', 'X', '50', '2', '1C', '1', 'X'],
    ['1', '1', '1', '2', '2', '2T', '2', '1', '1', '1'],
]

# Example initial state
initial_state = (0, 0, 500)  # Replace with the actual initial state

# Find the optimal route
find_optimal_route(initial_state, city_map)
