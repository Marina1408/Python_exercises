import random

print('Ця програма згенерую список чисел довжиною N')
N = int(input("Введіть число N\n  "))
arr = random.sample(range(1, 100), N)
print("Input list: {}".format(arr))

# bubble sort
for i in range(0, N):
	for j in range(0, (N - 1)):
		if arr[j] % 2 == 0 and arr[j+1] % 2 == 0:
			if arr[j] >= arr[j+1]:
				tmp = arr[j]
				arr[j] = arr[j+1]
				arr[j+1] = tmp
		elif arr[j] % 2 != 0 and arr[j+1] % 2 == 0:
			tmp = arr[j]
			arr[j] = arr[j+1]
			arr[j+1] = tmp
		else:
			if arr[j] % 2 != 0 and arr[j+1] % 2 != 0:
				if arr[j] >= arr[j+1]:
				    tmp = arr[j]
				    arr[j] = arr[j+1]
				    arr[j+1] = tmp
		
print("Output list: {}".format(arr))