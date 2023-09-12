import os
os.system('CLS')#clear для систем Linux

def simple_exm(num):
    chis = 2
    while chis ** 2 < num and num % chis != 0:
        chis += 1
    return chis ** 2 > num


def simple_generator(num):
    start = 1
    while num > 1:
        start += 1
        num -= 1
        if simple_exm(start):
            yield start

print(*simple_generator(100))