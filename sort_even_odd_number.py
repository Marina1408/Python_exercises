import random

def merge_sort(l):
	""" Recursive merge sort """

	if len(l) > 1:
		mid = len(l) // 2
		left = l[:mid]
		right = l[mid:]

		merge_sort(left)
		merge_sort(right)

		i = j = k = 0
		while i < len(left) and j < len(right):
			if left[i] % 2 != 0 and right[j] % 2 != 0:
				if left[i] > right[j]:
					l[k] = right[j]
					j += 1
				else:
					l[k] = left[i]
					i += 1
			elif left[i] % 2 != 0 and right[j] % 2 == 0:
				l[k] = left[i]
				i += 1
			elif left[i] % 2 == 0 and right[j] % 2 != 0:
				l[k] = right[j]
				j += 1
			else:
				if left[i] % 2 == 0 and right[j] % 2 == 0:
					if left[i] > right[j]:
						l[k] = right[j]
						j += 1
					else:
						l[k] = left[i]
						i += 1
			k += 1

		if i < len(left):
			l[k: k + len(left[i:])] = left[i:]
		if j < len(right):
			l[k: k + len(right[j:])] = right[j:]

n = int(input("Вкажіть довжину списку \n  "))
lst = random.sample(range(1, 100), n)
print("Input list: {}".format(lst)) 
merge_sort(lst)
print("Output list: {}".format(lst))