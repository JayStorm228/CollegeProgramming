print('''
	Эта программа считает среднее аримфетическое всех чисел этой последовательности
	''')
from custom_assertions import *
Array = CreateList(UserInput('Введите длинну последовательности: ', int), float)
print(f'Среднее значение: {sum(Array)/len(Array)}')