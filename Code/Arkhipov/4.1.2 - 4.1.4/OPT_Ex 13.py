import cmath
import random as r
import re
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Callable, List

LinearEquationPattern: re.Pattern[str] = re.compile(
    r"^\s*([-+]?(?:\d*\.?\d*(?:[eE][-+]?\d+)?)?)\s*[xX]\s*(?:([+-])\s*(\d*\.?\d*(?:[eE][-+]?\d+)?)|)\s*=\s*0\s*$"
)
QuadraticEquationPattern: re.Pattern[str] = re.compile(
    r"^\s*([-+]?(?:\d*\.?\d*(?:[eE][-+]?\d+)?)?)\s*[xX]\^2\s*((?:[+-]\s*\d*\.?\d*(?:[eE][-+]?\d+)?\s*[xX]\s*)?(?:[+-]\s*\d*\.?\d*(?:[eE][-+]?\d+)?)*)\s*=\s*0\s*$"
)


def Validate_Linear(Equation: str) -> None:
    if not bool(LinearEquationPattern.match(Equation)):
        raise ValueError(
            f"Equation does not match ax+b=0 or ax-b=0 pattern!\nGiven: {Equation}"
        )


def format_complex(z: complex, precision: int = 4) -> str:
    """Форматирует комплексное число до указанной точности."""
    real = round(z.real, precision)
    imag = round(z.imag, precision)

    if imag == 0:
        return f"{real:.{precision}f}"
    if real == 0:
        return f"{imag:+.{precision}f}j"
    return f"{real:.{precision}f}{imag:+.{precision}f}j"


@dataclass
class Equation(ABC):
    equation: str

    @property
    @abstractmethod
    def Solve(self) -> List[complex]: ...
    @abstractmethod
    def __str__(self) -> str: ...


@dataclass
class LinearEquation(Equation):
    """ax + b = 0"""

    def coefficients(self) -> tuple[float, float]:
        match = LinearEquationPattern.match(self.equation.strip())
        if not match:
            raise ValueError(f"Equation '{self.equation}' does not match pattern!")
        a_str, sign_b, b_str = match.groups()

        # Обработка a: '' или отсутствующий -> 1.0 по знаку
        if not a_str or a_str == "":
            a = 1.0
        elif a_str == "-":
            a = -1.0
        elif a_str == "+":
            a = 1.0
        else:
            a = float(a_str)

        # Обработка b: '' -> 0.0
        if not b_str or b_str == "":
            b = 0.0
        else:
            b_abs = float(b_str) if b_str else 0.0
            b = b_abs if sign_b == "+" else -b_abs

        return a, b

    @property
    def Solve(self) -> List[complex]:
        a, b = self.coefficients()
        if a == 0:
            raise ValueError("a cannot be zero in linear equation")
        return [complex(-b / a)]

    def __post_init__(self):
        if not LinearEquationPattern.match(self.equation.strip()):
            raise ValueError(f"Invalid linear equation: {self.equation}")

    def __str__(self) -> str:
        a, b = self.coefficients()
        [x] = self.Solve  # корень всегда один
        x_str = format_complex(x)

        return f"""
    Linear Equation: {self.equation}
    Coefficients: a = {a:.4f}, b = {b:.4f}
    Answer: x = {x_str}
    """.strip()


@dataclass
class QuadraticEquation(Equation):
    """ax^2+bx+c=0"""

    def coefficients(self) -> tuple[float, float, float]:
        match = QuadraticEquationPattern.match(self.equation.strip())
        if not match:
            raise ValueError(f"Equation '{self.equation}' does not match pattern!")

        a_str, remainder = match.groups()

        # Парсинг a (аналогично линейному: ''→1, '-'→-1)
        if not a_str or a_str == "":
            a = 1.0
        elif a_str == "-":
            a = -1.0
        else:
            a = float(a_str)

        # Парсинг хвоста remainder: +bx + c → (b, c)
        b, c = 0.0, 0.0
        if remainder:
            # Разбор по знакам [+-]
            terms = re.findall(
                r"([+-])\s*(\d*\.?\d*(?:[eE][-+]?\d+)?)\s*([xX]\^?2?)?", remainder
            )

            for sign, coef_str, var in terms:
                coef = float(coef_str) if coef_str else 1.0
                if var:  # содержит x → коэффициент при b
                    b += coef if sign == "+" else -coef
                else:  # константа → c
                    c += coef if sign == "+" else -coef

        return a, b, c

    @property
    def Solve(self) -> List[complex]:
        """Корни квадратного уравнения: x = [-b ± sqrt(D)] / (2a), D = b² - 4ac"""
        a, b, c = self.coefficients()

        if a == 0:
            raise ValueError("Деление на ноль: коэффициент a не может быть 0")

        D: float = b**2 - 4 * a * c  # дискриминант

        x1: complex = (-b + cmath.sqrt(D)) / (2 * a)
        x2: complex = (-b - cmath.sqrt(D)) / (2 * a)

        return [x1, x2] if x1 != x2 else [x1]

    def __post_init__(self):
        if not QuadraticEquationPattern.match(self.equation.strip()):
            raise ValueError(f"Invalid quadratic equation: {self.equation}")

    def __str__(self) -> str:
        a, b, c = self.coefficients()
        roots: List[complex] = self.Solve
        roots_str: str = ", ".join(format_complex(root) for root in roots)

        return f"""
    Quadratic Equation: {self.equation}
    Coefficients: a = {a:.4f}, b = {b:.4f}, c = {c:.4f}
    Roots: {roots_str}
    """.strip()


def main() -> None:
    EquationFactories: dict[int, Callable[[], Equation]] = {
        1: lambda: LinearEquation(
            f"{r.randint(0, 10)}x {r.choice(["+", "-"])} {r.randint(0, 10)} = 0"
        ),
        2: lambda: QuadraticEquation(
            f"{r.randint(-10, 10)}x^2 {r.choice(["+", "-"])} {r.randint(0, 10)}x {r.choice(["+", "-"])} {r.randint(0, 10)} = 0"
        ),
    }
    EquationAmount: int = r.randint(1, 10)
    EquationList: List[Equation] = [
        EquationFactories[r.randint(1, len(EquationFactories))]()
        for _ in range(EquationAmount)
    ]
    for equation in EquationList:
        print(equation, end="\n\n")


if __name__ == "__main__":
    main()
