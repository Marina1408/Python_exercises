def add_fib_number(stop):
	num1, num2 = 0, 1
	fib_num = num1 + num2
	print(num1)
	print(num2)
	print(fib_num)
	while fib_num <= stop:
		num1, num2 = num2, fib_num
		fib_num = num1 + num2
		if fib_num <= stop:
			yield fib_num
		
			
res = add_fib_number(100)

for num in res:
	print(num) 