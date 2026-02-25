import random as r
class SizeError(Exception):
    def __init__(self, size):
        self.size = size
        self.message = f'Wrong size of Argument! Expected list with {self.size} values!'
        super().__init__(self.message)
        
def UserInput(text:str, DATAtype):
    variable = None
    if DATAtype == float: #Принимаем на ввод дробные числа
        while variable == None:
            variable = input(text)
            try:
                variable = float(variable)

            except ValueError:
                print(f'\'{variable}\' не является корректным значением. Если вы вводите дробное значеине, вводите его через точку(Пр.: 4.5)')
                variable = None
                continue
        return variable

    elif DATAtype == int: # Получим целое число
        while True:
            variable = input(text)
            if '.' in variable:
                print('''                    
Вы ввели дробное значение.
Пожалуйста, введите целое значение.     
''')
                variable = None
            else:
                try: 
                    variable = int(variable)
                except ValueError:
                    print(f'\'{variable}\' не является корректным значением.')
                    variable = None
            if variable != None:
                break
        return variable     

    elif DATAtype == str: # Полчить строковое значение
        variable = input(text)
        return variable
    
    else:   raise TypeError(f'''{DATAtype} is wrong type of value!
                            Allowed types: str, int, float''')
		
def CreateList(size, Type): #Генератор списков с целыми/дробными значениями с клавиатуры
    if type(size) != int: 
        raise TypeError(f'''<{size}> is invalid argument!
                        Size must be an integer value!''')
    if type(Type) == int or type(Type) == float: 
        raise TypeError(f'''<{Type}> is invalid type!
                        Supported types: int, float''')
    
    print('На основе введённых чисел будет создан список.\nНажмите  Еnter, чтобы закончить ввод')

    output = []
    counter = 1
    while len(output) != size:
        output.append(UserInput(f'Введите число {counter}: ', Type))
        counter += 1
    return output

def CreateRandomList(size:int, Bounds:list, Type): # Список случайных значений
    output = []
    if type(size) != int:
        raise TypeError(f'Expected int type, not {type(size)} type!')
    if type(Bounds) != list:
        raise TypeError(f'Expected list type, not {type(Bounds)} type!')
    if len(Bounds) != 2:
        raise SizeError(2)
    if Bounds[0] > Bounds[1]:
        raise ValueError(f'Bounds[0]={Bounds[0]} value must be bigger than Bounds[1]={Bounds[1]} value! ')

    if Type == int: # Случайные Целые значения
        for w in range(size):
            output.append(r.randint(Bounds[0], Bounds[1]))
        return output
    
    elif Type == float: # Случайные Дробные значения
        for w in range(size):
            output.append(r.uniform(Bounds[0], Bounds[1]))
        return output
    
    else: raise TypeError(f'''<{type}> is an invalid type.
                          Supported types: float, int''')



if __name__ == '__main__':
    print(UserInput('test', float))