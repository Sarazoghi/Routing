from testcases import START_ENERGY, city_map, target_coord

class State:
    def __init__(self, target: tuple, current: tuple = None, energy: int = START_ENERGY):
        self.current = current
        self.energy = energy
        self.target = target
        self.cost_val = START_ENERGY - energy
        if not current:
            self.heu_val = float('inf')
        else:
            self.heu_val = manhat_heu(current, target)
        self.total_val = self.cost_val + self.heu_val
    
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
    
    def getInfo(self):
        return (self.getCurrent(),
                self.getEnergy(),
                self.getCostVal(),
                self.getHeuVal(),
                self.getTotalVal())

def manhat_heu(state: tuple, target: tuple):
    state_x, state_y = state
    target_x, target_y = target
    return abs(state_x - target_x) + abs(state_y - target_y)

moves = {
    'U': (0, -1),
    'D': (0, 1),
    'L': (-1, 0),
    'R': (1, 0)
}

def successor_func(state: State):
    if state.getCurrent() is not None:
        successor_states = []
        state_x, state_y = state.getCurrent()
        for move in moves:
            move_x, move_y = moves[move]
            next_x = state_x + move_x
            next_y = state_y + move_y
            if (0 <= next_x < len(city_map)) and (0 <= next_y < len(city_map[0])):
                next_state = State(state.getTarget(),
                                   (next_x, next_y),
                                   state.getEnergy() + city_map[next_x][next_y])                                
                successor_states.append(next_state)
        return successor_states
    else:
        successor_states = []
        successor_states.append(State(state.getTarget(),
                                      (0, 0),
                                      state.getEnergy() + city_map[0][0]))
        return successor_states
