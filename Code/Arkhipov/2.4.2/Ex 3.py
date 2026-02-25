import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../Mods')))
from custom_assertions import *
print('''
Эта программа определяет среднее арифметическое значение элементов удовлетворяющих условию

Условие - элемент по модулю больше числа C

число С вводится с клавиатуры
''')

C = UserInput('Введите число С: ', float)
InputTuple = tuple(CreateList(UserInput('Введите размер массива: ', int), int))
output = []

for w in InputTuple:
    if abs(w) > C:
        output.append(w)

if len(output) < 0:
    print(f'''
Введённые значения: {', '.join(map(str, InputTuple))}
Среди них удовлетворяют условию: 0
''')
    
else:       
    print(f'''
Удовлетворительные значения: {', '.join(map(str, output))}
Их среднее значение: {sum(output)/len(output)}
''')


    
