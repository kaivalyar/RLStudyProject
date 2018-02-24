from mortgage import State

class Agent():
    
    def __init__(self):
        self.policies = {}
        
    def get_action(self, opportunities, state):
        policy = self.policies.get(state)
        if policy is None:
            policy = get_random_policy()
        perturb(policy)
        self.policies[state] = policy
        return sample_action(policy, opportunities)

