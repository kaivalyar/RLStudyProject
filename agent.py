from mortgage import State
from scipy.linalg import hadamard
import math
import random
import numpy as np



delta = 0.01
L = 1
alpha = 0.05

C = 2**(math.ceil(math.log(12, 2))) # C = 16
hadamard = hadamard(C)
hbar = hadamard[:, 1:12]
offset = random.randint(0,15)

class Agent():

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
    
    def normalize(v):
        norm = np.linalg.norm(v, ord=1)
        if norm == 0:
           return v
        return v / norm
        
    def get_action(self, opportunities, state):
        policy = self.policies.get(state)
        if policy is None:
            policy = self.get_random_policy()
            self.updates[state] = 0
            self.policies[state] = policy
        if not opportunities:
            print("No refinance because no opportunity, returning ", state.variable_fraction)
            return state.variable_fraction # same fb implies no refinancing
        #print("updatedict = ", self.updates)
        result = self.sample_action(policy)
        #Agent.update_policy(state, result)
        print("Sampled action with given policy is: ", result)
        return result

    def update(self, action, reward, state, time_passed, current_coupon_payment):
        print("updating state = {}".format(state))
        n = self.updates[state]
        policy = self.policies[state]
        print("previous policy = ", policy)
        print("n (iteration value) = ", n)
        a = Agent.a(n)
        inverse_del_pi_i = Agent.inverse(Agent.get_del_pi_i(n))
        print("inverse del pi i = ", inverse_del_pi_i)
        v_n_l = Agent.V(n, state, reward, time_passed, current_coupon_payment)
        print("Vnl = ", v_n_l)
        new_policy = Agent.project(policy + a*(v_n_l/delta)*inverse_del_pi_i)
        print("new policy = ", new_policy)
        self.policies[state] = new_policy
        self.updates[state] = n+1
        
    def get_del_pi_i(n):
        return hbar[(n+offset)%C]
    
    def inverse(del_pi_i):
        #print(del_pi_i)
        #print(del_pi_i.shape)
        return del_pi_i

    def a(n):
        a = 1/(n+1)
        return a
    
    def b(n):
        b = 1/(n+1)
        return b

    def V(n, state, reward, time_passed, current_coupon_payment):
        if n == 0: # base case
            return 2
        b = Agent.b(n)


        del_pi_i = Agent.get_del_pi_i(n)
        pi_bar = Agent.project(self.policies[state]+delta*del_pi_i)
        new_fb = self.sample_action(pi_bar)
        
        c = current_coupon_payment
        fb = state.variable_fraction
        vt = state.variable_interest_rate
        rt = state.base_interest_rate # should be mt!
        days = 30
        
        if fb == new_fb: # no expected refinance
            e_reward = c + c*fb*vt + c*(1-fb)*rt
        else:
            e_reward = c + c*fb*vt*(time_passed/days) + c*(1-fb)*rt*(time_passed/days)
        val = Agent.eV(n-1, None, e_reward)


        return (1-b)*Agent.V(n-1, state, reward, time_passed, current_coupon_payment) + b*(reward + alpha*( val ))
    
    def eV(n, state, reward):
        if n == 0: # base case
            return 2
        b = Agent.b(n)
        return (1-b)*Agent.eV(n-1, state, reward) + b*(reward)
    
    def project(policy):
        minimum = np.amin(policy)
        if (minimum < 0):
            policy += abs(minimum)
        projection = Agent.normalize(policy)
        return projection





