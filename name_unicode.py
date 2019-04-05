name = input("Введіть своє ім'я \n > ")
u_name = ''
for letter in name:
	u_name = u_name + str(ord(letter))
print(u_name)
print(bin(int(u_name)))