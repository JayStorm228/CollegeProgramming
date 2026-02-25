from math import *
print('''
	Эта программа вычисляет средний балл по оценкам ученика.
	На экран будет выведено округлённое целое значение среднего балла
	Нажмите ENTER чтобы закончить ввод оценок.
	Возможные оценки: 2, 3, 4, 5.
	''')
a = []
b = []
marks = '2345'

while not('' in a):
        inn = input('Введите оценку или нажмите ENTER чтобы закончить ввод: ')
        if inn in marks:
                a.append(inn)
        else:
                print(f'"{inn}" не является корректной оценкой. Попробуйте другое значение')
                
a.remove('')

for w in a:
	c = int(w)
	b.append(c)
output = sum(b)/len(b)
output = round(output, 2)
output1 = round(output)

if output >= 4.5:
        print(f'Средний балл: {output}. Итоговая оценка: {output1} - "Отлично"')
elif (output >= 3.5) and (output < 4.5):
        print(f'Средний балл: {output}. Итоговая оценка: {output1} - "Хорошо"')
elif (output >= 2.5) and (output < 3.5):
        print(f'Средний балл: {output}. Итоговая оценка: {output1} - "Удовлетворительно"')
else:
        print(f'Средний балл: {output}. Итоговая оценка: {output1} - "Неудовлетворительно"')
input()






