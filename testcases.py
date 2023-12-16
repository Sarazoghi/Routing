import copy

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
    ['1', '1', '1', '2', 'X', '2T', '2', '1', '1', '1'],
]

initial_map = [
    ['1R', 'X',  'X', 'X', 'X', 'X',  'X', 'X',  'X', 'X'],
    ['1',  'X',  'X', 'X', 'X', 'X',  'X', 'X',  'X', 'X'],
    ['5',  '1I', '1', 'X', 'X', 'X',  'X', 'X',  '1', '1T'],
    ['X',  'X',  '1', '6', '5', '5',  'X', 'X',  '1', 'X'],
    ['X',  'X',  'X', 'X', 'X', '50', '2', '1C', '1', 'X'],
    ['X',  'X',  'X', 'X', 'X', '2T', 'X', 'X',  'X', 'X'],
]
city_map = copy.deepcopy(initial_map)
target_coord = []
START_ENERGY = 500
bonus_values = {
    'C': 10,
    'B': 5,
    'I': 12
}
moves = {
    'U': (-1, 0),
    'D': (1, 0),
    'L': (0, -1),
    'R': (0, 1)
}

for row in range(rows):
    for index in range(cols):
        if initial_map[row][index].isdigit():
            city_map[row][index] = -int(initial_map[row][index])
        elif initial_map[row][index][-1:] == 'R':
            city_map[row][index] = -int(initial_map[row][index][:-1])
        elif initial_map[row][index][-1:] == 'T':
            target_coord.append((row, index))
            city_map[row][index] = -int(initial_map[row][index][:-1])
        elif initial_map[row][index] == 'X':
            city_map[row][index] = float('-inf')
        elif initial_map[row][index][-1:] == 'C' or initial_map[row][index][-1:] == 'B' or initial_map[row][index][-1:] == 'I':
            city_map[row][index] = -int(initial_map[row][index][:-1]) + bonus_values[initial_map[row][index][-1:]]
            
def convert_to_str(steps: list):
    def diff_tuple(first, second):
        return tuple(x - y for x, y in zip(first, second))
    def swap_keyvalue(dictionary: dict):
        return {value: key if not isinstance(key, dict) else swap_keyvalue(key) for key, value in dictionary.items()}
    result_str = ''
    for step1, step2 in zip(steps[1:], steps[:-1]):
        result_str += swap_keyvalue(moves)[diff_tuple(step1, step2)]
    return result_str

temp_flat_map = []
for row in city_map:
    temp_flat_map.extend(row)
flat_map = []
for item in temp_flat_map:
    if item != float('-inf'):
        flat_map.append(item)
biggest_cost = min(flat_map)
most_cost = biggest_cost * rows * cols