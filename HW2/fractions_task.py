from fractions import Fraction

import os
os.system('CLS')#clear для систем Linux


def valid_fraction(n):
    if("/" in n):
        l = n.split("/")
        if l[0].isdigit() == True and  l[1].isdigit() == True:
            return True
        else:
            return False
    else:
        return False
    
def fraction_reduction(ch,zn):
    for i in range(2,zn+1):
        if (ch % i == 0 and zn % i == 0):
            ch = ch/i
            zn = zn/i

    return(str(int(ch))+"/"+str(int(zn)))

def frac_exm(l,k):
    a1 = "0x"+str(l)
    a2 = hex(k)
    if a1 == a2:
        print(f"Перевод произведен удачно.Программа посчитала '{a1}' а функция 'hex' выдала '{a2}'")
        return True
    else:
        print(f"Что-то пошло не так. Программа посчитала '{a1}' а функция 'hex' выдала '{a2}'")
        return False

def hex_exm(l,k,s,m):
    summ = s
    multl = m
    a = Fraction(l)
    b = Fraction(k)
    if str((a+b)) == str(summ) and str(a*b) == str(multl):
        print(f"Перевод произведен удачно. Программа насчитала '{summ}' и '{multl}', а функция 'Fraction' выдала '{a+b}' и '{a*b}'")
        return True
    else:
        print(f"Что-то пошло не так.Программа насчитала a+b='{summ}' и a*b='{multl}', а функция 'Fraction' выдала a+b='{a+b}' и a*b='{a*b}'")
        return False


flag = 0

while flag == 0:
    print("Вводить дроби необходимо в виде N/N")
    a1  = input("Введите первую дробь: ")
    a2 = input("Введите вторую дробь: ")
    if(valid_fraction(a1) and valid_fraction(a2)):
        print("Оба числа дроби\n")
        a1_dr = a1.split("/")
        a2_dr = a2.split("/")
        ch_dr_sum = (int(a1_dr[0])*int(a2_dr[1]))+(int(a2_dr[0])*int(a1_dr[1]))
        zn_dr_sum = int(a2_dr[1])*int(a1_dr[1])
        ch_dr_mult = int(a2_dr[0])*int(a1_dr[0])
        zn_dr_mult = int(a2_dr[1])*int(a1_dr[1])
        sum = fraction_reduction(ch_dr_sum,zn_dr_sum)
        mult= fraction_reduction(ch_dr_mult,zn_dr_mult)
        print("Сумма дробей равна :" ,sum)
        print("Произведение дробей равно :" ,mult,"\n")
        hex_exm(a1,a2,sum,mult)
        flag = 1

    else:
        print("Одно или оба введеных числа не являтся дробью\n")



