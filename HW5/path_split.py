import os
os.system('CLS')#clear для систем Linux

path_str = 'C:/Users/User/Desktop/Developer/FinalControl/linux.pdf'

def split_path_1(txt):
    path = txt[:txt.rfind("/")]+"/"
    elements = txt.split('/')
    last_elements = elements[-1].split('.')
    itog = (path,last_elements[0],last_elements[1])
    return itog

print(split_path_1(path_str))