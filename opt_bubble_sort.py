import random

print('Ця програма згенерую список чисел довжиною N')
N = int(input("Введіть число N\n  "))
arr = random.sample(range(1, 100), N)
print("Input list: {}".format(arr))

# bubble sort
for i in range(0, N):
	swapped = 0
	for j in range(0, (N - i - 1)):
		if arr[j] >= arr[j+1]:
			tmp = arr[j]
			arr[j] = arr[j+1]
			arr[j+1] = tmp
			swapped = 1
	if swapped == 0:
		break
			
	
print("Output list: {}".format(arr))