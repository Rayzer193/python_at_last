import os
os.system('CLS')#clear для систем Linux

print("Таблица умножения")
for i in range(2,11):
    print()
    for j in range(2,6):
        print(j,"*",i,"=",i*j,end = "   ")
print()
for i in range(2,11):
    print()
    for j in range(6,10):
        print(j,"*",i,"=",i*j,end = "   ")