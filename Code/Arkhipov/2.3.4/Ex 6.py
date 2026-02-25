print('''Эта программа вычисляет сумму всех введённых не равных нулю чисел
''')
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../Mods')))
from custom_assertions import *

AllNumbers = []
a = None
while True:
    a = UserInput('Введите число: ', float)
    if a == 0:
        print('Вы ввели ноль! Ввод чисел завершён')
        break
    else: AllNumbers.append(a)
print(f'''Введённые числа: {', '.join(map(str, AllNumbers))}
Их сумма: {sum(AllNumbers)}
      ''')