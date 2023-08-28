import os
os.system('CLS')#clear для систем Linux

print("Стороны треугольники")
a = int(input("Введите первую сторону (A): "))
b = int(input("Введите вторую сторону (B): "))
c = int(input("Введите третью сторону (C): "))
if(a + b < c or a + c < b or b + c < a):
    print("Треугольника не существует")
elif(a == b ==c):
    print("Треугольник равносторонний")
elif(a == b or a == c or b == c):
    print("Треугольник равнобедренный")
elif(a*a+b*b==c*c or a*a+c*c==b*b or c*c+b*b==a*a):
    print("Треугольник прямоугольный")
else:
    print("Треугольник существует")