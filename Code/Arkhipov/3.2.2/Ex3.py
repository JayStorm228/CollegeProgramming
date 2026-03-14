import random as r
import string
from pathlib import Path

CWD: Path = Path(__file__).resolve().parent
Text_name = "Ex3.txt"
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
Words = [_.translate(str.maketrans("", "", string.punctuation)) for _ in text.split()]
LenWords: list[int] = [len(_) for _ in Words]
MaxLenWord: int = max(LenWords)
MinLenWord: int = min(LenWords)

print(
    f"""
Original text: \n{text}\n
Longest word len: {MinLenWord}
Shortest word len: {MaxLenWord}
"""
)
