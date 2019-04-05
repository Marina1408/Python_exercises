a = input("Input string\n > ")
b = a.split()
b.sort()
print(b)
c = []
for items in b:
	print(items,':',b.count(items))
	r = items,':',b.count(items)
	c.append(r)
for items in c[:]:
	if c.count(items) >= 2:
		c.remove(items)
print(c)







