from testcases import START_ENERGY, city_map, target_coord, rows, cols

class State:
    def __init__(self, target: tuple, current: tuple = None, energy: int = START_ENERGY, steps: list = None):
        self.current = current
        self.energy = energy
        self.target = target
        self.cost_val = START_ENERGY - energy
        if not current:
            self.heu_val = float('-inf')
        else:
            self.heu_val = manhat_heu(current, target)
        self.total_val = self.cost_val + self.heu_val
        self.steps = steps
    
    def getCurrent(self):
        return self.current
    
    def getEnergy(self):
        return self.energy
    
    def getCostVal(self):
        return self.cost_val
    
    def getHeuVal(self):
        return self.heu_val
    
    def getTarget(self):
        return self.target
    
    def getTotalVal(self):
        return self.total_val
    
    def getSteps(self):
        return self.steps
    
    def getInfo(self):
        return (self.getCurrent(),
                self.getEnergy(),
                self.getCostVal(),
                self.getHeuVal(),
                self.getTotalVal(),
                self.getSteps())

def manhat_heu(state: tuple, target: tuple):
    state_x, state_y = state
    target_x, target_y = target
    return abs(state_x - target_x) + abs(state_y - target_y)

moves = {
    'U': (-1, 0),
    'D': (1, 0),
    'L': (0, -1),
    'R': (0, 1)
}

def successor_func(state: State):
    successor_states = []
    if state.getCurrent() is not None:
        state_x, state_y = state.getCurrent()
        for move in moves:
            move_x, move_y = moves[move]
            next_x = state_x + move_x
            next_y = state_y + move_y
            if (0 <= next_x < rows) and (0 <= next_y < cols):
                successor_states.append(State(state.getTarget(),
                                              (next_x, next_y),
                                              state.getEnergy() + city_map[next_x][next_y],
                                              state.getSteps() + [state.getCurrent()]))
    else:
        successor_states.append(State(state.getTarget(),
                                      (0, 0),
                                      state.getEnergy() + city_map[0][0],
                                      []))
    return successor_states

start_state = State(target_coord[0])
print(start_state.getInfo())
first_move = successor_func(start_state)
second_move = []
for state in first_move:
    second_move.extend(successor_func(state))
    print(state.getInfo())
third_move = []
for state in second_move:
    third_move.extend(successor_func(state))
    print(state.getInfo())
for state in third_move:
    print(state.getInfo())