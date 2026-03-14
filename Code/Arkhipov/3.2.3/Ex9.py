import random as r
import string
from pathlib import Path

# Конфигурации
CWD: Path = Path(__file__).resolve().parent
Text_name = "Ex9.txt"
Text_path: Path = CWD / "output" / Text_name
encoding = "utf-8"
Text_path.parent.mkdir(exist_ok=True)

# Генерация текстового файла
Alphabet: list[str] = list(string.ascii_lowercase)
Length = 100
GeneratedSequence: list[str] = list()
for _ in range(Length):
    WordLen = r.randint(1, 10)
    Symbols: list[str] = r.choices(Alphabet, k=WordLen)
    Word = "".join(Symbols)
    GeneratedSequence.append(Word)
Text_path.write_text(", ".join(GeneratedSequence), encoding=encoding)


# Решений задачи
SearchedLetter, ReplaceByLetter = r.sample(Alphabet, 2)
text: str = Text_path.read_text(encoding=encoding)
NewText: str = "".join([ReplaceByLetter if w == SearchedLetter else w for w in text])

NewText_name = "Ex9NEW.txt"
Newtext_path: Path = CWD / "output" / NewText_name

with Newtext_path.open("w", encoding=encoding) as f:
    f.writelines(NewText + "\n")
print(
    f"""
Original text: \n{text}
Letter to be replaced: {SearchedLetter}
Letter to replace with: {ReplaceByLetter}
Replaced {text.count(SearchedLetter)}: \n{NewText}

    """.strip()
)
