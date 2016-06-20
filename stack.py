class stack:

	def __init__(self):
		self.stack_main = []

	def push(self,val):
		self.stack_main.append(val)

	def pop(self):
		return self.stack_main.pop()

	def size(self):
		return len(self.stack_main)

	def top(self):
		return self.stack_main[-1]

	def __getitem__(self,key):
		return self.stack_main[key] if key!= 'top' else self.stack_main[-1]


S = stack()
S.push(3)
S.push(5)
S.push(6)
S.push(8)
S.push(19134)
print [S.pop() for i in range(4)]
print S['top']
print S.size()
