print('''
	Эта программа показывает максимальное и минимальное значение введённой последовательности
 ''')
from custom_assertions import *
Array = CreateList(UserInput('Введите длинну последовательности: ', int), float)
print(f'''Максимальное значение: {max(Array)}
Минимальное значение: {min(Array)}''')
    
