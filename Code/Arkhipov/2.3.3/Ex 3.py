print('''Эта программа находит, каких чисел больше в введённой последовательности целых чисел
      Введите число 1, чтобы закончить ввод
''')
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../Mods')))
from custom_assertions import *

a = None
PositiveNumbers = []
NegativeNumbers = []

while True:
    a = UserInput('Введите число: ',int)    
    if a == 1:
        break
    elif a > 0:
        PositiveNumbers.append(a)
    elif a<0:
        NegativeNumbers.append(a)

if len(PositiveNumbers)>len(NegativeNumbers):
    print(f'Больше Положительных на {len(PositiveNumbers)-len(NegativeNumbers)}')
elif len(PositiveNumbers)<len(NegativeNumbers):
    print(f'Больше отрицательных на {len(NegativeNumbers)-len(PositiveNumbers)}')
else:
    print(f'равное количество тех и других: {len(PositiveNumbers)}')