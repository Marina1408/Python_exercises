import random

print('Ця програма згенерую список чисел довжиною N')
N = int(input("Введіть число N\n > "))
a = random.sample(range(1, 100), N)
print("Input list: {}".format(a))

# choice sort
for i in range(0, N):
	min = i
	for j in range((i + 1), N):
		if a[min] > a[j]:
			min = j
	tmp = a[i]			
	a[i] = a[min]
	a[min] = tmp
	
print("Output list: {}".format(a))
