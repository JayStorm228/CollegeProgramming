print('''
	Эта программа показывает максимальное значение введённой последовательности
	''')
from custom_assertions import *
Array = CreateList(UserInput('Введите длинну последовательности: ', int), float)
print(f'Максимальное значение: {max(Array)}')
    