import random as r
import string
from pathlib import Path

# Конфигурации
Text_name = "Ex12.txt"
CWD: Path = Path(__file__).resolve().parent
Text_path: Path = CWD / Text_name
encoding = "utf-8"

# Генерация текстового файла
Alphabet: list[str] = list(string.ascii_lowercase)
with Text_path.open("w", encoding=encoding) as f:
    SelectedSymbols: list[str] = [r.choice(Alphabet) for _ in range(100)]
    f.writelines("".join(SelectedSymbols) + "\n")

# Решение задачи
text: str = Text_path.read_text(encoding=encoding)
CountSymbol: str = r.choice(Alphabet)
Amount = str(text.count(CountSymbol))

NewText_name = "Ex12NEW.txt"
NewText_path: Path = CWD / NewText_name
NewText_path.write_text(Amount)

print(
    f"""
Original Text: {text}
Amount of "{CountSymbol}": {Amount}
    """.strip()
)
