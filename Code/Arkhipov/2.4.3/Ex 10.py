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
    """Эта программа создаёт список случайных значений, в который вы можете вставить целое число.
      После чего список будет отсортирован по возрастанию.
      """
)
a = CreateRandomList(UserInput("Введите размер списка: ", int), [0, 10], int)
print(f"Исходный список: {a}")
Number = UserInput("Введите число, которое хотите вставить в этот список: ", int)
a.append(Number)
print(f"Отсортированный список: {sorted(a)}")
