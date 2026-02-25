print('''Эта программа принимает на ввод критическое число.
      После чего считает сумму всех введённых чисел, до тех пор пока она не превышает критическое значение.
      Программа выводит количество чисел, которое потребовалось, чтобы превысить критическое значение
''')
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../Mods')))
from custom_assertions import *

CriticalNumber = UserInput('Введите критическое значение: ',float)
Sum = 0 
counter = 0

while Sum <= CriticalNumber:
    Number = UserInput('Введите число: ', float)
    Sum+=Number
    counter+=1

print(f'''
Итоговая сумма: {Sum}
Количество значений, которое потребовалось ввести: {counter}
      ''')