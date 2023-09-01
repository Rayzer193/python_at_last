import os
os.system('CLS')#clear для систем Linux

def valid(n):
    if n.isdigit() == True:
        return True
    else:
        return False
    
def isfloat(n):
    try:
        float(n)
        return True
    except ValueError:
        return False
    

res = input("Введите данные: ")

if valid(res) == True:
    print(f"Вы ввели число {res}")
elif isfloat(res) == True:
    print(f"Вы ввели дробное число {res}")
else:
    print(f"Вы ввели текст '{res}'")
