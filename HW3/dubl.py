import os
os.system('CLS')#clear для систем Linux

list1 = [1, 2, 2, 3, 4, 4, 4, 4, 5, 6, 6]
itog = []

for i in range(len(list1)):
    a = list1[i]
    if list1.count(a) > 1:
        itog.append(list1[i])
    else:
        {}

itog = set(itog)

print(f"Начлальный список: {list1} \nТолько повторы: {itog}")