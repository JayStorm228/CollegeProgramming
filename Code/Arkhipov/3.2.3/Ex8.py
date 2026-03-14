import random as r
import string
from pathlib import Path

# Конфигурации
CWD: Path = Path(__file__).resolve().parent
Text_name = "Ex8.txt"
Text_path: Path = CWD / "output" / Text_name
encoding = "utf-8"
Text_path.parent.mkdir(exist_ok=True)

# Генерация текстового файла
Alphabet: list[str] = list(string.ascii_lowercase)
with Text_path.open("w", encoding=encoding) as f:
    SelectedSymbols: list[str] = [r.choice(Alphabet) for _ in range(100)]
    f.write("".join(SelectedSymbols) + "\n")
    SelectedSymbols: list[str] = [r.choice(Alphabet) for _ in range(100)]
    f.write("".join(SelectedSymbols) + "\n")

# Получение двух строк из файла
text: str = Text_path.read_text(encoding=encoding)
Row1, Row2 = text.splitlines()
NewText: str = ""
# Запись повторяющихся уникальных символов из двух строк
for symbol in Row1:
    if symbol in Row2 and symbol not in NewText:
        NewText += symbol

# Запись итога в файл
NewText_name = "Ex8NEW.txt"
NewText_path: Path = CWD / "output" / NewText_name
NewText_path.write_text(NewText, encoding=encoding)

print(
    f"""
Original text: \n{text}
Symbols in both rows of original text: \n{NewText}
    """.strip()
)
