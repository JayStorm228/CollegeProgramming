import random as r
import string
from pathlib import Path

# Конфигурации
Text_name = "Ex14.txt"
CWD: Path = Path(__file__).resolve().parent
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
text: str = Text_path.read_text(encoding=encoding)
NewText: str = ", ".join([word for word in text.split(", ") if len(word) >= 2])
Removed = ", ".join([word for word in text.split(", ") if len(word) < 2])
NewText_name = "Ex14NEW.txt"
NewText_path = CWD / "output" / NewText_name
NewText_path.write_text(NewText, encoding=encoding)
print(
    f"""
Original text: \n{text}
New text: \n{NewText}
Removed words: \n{Removed}
    """.strip()
)
