import sys
import os

# всё что идёт для принта - для импорта модуля)
current_file = os.path.abspath(__file__)
repo_root = os.path.abspath(os.path.join(current_file, "..", "..", "..", ".."))
mods_path = os.path.join(repo_root, "Mods")
if mods_path not in sys.path:
    sys.path.insert(0, mods_path)
try:
    from custom_assertions import *
except ImportError as e:
    print(f"Модуль custom_assertions не найден: {e}")
    exit()

print(
    """"Эта программа вычисляет кусочно заданную функцию
      z = 1 - e^(xy + ab) # xy > 0
      z = b - min{ax, y} # xy = 0
      z = max{x^3, e^y, ( |ln y^2| )^( 1/2 )} # xy <0
"""
)

import random as r
import math as m

x, a = -1, -4  # r.randint(-10, 10), r.randint(-10, 10)
b, y = -4, -4  # r.randint(-10, 10), r.randint(-10, 10)

Accuracy = UserInput("Введите количество знаков после запятой: ", int)

if x * y > 0:
    Fx = 1 - m.e ** (x * y + a * b)
    StrFx = "1 - e ^ (xy + ab)  # xy > 0"
elif x * y == 0:
    Fx = b - min(a * x, y)
    StrFx = "z = b - min{ax, y} # xy = 0"
elif x * y < 0:
    Fx = max(x**3, m.e**y, abs(m.log(y**2)) ** (1 / 2))
    StrFx = "max{x^3, e^y, ( |ln y^2| )^( 1/2 )} # xy <0"

print(
    f"""
Исходные значения:
    x = {x}
    y = {y}
    a = {a}
    b = {b}
Значение функции z при текущих значениях: {round(Fx, Accuracy)}
Подходящий отрезок кусочно заданной функции: {StrFx}
Точность вычисления: до {Accuracy} знака
"""
)
input("\nНажмите ENTER, чтобы выйти.")
