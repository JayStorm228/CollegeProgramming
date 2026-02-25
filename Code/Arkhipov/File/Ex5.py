from pathlib import Path

Text_name = "Ex5.txt"
CWD: Path = Path(__file__).resolve().parent
Text_path: Path = CWD / Text_name
encoding = "utf-8"

with Text_path.open("r", encoding=encoding) as f:
    text: str = f.read()

stack = []
brackets: dict[str, str] = {"(": ")", "[": "]", "{": "}"}
"""
Правила постановки скобок:
1) Должен быть пробел перед открывающей скобкой
2) Не должно быть пробела после открывающей скобки
3) Должен быть пробел/знак препинания после закрывающей скобки
4) Не должно быть пробела перед закрывающей скобкой
"""
for line_num, line in enumerate(text.split("\n"), 1):
    for col, char in enumerate(line, 1):
        # Проверки стиля для круглых скобок
        if char == "(":
            # 1) Должен быть пробел ПЕРЕД (
            if col > 1 and not line[col - 2].isspace():
                print(
                    f"Ошибка: строка {line_num}, позиция {col} - Нет пробела перед открывающей скобкой"
                )
            # 2) Не должно быть пробела ПОСЛЕ (
            if col < len(line) and line[col].isspace():
                print(
                    f"Ошибка: строка {line_num}, позиция {col+1} - Лишний пробел после открывающей скобки"
                )

        elif char == ")":
            # 3) Не должно быть пробела ПЕРЕД )
            if col > 1 and line[col - 2].isspace():
                print(
                    f"Ошибка: строка {line_num}, позиция {col} - Лишний пробел перед закрывающей скобкой"
                )
            # 4) После ) либо пробел, либо пунктуация, либо конец строки
            if col < len(line):
                next_ch = line[col]
                if not (next_ch.isspace() or next_ch in ",.!?:;"):
                    print(
                        f"Ошибка: строка {line_num}, позиция {col+1} - Ожидался пробел или знак препинания после закрывающей скобки"
                    )

        # Баланс скобок (круглые)
        if char == "(":
            stack.append((char, line_num, col))
        elif char == ")":
            if not stack:
                print(f"Ошибка: строка {line_num}, позиция {col} - Скобка не открыта")
                exit()
            open_br, o_line, o_col = stack.pop()
            if open_br != "(":
                print(
                    f'Ошибка: строка {line_num}, позиция {col} - Неправильная "{char}" (открыта {o_line}:{o_col})'
                )
                exit()

if stack:
    opens: list[str] = [f"({line}:{column})" for _, line, column in stack]
    print("Не закрыты:", ", ".join(opens))
else:
    print("Скобки правильные по структуре")
