
class State:
	def __init__(self,rt,fb,vt,n):
		self.rt=rt
		self.fb=fb
		self.vt=vt
		self.n=n
		
# A class which will maintain a list of states and return the 


class Agent:
	def __init__(self):
		self.states=dict()

	def action(self,rt,fb,vt,n):
		current_state=State(rt,fb,vt,n)
		return self.states[current_state]



