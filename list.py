import random

N = int(input("Вкажіть довжину першого списку \n > "))
a = random.sample(range(1, 100), N)
print("Input list: {}".format(a))
M = int(input("Вкажіть довжину другого списку \n > "))
b = random.sample(range(1, 100), M)
print("Input list: {}".format(b))
c = list()

for number1 in a:
	for number2 in b:
		if number1 == number2:
			c.append(number1)

print("Output list: {}".format(c))
