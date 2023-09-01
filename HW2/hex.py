import os
os.system('CLS')#clear для систем Linux

num = input("Введите число: ")

def valid(n):
    if n.isdigit() == True:
        return True
    else:
        return False

def hex_exm(l,k):
    a1 = "0x"+str(l)
    a2 = hex(k)
    if a1 == a2:
        print(f"Перевод произведен удачно.Программа посчитала '{a1}' а функция 'hex' выдала '{a2}'")
        return True
    else:
        print(f"Что-то пошло не так. Программа посчитала '{a1}' а функция 'hex' выдала '{a2}'")
        return False
        
f = 1
while f > 0:
    if valid(num) == True:
        xx = int(num)
        num=int(num)
        s = ''
        h = '0123456789abcdef'
        
        while num > 0:
            s = h[num % 16] + s
            num = num // 16
        f = 0
        if(hex_exm(s,xx)):
            print("Число в шестнадцатеричной системе:",s)
        else:
            print(f"Число {s} не является шестнадцатеричным представлением числа {xx}")
    else:
        print("Необходимо ввести число")
        num = input("Введите число: ")

