import random as r
import re
import string
from pathlib import Path

# Конфигурации
Text_name = "Ex15.txt"
CWD: Path = Path(__file__).resolve().parent
Text_path: Path = CWD / Text_name
encoding = "utf-8"

# Генератор текстового файла
Alphabet: list[str] = list(string.ascii_lowercase)
Length = 100
GeneratedSequence: list[str] = list()
for _ in range(Length):
    WordLen = r.randint(1, 10)
    Symbols: list[str] = r.choices(Alphabet, k=WordLen)
    Word = "".join(Symbols)
    GeneratedSequence.append(Word)
Text_path.write_text(",  ".join(GeneratedSequence), encoding=encoding)

# решение задачи
pattern = r"\s+"
text = Text_path.read_text(encoding=encoding)
NewText = re.sub(r"\s+", " ", text)

NewText_name = "Ex15NEW.txt"
NewText_path = CWD / NewText_name
NewText_path.write_text(NewText, encoding=encoding)

print(
    f"""
Original text: \n{text}
Cleaned whitespaces: \n{NewText}
    """.strip()
)
