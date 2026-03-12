import random as r
import string
from pathlib import Path

# Конфигурации
Text_name = "Ex9.txt"
CWD: Path = Path(__file__).resolve().parent
Text_path: Path = CWD / Text_name
encoding = "utf-8"

# Генерация текстового файла
Alphabet: list[str] = list(string.ascii_lowercase)
with Text_path.open("w", encoding=encoding) as f:
    SelectedSymbols: list[str] = [r.choice(Alphabet) for _ in range(100)]
    f.writelines("".join(SelectedSymbols) + "\n")


# Решений задачи
SearchedLetter, ReplaceByLetter = r.sample(Alphabet, 2)
with Text_path.open("r", encoding=encoding) as f:
    text: str = f.read().rstrip()
NewText = "".join([ReplaceByLetter if w == SearchedLetter else w for w in text])

NewText_name = "Ex9NEW.txt"
Newtext_path: Path = CWD / NewText_name

with Newtext_path.open("w", encoding=encoding) as f:
    f.writelines(NewText + "\n")
print(
    f"""
Original text:
Letter to be replaced: {SearchedLetter}
Letter to replace with: {ReplaceByLetter}
Replaced {text.count(SearchedLetter)}
    """.strip()
)
