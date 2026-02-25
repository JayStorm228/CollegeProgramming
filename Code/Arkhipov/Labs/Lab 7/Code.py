print(
    """
Вычислите и выведите члены последовательности, значение которых больше порогового
x, x^2/2!, x^3/3!, x^n/n!
Пороговое значение: 0.001
Значение х: 0.2
    """
)
import math as m
import pandas as pd


def Function(X, N):
    return round(X**N / m.factorial(N), 5)


N_Value = 1
X_Value = 0.2
Critical = 0.001
F_Values = []
N_Values = []

while Function(X_Value, N_Value) > Critical:
    F_Values.append(Function(X_Value, N_Value))
    N_Values.append(N_Value)
    N_Value += 1

Table = pd.DataFrame({"N": N_Values, "Значение последовательности": F_Values})
print(Table)
# Сугубо для удобства сохранения
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, "Answer.csv")
Table.to_csv(csv_path, encoding="utf-8", sep=";")
