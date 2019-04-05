import random

print('Ця програма згенерую список чисел довжиною N')
N = int(input("Введіть число N\n > "))
numbers = [random.randint(1,10) for i in range(N)]
print("Input list: {}".format(numbers))

for number in numbers[:]:
	if numbers.count(number) >= 2:
		numbers.remove(number)
				
print("Output list: {}".format(numbers))		




