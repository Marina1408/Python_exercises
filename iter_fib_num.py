class AddFibNumber:

	def __init__(self, stop=100):
		self.stop = stop	

	def __iter__(self):
		self.a = 0
		self.b = 1
		return self

	def __next__(self):
		fib_num = self.a + self.b
		if fib_num <= self.stop:
			self.a = self.b
			self.b = fib_num	
			return fib_num	
		else:
			raise StopIteration
			

for n in AddFibNumber():
	print(n) 


