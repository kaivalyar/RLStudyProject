from mortgage import Mortgage
from agent import Agent
import numpy as np
import random

class Simulator():
    
    def __init__(self):
        self.m = Mortgage()
    
    def simulate():
        s = Simulator()
        a = Agent()
        for i in range(10):
            print('\n\n------')
            print('\ngetting action from agent')
            action = a.get_action(s.m.refinance_opportunities(), s.m.state())
            print("\nenacting action in environment")            
            reward = s.m.enact(action)
            print("reward: ", reward)
            

def main():
    np.random.seed(0)
    random.seed(0)
    Simulator.simulate()

if __name__ == '__main__':
    main()

