import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../Mods')))
from custom_assertions import *
print('''
Этп программа вычисляет максимальное и минимальное значение среди нечётных элементов массива из 10 элементов
''')

Tuple = []
output = []
while len(Tuple) != 10:
    Tuple.append(UserInput('Введите число: ', int))
Tuple = tuple(Tuple)

for w in Tuple:
    if w > 0 and w%2 == 1:
        output.append(w)
print(f'''
Удовлетворительные значения: {', '.join(map(str, output))}
Максимальное: {max(output)}
Минимальное: {min(output)}
''')

    
