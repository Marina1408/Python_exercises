import re

email = input("Input your email, please!\n > ")
sample_email = re.compile('[A-za-z0-9._]*[@][a-z]{2,3}')
check = sample_email.match(email)
if check:
	print('Your email {} is correct.'.format(email))
else:
    print('You inputed incorrect emeil!')
