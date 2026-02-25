a = int(input("Введите значение a "))
b = int(input("Введите значение b "))
c = int(input("Введите значение c "))

min_ = a
if b<min_:
	min_ = b
if c<min_:
	min_=c
print(f'Минимальное из трёх чисел: {min_}')
input()
