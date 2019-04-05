import random

n = int(input("Вкажіть довжину списку \n  "))
lst = random.sample(range(1, 100), n)
print("Input list: {}".format(lst)) 

# merger sort
sub_list_size = 1
list_size = n
while sub_list_size < list_size:
	start = 0
	while start < list_size - 1:
		mid = min(start + sub_list_size - 1, list_size - 1)
		end = min(start + 2 * sub_list_size - 1, list_size - 1)

		mlist_1_size = mid - start + 1
		mlist_2_size = end - mid

		mlist_1 = lst[start: start + mlist_1_size]
		mlist_2 = lst[mid + 1: mid + mlist_2_size + 1]

		i, j, k = 0, 0, start
		while i < mlist_1_size and j < mlist_2_size:
			if mlist_1[i] > mlist_2[j]:
				lst[k] = mlist_2[j]
				j += 1
			else:
				lst[k] = mlist_1[i]
				i += 1
			k += 1

		if i < mlist_1_size:
			lst[k: k + len(mlist_1[i:])] = mlist_1[i:]

		if j < mlist_2_size:
			lst[k: k + len(mlist_2[j:])] = mlist_2[j:]

		start = start + sub_list_size * 2
	sub_list_size = sub_list_size * 2

print("Output list: {}".format(lst))






			



