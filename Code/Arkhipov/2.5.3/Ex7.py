print(
    """"Эта программа удаляет все пробелы в строке
"""
)

String = input("Введите вашу строку: ")
UpdStr = String.replace(" ", "")
print(
    f"""Строка: {String}
Строка без пробелов: {UpdStr}"""
)
input("\nНажмите ENTER, чтобы выйти.")
