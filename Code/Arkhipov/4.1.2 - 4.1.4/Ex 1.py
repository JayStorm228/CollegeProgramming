import math as m
import random as r
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Callable, TypeAlias

FigureFactory: TypeAlias = Callable[[], "Figure"]


class Figure(ABC):
    @property
    @abstractmethod
    def area(self) -> float:
        pass

    @property
    @abstractmethod
    def perimeter(self) -> float:
        pass


@dataclass
class Rect(Figure):
    _length: float = 0.0
    _width: float = 0.0

    def __post_init__(self) -> None:
        self.length = self._length
        self.width = self._width

    @property
    def length(self) -> float:
        return self._length

    @property
    def width(self) -> float:
        return self._width

    @length.setter
    def length(self, value: int | float) -> None:
        if value <= 0:
            raise ValueError("Length cannot be negative!")
        self._length = float(value)

    @width.setter
    def width(self, value: int | float) -> None:
        if value <= 0:
            raise ValueError("Width cannot be negative!")
        self._width = float(value)

    @property
    def area(self) -> float:
        return self.length * self.width

    @property
    def perimeter(self) -> float:
        return (self.length + self.width) * 2

    def __str__(self) -> str:
        return f"""
Rectangle
Length: {self.length}
Width: {self.width}
Area: {self.area:.4f}
Perimeter: {self.perimeter:.4f}
        """.strip()


@dataclass
class Circle(Figure):
    _radius: float = 0.0

    def __post_init__(self) -> None:
        self.radius = self._radius

    @property
    def radius(self) -> float:
        return self._radius

    @radius.setter
    def radius(self, value: int | float) -> None:
        if value <= 0:
            raise ValueError("Radius cannot be negative!")
        self._radius = value

    @property
    def area(self) -> float:
        return m.pi * self.radius**2

    @property
    def perimeter(self) -> float:
        return 2 * m.pi * self.radius

    def __str__(self) -> str:
        return f"""
Circle
Radius: {self._radius}
Area: {self.area:.4f}
Perimeter: {self.perimeter:.4f}
        """.strip()


@dataclass
class Triangle(Figure):
    _sides: tuple[float, float, float] = (0.0, 0.0, 0.0)

    def __post_init__(self) -> None:
        self.sides = self._sides

    @property
    def sides(self) -> tuple[float, float, float]:
        return self._sides

    @sides.setter
    def sides(self, value: tuple[float, float, float]) -> None:
        if len(value) != 3 or any(s <= 0 for s in value):
            raise ValueError(f"Invalid sides: {value} — each side must be > 0")
        a, b, c = sorted(value)
        if a + b <= c:
            raise ValueError(f"Invalid triangle: {value} (a+b={a+b} <= c={c})")
        self._sides = value

    @property
    def area(self) -> float:
        a, b, c = self._sides
        half_perimeter: float = (a + b + c) / 2
        return (
            half_perimeter
            * (half_perimeter - a)
            * (half_perimeter - b)
            * (half_perimeter - c)
        ) ** 0.5

    @property
    def perimeter(self) -> float:
        return sum(self._sides)

    def __str__(self) -> str:
        return f"""
Triangle
Sides(a, b, c): {', '.join(map(str, self.sides))}
Area: {self.area:.4f}
Perimeter: {self.perimeter:.4f}
        """.strip()


def random_triangle() -> Triangle:
    while True:
        sides: tuple[int, int, int] = (
            r.randint(1, 50),
            r.randint(1, 50),
            r.randint(1, 50),
        )
        try:
            return Triangle(sides)
        except ValueError:
            continue


def main() -> None:
    FigureFactories: dict[int, FigureFactory] = {
        1: lambda: Circle(r.randint(1, 10)),  # radius = random
        2: lambda: Rect(r.randint(1, 10), r.randint(1, 10)),
        3: lambda: random_triangle(),
    }
    FiguresAmount: int = r.randint(5, 10)
    print(f"Initializing {FiguresAmount} figures of {len(FigureFactories)} types...\n")
    FiguresList: list[Figure] = [
        FigureFactories[r.randint(1, len(FigureFactories))]()
        for _ in range(FiguresAmount)
    ]
    for w in FiguresList:
        print(f"{w}\n\n")


if __name__ == "__main__":
    main()
