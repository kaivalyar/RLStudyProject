class State():
    
    def __init__(self, base_interest_rate, variable_fraction, variable_interest_rate, number_of_payments):
        self.base_interest_rate = base_interest_rate
        self.variable_fraction = variable_fraction
        self.variable_interest_rate = variable_interest_rate
        self.number_of_payements = number_of_payements
    
    def __hash__(self):
        return hash((self.base_interest_rate, self.variable_fraction, self.variable_interest_rate, self.number_of_payments))

class Mortgage():
    
    def __init__(self):
        self.principle_balance = 0
        self.total_payments = 60
        self.days = 0
        self.coupon_payment = 0
        
        self.base_interest_rate=0.0                               
        self.fixed_interest_rate = self.base_interest_rate+0.005 #m=rt+b
        self.variable_fraction = 0.0
        self.variable_interest_rate = 0.0
        self.number_of_payements = 0
    
    def enact(self, action):
        if refinance:
            pass
        else:
            pass
        return self.get_reward(action)
    
    def get_reward(self, action):
        return reward
    
    def refinance_opportunities(self):
        if (poisson(self.days)):
            return Mortgage()
        else:
            return None
    
    def state(self):
        return State(self.base_interest_rate, self.variable_fraction, self.variable_interest_rate, self.number_of_payments)
    

    def recalculate_principal_balance(self):
        return