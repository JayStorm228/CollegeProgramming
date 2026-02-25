print(
    """
Вычислите значения z, соответствующие каждому значению х
хn <= x <= xk, шаг изменения равен dx
        | (x**3 + ax)**(1/4)
    z = | ------------------
        | ln( ( a**7 + x**(1/2) )**(1/2)  )
Задача: Определить среднее арифметическое значений z
Контрольные значения:
    a = 5.27
    xn = 1, xk = 10, dx = 1
        """
)

import math as m, numpy as np, pandas as pd

Accuracy = None
while Accuracy == None:
    try:
        Accuracy = int(input("Введите точность вычислений:"))
    except ValueError:
        Accuracy = None
        print(f"Ошибка ввода: {Accuracy} не является числом")

a, Xn, Xk, dx = 5.27, 1, 10, 1
N_Values = int((Xk - Xn) / dx) + 1
X_Values = np.linspace(Xn, Xk, N_Values)


def Z(x):
    Num = (x**3 + a * x) ** (1 / 4)
    Den = (a**7 + x ** (1 / 2)) ** (1 / 2)
    return Num / Den


z = np.vectorize(Z)
Z_Values = z(X_Values)
Z_Mean = np.around(np.mean(Z_Values), Accuracy)
RoundedX, RoundedZ = np.around(X_Values, Accuracy), np.around(Z_Values, Accuracy)
Table = pd.DataFrame({"X": RoundedX, "Z": RoundedZ})
print(
    f"""a = {a}; Xn = {Xn}; Xk = {Xk}, dx = {dx}
Таблица значений: \n{Table}\n
Среднее значение функции z: {Z_Mean}"""
)
# для сохранения
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, "Answer.csv")
Table.to_csv(csv_path, encoding="utf-8", sep=";")
