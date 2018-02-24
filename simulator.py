from mortgage import Mortgage
from agent import Agent

class Simulator():
    
    def __init__(self):
        self.m = Mortgage()
        self.options = self.m.refinance_opportunities()
    
    def simulate():
        s = Simulator()
        a = Agent()
        while(True):
            action = a.get_action(s.opportunities, s.m.state())
            reward = self.m.enact(action)
            

