import random as r
import string
from pathlib import Path

# Конфигурации
Text_name = "Ex10.txt"
CWD: Path = Path(__file__).resolve().parent
Text_path: Path = CWD / Text_name
encoding = "utf-8"

# Генератор текстового файла
words: list[str] = [
    "кот",
    "солнце",
    "дерево",
    "река",
    "небо",
    "дом",
    "книга",
    "дождь",
    "птица",
    "луна",
]
SelectedWords: list[str] = [r.choice(words) for _ in range(1, 10)]
GeneratedSequence = ", ".join(SelectedWords)
Text_path.write_text(GeneratedSequence, encoding=encoding)

# Решение задачи
Text: list[str] = Text_path.read_text(encoding=encoding).split()

NewText: str = ", ".join([word[::-1].strip(string.punctuation) for word in Text])
NewText_name = "Ex10NEW.txt"
NewText_path: Path = CWD / NewText_name
NewText_path.write_text(NewText, encoding=encoding)

print(
    f"""
Original text: \n{Text_path.read_text(encoding=encoding)}\n
Remade text: \n{NewText}
    """.strip()
)
