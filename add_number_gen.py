def add_number(num, stop):
	while num <= stop:
		yield num
		num +=5

res = add_number(0, 100)

for num in res:
	print(num)
    






