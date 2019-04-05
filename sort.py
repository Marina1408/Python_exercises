a = [int(i) for i in input("Введіть список чисел через пробіл \n > ").split()]

def sort(l, i):
	"""
	This program recursive checks if the list is sorted
	"""
	
	while i < (len(l) - 1):
		if l[i] <= l[i+1]:
			sort(l, i+1)
			return print("This list is sorted")
		else:
			return print("This list is not sorted!!!!")
			break
		
sort(a, 0)