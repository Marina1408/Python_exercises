l_x = []
l_y = []

for i in range(4):
    try:
        x, y = map(int, input('Please input the number of rows and '
                              'columns separated by a comma\n').split(','))
    except ValueError:
        print("You've entered an incorrect format of numbers!\n"
              "Try again!")
        break
    l_x.append(x)
    l_y.append(y)

for n in range(4):
    r = 1
    arr = []
    try:
        for i in range(l_x[n]):
            arr.append([])
            for j in range(l_y[n]):
                arr[i].append(r)
                r += 1
    except IndexError:
        print("Error!")
        break
    print(arr)
