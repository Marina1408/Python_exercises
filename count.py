import random

N = int(input("Вкажіть довжину списку\n > "))
l = [random.randint(1,10) for i in range(N)]
print("Input list: {}".format(l))

# insertion sort
for i in range(1, N):
	k = l[i]
	j = i - 1
	while j >= 0 and k < l[j]:
		l[j+1] = l[j]
		j -= 1
	l[j+1] = k

print("Output list: {}".format(l))

items = [l[0]]
count = [1]

for i in range(1, len(l)):
	if l[i] != l[i-1]:
		items.append(l[i])
		count.append(1)
	else:
		count[-1] += 1

for i in range(1, len(count)):
	k = count[i]
	d = items[i]
	j = i - 1
	while j >= 0 and k > count[j]:
		count[j+1] = count[j]
		items[j+1] = items[j]
		j -= 1
	count[j+1] = k
	items[j+1] = d

result = []

for i in range(len(count)):
	for j in range(count[i]):
		result.append(items[i])

print("Result: {}".format(result))