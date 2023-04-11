#№1
a, n = 1, 3.14  
while a ** 0.5 <= n:
    if a ** 0.5 < 3.14:
        print(f"{a ** 0.5} ({a})")
    a += 1
#№2 
a, b = int(input()), int(input())     
while a < b:
    a += 1
    print(a)
#№3 
a, b = int(input()), int(input())     
while a < b:
    b -= 1
    print(b)
#№4
n, a = int(input()), 1
while a * 3 < n:
    a += 1
print(a, a * 3)
#№5
n, a = int(input()), 1
while a * 3 < n:
    a += 1
if a * 3 > n:
    print(a - 1)
else:
    print(a)