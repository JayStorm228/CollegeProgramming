print('''Эта программа шифрует введённую строку
Шифр: ASCII код символа - 10
''')
string = input('Введите строку: ')
StrList = []
for w in string:
    StrList.append(w)
for i in range(len(StrList)):
    Cypher = ord(StrList[i])
    Cypher-=10
    StrList[i] = chr(Cypher)
print(f'Зашифрованная строка: {''.join(map(str, StrList))}')
input('\nНажмите ENTER, чтобы выйти.')
