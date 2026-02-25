from pathlib import Path

FileName = "Ex2.txt"
path: Path = Path(__file__).resolve().parent
file: Path = path / FileName
encoding = "utf-8"
with file.open("r", encoding=encoding) as f:
    text: str = f.read()

words: list[str] = text.split()
LenWords: int = len(words)

print(
    f"""
Исходное предложение: {text}
Количество слов: {LenWords}
"""
)
