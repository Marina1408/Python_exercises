a = int(input("Вкажіть число a \n  "))
b = int(input("Вкажіть число b \n  "))
if a == b:
	print('Числа не можуть бути однаковими')
elif a > b:
	while a > b:
		a = a - b
	print('Найбільший спільний дільник = {}'.format(a))
else:
	while b > a:
			b = b - a
	print('Найбільший спільний дільник = {}'.format(b))
