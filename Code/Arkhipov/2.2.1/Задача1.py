print('''
Эта программа вычисляет среднюю температуру за неделю по входящим данным с ПН во ВС.
Среднее значение округлено до целых.
''')
mon = int(input('ПН: '))
tue = int(input('ВТ: '))
wed = int(input('СР: '))
thu = int(input('ЧТ: '))
fri = int(input('ПТ: '))
sat = int(input('СБ: '))
sun = int(input('ВС: '))
a = [mon, tue, wed, thu, fri, sat, sun]
middle = int(sum(a)/len(a))
if middle < 10:
    print(f'Холодно! {middle}C')
if middle > 25:
    print(f'Жарко! {middle}C')
else:
    print(f'Умеренно. {middle}C')
