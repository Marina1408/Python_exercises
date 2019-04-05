class AddPrimeNumber:

	def __init__(self, stop=101):
		self.stop = stop	

	def __iter__(self):
		self.n = 1
		return self

	def __next__(self):
		if self.n <= self.stop:
			self.n += 1
			for x in range(2, self.n):
				if self.n % x == 0:
					return False
			if True:
				return self.n
		else:
			raise StopIteration
			

for n in AddPrimeNumber():
	if n == False:
		continue
	print(n) 
