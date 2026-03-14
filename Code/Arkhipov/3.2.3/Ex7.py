import random as r
import string
from pathlib import Path

CWD: Path = Path(__file__).resolve().parent
Text_name = "Ex7.txt"
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

# Решение задачи
text = Text_path.read_text(encoding=encoding)
RemovedPunctuation = text.translate(str.maketrans("", "", string.punctuation))
Words: list[str] = RemovedPunctuation.split()
Words[0], Words[-1] = Words[-1], Words[0]
NewText: str = ", ".join(Words)

NewText_name = "Ex7NEW.txt"
NewText_path: Path = CWD / "output" / NewText_name
NewText_path.write_text(NewText, encoding=encoding)

print(
    f"""
Original text: \n{text}
First and Last words have been swapped: \n{NewText}
    """.strip()
)
