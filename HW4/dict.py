import os
os.system('CLS')#clear для систем Linux

def dictionary(**elements) -> dict[object,object]:
    re_dict = {}
    for key,value in elements.items():
        if isinstance(value, (int, float, str, tuple, frozenset)):
            re_dict.setdefault(value,key)
        else:
            re_dict.setdefault(str(value),key)
    return re_dict

print(dictionary(apple = 5, soup = "суп", ls = [1,5,7,9], tt = (1,3,5), shelk = {1:'!',2:"@",3:"#"}, pi = 3.14, pp = [10,9,8,7]))
