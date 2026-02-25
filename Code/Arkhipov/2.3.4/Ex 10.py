print('''Эта программа вычисляет идеальный вес для взрослых людей по формуле:
    Идеальный вес = Рост - 100
''')
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../Mods')))
from custom_assertions import *

while True:
    Height = UserInput('Введите значение вашего роста(см): ',int)
    if Height == 250:
        print('Вы вышли из программы.')
        break
    else:
        print(f'Ваш идеальный вес: {Height-100}')