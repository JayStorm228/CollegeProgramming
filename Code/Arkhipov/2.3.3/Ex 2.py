print('''Эта программа находит количество положительных значений в вещественной последовательности чисел, а также минимальное из них.
      Введите число 5, чтобы прекратить ввод последовательности и получить ответ.
      ''')
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../Mods')))
from custom_assertions import *
a = None
output = []

while True:
    if a == 5:
        break
    a = UserInput('Введите число: ',float)
    if a > 0:
        output.append(a)
    
print(f'''
Количество положительных значений, среди введённых: {len(output)}
Минимальное из них: {min(output)}
      ''')