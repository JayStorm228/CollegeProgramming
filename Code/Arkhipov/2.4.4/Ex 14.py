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
print('''Эта программа формирует два массива, которые содержат индексы положительных и отрицательных элементов
      Исходный массив генерируется случайно/
''')

Array = CreateRandomList(10, [-10, 10], int)
NegID = []
PosID = []

for w in Array:
    if w>0:
        PosID.append(Array.index(w))
    elif w<0:
        NegID.append(Array.index(w))
print(f'''Сгенерированный массив: {Array}
Индексы положительных элементов: {PosID}
Индексы отрицательных элементов: {NegID}
      ''')
input('\nНажмите ENTER, чтобы выйти.')