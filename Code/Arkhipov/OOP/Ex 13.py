import random as r
import re
from abc import ABC, abstractmethod
from dataclasses import dataclass

LinearEquationPattern: re.Pattern[str] = re.compile(
    r"^\s*([-+]?(?:\d*\.?\d*(?:[eE][-+]?\d+)?)?)\s*[xX]\s*(?:([+-])\s*(\d*\.?\d*(?:[eE][-+]?\d+)?)|)\s*=\s*0\s*$"
)


def Validate_Linear(Equation: str) -> None:
    if not isinstance(Equation, str):
        raise ValueError(f"Equation must be a string!\nGiven: {type(Equation)}")
    if not bool(LinearEquationPattern.match(Equation)):
        raise ValueError(
            f"Equation does not match ax+b=0 or ax-b=0 pattern!\nGiven: {Equation}"
        )


@dataclass
class Equation(ABC):
    equation: str

    @property
    @abstractmethod
    def Solve(self) -> list[float | int]: ...

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
    def Solve(self) -> list[float | int]:
        a, b = self.coefficients()
        if a == 0:
            raise ValueError("a cannot be zero in linear equation")
        return [-b / a]

@dataclass
class QuadraticEquation(Equation):


def main() -> None:
    equation: LinearEquation = LinearEquation(
        equation=f"{r.randint(-10,10)}x {r.randint(1,10)} = 0"
    )
    print(equation.equation, equation.coefficients())


if __name__ == "__main__":
    main()
