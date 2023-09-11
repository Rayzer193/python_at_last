import os
os.system('CLS')#clear для систем Linux

start_matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
itog_matrix = []

def matrix_trans(matrix: list[list[int]]) -> list[list[int]]:
    itog_matrix = [[0 for _ in range(len(matrix))] for _ in range(len(matrix[0]))]
    for i in range (len(matrix)):
        for j in range (len(matrix[i])):
            itog_matrix[j][i] = matrix [i][j]
    return itog_matrix

def print_matrix(text: str, matrix: list[list[int]]) -> None:
    print(text)
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j],end = "\t")
        print()
    print()

print_matrix("Изначальная матрица: ",start_matrix)
print_matrix("Транспонированная матрица: ", matrix_trans(start_matrix))