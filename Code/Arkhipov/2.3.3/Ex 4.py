print('''Эта программа вычисляет сумму всех положительных и сумму всех отрицательных значений в введённой последовательности.
      Введите 0, чтобы закончить ввод
''')
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../Mods')))
from custom_assertions import *

a = None
PositiveNumbers = []
NegativeNumbers = []
AllNumbers = []
while True:
    a = UserInput('Введите число: ',int)
    if a == 0:
        break
    AllNumbers.append(a)
    if a > 0:
        PositiveNumbers.append(a)
    elif a<0:
        NegativeNumbers.append(a)

print(f'''Введённые значения: {', '.join(map(str, AllNumbers))}
Сумма положительных: {sum(PositiveNumbers)}
Сумма отрицательныъ: {sum(NegativeNumbers)}
      ''')