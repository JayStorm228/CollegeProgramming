import random as r
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from math import cos, radians, sin
from typing import Callable, TypeAlias

TriangleFactory: TypeAlias = Callable[[], "Triangle"]


<<<<<<< HEAD:Code/Arkhipov/OOP/Ex 3.py
=======
def validate_triangle(triangle: "Triangle") -> None:
    if triangle.Side1 <= 0 or triangle.Side2 <= 0:
        raise ValueError(
            f"Стороны должны быть > 0: Side1={triangle.Side1}, Side2={triangle.Side2}"
        )

    if not (0 < triangle.Angle_12 <= 90):
        raise ValueError(
            f"Угол между двумя сторонами должен быть в (0°, 90°): {triangle.Angle_12}°"
        )
    side3 = triangle.Side3
    sides: list[float] = sorted((triangle.Side1, triangle.Side2, side3))
    if sides[0] + sides[1] < sides[2]:
        raise ValueError(
            f"Неравенство треугольника нарушено: {triangle.Side1}, {triangle.Side2}, {triangle.Side3}"
        )


>>>>>>> e0ee5b8 (4.1.2 - 4.1.4 and small overall changes):Code/Arkhipov/4.1.2 - 4.1.4/Ex 3.py
@dataclass
class Triangle(ABC):
    Side1: float
    Side2: float
    Angle_12: float
<<<<<<< HEAD:Code/Arkhipov/OOP/Ex 3.py

    def __post_init__(self) -> None:
        self._validate_triangle()

    def _validate_triangle(self) -> None:
        if self.Side1 <= 0 or self.Side2 <= 0:
            raise ValueError(
                f"Стороны должны быть > 0: Side1={self.Side1}, Side2={self.Side2}"
            )

        if not (0 < self.Angle_12 <= 90):
            raise ValueError(
                f"Угол между сторонами должен быть в (0°, 90°): {self.Angle_12}°"
            )

        side3: float = self.Side3
        sides: list[float] = sorted((self.Side1, self.Side2, side3))
        if sides[0] + sides[1] <= sides[2]:
            raise ValueError(
                f"Неравенство треугольника нарушено: {self.Side1}, {self.Side2}, {side3}"
            )
=======

    def __post_init__(self) -> None:
        validate_triangle(self)
>>>>>>> e0ee5b8 (4.1.2 - 4.1.4 and small overall changes):Code/Arkhipov/4.1.2 - 4.1.4/Ex 3.py

    @property
    def Side3(self) -> float:
        angle_rad: float = radians(self.Angle_12)
        side3_sq: float = (
            self.Side1**2 + self.Side2**2 - 2 * self.Side1 * self.Side2 * cos(angle_rad)
        )
        return side3_sq**0.5

    @property
    @abstractmethod
    def area(self) -> float: ...

    @property
    @abstractmethod
    def perimeter(self) -> float: ...

    def __str__(self) -> str:
        return f"""
Triangle:
    Side1 = {self.Side1:.2f}
    Side2 = {self.Side2:.2f}
    Side3 = {self.Side3:.2f}
    ∠(Side1, Side2) = {self.Angle_12:.2f}°
    ---
    Area = {self.area:.2f}
    Perimeter = {self.perimeter:.2f}
""".strip()


@dataclass
class RightTriangle(Triangle):
    """Прямоугольный: угол между Side1 и Side2 = 90°"""

    Angle_12: float = field(init=False, default=90)

    @property
    def area(self) -> float:
        return 0.5 * self.Side1 * self.Side2

    @property
    def perimeter(self) -> float:
        return self.Side1 + self.Side2 + self.Side3

    def __str__(self) -> str:
<<<<<<< HEAD:Code/Arkhipov/OOP/Ex 3.py
        return super().__str__() + "\n    Type: Right"
=======
        return super().__str__() + "\n    ---\n    Type: Right"
>>>>>>> e0ee5b8 (4.1.2 - 4.1.4 and small overall changes):Code/Arkhipov/4.1.2 - 4.1.4/Ex 3.py


