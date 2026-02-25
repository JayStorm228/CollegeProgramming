import random as r
from abc import ABC, abstractmethod
from math import cos, radians, sin
from typing import Callable


class Triangle(ABC):
    def __init__(self, side1: float, side2: float, angle_12: float) -> None:
        self.Side1: float = side1
        self.Side2: float = side2
        self.Angle_12: float = angle_12
        self._validate_triangle()

    def _validate_triangle(self) -> None:
        if self.Side1 <= 0 or self.Side2 <= 0:
            raise ValueError(
                f"Стороны должны быть > 0: Side1={self.Side1}, Side2={self.Side2}"
            )

        if not (0 < self.Angle_12 < 180):
            raise ValueError(
                f"Угол Angle_12 должен быть в (0°, 180°): {self.Angle_12}°"
            )

        side3 = self.Side3
        if (
            self.Side1 + self.Side2 <= side3
            or self.Side1 + side3 <= self.Side2
            or self.Side2 + side3 <= self.Side1
        ):
            raise ValueError(
                f"Неравенство треугольника нарушено: {self.Side1}, {self.Side2}, {side3}"
            )

    @property
    def Side3(self) -> float:
        angle_rad = radians(self.Angle_12)
        side3_sq = (
            self.Side1**2 + self.Side2**2 - 2 * self.Side1 * self.Side2 * cos(angle_rad)
        )
        if side3_sq < 0:
            raise ValueError("Side3^2 < 0 — невозможно!")
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


class RightTriangle(Triangle):
    """Прямоугольный: угол между Side1 и Side2 = 90°"""

    def __init__(self, leg1: float, leg2: float) -> None:
        super().__init__(leg1, leg2, 90.0)

    @property
    def area(self) -> float:
        return 0.5 * self.Side1 * self.Side2

    @property
    def perimeter(self) -> float:
        return self.Side1 + self.Side2 + self.Side3

    def __str__(self) -> str:
        return super().__str__() + "\nType: Right"


class IsoscelesTriangle(Triangle):
    """Равнобедренный: Side2 = боковая сторона, угол между основанием и боковой."""

    def __init__(self, base: float, leg: float, angle_base_leg: float) -> None:
        # angle_base_leg — угол между основанием (base) и боковой (leg)
        super().__init__(base, leg, angle_base_leg)

    @property
    def area(self) -> float:
        return self.Side1 * self.Side2 * sin(radians(self.Angle_12)) / 2

    @property
    def perimeter(self) -> float:
        return self.Side1 + self.Side2 + self.Side3

    def __str__(self) -> str:
        return super().__str__() + "\nType: Isosceles"


class EquilateralTriangle(Triangle):
    """Равносторонний: все стороны равны, угол = 60°."""

    def __init__(self, side: float) -> None:
        super().__init__(side, side, 60.0)

    @property
    def area(self) -> float:
        return (self.Side1**2 * 3**0.5) / 4

    @property
    def perimeter(self) -> float:
        return 3 * self.Side1

    def __str__(self) -> str:
        return super().__str__() + "\nType: Equilateral"


def main() -> None:
    TriangleFactories: dict[int, Callable[[], Triangle]] = {
        1: lambda: RightTriangle(leg1=r.randint(1, 100), leg2=r.randint(1, 100)),
        2: lambda: IsoscelesTriangle(
            base=r.randint(1, 100),
            leg=r.randint(1, 100),
            angle_base_leg=r.randint(1, 90),
        ),
        3: lambda: EquilateralTriangle(side=r.randint(1, 100)),
    }
    TrianglesAmount: int = r.randint(1, 10)
    print(f"Initializing {TrianglesAmount} triangles of {len(TriangleFactories)} types")
    TrianglesList: list[Triangle] = [
        TriangleFactories[r.randint(1, len(TriangleFactories))]()
        for _ in range(TrianglesAmount)
    ]
    for w in TrianglesList:
        print(w, end="\n\n")


if __name__ == "__main__":
    main()
