from testcases import target_coord, city_map
from succ_func import successor_func, State

start_states = []
for target in target_coord:
    start_states.extend(successor_func(State(target)))
start_state = start_states[0]
for st_state in start_states:
    if st_state.getTotalVal() < start_state.getTotalVal():
        start_state = st_state
        
def astar(state: State):
    successor_states = successor_func(state)
    