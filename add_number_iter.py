class AddNumber:

	def __init__(self, num=0, stop=100):
		self.num = num
		self.stop = stop

	def __iter__(self):
		self.n = 0
		return self

	def __next__(self):
		if self.n <= self.stop:
			result = self.n + self.num
			self.n += 5
			return result
		else:
			raise StopIteration
			

for n in AddNumber():
	print(n)