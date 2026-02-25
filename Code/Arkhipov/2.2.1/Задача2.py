
print('''
Эта программа считает выручку продавцов: Иванова, Петрова и Сидорова - за квартал, по данным, вводимым за месяцы 1, 2, 3.
Вам будет предоставлен отчёт и возможные действия с этими сотрудниками
''')

month1_Sidorov = int(input('Месяц 1 Сидорова: '))
month2_Sidorov = int(input('Месяц 2 Сидорова: '))
month3_Sidorov = int(input('Месяц 3 Сидорова: '))
month1_Petrov = int(input('Месяц 1 Петрова: '))
month2_Petrov = int(input('Месяц 2 Петрова: '))
month3_Petrov = int(input('Месяц 3 Петрова: '))
month1_Ivanov = int(input('Месяц 1 Иванова: '))
month2_Ivanov = int(input('Месяц 2 Иванова: '))
month3_Ivanov = int(input('Месяц 3 Иванова: '))

Ivanov = month1_Ivanov + month2_Ivanov + month3_Ivanov
Petrov = month1_Petrov + month2_Petrov + month3_Petrov
Sidorov = month1_Sidorov+  month3_Sidorov + month2_Sidorov

if Ivanov>500000:
	print(f'Выручка Иванова: {Ivanov}. Достоин премии.')
elif Ivanov>800000:
	print(f'Выручка Иванова: {Ivanov}. Достоин премии и доски почёта.')
elif Ivanov<0:
	print(f'Убыток Иванова: {Ivanov}. Достоин штрафа')
else:
	print(f'Выручка Иванова: {Ivanov}.')

if Petrov>500000:
	print(f'Выручка Петрова: {Petrov}. Достоин премии.')
elif Petrov>800000:
	print(f'Выручка Петрова: {Petrov}. Достоин премии и доски почёта.')
elif Petrov<0:
	print(f'Убыток Петрова: {Petrov}. Достоин штрафа')
else:
	print(f'Выручка Петрова: {Petrov}.')

if Sidorov>500000:
	print(f'Выручка Сидорова: {Sidorov}. Достоин премии.')
elif Sidorov>800000:
	print(f'Выручка Сидорова: {Sidorov}. Достоин премии и доски почёта.')
elif Sidorov<0:
	print(f'Убыток Сидорова: {Sidorov}. Достоин штрафа')
else:
	print(f'Выручка Сидорова: {Sidorov}.')


'''
def income(employee):
	income = 0
	employees = ['Иванов', "Петров", "Сидоров"]
	if employee in employees:
                for w in range(2):
                	income+=int(input('Введите выручку: '))
	
                if income > 500000:
                        print(f'Выручка {employee}: {income}. Достоин премии.')
                elif income > 800000:
                	print(f'Выручка {employee}: {income}. Достоин премии и доски почёта.')
		elif income < 0:
			print(f'Убыток {employee}: {income}. Достоин штрафа.')	
		else:
			print(f'Выручка {employee}: {income}.')
	
        else:
                print(f'{employee} не работает в компании. Работники: {employees}.')
	'''
