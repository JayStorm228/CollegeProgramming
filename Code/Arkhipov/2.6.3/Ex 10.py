import numpy as np

Matrix = Matrix = np.random.randint(1, 41, (5, 5))
print(
    f"""Матрица: \n{Matrix}\n
Главная диагональ: {Matrix.diagonal()}
Параллельная диагональ ниже главной: {Matrix.diagonal(offset=-1)},
сумма её элементов: {Matrix.diagonal(offset=-1).sum()}

Побочная диагональ: {np.fliplr(Matrix).diagonal()}
Параллельная диагональ ниже побочной: {np.fliplr(Matrix).diagonal(offset=-1)}, 
сумма её элементов: {np.fliplr(Matrix).diagonal(offset=-1).sum()}"""
)
