print('Ця програма згенерую список чисел Фібоначе до заданого числа N')
N = int(input("Введіть число N\n > "))
a = 0
print(a)
b = 1
print(b)
c = a + b

while b < N:
    
    c = a + b
    if c < N or c == N:
        print (c)
    a = b
    b = c

    
   
