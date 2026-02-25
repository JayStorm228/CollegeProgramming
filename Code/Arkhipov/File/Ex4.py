import re
from pathlib import Path

Text_name = "Ex4.txt"
CWD: Path = Path(__file__).resolve().parent
Text_path: Path = CWD / Text_name
encoding = "utf-8"

with Text_path.open("r", encoding=encoding) as f:
    text: str = f.read()

NewText: str = re.sub(r"(.)\1+", r"\1", text)
NewText_name = "New String.txt"
NewText_path = CWD / NewText_name
with NewText_path.open("w", encoding=encoding) as f:
    f.write(NewText)
