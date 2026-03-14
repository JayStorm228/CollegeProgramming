import random as r
import re
from pathlib import Path

# Конфигурации
CWD: Path = Path(__file__).resolve().parent
Text_name = "Ex13.txt"
Text_path: Path = CWD / "output" / Text_name
encoding = "utf-8"
Text_path.parent.mkdir(exist_ok=True)


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
num_wraps: int = r.randint(1, len(SelectedWords) // 2)
indices_to_wrap: list[int] = r.sample(range(len(SelectedWords)), num_wraps)
for index in indices_to_wrap:
    word: str = SelectedWords[index]
    SelectedWords[index] = f"({word})"
Text_path.write_text(", ".join(SelectedWords), encoding=encoding)

# Решение задачи
pattern = r"\(([^)]*)\)"
text = Text_path.read_text(encoding=encoding)
NewText: str = re.sub(pattern, "()", text)

NewText_name = "Ex13NEW.txt"
NewText_path = CWD / "output" / NewText_name
NewText_path.write_text(NewText, encoding=encoding)

print(
    f"""
Original Text: \n{text}
Sentences in "()" brackets removed: \n{NewText}
    """.strip()
)
