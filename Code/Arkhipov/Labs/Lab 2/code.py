# x < 1,3
# x = 1,3
# x > 1,3

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
    """Эта программа находит значение кусочно заданной функции:
    y = pi * (x**2) - (7 / (x**2)) # x < 1,3
    y = a * (x**3) + 7 * (x ** (1 / 2)) # x = 1,3
    y = ln(x + 7 * (x ** (1 / 2))) # x > 1,3
"""
)

import math as m

a = UserInput("Введите значение а: ", float)
x = UserInput("Введите значение х: ", float)

if x < 1.3:
    Fx = m.pi * (x**2) - (7 / (x**2))
    print(f"f(x) = {Fx}")
elif x == 1.3:
    Fx = a * (x**3) + 7 * (x ** (1 / 2))
    print(f"f(x) = {Fx}")
elif x > 1.3:
    Fx = m.log(x + 7 * (x ** (1 / 2)))
    print(f"f(x) = {Fx}")
