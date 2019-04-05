def factorial(x):
	"""x!"""
	if x <= 0:
		return 1
	else:
		return x * factorial(x - 1)

n = int(input("Вкажіть факторіал якого числа шукати \n  "))
print(factorial(n))

