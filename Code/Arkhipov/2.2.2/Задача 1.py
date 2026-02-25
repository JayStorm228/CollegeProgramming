print('''
	Эта программа решает квадратные уравнения по заданным коэффицентам
	Вид уравнения: ax^2 + bx + c = 0
	Коэффиценты вводятся с клавиатуры
	''')
a = int(input('а = '))
b = int(input('b = '))
c = int(input('c = '))

D = b**2-4*a*c

if D>0:
    x1 = (-b+D**(1/2))/(2*a)
    x2  = (-b-D**(1/2))/(2*a)
    print('D > 0')
    print(f'x1 = {x1}, x2 = {x2}')
elif D == 0:
    x = (-b)/(2*a)
    print('D = 0')
    print(f'x = {x}')
else:
    print('D < 0')
    print('Решений нет.')

input()
