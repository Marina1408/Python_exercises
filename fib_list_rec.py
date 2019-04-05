def fib(n):
	"""Recursive list fibonache"""
	result = []
	a, b = 0, 1
	while b < n:
		result.append(b)
		a, b = b, b + a
	return result

print('Ця програма згенерую список чисел Фібоначе до заданого числа X')
x = int(input("Введіть число N\n > "))
print(fib(x))