import json
import random as r
from abc import ABC, abstractmethod
from dataclasses import dataclass
from pathlib import Path
from typing import Callable

FileName = "Data.json"
CWD: Path = Path(__file__).resolve().parent
DataPath: Path = CWD / FileName
encoding = "utf-8"


def ValidateAge(value) -> bool:
    return isinstance(value, int) and value > 0


def ValidatePrice(price) -> bool:
    return (isinstance(price, (float, int))) and price > 0


@dataclass
class Item(ABC):
    Title: str
    Price: float
    Age: int

    @abstractmethod
    def can_buy(self, Age: int) -> bool: ...

    def __str__(self) -> str:
        return f"""
{self.Title}:
{self.Price=}, can be used from {self.Age} y.o.
        """.strip()

    def __post_init__(self) -> None:
        if not ValidateAge(self.Age):
            raise ValueError(f"Given age: {self.Age} must be an integer!")

        if not ValidatePrice(self.Price):
            raise ValueError(f"Given price: {self.Price} must be bigger than 0!")


@dataclass
class Toy(Item):
    Manufacturer: str
    Material: str

    def can_buy(self, Age: int) -> bool:
        return self.Age <= Age

    def __str__(self) -> str:
        return super().__str__() + f"\n{self.Manufacturer=}, made of {self.Material}"


@dataclass
class Book(Item):
    Author: str
    Edition: str

    def can_buy(self, Age: int) -> bool:
        return self.Age <= Age

    def __str__(self) -> str:
        return (
            super()
            .__str__()
            .replace(
                f"{self.Title}",
                f"{self.Title} written by {self.Author}. Edition: {self.Edition}",
            )
        )


@dataclass
class SportsInventory(Item):
    Manufacturer: str

    def can_buy(self, Age: int) -> bool:
        return self.Age <= Age

    def __str__(self) -> str:
        return (
            super()
            .__str__()
            .replace(f"{self.Title}", f"{self.Title} made by {self.Manufacturer}")
        )


def main() -> None:
    data: dict[str, list[str]] = json.loads(DataPath.read_text(encoding=encoding))
    ItemsFactories: dict[int, Callable[[dict[str, list[str]]], Item]] = {
        1: lambda data: Toy(
            Title=r.choice(data["Toy"]),
            Price=r.randint(10, 100),
            Age=r.randint(1, 10),
            Manufacturer=r.choice(data["Manufacturer"]),
            Material=r.choice(data["Material"]),
        ),
        2: lambda data: Book(
            Title=r.choice(data["Title"]),
            Price=r.randint(150, 400),
            Age=r.randint(12, 20),
            Edition=r.choice(data["Edition"]),
            Author=r.choice(data["Author"]),
        ),
        3: lambda data: SportsInventory(
            Title=r.choice(data["SportEquipmentTitle"]),
            Price=r.randint(300, 1000),
            Age=r.randint(16, 20),
            Manufacturer=r.choice(data["Manufacturer"]),
        ),
    }
    ItemsAmount: int = r.randint(1, 10)
    print(f"Initializing {ItemsAmount} items of {len(ItemsFactories)} types")
    ItemsList: list[Item] = [
        ItemsFactories[r.randint(1, len(ItemsFactories))](data)
        for _ in range(ItemsAmount)
    ]
    SearchedAge: int = r.randint(1, 18)
    print(f"Searching for items which age restriction is below {SearchedAge}")
    output: list[Item] = [item for item in ItemsList if item.can_buy(SearchedAge)]
    print(f"Found: {len(output)}")
    if output:
        for w in output:
            print(w, end="\n\n")


if __name__ == "__main__":
    main()
