import random as r
import string
from pathlib import Path

CWD: Path = Path(__file__).resolve().parent
Text_name = "Ex2.txt"
Text_path: Path = CWD / "output" / Text_name
encoding = "utf-8"
Text_path.parent.mkdir(exist_ok=True)

# Генератор текстового файла
Alphabet: list[str] = list(string.ascii_lowercase)
Length = 100
GeneratedSequence: list[str] = list()
for _ in range(Length):
    WordLen = r.randint(1, 10)
    Symbols: list[str] = r.choices(Alphabet, k=WordLen)
    Word = "".join(Symbols)
    GeneratedSequence.append(Word)
Text_path.write_text(", ".join(GeneratedSequence), encoding=encoding)


text = Text_path.read_text(encoding=encoding)
words: list[str] = text.split()
LenWords: int = len(words)

print(
    f"""
Исходное предложение: \n{text}
Количество слов: {LenWords}
"""
)
