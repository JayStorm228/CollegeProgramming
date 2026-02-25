print('''
	Эта программа считает количество отрицательных температур среди всех введённых
	''')
from custom_assertions import *
NegativeTemps = []
Size = UserInput('Введите количество температур: ', int)
for w in range(Size):
    Temp = UserInput('Введите значение температуры: ', int)
    if Temp < 0:
        NegativeTemps.append(Temp)
print(f'Количество отрицательных чисел в последовательности: {len(NegativeTemps)}')
    
