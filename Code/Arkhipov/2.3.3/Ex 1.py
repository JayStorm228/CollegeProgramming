print(
    """Эта программа находит максимальное значение функции на заданном промежутке [a, b] с шагом h
Функция: y = (cos x)/(sin x)
      """
)
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

import math as m

a = UserInput("Введите значение a: ", int)
b = UserInput("Введите значение b: ", int)
h = UserInput("Введите значение h: ", int)
output = []

for w in range(a, b + 1, h):
    output.append(m.cos(w) / m.sin(w))
print(
    f"Максимальное значение на промежутке: [{a}, {b}] c шагом {h}: {round(max(output), 2)}"
)
