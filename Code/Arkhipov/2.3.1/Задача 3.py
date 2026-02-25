print('''
	Эта программа считает среднее аримфетическое только отрицательных значений этой последовательности
	
	''')
from custom_assertions import *
NegativeTemps = []
Size = UserInput('Введите количество температур: ', int)
for w in range(Size):
    Temp = UserInput('Введите значение температуры: ', int)
    if Temp < 0:
        NegativeTemps.append(Temp)

print(f'Среднее значение: {sum(NegativeTemps)/len(NegativeTemps)}')
    
