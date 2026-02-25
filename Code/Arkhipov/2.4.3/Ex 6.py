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

print(
    """Эта программа находит процент нечётных чисел в случайном списке заданного размера.
      """
)
a = CreateRandomList(UserInput("Введите размер списка: ", int), [1, 40], int)

Even = []
Uneven = []

for w in a:
    if w % 2 == 1:
        Uneven.append(w)
    else:
        Even.append(w)

Uneven_percent = round(len(Uneven) / len(a), 2)

print(
    f"""Исходный список: {a}
Процент нечётных = {Uneven_percent}"""
)
