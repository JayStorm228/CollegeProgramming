import re
from pathlib import Path

path: Path = Path(__file__).resolve().parent
file: Path = path / "Ex1.txt"
encoding = "utf-8"
with file.open("r", encoding=encoding) as f:
    text: str = f.read()

SymbolsCount: dict[str, int] = {
    "aa": text.count("aa") + text.count("аа"),
    "oo": text.count("oo") + text.count("оо"),
    "kk": text.count("kk") + text.count("кк"),
}

chars: str = "aokаок"
NewText: str = re.sub(r"(.)\1{1}", r"\1", text)
print(
    f"""
Исходный текст: {text}
Количество повторяемых символов:
    аа: {SymbolsCount['aa']}
    оо: {SymbolsCount['oo']}
    kk: {SymbolsCount['kk']}
Изменённый текст: {NewText}
"""
)
