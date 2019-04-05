a = input("Input string\n > ")
b = a.split()
b.sort()
b.append(0)
for i in range(0, len(b) -1):
	if b[i] == b[i + 1]:
		continue
	print(b[i],':',b.count(b[i]))






