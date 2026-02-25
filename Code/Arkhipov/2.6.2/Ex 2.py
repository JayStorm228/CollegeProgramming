print(
    """
Эта программа заполняет матрицу случайными элементами в диапазоне от 1 до 40
После чего находит сумму элементов, сумма индексов которых равна 4 
   """  # По сути, ищем побочную диагональ и сумму её элементов
)
import numpy as np

Matrix = np.random.randint(1, 41, (5, 5))
IndexSum = np.sum(np.indices(Matrix.shape), axis=0)
AntiDiag = Matrix[IndexSum == 4]
TotalSum = np.sum(AntiDiag)

print(
    f"""Матрица: \n{Matrix}\n
Элементы: {AntiDiag}
Их Сумма: {TotalSum}
      """
)
