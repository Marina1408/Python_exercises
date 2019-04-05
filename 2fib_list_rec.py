def fib(n):
	"""Recursive list fibonache"""
	if n < 3:
		return 1
	else:
		return fib(n - 1) + fib (n - 2)

print('Ця програма згенерую число Фібоначе з індексом X')
x = int(input("Введіть індекс X\n > "))
print(fib(x))