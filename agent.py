from mortgage import State
import random
import numpy as np

class Agent():
    
    def __init__(self):
        self.policies = {}
        
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
        policy = self.policies.get(state)
        if policy is None:
            policy = self.get_random_policy()
        self.perturb(policy)
        self.policies[state] = policy
        if not opportunities:
            print("No refinance because no opportunity, returning ", state.variable_fraction)
            return state.variable_fraction # same fb implies no refinancing
        result = self.sample_action(policy)
        print("Sampled action with given policy is: ", result)
        return result

