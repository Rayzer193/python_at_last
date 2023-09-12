import os
os.system('CLS')#clear для систем Linux

s = int(input("Сколько чисел Фибаначи получить: "))

def fibonacci(num):
    first, second = 0, 1
    c = 1
    while c <= num:
        c += 1
        yield first
        first, second = second, first + second

print(*fibonacci(s))
