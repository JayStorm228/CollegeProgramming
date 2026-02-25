import string as s

print(
    """"Эта программа находит самое длинное слово и самое короткое слово
"""
)

String = input("Введите вашу строку: ")
UpdString = String.translate(str.maketrans("", "", s.punctuation))
StrList = UpdString.split(" ")
LenList = [len(i) for i in StrList]

MaxLen = max(LenList)
MaxLenWord = StrList[LenList.index(MaxLen)]

MinLen = min(LenList)
MinLenWord = StrList[LenList.index(MinLen)]


print(
    f"""
Исходная строка: {String}
Самое длинное слово: {MaxLenWord}; Его длинна: {MaxLen}
Самое короткое слово: {MinLenWord}; Его длинна: {MinLen}
"""
)
