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

print('''"Эта программа генерирует список случайных элементов и выводит на экран среднее арифметическое квадратов положительных чисел
''')
Size = UserInput('Введите размер массива: ', int)
Array = CreateRandomList(Size, [-20, 40], int)
PosNumsSqr = []

for w in Array:
    if w > 0:
        PosNumsSqr.append(w**2)
print(f'''Исходный список: {Array}
Список среднего значения квадратов положительных элементов: {round(sum(PosNumsSqr)/len(PosNumsSqr), 2)}
      ''')
input('\nНажмите ENTER, чтобы выйти.')