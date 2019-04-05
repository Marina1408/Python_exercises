import random

n = int(input("Вкажіть довжину кінцевого списку чисел Фібоначе n\n  "))
N = n * 5
arr1 = []
a = 0
arr1.append(a)
b = 1
arr1.append(b)
c = a + b
while len(arr1) <= N:
    c = a + b
    arr1.append(c)
    a = b
    b = c
print("List1: {}".format(arr1))
arr2 = random.sample(arr1, n)
print("List2: {}".format(arr2))
# insertion sort
for i in range(1, n):
	k = arr2[i]
	j = i - 1
	while j >= 0 and k < arr2[j]:
		arr2[j+1] = arr2[j]
		j -= 1
	arr2[j+1] = k
print("Output list: {}".format(arr2))