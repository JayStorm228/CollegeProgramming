import numpy as np
import sys
import os

# всё что идёт для принта - для импорта модуля)
current_file = os.path.abspath(__file__)
repo_root = os.path.abspath(os.path.join(current_file, "..", "..", ".."))
mods_path = os.path.join(repo_root, "Mods")
if mods_path not in sys.path:
    sys.path.insert(0, mods_path)
try:
    from custom_assertions import *
except ImportError as e:
    print(f"Модуль custom_assertions не найден: {e}")
    exit()

Matrix = np.random.randint(1, 41, (5, 5))

print(f"Созданная матрица:\n{Matrix}\n")

LowerBound = UserInput("Введите нижний предел диапазона: ", int)
UpperBound = UserInput("Введите верхний предел диапазона: ", int)
mask = (Matrix > LowerBound) & (Matrix < UpperBound)
filtered = np.where(mask, Matrix, 0)

print(f"Значения вне диапазона заменены на 0:\n{filtered}\n")

for i in range(filtered.shape[0]):
    row = filtered[i, :]
    valid_elements = row[row != 0]
    if valid_elements.size > 0:
        mean_val = valid_elements.mean()
        print(f"Среднее арифметическое строки {i+1}: {mean_val}")
    else:
        print(f"В строке {i+1} нет подходящих значений")

input("Нажмите Enter чтобы выйти")
