import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../Mods')))
from custom_assertions import *
print('''Эта программа сортирует список случайных элементов.
      Формат сортировк: Положительные значения, Отрицательные значения, Нулевые значения.
      ''')
a = CreateRandomList(UserInput('Введите размер списка: ', int), [-10, 10], int)

Positive = []
Negative = []
Zeros = []

for w in a:
    if w > 0:
        Positive.append(w)
    elif w < 0:
        Negative.append(w)
    elif w == 0:
        Zeros.append(w)
output = sorted(Positive) + sorted(Negative) + Zeros
print(f''' 
Исходный список: {a}
Отсортированный список: {output}
''')



    
