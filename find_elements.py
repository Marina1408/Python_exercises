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
		if l[j] <= splitter:
			i += 1
			l[i], l[j] = l[j], l[i]
	l[i+1], l[end] = l[end], l[i+1]
	return i+1

def quick_sort(l, start, end):
	"""
	Sorts list of items using quick sort algorithm.

	This is iterative implementation of quick sort algorithm.
	"""

	stack = []
	stack.append(start)
	stack.append(end)
	while stack:
		end = stack.pop()
		start = stack.pop()
		s = split(l, start, end)

		if s-1 > start:
			stack.append(start)
			stack.append(s - 1)

		if s+1 < end:
			stack.append(s + 1)
			stack.append(end)

quick_sort(lst, 0, len(lst) - 1)
print("Output list: {}".format(lst))
number = int(input("Введіть число для якого треба знайти найближчу пару \n  "))
max = 0

for i in range(0, n - 1):
	j = i + 1
	while j < n:
		sum = lst[i] + lst[j]
		if sum <= number and sum > max:
			max = sum
			max_i = i
			max_j = j
		j += 1
	i += 1

print(max, lst[max_i], lst[max_j])




