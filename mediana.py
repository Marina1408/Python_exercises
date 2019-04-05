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
			if left[i] < right[j]:
				l[k] = left[i]
				i += 1
			else:
				l[k] = right[j]
				j += 1
			k += 1

		if i < len(left):
			l[k: k + len(left[i:])] = left[i:]
		if j < len(right):
			l[k: k + len(right[j:])] = right[j:]


N = int(input("Вкажіть довжину першого списку \n  "))
lst1 = random.sample(range(1, 100), N)
print("Input list_1: {}".format(lst1)) 
M = int(input("Вкажіть довжину другого списку \n  "))
lst2 = random.sample(range(1, 100), M)
print("Input list_2: {}".format(lst2)) 
merge_sort(lst1)
merge_sort(lst2)
print("Output list_1: {}".format(lst1))
print("Output list_2: {}".format(lst2))

if N % 2 == 0:
	mediana_1 = (lst1[(N - 1) // 2] + lst1[(N - 1) // 2 + 1]) / 2
else:
	mediana_1 = lst1[N // 2]
print(mediana_1)
if M % 2 == 0:
	mediana_2 = (lst2[(M - 1) // 2] + lst2[(M - 1)// 2 + 1]) / 2
else:
	mediana_2 = lst2[M // 2] 
print(mediana_2)
mediana = (mediana_1 + mediana_2) / 2
print("Медіаною двох списків є число {}".format(mediana))