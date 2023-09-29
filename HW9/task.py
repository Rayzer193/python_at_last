import csv
import os
import json
import os.path
from typing import Callable
from random import randint

os.system('CLS')#clear для систем Linux

def create_csv(file_name: str = 'exemple.csv', min_row: int = 10, max_row: int = 1000, min_value: int = -100,
                    max_value: int = 100):
    count = randint(min_row, max_row)
    params = [[randint(min_value, max_value) for _ in range(3)] for _ in range(count)]
    with open(file_name, 'w', newline='', encoding='utf-8') as file:
        csv_writer = csv.writer(file, dialect='excel')
        csv_writer.writerows(params)

def csv_decor(func: Callable):
    result_dict = {}

    def wrapper(*args):
        if len(args) == 1:
            if os.path.isfile(*args):
                with open(*args, 'r', encoding='utf-8') as file:
                    csv_reader = csv.reader(file, dialect='excel')
                    for line in csv_reader:
                        a, b, c = (list(map(int, line)))
                        if a:
                            result_dict[f'{a=}, {b=}, {c=}'] = func(a, b, c)
        elif len(args) == 3:
            if args[0]:
                result_dict[f'a={args[0]}, b={args[1]}, c={args[2]}'] = func(*args)
        return result_dict

    return wrapper


def json_decor(filename: str = 'itog.json'):
    def decor(func: Callable):
        def wrapper(*args):
            result = func(*args)
            with open(filename, 'w', encoding='utf-8') as file:
                json.dump(result, file, indent=4, ensure_ascii=False)
            return result

        return wrapper

    return decor


@json_decor()
@csv_decor
def solv(a: int, b: int, c: int) -> float | tuple | str:
    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:
        return 'Корней нет'
    elif discriminant == 0:
        return round((-b) / 2 * a, 3)
    return round((-b - discriminant ** 0.5) / 2 * a, 3), round((-b + discriminant ** 0.5) / 2 * a, 3)


if __name__ == '__main__':
    create_csv()
    solv('exemple.csv')