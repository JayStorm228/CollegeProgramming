import random


def print_matrix(matrix, title=""):
    if title:
        print(title)
    for row in matrix:
        print(" ".join(f"{x:7.2f}" for x in row))


size = 8

K = [[-15 + 30 * random.random() for _ in range(size)] for _ in range(size)]

print_matrix(K, "Сгенерированная матрица K:")

max_abs_val = abs(K[0][0])
max_row, max_col = 0, 0

for i in range(size):
    for j in range(size):
        if abs(K[i][j]) > max_abs_val:
            max_abs_val = abs(K[i][j])
            max_row, max_col = i, j

print(
    f"""Самый большой элемент по модулю: {K[max_row][max_col]:.2f}
Найден в строке: {max_row}, в столбце: {max_col}"""
)

L = [
    [K[i][j] for j in range(size) if j != max_col] for i in range(size) if i != max_row
]

print_matrix(L, "Матрица L после удаления строки и столбца:")
