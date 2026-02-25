import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../Mods')))
from custom_assertions import *
print('''
Эта программа разделяет введённые значения на чётные и нечётные
''')
Input = CreateList(UserInput('Введите значение: ', int), int)
EvenList = []
UnEvenList = []

for w in Input:
    if w%2 == 0:
        EvenList.append(w)
    else:   UnEvenList.append(w)
print(f'''
Список чётных элементов: {EvenList}
Список нечётных элементов: {UnEvenList}
''')


