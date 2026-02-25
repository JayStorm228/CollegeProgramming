import json
import random as r
from abc import ABC, abstractmethod
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable

FileName = "Data.json"
CWD: Path = Path(__file__).resolve().parent
DataPath: Path = CWD / FileName
encoding = "utf-8"


def Validate_Positive(value: Any, name: str = "value") -> None:
    if not (isinstance(value, float | int)):
        raise ValueError(
            f"{name.capitalize()!r} must be a number!\nGiven: {type(value)}"
        )
    if value < 0:
        raise ValueError(f"{name.capitalize()!r} must be a positive number!")


@dataclass
class Toy(ABC):
    Color: str
    Price: float  # $

    @abstractmethod
    def __str__(self) -> str: ...
    def match_color(self, color) -> bool:
        return self.Color == color

    def __post_init__(self) -> None:
        Validate_Positive(self.Price, "Price")


@dataclass
class Cube(Toy):
    Material: str
    EdgeSize: float  # cm

    def __str__(self) -> str:
        return f"""
A {self.Color} toy cube made of {self.Material}
Its edge size is {self.EdgeSize}
It costs {self.Price}$
""".strip()

    def __post_init__(self) -> None:
        super().__post_init__()
        Validate_Positive(self.EdgeSize, "Edge Size")


@dataclass
class Ball(Toy):
    Diameter: float  # cm
    Material: str

    def __str__(self) -> str:
        return f"""
A {self.Color} ball of {self.Diameter} cm diameter
It is made of {self.Material}
It costs {self.Price}$
""".strip()

    def __post_init__(self) -> None:
        super().__post_init__()
        Validate_Positive(self.Diameter, "Diameter")


@dataclass
class Car(Toy):
    Manufacturer: str
    Title: str

    def __str__(self) -> str:
        return f"""
A {self.Color} car named {self.Title!r}
it is made by {self.Manufacturer}
It costs {self.Price}$
"""


def main() -> None:
    data: dict[str, list[str]] = json.loads(DataPath.read_text(encoding=encoding))
    ToyFactories: dict[int, Callable[[dict[str, list[str]]], Toy]] = {
        1: lambda data: Cube(
            Color=r.choice(data["Color"]),
            Price=round(r.uniform(10, 50), 2),
            Material=r.choice(data["Material"]),
            EdgeSize=round(r.uniform(5, 15), 2),
        ),
        2: lambda data: Ball(
            Color=r.choice(data["Color"]),
            Price=round(r.uniform(30, 100), 2),
            Diameter=round(r.uniform(10, 30), 2),
            Material=r.choice(data["Material"]),
        ),
        3: lambda data: Car(
            Color=r.choice(data["Color"]),
            Price=round(r.uniform(100, 500), 2),
            Manufacturer=r.choice(data["Manufacturer"]),
            Title=r.choice(data["Mark"]),
        ),
    }
    ToyAmount: int = r.randint(1, 10)

    print(f"Initializing {ToyAmount} toys of {len(ToyFactories)} types")
    ToyList: list[Toy] = [
        ToyFactories[r.randint(1, len(ToyFactories))](data) for _ in range(ToyAmount)
    ]

    SearchedColor: str = r.choice(data["Color"])
    print(f"Searching for {SearchedColor} toys...")
    output: list[Toy] = [toy for toy in ToyList if toy.match_color(SearchedColor)]
    print(f"Found: {len(output)}")
    if output:
        for w in output:
            print(w, end="\n\n")


if __name__ == "__main__":
    main()
