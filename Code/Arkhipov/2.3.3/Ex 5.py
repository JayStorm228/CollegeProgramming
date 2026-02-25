print('''Эта программа вычисляет сумму всех введённых целых положительных чисел вплоть до первого введённого отричательного числа.
''')
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../Mods')))
from custom_assertions import *

PositiveNumbers = []
a = 1
while True:
    a = UserInput('Введите число: ', int)
    if a < 0:
        break
    elif a > 0:
        PositiveNumbers.append(a)
    else: print('Вы ввели ноль.')
print(f'''Введённые положительные значения: {', '.join(map(str, PositiveNumbers))}
Сумма всех положительных элементов: {sum(PositiveNumbers)}
      ''')