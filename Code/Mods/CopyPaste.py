import sys
import os
# всё что идёт для принта - для импорта модуля)
current_file = os.path.abspath(__file__) #текущий путь
repo_root = os.path.abspath(os.path.join(current_file, "..", "..", "..")) #Путь от текущей папки в корневую
mods_path = os.path.join(repo_root, "Mods") # Путь к папке с модулями
if mods_path not in sys.path: #Добавление в sys.path
    sys.path.insert(0, mods_path)
try:
    from custom_assertions import *
except ImportError as e:
    print(f"Модуль custom_assertions не найден: {e}")
    exit()

print('''"Эта программа
''')



print(f'''
''')
input('\nНажмите ENTER, чтобы выйти.')