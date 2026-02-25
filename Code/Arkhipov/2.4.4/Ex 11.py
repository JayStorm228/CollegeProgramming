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

Array = CreateList(UserInput("Введите размер списка: ", int), float)
for w in range(3):
    Array.remove(0)
print(f"Изменённый список: {Array}")

input("Нажмите ENTER, чтобы выйти.")
