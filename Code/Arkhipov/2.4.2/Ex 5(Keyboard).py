import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../Mods')))
from custom_assertions import *

print('''
Эта программа изменяет введённый массив по следующим критериям:

Если элемент положительный, он уменьшится в два раза
Если элемент отрицательный, он заменится порядковым номером элемента
''')
Data = CreateList(UserInput('Введите размер списка: ', int), int)
print(f'Исходный список: {Data}')
for i in range(len(Data)):
    if Data[i] > 0:
        Data[i] = Data[i]/2
    if Data[i] < 0:
        Data[i] = i
print(f'Изменённый список: {Data}')
            


    
