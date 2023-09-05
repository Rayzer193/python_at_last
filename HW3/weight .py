import os
os.system('CLS')#clear для систем Linux

things = {"Палатка":5, "Вода":2, "Еда":2, "Одежда":3, "Аптечка":1, "Дрова": 4, "Инструменты":3}
max_w = 8

things_with = []
for key, value in things.items():
    if value <= max_w:
        things_with.append(key)
        max_w -= value

print(things_with)
