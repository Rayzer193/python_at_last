from abc import ABC, abstractmethod
import os
os.system('CLS')#clear для систем Linux

class Pet(ABC):
    def __init__(self, name: str, age: int):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    @abstractmethod
    def get_unique_property(self):
        """Уникальное свойство"""


class Cat(Pet):
    __type_animal = 'Кошка'

    def __init__(self, name, age, unique_property='Мягкое и пушистое'):
        super().__init__(name, age)
        self.__unique_property = unique_property

    @classmethod
    def get_type(cls):
        return cls.__type_animal

    def get_unique_property(self):
        return self.__unique_property


class Dog(Pet):
    __type_animal = 'Собака'

    def __init__(self, name, age, unique_property='Энергичное и доброе'):
        super().__init__(name, age)
        self.__unique_property = unique_property

    @classmethod
    def get_type(cls):
        return cls.__type_animal

    def get_unique_property(self):
        return self.__unique_property


class Hamster(Pet):
    __type_animal = 'Хомячок'

    def __init__(self, name, age, unique_property='Быстрый и мертвый'):
        super().__init__(name, age)
        self.__unique_property = unique_property

    @classmethod
    def get_type(cls):
        return cls.__type_animal

    def get_unique_property(self):
        return self.__unique_property


class CreateAnimal:
    __all_animal = [Dog, Cat, Hamster]

    def __init__(self, type_animal: str, name: str, age: int, unique_property=None):
        if type_animal.title() in [item.get_type() for item in self.__all_animal]:
            for item in self.__all_animal:
                if type_animal.title() == item.get_type():
                    if unique_property is not None:
                        self.pet = item(name, age, unique_property)
                    else:
                        self.pet = item(name, age)
        else:
            raise ValueError

Type = int(input("Выберите тип животного\n1.Кошка\n2.Собака\n3.Хомячок\nУкажите номер: "))
Name = input("Напишите кличку питомцу:")
Age = int(input("Сколько лет вашему питомцу:"))
Types = {1:'Кошка',2:'Собака',3:'Хомячок'}
my_pet = CreateAnimal(Types[Type], Name, Age)
print('\n','Тип:', my_pet.pet.get_type(),'\n','Имя:', my_pet.pet.get_name(),'\n','Возраст:', my_pet.pet.get_age(),'\n','Свойство:', my_pet.pet.get_unique_property())
