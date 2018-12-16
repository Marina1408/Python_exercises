import random
print('Привіт! Ця програма призначена для вгадування числа')
number_user = int(input("Введіть число\n > "))

number = random.randint(1,100)

while number_user != number:

	if number_user > number:
		print('Введене число є більшим за те, яке потрібно вгадати')
		number_user = int(input("Введіть число\n > "))
	else:
		print('Введене число є меншим за те, яке потрібно вгадати')
		number_user = int(input("Введіть число\n > ")) 

print('Ура!!! Ви вгадали число!!!')
