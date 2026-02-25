print(
    """
Постройте таблицу значений и найдите наибольшее значение функции y=f(x)
При изменении х на отрезке [a, b] с шагом h

Y = 3*cos(2x +1 )**2
Отрезок: [-pi, pi] шаг pi/8
"""
)

import math as m
import numpy as np
import pandas as pd

Accuracy = None
while Accuracy == None:
    try:
        Accuracy = int(input("Введите точность вычислений:"))
    except ValueError:
        Accuracy = None
        print(f"Ошибка ввода: {Accuracy} не является корректным числом")

X_Values = np.linspace(-m.pi, m.pi, int((m.pi - (-m.pi)) / (m.pi / 8)) + 1)


def Y(x):
    return 3 * m.cos(2 * x + 1) ** 2


Vector = np.vectorize(Y)
Y_Values = Vector(X_Values)
Max_Idx = np.argmax(Y_Values)
max_x, max_y = X_Values[Max_Idx], Y_Values[Max_Idx]
RoundX, RoundY = np.around(X_Values, Accuracy), np.around(Y_Values, Accuracy)
max_x_rounded, max_y_rounded = np.round(max_x, Accuracy), np.round(max_y, Accuracy)
Table = pd.DataFrame({"x": RoundX, "y": RoundY})
max_row = pd.DataFrame(
    {"x": [max_x_rounded], "y": [max_y_rounded]}, index=["Макс Значения"]
)
Table = pd.concat([Table, max_row])
print(Table)

# для сохранения
import os


script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, "Answer.csv")
Table.to_csv(csv_path, index=True, encoding="utf-8", sep=";")
