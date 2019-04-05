import random

n = int(input("Вкажіть довжину списку \n  "))
lst = random.sample(range(1, 100), n)
print("Input list: {}".format(lst)) 

def split(l, start, end):
	"""
	Splits list into two parts.

	Splits list into two parts each element of first part
	are not bigger then every element of last part.
	"""

	i = start - 1
	splitter = l[end]

	for j in range(start, end):
		if splitter % 2 == 0:
			if l[j] % 2 == 0:
				if l[j] >= splitter:
					i += 1
					l[i], l[j] = l[j], l[i]
		else:
			if l[j] % 2 == 0:
				i += 1
				l[i], l[j] = l[j], l[i]
			else:
				if l[j] <= splitter:
					i += 1
					l[i], l[j] = l[j], l[i]

	l[i+1], l[end] = l[end], l[i+1]
	return i+1

def quick_sort(l, start, end):
	"""
	Sorts list of items using quick sort algorithm.

	This is recursive implementation of quick sort algorithm.
	"""

	if start < end:
		s = split(l, start, end)
		quick_sort(l, start, s - 1)
		quick_sort(l, s + 1, end)	

quick_sort(lst, 0, len(lst) - 1)
print("Output list: {}".format(lst))