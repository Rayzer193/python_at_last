import os
os.system('CLS')#clear для систем Linux
from collections import Counter
print("---НОВАЯ ПРОГРАММА---")
people = {"Вася":("Палатка", "Вода", "Еда", "Инструменты"),"Юра":("Одежда","Вода", "Дрова",),
          "Петя":("Палатка", "Одежда", "Еда", "Вода")}
#Общие списки
keys_list=[]
value_list = []
all_things = {}
diff = []

for key in people.keys():
    keys_list.append(key)   

for value in people.values():
    value_list.append(value)  

for l in range(len(keys_list)):
    all_things = set(all_things).union((set(people[keys_list[l]])))

#Предмет который есть у всех
itog1 = all_things
for i in range(len(keys_list)):
    itog1 = itog1.intersection(value_list[i])

print(f"У всех друзей есть предмет(ы): ",end = "")
for m in itog1:  
    print(m, end = " ")

#Уникальные предметы
for k in range(len(keys_list)):
    for g in range(len((people[keys_list[k]]))):
        diff.append(people[keys_list[k]][g])
c = Counter(diff)
res1 = list(filter(lambda x: c[x] == 1, diff))
print(f"\nТолько у одного друга есть предмет(ы): ",end = "")
for m in res1:  
    print(m, end = " ")

#У всех кроме одного
diff = []
dl = len(keys_list)-1
for k in range(len(keys_list)):
    for g in range(len((people[keys_list[k]]))):
        diff.append(people[keys_list[k]][g])
c = Counter(diff)
res2 = list(filter(lambda x: c[x] == dl, diff))
res2 = set(res2)
print(f"\nУ всех кроме одного есть предметы: ",end = "")
for m in res2:  
    print(m, end = " ")

people_without = []
res2 = list(res2)
for key in people.keys():
    for p in range(len(res2)):

        if res2[p] not in people[key]:
            s = str(key)
            people_without.append(s)
        else:  
            {}
people_without = set(people_without)
print(f".Имена этих людей: ",end = "")
for m in people_without:  
    print(m, end = " ")