import numpy as np

print(
    """"Эта программа
"""
)

import numpy as np

Matrix = np.random.randint(1, 21, (5, 5))
MainDiag = []
LowerDiag = []

for w in range(Matrix.shape[0]):
    MainDiag_elements = (int(x) for x in Matrix.diagonal(offset=w))
    MainDiag.extend(MainDiag_elements)

for w in range(1, Matrix.shape[0]):
    LowerDiag_elements = (int(x) for x in Matrix.diagonal(offset=-w))
    LowerDiag.extend(LowerDiag_elements)

print(
    f"""Матрица:\n{Matrix}\n
Элементы главной диагонали и выше: {MainDiag}
Элементы ниже главной диагонали: {LowerDiag}"""
)
input("\nНажмите ENTER, чтобы выйти.")
