print(
    """
Будет создан массив элементов размером 10х10 .
Каждый элемент считается по формуле:
    -5 + 10* r
    * r - случайное значение от 0 до 1 включительно
Вместо положительных элементов появятся единицы
Вместо отрицательных - нули
Программа выведет нижний треугольник этой матрицы.
    """
)
import pandas as pd
import numpy as np
import os

script_dir = os.path.dirname(os.path.abspath(__file__))

Accuracy = None
while Accuracy == None:
    try:
        Accuracy = int(input("Введите точность вычислений:"))
    except ValueError:
        Accuracy = None
        print(f"Ошибка ввода: {Accuracy} не является числом")

Matrix = -5 + 10 * np.random.random((10, 10))

# Для контекстной обработки округления:
# таким образом, мы выведем на экран матрицу с округлёнными значениями
# но исходная матрица останется не тронутой
with np.printoptions(precision=Accuracy, suppress=True):
    print(f"Созданная матрица значений: \n{Matrix}\n")
csv_path = os.path.join(script_dir, "Matrix.csv")
pd.DataFrame(
    np.around(Matrix, Accuracy),
    columns=[f"Col {i}" for i in range(Matrix.shape[1])],
    index=[f"Row {i}" for i in range(Matrix.shape[0])],
).to_csv(csv_path, index=True, encoding="utf-8", sep=";")
Matrix[Matrix > 0] = 1
Matrix[Matrix < 0] = 0
output = np.tril(Matrix)
print(f"Ответ: \n{output}\n")

# для сохранения, не влияет на выполнение задания


csv_path = os.path.join(script_dir, "Answer.csv")
pd.DataFrame(
    output,
    columns=[f"Col {i}" for i in range(output.shape[1])],
    index=[f"Row {i}" for i in range(output.shape[0])],
).to_csv(csv_path, index=True, encoding="utf-8", sep=";")
