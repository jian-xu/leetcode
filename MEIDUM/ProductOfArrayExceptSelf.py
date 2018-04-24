def func(x):
    total = 1
    count = len(x)
    for num in range(count):
        total = total*x[num]
    for num in range(count):
        temp = total/(x[num])
        z = [temp]
        y = list.append(z)
    return y

x = [1, 2, 3, 4]
print(func(x))