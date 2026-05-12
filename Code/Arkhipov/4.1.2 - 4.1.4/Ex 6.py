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
type ItemFactory = Callable[[dict[str, list[str]]], Item]


def ValidateAge(value: Any) -> None:
    if not isinstance(value, int):
        raise TypeError(f"Age must be an integer! Given: {type(value)!r}")
    if not value > 0:
        raise ValueError(f"Age must be greater than zero! Given: {value!r}")


def ValidatePrice(price: Any) -> None:
    if not isinstance(price, (float, int)):
        raise TypeError(f"Price must be a float or int value! Given: {type(price)}")
    if not price > 0:
        raise ValueError(f"Price must be greater than zero! Given: {price!r}")


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
Price is {self.Price}$, can be used from {self.Age} y.o.
        """.strip()

    def __post_init__(self) -> None:
        ValidatePrice(self.Price)
        ValidateAge(self.Age)


@dataclass
class Toy(Item):
    Manufacturer: str
    Material: str

    def can_buy(self, Age: int) -> bool:
        return self.Age <= Age

    def __str__(self) -> str:
        return super().__str__() + f"\nmade of {self.Material} by {self.Manufacturer!r}"


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
    ItemsFactories: dict[int, ItemFactory] = {
        1: lambda data: Toy(
            Title=r.choice(data["Toy"]),
            Price=r.randint(10, 100),
            Age=r.randint(1, 10),
            Manufacturer=r.choice(data["Manufacturer"]),
            Material=r.choice(data["Material"]),
        ),
        2: lambda data: Book(
            Title=r.choice(data["Titles"]),
            Price=r.randint(150, 400),
            Age=r.randint(12, 20),
            Edition=r.choice(data["Publishers"]),
            Author=r.choice(data["Author"]),
        ),
        3: lambda data: SportsInventory(
            Title=r.choice(data["SportEquipmentTitle"]),
            Price=r.randint(300, 1000),
            Age=r.randint(16, 20),
            Manufacturer=r.choice(data["Manufacturer"]),
        ),
    }
    ItemsAmount: int = r.randint(5, 15)
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
