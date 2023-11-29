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
                energy_cost = 0  # No additional energy cost for targets
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
            else :
                print("YOU ARE A LOSER :)")

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

# Generate successor states from the initial state
successors = successor(initial_state, city_map)

# Print the generated successor states with energy cost
for s in successors:
    x, y, energy = s
    print(f"New Position: ({x}, {y}), New Energy: {energy}")
