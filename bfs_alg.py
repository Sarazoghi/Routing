from testcases import START_ENERGY, city_map, target_coord ,rows , cols
from succ_func import State, successor_func,moves
from queue import Queue
import time


# start_state = State(target_coord[0])
# print(start_state.getInfo())
# first_move = successor_func(start_state)
# second_move = []
# for state in first_move:
#     second_move.extend(successor_func(state))
#     print("First",state.getInfo())
# third_move = []
# for state in second_move:
#     third_move.extend(successor_func(state))
#     print("Second",state.getInfo())
# for state in third_move:
#     print(state.getInfo())
def bfs(start_state,start_energy) : 
    print(start_state.getInfo())

    moves = [start_state]

    for i in range(cols):
        new_moves = []
        for state in moves:
            new_moves.extend(successor_func(state))
        moves = new_moves

    for state in moves:
        print(state.getInfo())
    return


start_state = State(target_coord[0])
start_energy = START_ENERGY;

bfs(start_state,start_energy);




