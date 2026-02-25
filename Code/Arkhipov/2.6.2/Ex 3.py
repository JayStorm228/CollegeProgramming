import numpy as np

print(
    """
    Программа создаёт матрицу 5х5, и заполняет её случайными элементами от 1 до 40
    После чего находит максимальный элемент побочной диагонали
"""
)
Matrix = np.random.randint(1, 41, (5, 5))
AntiDiag = np.fliplr(Matrix).diagonal()
Max = np.max(AntiDiag)
print(
    f"""Матрица \n{Matrix}\n
Побочная диагональ: {AntiDiag}
Максимальный элемент диагонали: {Max}
      """
)
