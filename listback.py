import random

def listback(l):
	"""reverse list"""
	return l[::-1]
		
n = int(input("Вкажіть довжину списку \n  "))
lst = random.sample(range(1, 100), n)
print("Input list: {}".format(lst)) 
print("Output list: {}".format(listback(lst)))