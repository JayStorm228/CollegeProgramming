import random as r
import re
import string
from pathlib import Path

CWD: Path = Path(__file__).resolve().parent
Text_name = "Ex1.txt"
Text_path: Path = CWD / "output" / Text_name
encoding = "utf-8"
Text_path.parent.mkdir(exist_ok=True)


# Генератор текстового файла
Alphabet: list[str] = list(string.ascii_lowercase)
Length = 100
GeneratedSequence: list[str] = list()
for _ in range(Length):
    WordLen = r.randint(1, 10)
    Symbols: list[str] = r.choices(Alphabet, k=WordLen)
    Word = "".join(Symbols)
    GeneratedSequence.append(Word)
Text_path.write_text(", ".join(GeneratedSequence), encoding=encoding)

# Решение задачи
text = Text_path.read_text(encoding=encoding)
SymbolsCount: dict[str, int] = {
    "aa": text.count("aa") + text.count("аа"),
    "oo": text.count("oo") + text.count("оо"),
    "kk": text.count("kk") + text.count("кк"),
}
chars: str = "aokаок"
NewText: str = re.sub(r"(.)\1{1}", r"\1", text)

print(
    f"""
Исходный текст: \n{text}
Количество повторяемых символов:
    аа: {SymbolsCount['aa']}
    оо: {SymbolsCount['oo']}
    kk: {SymbolsCount['kk']}
Изменённый текст: \n{NewText}
"""
)
