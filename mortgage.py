import numpy as np
import random

class State():
    
    def __init__(self, base_interest_rate, variable_fraction, variable_interest_rate, number_of_payments):
        self.base_interest_rate = base_interest_rate
        self.variable_fraction = variable_fraction
        self.variable_interest_rate = variable_interest_rate
        self.number_of_payments = number_of_payments
    
    def __hash__(self):
        return hash((self.base_interest_rate, self.variable_fraction, self.variable_interest_rate, self.number_of_payments))
    
    def __str__(self):
        return 'rt:{} fb:{} vt:{} n:{}'.format(self.base_interest_rate, self.variable_fraction, self.variable_interest_rate, self.number_of_payments)

class Mortgage():
    
    def __init__(self):
        self.principle_balance = 200000
        self.total_payments = 60
        self.days = 30 # total expected loan duration is 30*60 days
        self.coupon_payment = self.principle_balance / self.total_payments # might require more than N payments!
        
        self.base_interest_rate=0.06 # rt
        b = 0.005
        self.fixed_interest_rate = self.base_interest_rate + b # mt = rt+b
        self.variable_fraction = 0.0 #fb
        c = random.choice([2.0,2.5,3.0,3.5,4.0])
        self.variable_interest_rate = self.base_interest_rate + c # vt = rt + c
        self.number_of_payments = 0
    
    def enact(self, action):
        self.number_of_payments += 1
        self.principle_balance -= self.coupon_payment
        print("New balance after coupon payment: ", self.principle_balance)
        self.principle_balance += self.principle_balance*self.variable_fraction*(self.variable_interest_rate/12) + self.principle_balance*(1-self.variable_fraction)*(self.fixed_interest_rate/12)
        # compounding monthly, by 1/12th of the annual interest rate
        print("New balance after interest accrues: ", self.principle_balance)
        if self.principle_balance == 0:
            return "Loan completely paid back."

        print("Enacting action: ", action)
        if action == self.variable_fraction: # staying in the same state
            print("Staying in same state")
            pass
        else:
            print("Updating state... ")
            self.update_base_interest_rate()
            print("Updated rt: ", self.base_interest_rate)
            print("Updated mt: ", self.fixed_interest_rate)            
            self.variable_fraction = action
            print("Updated fb: ", self.variable_fraction)
            self.number_of_payments = 0
            self.principle_balance *= 1.02 # transaction cost = 2%
            print("New pb after transaction cost: ", self.principle_balance)
        c = random.choice([2.0,2.5,3.0,3.5,4.0])
        self.variable_interest_rate = self.base_interest_rate + c
        print("New vt:", self.variable_interest_rate)
        return self.get_reward(action)
    
    def get_reward(self, action):
        return random.randint(0,100)
    
    def refinance_opportunities(self):
        result = None
        if (np.random.poisson(lam=(1.0))>0):
            result = True
        else:
            result = False
        print("Refinance opportunities in poisson distribution with k = 1: ", result)
        return result
    
    def state(self):
        result = State(self.base_interest_rate, self.variable_fraction, self.variable_interest_rate, self.number_of_payments)
        print(result)
        return result
    

    def update_base_interest_rate(self):
        a=0.005
        multiplier = [-2.0, -1.0, 0.0, 1.0, 2.0]
        selected = random.choice(multiplier)
        print('updating rt by setting = rt+({}*a)'.format(selected))
        rt = self.base_interest_rate+(a*selected)
        
        if rt < 0.04:
            self.base_interest_rate = 0.04
        elif rt > 0.12:
            self.base_interest_rate = 0.12
        else:
            self.base_interest_rate = rt
        b = 0.005
        self.fixed_interest_rate = self.base_interest_rate + b

