import random as r
from pathlib import Path

# Конфигурации
Text_name = "Ex11.txt"
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
text: str = Text_path.read_text(encoding=encoding)
WordToReplace, WordReplaceWith = r.sample(words, 2)
# r.sample() заменяется на input() за пределами тестов
NewText: str = text.replace(WordToReplace, WordReplaceWith)

NewText_name = "Ex11NEW.txt"
NewText_path: Path = CWD / NewText_name
NewText_path.write_text(NewText, encoding=encoding)

print(
    f"""
Original text: \n{text}\n
Word "{WordToReplace}" is replaced by {WordReplaceWith}
Remade text: \n{NewText}
    """.strip()
)
