import random as r
import string
from pathlib import Path

# Конфигурации
CWD: Path = Path(__file__).resolve().parent
Text_name = "Ex12.txt"
Text_path: Path = CWD / "output" / Text_name
encoding = "utf-8"
Text_path.parent.mkdir(exist_ok=True)

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
NewText_path: Path = CWD / "output" / NewText_name
NewText_path.write_text(Amount)

print(
    f"""
Original Text: {text}
Amount of "{CountSymbol}": {Amount}
    """.strip()
)
