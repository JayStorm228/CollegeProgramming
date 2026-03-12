import random as r
import string
from pathlib import Path

Text_name = "Ex7.txt"
CWD: Path = Path(__file__).resolve().parent
Text_path: Path = CWD / Text_name
encoding = "utf-8"

# Генератор текстового файла
with Text_path.open("w", encoding=encoding) as f:
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
    f.write(GeneratedSequence)

# Решение задачи
with Text_path.open("r", encoding=encoding) as f:
    text: str = f.read()

RemovedPunctuation = text.translate(str.maketrans("", "", string.punctuation))
Words: list[str] = RemovedPunctuation.split()
Words[0], Words[-1] = Words[-1], Words[0]

NewText_name = "Ex7NEW.txt"
NewText_path = CWD / NewText_name

with NewText_path.open("w", encoding=encoding) as f:
    f.write(", ".join(Words))
