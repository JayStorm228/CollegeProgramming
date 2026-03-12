import random as r
from pathlib import Path

Text_name = "Ex6.txt"
CWD: Path = Path(__file__).resolve().parent
Text_path: Path = CWD / Text_name
encoding = "utf-8"

# Генератор текстового файла
with Text_path.open("w", encoding=encoding) as f:
    Plus: list[str] = ["+" for _ in range(r.randint(1, 100))]
    Minus: list[str] = ["-" for _ in range(r.randint(1, 100))]
    Asterisk: list[str] = ["*" for _ in range(r.randint(1, 100))]
    GeneratedSequence = "".join(Plus + Minus + Asterisk)
    f.write(GeneratedSequence)

# Решение задачи
with Text_path.open("r", encoding=encoding) as f:
    text: str = f.read()

PlusCount: int = text.count("+")
MinusCount: int = text.count("-")
AsteriskCount: int = text.count("*")

# Вывод
print(
    f"""
Textfile: \n{text}\n
Found "Minus" symbols: {MinusCount}
Found "Plus" symbols: {PlusCount}
Found "Asterisk" symbols: {AsteriskCount}
    """.strip()
)
