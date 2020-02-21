from math import factorial
import random

class Solver:
    
    def __init__(self, board_size):
        self.board_size = board_size
        
    def generateState(self):
        state = []
        for i in range(self.board_size):
            state.append(random.randint(0, self.board_size))
        return state
        
    def checkValidState(self, state):
        for x in state:
            if x < 0 or x >= self.board_size:
                return False
        return len(state) != self.board_size
    
    def checkValid(self, states):
        for idx in range(len(states)):
            if self.checkValidState(states[idx]):
                return tuple((True, idx))
        return tuple((False, -1))
    
    def nCr(self, n, r):
        return int(factorial(n) / factorial(r) / factorial(n-r))
    
    def calcPairs(self, state):
        """Calculate number of pairs of attacking queens"""
        h = 0
        # Get number of pairs of queens in the same row
        for x in state:
            if state.count(x) > 1:
               h += self.nCr(state.count(x), 2) # Add number of pairs
               
        # Get number of pairs of queens on diagonals
        total = 0
        for i in range(len(state)):
            x = state[i]
            for j in range(len(state)):
                if j != i:
                    y = state[j]
                    # If difference in index of two values is equal to the difference 
                    # of their values, they are on the same diagonal line
                    if i - j == x - y:
                        total += 1
        h += total / 2  # Half total to remove pairs from symmetry
        return h
        
    def fitness(self, states):
        """Orders states list by number of pairs of attacking queens"""
        rank = []
        for state in states:
            rank.append(tuple((state, self.calcPairs(state))))
        rank.sort(key=lambda x: x[1])
        
        sorted_states = [x[0] for x in rank]  # Get states in sorted order
        return sorted_states
                    
    def genetic(self):
        states = []
        
        for i in range(4):
            states.append(self.generateState())
                
        while not self.checkValid(states)[0]:
            states = self.fitness(states)
            # Selection
            # Crossover
            # Mutation
            
        goal_state = states[self.checkValid(states)[1]]
            
        return goal_state


if __name__ == "__main__":
    solver = Solver(8)
    solver.genetic()