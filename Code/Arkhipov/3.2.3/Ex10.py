import random as r
import string
from pathlib import Path

# Конфигурации
CWD: Path = Path(__file__).resolve().parent
Text_name = "Ex10.txt"
Text_path: Path = CWD / "output" / Text_name
encoding = "utf-8"
Text_path.parent.mkdir(exist_ok=True)

# Генерация текстового файла
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
text: str = Text_path.read_text(encoding=encoding)
translator = str.maketrans("", "", string.punctuation)
Words: list[str] = str.translate(text, translator).split()

Palindromes: list[str] = ["".join(word[::-1]) for word in Words]
NewText: str = ", ".join(Palindromes)
NewText_name = "Ex10NEW.txt"
NewText_path: Path = CWD / "output" / NewText_name
NewText_path.write_text(NewText, encoding=encoding)

print(
    f"""
Original text: \n{text}\n
Remade text: \n{NewText}
    """.strip()
)
