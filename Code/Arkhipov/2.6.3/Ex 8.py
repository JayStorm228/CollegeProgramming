import numpy as np

Matrix = np.random.randint(1, 51, (5, 5))
print(
    f"""Матрица: \n{Matrix}\n
Главная диагональ: {Matrix.diagonal()}
Побочная диагональ: {np.fliplr(Matrix).diagonal()}
"""
)
