class Mortgage():
    
    def __init__(self):
        principle_balance = 0.0
        variable_fraction = 0.0
        fixed_interest_rate = 0.0
        variable_interest_rate = 0.0
        
    
class Simulator():
    def __init__(self):
        m = Mortgage()
    
    simulate(self, action = None):
        self.enact(action)
        opportunities = getPoissonOpportunities(self.m)
        yield(self.m, opportunities)
        
