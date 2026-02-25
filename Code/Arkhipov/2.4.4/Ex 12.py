print(
    """Эта программа считает количество знакопеременных пар
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

Size = UserInput("Размер массива: ", int)
Array = CreateRandomList(Size, [-2, 2], int)
count = 0
for w in range(len(Array) - 1):
    Expression1 = Array[w] > 0 and Array[w + 1] < 0  # + -
    Expression2 = Array[w] < 0 and Array[w + 1] > 0  # - +
    if Expression1 or Expression2:
        count += 1

print(
    f"""Созданныйй массив: {Array}
Количество знакочередующихся пар: {count}
"""
)


input("Нажмите ENTER, чтобы выйти.")
