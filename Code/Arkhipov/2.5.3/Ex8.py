String = input("Введите вашу строку: ")
Word = input("Введите слово, которое хотите удалить: ")
NewStr = String.replace(Word, "")
print(
    f"""Исходная строка: {String}
После удаления слова: {NewStr}"""
)
input("Нажмите Enter чтобы выйти")
