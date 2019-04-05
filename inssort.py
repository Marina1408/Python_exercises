import random

print('Ця програма згенерую список чисел довжиною N')
N = int(input("Введіть число N\n > "))
arr = random.sample(range(1, 100), N)
print("Input list: {}".format(arr))

# insertion sort
for i in range(1, N):
	k = arr[i]
	j = i - 1
	while j >= 0 and k < arr[j]:
		arr[j+1] = arr[j]
		j -= 1
	arr[j+1] = k
print("Output list: {}".format(arr))
