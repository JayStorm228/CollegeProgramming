from pathlib import Path
from typing import List, Tuple

CWD = Path(__file__).resolve().parent
Text_path = CWD / "output" / "Ex5.txt"
Text_path.parent.mkdir(exist_ok=True)

with Text_path.open("r", encoding="utf-8") as f:
    text = f.read()

stack: List[Tuple[str, int, int]] = []
punct = set(",.!?:;")

for line_num, line in enumerate(text.splitlines(), 1):
    for col, char in enumerate(line, 1):
        if char == "(":
            if col > 1 and not line[col - 2].isspace():
                print(
                    f"Ошибка: строка {line_num}, позиция {col} - Нет пробела перед открывающей скобкой"
                )
            if col < len(line) and line[col].isspace():
                print(
                    f"Ошибка: строка {line_num}, позиция {col+1} - Лишний пробел после открывающей скобки"
                )
            stack.append((char, line_num, col))
        elif char == ")":
            if col > 1 and line[col - 2].isspace():
                print(
                    f"Ошибка: строка {line_num}, позиция {col} - Лишний пробел перед закрывающей скобкой"
                )
            if col < len(line) and line[col] not in punct and not line[col].isspace():
                print(
                    f"Ошибка: строка {line_num}, позиция {col+1} - Ожидался пробел или знак препинания после закрывающей скобки"
                )

            if not stack:
                print(f"Ошибка: строка {line_num}, позиция {col} - Скобка не открыта")
                raise ValueError("Unmatched closing bracket")
            open_br, o_line, o_col = stack.pop()
            if open_br != "(":
                print(
                    f'Ошибка: строка {line_num}, позиция {col} - Неправильная "{char}" (открыта {o_line}:{o_col})'
                )
                raise ValueError("Mismatched brackets")

if stack:
    opens = [f"({ln}:{c})" for _, ln, c in stack]
    print("Не закрыты:", ", ".join(opens))
else:
    print("Скобки правильные по структуре")
