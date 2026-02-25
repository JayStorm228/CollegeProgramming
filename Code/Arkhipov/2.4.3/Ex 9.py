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
    """Эта программа создаёт список случайных значений, после чего меняет местами первое и максимальное значение.
      """
)
a = CreateRandomList(UserInput("Введите размер списка: ", int), [1, 30], int)
print(f"Исходный список: {a}")
first = a[0]
Max = max(a)
Max_index = a.index(Max)
a[0] = Max
a[Max_index] = first

print(f"Отсортированный список: {a}")
