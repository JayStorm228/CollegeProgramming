import string as s

print(
    """"Эта программа находит самое длинное слово и количество слов такой же длины
"""
)

String = input("Введите вашу строку: ")
UpdString = String.translate(str.maketrans("", "", s.punctuation))
StrList = UpdString.split(" ")
LenList = [len(i) for i in StrList]
MaxLen = max(LenList)
MaxLenIDX = LenList.index(MaxLen)
MaxLenWord = StrList[MaxLenIDX]
MaxLenCount = LenList.count(MaxLen)

print(
    f"""Исходная строка: {String}
Самое длинное слово: {MaxLenWord}
Его длинна: {MaxLen}
Количество слов с такой же длинной: {MaxLenCount}"""
)
input("\nНажмите ENTER, чтобы выйти.")
