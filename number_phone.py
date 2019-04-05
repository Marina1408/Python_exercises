import re

number_phone = input("Input your phone number, please!\n > ")
sample_number = re.compile('[(][0-9]{3}[)][0-9]{3}-[0-9]{4}')
check = sample_number.match(number_phone)
if check:
	print('Your phone number {} is correct.'.format(number_phone))
else:
    print('You number_phone is incorrect!\nPlease try again in corect' 
    	  ' format (xxx)xxx-xxxx')