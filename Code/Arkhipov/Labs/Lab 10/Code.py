print(
    """Эта программа подсчитывает среднюю длину слов во введённой строке
"""
)
import string as s

text = input("Введите строку: ")
Words = text.translate(str.maketrans("", "", s.punctuation)).split()
if Words:
    Average = sum([len(word) for word in Words]) / len(Words)
    print(f'Средняя длина слов в строке "{text}": {Average:.2f}')
else:
    print(f'В строке "{text}" нет слов')
