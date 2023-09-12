import os
os.system('CLS')#clear для систем Linux

names = ['Вася', 'Петя', 'Коля', 'Зина']
salary = [15000, 25000, 17000, 22000]
allowance = ['10.25%', '10.1%', '20.22%', '17.7%']

def dict_gen(name,prise,procent):
    dictr = {}
    for i in range(len(name)):
        key = name[i]
        value = prise[i] * float(procent[i][:-1])/100
        elem = (key,value)
        dictr.update([elem])
    return dictr

print(dict_gen(names,salary,allowance))