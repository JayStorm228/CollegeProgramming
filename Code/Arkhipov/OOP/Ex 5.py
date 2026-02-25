import json
import random as r
import re
from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import date, datetime
from pathlib import Path
from typing import Callable

# Шаблон "дд.мм.гггг"
DATE_PATTERN: re.Pattern[str] = re.compile(
    r"^(0[1-9]|[12]\d|3[01])\.(0[1-9]|1[0-2])\.(19|20)\d{2}$"
)


def parse_date(date_str: str) -> date:
    """Parse a string in dd.mm.yyyy format into a date object with validation."""
    if not DATE_PATTERN.match(date_str):
        raise ValueError(f"{date_str!r} does not match the dd.mm.yyyy format")
    try:
        return datetime.strptime(date_str, "%d.%m.%Y").date()
    except ValueError as err:
        raise ValueError(f"{date_str!r} is not a valid calendar date") from err


FileName = "Data.json"
CWD: Path = Path(__file__).resolve().parent
DataPath: Path = CWD / FileName
encoding = "utf-8"


def validate_positive(number) -> bool:
    try:
        return float(number) > 0
    except (TypeError, ValueError):
        return False


@dataclass
class Item(ABC):
    name: str
    price: float

    def __post_init__(self) -> None:
        if not validate_positive(self.price):
            raise ValueError(
                f"{self.price} is invalid: price must be a non-negative number"
            )

    @abstractmethod
    def can_buy(self, money: float) -> bool: ...

    @abstractmethod
    def __str__(self) -> str: ...


@dataclass
class Product(Item):
    create_date: date
    expire_date: date

    @classmethod
    def from_strings(
        cls, name: str, price: float, create_str: str, expire_str: str
    ) -> "Product":
        """Helper constructor: accepts date strings."""
        create_dt: date = parse_date(create_str)
        expire_dt: date = parse_date(expire_str)
        if create_dt > expire_dt:
            raise ValueError(
                f"Expire date ({expire_str}) must be later than create date ({create_str})"
            )
        return cls(name=name, price=price, create_date=create_dt, expire_date=expire_dt)

    def can_buy(self, money: float) -> bool:
        return money >= self.price

    def __str__(self) -> str:
        return (
            f"Product(name={self.name!r}, price={self.price:.2f}, "
            f"create_date={self.create_date.isoformat()}, "
            f"expire_date={self.expire_date.isoformat()})"
        )


@dataclass
class Supply(Item):
    create_date: date
    expire_date: date
    amount: int

    @classmethod
    def from_strings(
        cls,
        name: str,
        price: float,
        amount: int,
        create_str: str,
        expire_str: str,
    ) -> "Supply":
        if not validate_positive(amount):
            raise ValueError(
                f'Amount "{amount}" is invalid — it must be a non-negative number'
            )
        create_dt: date = parse_date(create_str)
        expire_dt: date = parse_date(expire_str)
        if create_dt > expire_dt:
            raise ValueError(
                f"Expire date ({expire_str}) must be later than create date ({create_str})"
            )
        return cls(
            name=name,
            price=price,
            amount=amount,
            create_date=create_dt,
            expire_date=expire_dt,
        )

    @property
    def cost(self) -> float:
        return self.price * self.amount

    def can_buy(self, money: float) -> bool:
        return money >= self.cost

    def __str__(self) -> str:
        return (
            f"Supply(name={self.name!r}, price={self.price:.2f}, amount={self.amount}, "
            f"cost={self.cost:.2f}, "
            f"create_date={self.create_date.isoformat()}, "
            f"expire_date={self.expire_date.isoformat()})"
        )


@dataclass
class Phone(Item):
    def can_buy(self, money: float) -> bool:
        return money >= self.price

    def __str__(self) -> str:
        return f"Phone(name={self.name!r}, price={self.price:.2f})"


def main() -> None:
    data: dict[str, list[str]] = json.loads(DataPath.read_text(encoding=encoding))
    ItemsFactories: dict[int, Callable[[dict[str, list[str]]], Item]] = {
        1: lambda data: Product.from_strings(
            name=r.choice(data["Product"]),
            price=r.randint(100, 500),
            create_str=r.choice(data["Date"]),
            expire_str=r.choice(data["Date"]),
        ),
        2: lambda data: Supply.from_strings(
            name=r.choice(data["Product"]),
            price=r.randint(100, 300),
            create_str=r.choice(data["Date"]),
            expire_str=r.choice(data["Date"]),
            amount=r.randint(1, 10),
        ),
        3: lambda data: Phone(
            name=r.choice(data["PhoneModel"]),
            price=r.randint(100, 500),
        ),
    }
    ItemsAmount: int = r.randint(1, 10)
    print(f"Initializing {ItemsAmount} items of {len(ItemsFactories)} types")
    SearchedCost: int = r.randint(300, 10000)
    print(f"Searching for items cheaper than {SearchedCost}$")
    ItemsList: list[Item] = [
        ItemsFactories[r.randint(1, len(ItemsFactories))](data)
        for _ in range(ItemsAmount)
    ]
    output: list[Item] = [item for item in ItemsList if item.can_buy(SearchedCost)]
    print(f"Found: {len(output)}")
    if output:
        for w in output:
            print(w, end="\n\n")


if __name__ == "__main__":
    main()
