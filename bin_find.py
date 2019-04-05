import random

n = int(input("Вкажіть довжину списку \n  "))
a = random.sample(range(1, 100), n)
print("Input list: {}".format(a))
# insertion sort
for i in range(1, n):
	k = a[i]
	j = i - 1
	while j >= 0 and k < a[j]:
		a[j+1] = a[j]
		j -= 1
	a[j+1] = k
print("Output list: {}".format(a))
# binary search
number = int(input("Введіть число, яке ви шукаєте зі списку \n  "))
left = 0
right = n
while left <= right:
	middle = left + int(((right - left) / 2))
	if a[middle] == number:
		print('Ваше число знаходиться на позиції {}'.format(middle))
		break
	if a[middle] < number:
		left = middle + 1
	else:
		right = middle - 1

