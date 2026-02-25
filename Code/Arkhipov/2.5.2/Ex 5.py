print(
    """Эта программа проверяет, является ли строка палиндромом
"""
)
import string as s

InputStr = input("Введите строку: ")
string = InputStr.translate(str.maketrans("", "", s.punctuation + " ")).lower()
string_list = []
for w in string:
    string_list.append(w)
ReversedStr = "".join(map(str, string_list[::-1]))
if string == ReversedStr:
    print(f"{InputStr} - Палиндром")
else:
    print(f"{InputStr} - Не палиндром")
input("\nНажмите ENTER, чтобы выйти.")
