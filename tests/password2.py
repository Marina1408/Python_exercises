import re

password_list = str(input(
	"Input your passwords through comma for check, please!\n > ")).split(',')

sample_password = re.compile('([a-z]{1,2}[0-9]{1,2}[A-Z]{1,2}[@#+*]{1,2})|'
                             '([A-Z]{1,2}[a-z]{1,2}[0-9]{1,2}[@#+*]{1,2})|'
                             '([0-9]{1,2}[A-Z]{1,2}[@#+*]{1,2}[a-z]{1,2})|'
                             '([a-z]{1,2}[@#+*]{1,2}[A-Z]{1,2}[0-9]{1,2})')

i = 0
l = []

for password in password_list:
	check = sample_password.match(password)
	if check and len(password) <= 6:
		l.append(password)
	else:
		i += 1

print("Your correct passwords:\n{}".format(l))

if i == len(password_list):
	print('All your passwords are incorrect!')