@dataclass
class IsoscelesTriangle(Triangle):
    """Равнобедренный: Side2 = боковая сторона, угол между основанием и боковой."""

    @property
    def Side3(self) -> float:
        return self.Side2

    @property
    def area(self) -> float:
        return self.Side1 * self.Side2 * sin(radians(self.Angle_12)) / 2

    @property
    def perimeter(self) -> float:
        return self.Side1 + self.Side2 + self.Side3

    def __str__(self) -> str:
<<<<<<< HEAD:Code/Arkhipov/OOP/Ex 3.py
        return super().__str__() + "\n    Type: Isosceles"
=======
        return super().__str__() + "\n    ---\n    Type: Isosceles"
>>>>>>> e0ee5b8 (4.1.2 - 4.1.4 and small overall changes):Code/Arkhipov/4.1.2 - 4.1.4/Ex 3.py


@dataclass
class EquilateralTriangle(Triangle):
    """Равносторонний: все стороны равны, угол = 60°."""

<<<<<<< HEAD:Code/Arkhipov/OOP/Ex 3.py
    Side1: float = field(init=False)
    Side2: float = field(init=False)
    Angle_12: float = field(init=False)
=======
    Side1: float = field(init=False, repr=False)
    Side2: float = field(init=False, repr=False)
    Angle_12: float = field(init=False, repr=False)
>>>>>>> e0ee5b8 (4.1.2 - 4.1.4 and small overall changes):Code/Arkhipov/4.1.2 - 4.1.4/Ex 3.py
    Side: float

    def __post_init__(self) -> None:
        self.Side1 = self.Side
        self.Side2 = self.Side
        self.Angle_12 = 60
<<<<<<< HEAD:Code/Arkhipov/OOP/Ex 3.py
        self._validate_triangle()
=======
        super().__post_init__()
>>>>>>> e0ee5b8 (4.1.2 - 4.1.4 and small overall changes):Code/Arkhipov/4.1.2 - 4.1.4/Ex 3.py

    @property
    def area(self) -> float:
        return (self.Side**2 * 3**0.5) / 4

    @property
    def perimeter(self) -> float:
        return 3 * self.Side

    def __str__(self) -> str:
<<<<<<< HEAD:Code/Arkhipov/OOP/Ex 3.py
        return super().__str__() + "\n    Type: Equilateral"


def generate_RightTriangle() -> RightTriangle:
    while True:
        try:
            triangle = RightTriangle(Side1=r.randint(1, 100), Side2=r.randint(1, 100))
        except ValueError:
            continue
        else:
            return triangle


def generate_IsoscelesTriangle() -> IsoscelesTriangle:
    while True:
        try:
            triangle = IsoscelesTriangle(
                Side1=r.randint(1, 100),
                Side2=r.randint(1, 100),
                Angle_12=r.randint(1, 90),
            )
        except ValueError:
            continue
        else:
            return triangle


def generate_EquilateralTriangle() -> EquilateralTriangle:
    while True:
        try:
            triangle = EquilateralTriangle(Side=r.randint(1, 100))
        except ValueError:
            continue
        else:
            return triangle


def main() -> None:
    TriangleFactories: dict[int, TriangleFactory] = {
        1: generate_RightTriangle,
        2: generate_IsoscelesTriangle,
        3: generate_EquilateralTriangle,
=======
        return super().__str__() + "\n    ---\n    Type: Equilateral"


def main() -> None:
    TriangleFactories: dict[int, Callable[[], Triangle]] = {
        1: lambda: RightTriangle(Side1=r.randint(1, 100), Side2=r.randint(1, 100)),
        2: lambda: IsoscelesTriangle(
            Side1=r.randint(1, 100), Side2=r.randint(1, 100), Angle_12=r.randint(1, 45)
        ),
        3: lambda: EquilateralTriangle(Side=r.randint(1, 10)),
>>>>>>> e0ee5b8 (4.1.2 - 4.1.4 and small overall changes):Code/Arkhipov/4.1.2 - 4.1.4/Ex 3.py
    }
    TrianglesAmount: int = r.randint(5, 10)
    print(f"Initializing {TrianglesAmount} triangles of {len(TriangleFactories)} types")
    TrianglesList: list[Triangle] = [
        TriangleFactories[r.randint(1, len(TriangleFactories))]()
        for _ in range(TrianglesAmount)
    ]
    for w in TrianglesList:
        print(w, end="\n\n")


if __name__ == "__main__":
    main()
