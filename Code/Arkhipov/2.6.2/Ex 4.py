import numpy as np

print(
    """
В матрице 5х5 случайных значений от 1 до 81 найдите чётные элементы и выведите их как список
      """
)

Matrix = np.random.randint(1, 81, (5, 5))
Even = Matrix[Matrix % 2 == 0].tolist()
print(
    f"""Матрица: \n{Matrix}\n
Чётные элементы: {Even}
      """
)
