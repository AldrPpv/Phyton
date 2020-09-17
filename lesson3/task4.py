def my_func(x, y):
    n = 1;
    for i in range(abs(y)):
        n *= x
    return 1 / n

x = float (input("Введите действительное положительное число x: "))
y = int(input("Введите целое отрицательное число y: "))

print(my_func(x, y))
