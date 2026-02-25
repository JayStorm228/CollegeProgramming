print(
    """Эта программа создаёт матрицу 5х5 со значениями от 1 до 40
После чего находит номера строк максимального элемента в каждой строке
"""
)
import numpy as np

Matrix = np.random.randint(1, 41, (5, 5))
output = np.argmax(Matrix, axis=0)


print(
    f"""Матрица: \n{Matrix}\n
Индекс максимального элемента каждой строки: {', '.join(map(str, output))}
"""
)
input("\nНажмите ENTER, чтобы выйти.")
