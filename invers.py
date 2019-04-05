import random

N = int(input("Вкажіть довжину списка\n > "))
arr = random.sample(range(1, 100), N)
print("List: {}".format(arr))
inversion = 0
for i in range(0, (N - 1)):
	j = i + 1
	if arr[i] > arr[j]:
		inversion = inversion + 1
print("Кількість інверсій у списку = {}".format(inversion))		
