print('''Эта программа считает количество знакопеременных пар
''')
import random as r
Size = int(input('Введите размер массива: '))
Array = [r.randint(-2, 2) for w in range(Size)]
count = 0
for w in range(Size-1):
    Expression1 = (Array[w]>0 and Array[w+1]<0) #+ -
    Expression2 = (Array[w]<0 and Array[w+1]>0) #- +
    if Expression1 or Expression2:
        count+=1
    
print(f'''Созданныйй массив: {Array}
Количество знакочередующихся пар: {count}
''')


input('Нажмите ENTER, чтобы выйти.')
