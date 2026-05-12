def validate_input(text: str) -> float:
    while True:
        try:
            value = float(input(text))
        except ValueError:
            print(
                "Ошибка ввода: \nВведите десятичную дробь, десятичный разделитель: '.' \n"
            )
            continue
        else:
            return value


def check_point(x: float, y: float) -> str:
    area1: bool = all((y >= 2, y <= 0.5 * x**2, x**2 + (y - 1.5) ** 2 <= 6.28, x > 0))
    area2: bool = all((y <= 2, y >= 0.5 * x**2))
    area3: bool = all((y >= 2, y <= 0.5 * x**2, x**2 + (y - 1.5) ** 2 <= 6.28, x < 0))

    if any((area1, area2, area3)):
        return f"Точка ({x}, {y}) принадлежит области"
    else:
        return f"Точка ({x}, {y}) не принадлежит области"


def main() -> None:
    x: float = validate_input("Введите значение x: ")
    y: float = validate_input("Введите значение y: ")
    print(check_point(x, y))


if __name__ == "__main__":
    main()
