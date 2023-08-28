import os
os.system('CLS')#clear для систем Linux

def valid(n):
    if n.isdigit() == True and 1 <= int(n) <= 100000:
        return True
    else:
        return False

num = input("Введите число: ")
f = 1
while f > 0:
    if valid(num) == True:
        c = 0
        for i in range(2, int(num) // 2+1):
            if (int(num) % i == 0):
                c = c+1
        if (c <= 0):
            print("Число простое")
            f = 1
            break
        else:
            print("Число не является простым")
            f = 1
            break
    else:
        print("Необходимо ввести число от 1 до 100000")
        num = input("Введите число: ")