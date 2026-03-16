import random as r
import re
import string
from pathlib import Path

CWD: Path = Path(__file__).resolve().parent
Text_name = "Ex7.txt"
Text_path: Path = CWD / "output" / Text_name
encoding = "utf-8"
Text_path.parent.mkdir(exist_ok=True)

# Генератор текстового файла
Eng = string.ascii_letters
Ru = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
Alphabet: list[str] = list(Eng + Ru)
Length = 100
GeneratedSequence: list[str] = list()
Separators = ",:; .|-"
for _ in range(Length):
    WordLen = r.randint(1, 10)
    Symbols: list[str] = r.choices(Alphabet, k=WordLen)
    Word = "".join(Symbols)
    GeneratedSequence.append(Word)
Text_path.write_text(
    GeneratedSequence[0].capitalize()
    + "".join(r.choice(Separators) + f" {item}" for item in GeneratedSequence[1:])
    + ".",
    encoding=encoding,
)

# Решение задачи
Text: str = Text_path.read_text(encoding=encoding)
Words: list[str] = re.findall(r"\w+", Text, flags=re.UNICODE)
if len(Words) >= 2:
    Words[0], Words[-1] = Words[-1], Words[0]
NewText: str = re.sub(r"\w+", lambda m: Words.pop(0), Text, flags=re.UNICODE)
NewText_name = "Ex7NEW.txt"
NewText_path: Path = CWD / "output" / NewText_name
NewText_path.write_text(NewText, encoding=encoding)

print(
    f"""
Original text: \n{Text}\n
First and Last words have been swapped: \n{NewText}
    """.strip()
)
