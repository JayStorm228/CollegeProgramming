import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../Mods')))
from custom_assertions import *
print('''
Это программа вычисляет произведение отрицательных элементов, имеющих нечётные индексы.
''')
Tuple = tuple(CreateList(UserInput('Введите количество чисел, которые вы будете вводить: ', int),int))# генератор списков
output = 1
for w in range(len(Tuple)):
    if w%2 == 1 and Tuple[w] < 0:
        output *= Tuple[w]
print(output)




