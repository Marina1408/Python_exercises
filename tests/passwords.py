import re

password_list = str(input(
    "Input your passwords through comma for check, please!\n > ")).split(',')

x1 = re.compile('[a-z]')
x2 = re.compile('[A-Z]')
x3 = re.compile('[0-9]')
x4 = re.compile('[@#+*]')

l = []
i = 0

for password in password_list:
    s1, s2, s3, s4 = 0, 0, 0, 0

    for x in password:

        if x1.match(x):
            s1 += 1
        if x2.match(x):
            s2 += 1
        if x3.match(x):
            s3 += 1
        if x4.match(x):
            s4 += 1

    if s1 == 1 or s1 == 2 and len(password) <= 6:
        if s2 == 1 or s2 == 2:
            if s3 == 1 or s3 == 2:
                if s4 == 1 or s4 == 2:
                    l.append(password)
    else:
        i += 1

l = str(l).replace("'", "").replace("[", "").replace("]", "")
print("Your correct passwords are:\n{}".format(l))

if i == len(password_list):
    print('All your passwords are incorrect!')
