import os
from random import randint as ri
#примечание: на отработку кода уходит 3-4 минуты
os.system('CLS')#clear для систем Linux

N = 8

def check_position(position: list[tuple]) -> bool:
    for i in range(len(position)):
        for j in range(i + 1, len(position)):
            if position[i][0] == position[j][0] or position[i][1] == position[j][1] or abs(position[i][0] - position[j][0]) == abs(position[i][1] - position[j][1]):
                return False
    return True


def get_good_position(n: int, m: int) -> list[list]:
    itog = []
    while len(itog) < m:
        random_position = [(ri(1, 8), ri(1, 8)) for _ in range(n)]
        if check_position(random_position):
            itog.append(random_position)
    return itog

queens_pos_1 = [(1, 3), (2, 4), (3, 5), (4, 7), (5, 1), (6, 2), (7, 5), (8, 6)]  # Неверные позиции
queens_pos_2 = [(1, 1), (2, 5), (3, 8), (4, 6), (5, 3), (6, 7), (7, 2), (8, 4)]  # Корректные позиции
print(check_position(queens_pos_1))
print(check_position(queens_pos_2))

for key, item in enumerate(get_good_position(N, 1), 1):
    print(f'{key}.', *item)