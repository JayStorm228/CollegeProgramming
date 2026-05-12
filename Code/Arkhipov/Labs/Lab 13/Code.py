import random as r
from dataclasses import dataclass


@dataclass
class Triangle:
    Side1: float
    Side2: float
    Side3: float

    def __post_init__(self) -> None:
        self.Sides: list[float] = sorted((self.Side1, self.Side2, self.Side3))
        self._validate_triangle()

    def _validate_triangle(self) -> None:

        if any((x <= 0 for x in self.Sides)):
            raise ValueError(
                f"\nSides must be greater than 0: \
\n{', '.join(map(str, self.Sides))}"
            )

        if self.Sides[0] + self.Sides[1] <= self.Sides[2]:
            raise ValueError(
                f"\nTriangle inequality violated: \
\n{', '.join(map(str, self.Sides))}"
            )

    @property
    def area(self) -> float:
        HalfPerimeter = self.perimeter * 0.5
        return (
            HalfPerimeter
            * (HalfPerimeter - self.Side1)
            * (HalfPerimeter - self.Side2)
            * (HalfPerimeter - self.Side3)
        ) ** 0.5

    @property
    def perimeter(self) -> float:
        return sum(self.Sides)

    def __str__(self) -> str:
        return f"""
Triangle:
    Side1\t {self.Side1:.2f}
    Side2\t {self.Side2:.2f}
    Side3\t {self.Side3:.2f}
    -------------------------------------
    Area\t {self.area:.2f}
    Perimeter\t {self.perimeter:.2f}
    -------------------------------------
    Height to Side1\t {self.heights[0]:.2f}
    Height to Side2\t {self.heights[1]:.2f}
    Height to Side3\t {self.heights[2]:.2f}
""".strip()

    @property
    def heights(self) -> tuple[float, float, float]:
        s: float = self.area
        h1: float = 2 * s / self.Side1
        h2: float = 2 * s / self.Side2
        h3: float = 2 * s / self.Side3
        return (h1, h2, h3)


def main() -> None:
    while True:
        try:
            sides: list[int] = r.sample(range(-100, 100), 3)
            triangle = Triangle(*sides)
        except ValueError:
            continue
        else:
            print(triangle)
            break


if __name__ == "__main__":
    main()
