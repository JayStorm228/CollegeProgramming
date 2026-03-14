import re
from pathlib import Path
from typing import List

CWD: Path = Path(__file__).resolve().parent
Text_path: Path = CWD / "output" / "Ex5.txt"
Fixed_path: Path = CWD / "output" / "Ex5NEW.txt"
encoding = "utf-8"
Text_path.parent.mkdir(exist_ok=True)

try:
    text = Text_path.read_text(encoding=encoding)
except FileNotFoundError:
    print("Файл Ex5.txt не найден!")
    exit(1)

lines: List[str] = text.splitlines(keepends=True)
new_lines: List[str] = []
punct: set[str] = set(",.!?:;")
errors: List[str] = []

for line_num, line in enumerate(lines, 1):
    chars = list(line)
    stack: List[int] = []  # позиции "(" в ТЕКУЩЕЙ строке (индекс в chars)
    col = 0

    while col < len(chars):
        char = chars[col]

        if char == "(":
            # Нет пробела перед (
            if col > 0 and not chars[col - 1].isspace():
                errors.append(
                    f"Добавлен пробел перед (: строка {line_num}, позиция {col+1}"
                )
                chars.insert(col, " ")
                col += 1

            # Лишний пробел после (
            if col + 1 < len(chars) and chars[col + 1].isspace():
                errors.append(
                    f"Удален лишний пробел после (: строка {line_num}, позиция {col+2}"
                )
                del chars[col + 1]
                continue

            stack.append(col)

        elif char == ")":
            # Лишний пробел перед )
            if col > 0 and chars[col - 1].isspace():
                errors.append(
                    f"Удален лишний пробел перед ): строка {line_num}, позиция {col}"
                )
                del chars[col - 1]
                col -= 1
                continue
            # Нет пробела или пунктуации после )
            if (
                col + 1 < len(chars)
                and not chars[col + 1].isspace()
                and chars[col + 1] not in punct
            ):
                errors.append(
                    f"Добавлен пробел после ): строка {line_num}, позиция {col+2}"
                )
                chars.insert(col + 1, " ")

            # Парность в пределах строки
            if not stack:
                # В этой строке закрывающих больше, чем открывающих — считаем ) лишней
                errors.append(f"Лишняя ): строка {line_num}, позиция {col+1} — удалена")
                del chars[col]
                continue
            else:
                stack.pop()

        col += 1

    # В этой строке остались незакрытые "(" — добавляем ) в конце строки
    if stack:
        for open_idx in stack:
            errors.append(
                f"Не закрыта (: строка {line_num}, позиция {open_idx+1} — добавлена ) в конце строки"
            )
        # Вставляем перед переводом строки, если он есть
        if chars and chars[-1] == "\n":
            insert_pos = len(chars) - 1
        else:
            insert_pos = len(chars)
        chars.insert(insert_pos, ")" * len(stack))

    new_lines.append("".join(chars))

fixed_text = "".join(new_lines)
Fixed_path.write_text(fixed_text, encoding=encoding)

if errors:
    print("Найдено и исправлено ошибок:", len(errors))
    for e in errors:
        print(e)
else:
    print("Ошибок не найдено.")

print("Исправленный текст сохранен в Ex5NEW.txt")

open_count = len(re.findall(r"\(", fixed_text))
close_count = len(re.findall(r"\)", fixed_text))
print(f"Открывающих скобок: {open_count}, закрывающих: {close_count}")
