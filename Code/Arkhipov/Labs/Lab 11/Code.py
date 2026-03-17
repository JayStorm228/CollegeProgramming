def validate_input(text: str) -> float:
    while True:
        try:
            return float(input(text))
        except ValueError:
            print("Значение должно быть дробным числом!")


def create_triangle() -> tuple[float, float, float]:
    while True:

        a: float = validate_input("Введите значение стороны а: ")
        b: float = validate_input("Введите значение стороны b: ")
        c: float = validate_input("Введите значение стороны c: ")
        if a <= 0 or b <= 0 or c <= 0:
            print(f"{a=}, {b=}, {c=}: Все стороны должны быть положительными: ")
            continue
        if a + b <= c or a + c <= b or b + c <= a:
            print(f"{a=}, {b=}, {c=}: Неравенство треугольника не выполняется")
            continue

        return a, b, c


def median(a: float, b: float, c: float) -> float:
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError(f"{a=}, {b=}, {c=}: Все стороны должны быть положительными: ")
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError(f"{a=}, {b=}, {c=}: Неравенство треугольника не выполняется")
    return (2 * b**2 + 2 * c**2 - a**2) ** 0.5


def main() -> None:
    a, b, c = create_triangle()
    median_A: float = median(a, b, c)
    median_B: float = median(b, a, c)
    median_C: float = median(c, a, b)
    print(
        f"""
Создан треугольник со сторонами: {a=}, {b=}, {c=}
Медианы:
    к стороне а: {median_A}
    к стороне b: {median_B}
    к стороне C: {median_C}
    """.strip()
    )
    input()


if __name__ == "__main__":
    main()
