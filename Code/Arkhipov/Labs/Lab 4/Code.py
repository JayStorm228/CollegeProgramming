import math as m
import numpy as np
import pandas as pd

print(
    """"Эта программа создаёт таблицу значений функции:
    F = Sin^2(x) + Ctg(x)
    При параметрах:
    Начальное значение: 1
    Конечное значения: 5
    Шаг: 0.5"""
)
Accuracy = None
while Accuracy == None:
    Accuracy = input("Введите значение точности: ")
    if "." in Accuracy:  # Чтобы не было ошибок с округлением
        Accuracy = None
        print(
            "Возможно вы вводите дробное число. Эта величина принимает только целые значения"
        )
    else:
        try:
            Accuracy = int(Accuracy)
        except ValueError:
            Accuracy = None
            print(f"{Accuracy} - Не число")
Start, Stop, Step = 1, 5, 0.5
X_Values = np.arange(Start, Stop + Step, Step)


def F(x):
    return m.sin(x) ** 2 + 1 / m.tan(x)


Fx = np.vectorize(F)
F_Values = Fx(X_Values)
Table = pd.DataFrame({"x": X_Values, "F(X)": np.around(F_Values, Accuracy)})
print(Table)
input("\nНажмите ENTER, чтобы выйти.")
