#№1
for i in range(10, 23):
    print(i * 2.54)

#№2
a = float(input("Введите значение текущего курса: "))
for i in range(1, 21):
    print(i * a)

#№3
a = int(input("Введите цифру, степени которой хотите вычислить: "))
for i in range(1, 21):
    print(a ** i)

#№4
for i in range(21):
    print(1.1 + i)

#№5
for i in range(1, 10):
    print(2 + i / 10)

#№6
for i in range(10):
    print(2 * i)

#№7
for i in range(1, 16):
    print(-1 + 2 * i)

#№8
for i in range(2, 21, 2):
    print(i ** 0.5)

#№9
a = int(input("Цена за 1 кг конфет: "))
for i in range(2, 11):
    print(f"Цена за {i} кг = {i * a}")

#№10
for i in range(int(input("Введите точку начала отрезка(a): ")), int(input("Введите точку конца отрезка(b): ")) + 1):
    print(f"y = {i ** 0.5}")
