print('''Эта программа находит сумму всех чётных чисел на указанном отрезке.
''')
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../Mods')))
from custom_assertions import *

LowerBound = UserInput('Введите значение нижнего предела: ', int)
UpperBound = UserInput('Введите значение верхнего предела: ', int)
EvenValues = []
for w in range(LowerBound, UpperBound):
    if w%2 == 0:
        EvenValues.append(w)
print(f'''Все чётные значения этого предела: {', '.join(map(str, EvenValues))}
Их сумма: {sum(EvenValues)}
      ''')