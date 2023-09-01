import os
import typing
os.system('CLS')#clear для систем Linux

a = 3
b = 3.12
c = "text"
ls = [a,b,c]

print(type(a),type(b),type(c),type(ls))
print(id(a),id(b),id(c),id(ls))
print(hash(a),hash(b),hash(c))
# print(hash(ls))

a: int | float = 3
b: float = 42.0
a = a/b
print(a.__doc__)
print("sdasdasd".upper())
print("sdasdasd".count("s"))

print(dir(a))
# help(int(a))

help()