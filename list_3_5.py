N = int(input("Введіть число, до якого генерувати список \n  "))
if N < 5:
	print('Введіть число більше рівне 5')

lst = []
a = 5
i = 1
while a <= N:
	if i % 2 != 0:
		if a % 5 == 0:
			lst.append(a)
			i += 1
	else:
		if a % 3 == 0:
			lst.append(a)
			i += 1
	a += 1

print("Output list: {}".format(lst))


