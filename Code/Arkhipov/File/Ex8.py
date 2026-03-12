import random as r
import string
from pathlib import Path

# Конфигурации
Text_name = "Ex8.txt"
CWD: Path = Path(__file__).resolve().parent
Text_path: Path = CWD / Text_name
encoding = "utf-8"

# Генерация текстового файла
Alphabet: list[str] = list(string.ascii_lowercase)
with Text_path.open("w", encoding=encoding) as f:
    SelectedSymbols: list[str] = [r.choice(Alphabet) for _ in range(100)]
    f.write("".join(SelectedSymbols) + "\n")
    SelectedSymbols: list[str] = [r.choice(Alphabet) for _ in range(100)]
    f.write("".join(SelectedSymbols) + "\n")

# Получение двух строк из файла
with Text_path.open("r", encoding=encoding) as f:
    text: list[str] = f.read().split("\n")

Row1: str = text[0]  # строка 1
Row2: str = text[1]  # строка 2
Row3: str = ""  # строка 3

# Запись повторяющихся уникальных символов из двух строк
for symbol in Row1:
    if symbol in Row2 and symbol not in Row3:
        Row3 += symbol

# Запись итога в файл
NewText_name = "Ex8NEW.txt"
NewText_path: Path = CWD / NewText_name
with NewText_path.open("w", encoding=encoding) as f:
    f.write(Row3)
