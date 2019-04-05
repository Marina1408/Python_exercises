def add_prime_number(num, stop):
	if num < 2:
			return False
	while num <= stop:
		is_prime = 1
		for x in range(2, num):
			if num % x == 0:
				is_prime = 0
		if is_prime == 1:
			yield num
		num += 1

			
res = add_prime_number(2, 101)

for num in res:
	print(num) 