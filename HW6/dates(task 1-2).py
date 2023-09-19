import os
os.system('CLS')#clear для систем Linux

mounthes = {"01": 31,"02": [28, 29],"03": 31,"04": 30,"05": 31,"06": 30,"07": 31,"08": 31,"09": 30,"10": 31,"11": 30,"12": 31}#верхняя граница по месяцам

def check_vysok_year(year: int) -> bool:#проверка на високосный год
    if not year % 400:
        return True
    elif year % 4 == 0 and year % 100 != 0:
        return True
    return False

def check_date(input_date: str) -> bool:#проверка даты на возможность
    date_ls = input_date.split('.')
    if date_ls[1] in mounthes.keys() and 1 <= int(date_ls[2]) <= 9999:
        if date_ls[1] != '02':
            return 1 <= int(date_ls[0]) <= mounthes.get(date_ls[1])
        else:
            if check_vysok_year(int(date_ls[2])):
                return 1 <= int(date_ls[0]) <= mounthes['02'][1]
            else:
                return 1 <= int(date_ls[0]) <= mounthes['02'][0]
    return False

def valid(n):#функция для проверки формата ввода
    if n.isdigit() == True and 1 <= int(n) <= 10000 and len(n) == 10:
        return True
    else:
        return False


start_date = input("Введите дату в формате DD.MM.YYYY: ")

strdatelist = start_date.split('.')
check = []

for i in range(len(strdatelist)):
    if valid(strdatelist[i]):
        check.append('1')
    else:
        check.append('0')

if '0' in check:
    print("Не верный формат ввода")
else:
    print(f"Введена дата:{start_date}\nДата существует:{check_date(start_date)}")