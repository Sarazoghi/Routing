# rows, cols = [int(item) for item in input().split()]
# city_map = []
# for row in range(rows):
#     city_map.append(input().split())
rows, cols = 6, 10
initial_map = [
    ['1R', '1', '1', '5', '5', '4', '2C', '1', '15', '1B'],
    ['1', '1', '5', '3', '5', '5', '4', '5', 'X', 'X'],
    ['5', '1I', '1', '6', '2', '2', '2', '1', '1', '1T'],
    ['X', 'X', '1', '6', '5', '5', '2', '1', '1', 'X'],
    ['X', 'X', '1', 'X', 'X', '50', '2', '1C', '1', 'X'],
    ['1', '1', '1', '2', '2', '2T', '2', '1', '1', '1'],
]
city_map = initial_map.copy()
target_coord = []
START_ENERGY = 500
bonus_values = {
    'C': 10,
    'B': 5,
    'I': 12
}

for row in range(rows):
    for index in range(cols):
        if city_map[row][index].isdigit():
            city_map[row][index] = -int(city_map[row][index])
        elif city_map[row][index][-1:] == 'R':
            city_map[row][index] = -int(city_map[row][index][:-1])
        elif city_map[row][index][-1:] == 'T':
            target_coord.append((row, index))
            city_map[row][index] = -int(city_map[row][index][:-1])
        elif city_map[row][index] == 'X':
            city_map[row][index] = float('-inf')
        elif city_map[row][index][-1:] == 'C' or city_map[row][index][-1:] == 'B' or city_map[row][index][-1:] == 'I':
            city_map[row][index] = -int(city_map[row][index][:-1]) + bonus_values[city_map[row][index][-1:]]