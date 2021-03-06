from random import choice

lst = [choice(range(10)) for i in range(5)]
print(f'Input list: {lst}')


def insertion_sort(l):
	for i in range(1, len(l)):
		k = l[i]
		j = i - 1
		while j >= 0 and l[j] > k:
			l[j+1] = l[j]
			j -= 1
		l[j+1] = k


def min_sum(lst):
	"""
	"""
	insertion_sort(lst)
	x = y = 0
	for i in range(len(lst)):
		if i % 2 != 0:
			x = x * 10 + lst[i]
		else:
			y = y * 10 + lst[i]

	print(f"First number: {x}")
	print(f"Second number: {y}")
	return x + y


print(f'Sum: {min_sum(lst)}')