from mortgage import State
from scipy.linalg import hadamard
import math
import random
import numpy as np


class Agent():

    delta = 0.001
    L = 1
    alpha = 0
    
    C = 2**(math.ceil(math.log(12, 2))) # C = 16
    hadamard = hadamard(C)
    hbar = hadamard[: 1:12]

    def __init__(self):
        self.policies = {} # dictionary mapping states to policies (s -> pi_i)
        self.updates = {}
        
    def sample_action(self, policy):
        return np.random.choice([0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0], p=policy)
    
    def get_random_policy(self):
        policy = np.random.random_sample((11,))
        policy = Agent.normalize(policy)
        print(policy)
        #print(sum(policy))
        return policy
    
    def perturb(self, policy):
        policy = policy
        pass

    def normalize(v):
        norm = np.linalg.norm(v, ord=1)
        if norm == 0:
           return v
        return v / norm
        
    def get_action(self, opportunities, state):
        if not opportunities:
            print("No refinance because no opportunity, returning ", state.variable_fraction)
            return state.variable_fraction # same fb implies no refinancing
        policy = self.policies.get(state)
        if policy is None:
            policy = self.get_random_policy()
        self.perturb(policy) # ?
        self.policies[state] = policy
        self.updates[state] = 0
        result = self.sample_action(policy)
        #Agent.update_policy(state, result)
        print("Sampled action with given policy is: ", result)
        return result

    def update(self, action, reward, state):
        n = self.updates[state]
        policy = self.policies[state]
        a = Agent.a(n)
        b = Agent.b(n)
        self.updates[state] = n+1
        

    def a(n):
        a = 1/(n+1)
        return a
    
    def b(n):
        b = 1/(n+1)
        return b

    def V(n, state, reward):
        if n == 0:
            return 2
        b = Agent.b(n)
        return (1-b)*Agent.V(n-1, state) + b*(reward + alpha*( 1 ))
    
            





