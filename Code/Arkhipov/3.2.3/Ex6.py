import random as r
from pathlib import Path

CWD: Path = Path(__file__).resolve().parent
Text_name = "Ex6.txt"
Text_path: Path = CWD / "output" / Text_name
encoding = "utf-8"
Text_path.parent.mkdir(exist_ok=True)

# Генератор текстового файла
with Text_path.open("w", encoding=encoding) as f:
    Plus: list[str] = ["+" for _ in range(r.randint(1, 100))]
    Minus: list[str] = ["-" for _ in range(r.randint(1, 100))]
    Asterisk: list[str] = ["*" for _ in range(r.randint(1, 100))]
    GeneratedSequence = "".join(Plus + Minus + Asterisk)
    f.write(GeneratedSequence)

# Решение задачи
text: str = Text_path.read_text(encoding=encoding)
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
