from testcases import *

class State:
    def __init__(self, targets: list = target_coord.copy(), current: tuple = None, energy: int = START_ENERGY, steps: list = None):
        self.current = current
        self.energy = energy
        self.targets = targets
        self.cost_val = START_ENERGY - energy
        if not current:
            self.heu_val = [float('-inf') for target in self.targets]
        else:
            self.heu_val = [manhat_heu(current, target) for target in self.targets]
        self.total_val = [self.cost_val + self.heu_val[i] for i in range(len(self.targets))]
        self.steps = steps
        
    def __lt__(self, other):
        if self.total_val != other.total_val:
            return sum(self.total_val) < sum(other.total_val)
        else:
            return self.energy > other.energy
        
    def __eq__(self, other):
        if isinstance(other, State):
            return (self.current == other.current and
                    self.targets == other.targets and
                    self.current in other.steps)
        return False
    
    def getCurrent(self):
        return self.current
    
    def getEnergy(self):
        return self.energy
    
    def getCostVal(self):
        return self.cost_val
    
    def getHeuVal(self):
        return self.heu_val
    
    def getTargets(self):
        return self.targets
    
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
        
    def setCostVal(self, costVal: int):
        self.cost_val = costVal
        self.total_val = [self.cost_val + self.heu_val[i] for i in range(len(self.targets))]
    
    def setHeuVal(self, targets: list):
        self.targets = targets
        self.heu_val = [manhat_heu(self.current, target) for target in self.targets]
        self.total_val = [self.cost_val + self.heu_val[i] for i in range(len(self.targets))]
        
    def setSteps(self, new_steps: list):
        self.steps = new_steps

def manhat_heu(current: tuple, target: tuple):
    state_x, state_y = current
    target_x, target_y = target
    return abs(state_x - target_x) + abs(state_y - target_y)

def successor_func(state: State):
    successor_states = []
    if state.getCurrent() is not None:
        state_x, state_y = state.getCurrent()
        for move in moves:
            move_x, move_y = moves[move]
            next_x = state_x + move_x
            next_y = state_y + move_y
            if (0 <= next_x < len(city_map)) and (0 <= next_y < len(city_map[0])):
                successor_states.append(State(state.getTargets(),
                                              (next_x, next_y),
                                              state.getEnergy() + city_map[next_x][next_y],
                                              state.getSteps() + [state.getCurrent()]))
                if initial_map[next_x][next_y][-1:] in bonus_values.keys():
                    city_map[next_x][next_y] -= bonus_values[initial_map[next_x][next_y][-1:]]
    else:
        successor_states.append(State(state.getTargets(),
                                      (0, 0),
                                      state.getEnergy() + city_map[0][0],
                                      []))
    return successor_states