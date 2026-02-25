import numpy as np

Matrix = np.random.randint(-15, 41, (5, 5))
PositiveMean = np.mean(Matrix[Matrix > 0])
Zeros = len(Matrix[Matrix == 0])
print(
    f"""Матрица: \n{Matrix}\n
Среднее положительных: {PositiveMean}
Количество нулей: {Zeros}
      """
)
