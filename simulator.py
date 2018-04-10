from mortgage import Mortgage
from agent import Agent
import numpy as np
import random
import timeit

class Simulator():
    
    def __init__(self):
        self.m = Mortgage()
    
    def simulate():
        s = Simulator()
        a = Agent()
        for i in range(10):
            print('\n\n------')
            print('\ngetting action from agent')
            state = s.m.state()
            action = a.get_action(s.m.refinance_opportunities(), state)
            print("\nenacting action in environment")            
            reward = s.m.enact(action)
            print("\nupdating agent policies based on reward = ", reward)
            a.update(action, reward, state)
            
            

def main():
    np.random.seed(0)
    random.seed(0)
    Simulator.simulate()

if __name__ == '__main__':
    main()

