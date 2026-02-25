import string as s
from pathlib import Path

FileName = "Ex3.txt"
path: Path = Path(__file__).resolve().parent
file: Path = path / FileName
encoding = "utf-8"
with file.open("r", encoding=encoding) as f:
    text: str = f.read()

Words: list[str] = text.split()
Words = [_.translate(str.maketrans("", "", s.punctuation)) for _ in Words]
LenWords: list[int] = [len(_) for _ in Words]
MaxLenWord: int = max(LenWords)
MinLenWord: int = min(LenWords)

print(
    f"""
Информация в текстовом файле: \n{text}\n
Самое длинное слово: {MinLenWord}
Самое короткое слово: {MaxLenWord}
"""
)
