import random

def listback(l, a, step):
	"""recursion reverse list"""
	if step < - len(l):
		return 1
	else:
		a.append(l[step])
		step -= 1
		listback(l, a, step)
	return a
		
n = int(input("Вкажіть довжину списку \n  "))
lst = random.sample(range(1, 100), n)
print("Input list: {}".format(lst)) 
a = []
print("Output list: {}".format(listback(lst, a, -1)))