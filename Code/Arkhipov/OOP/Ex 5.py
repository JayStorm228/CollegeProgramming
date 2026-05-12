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
ItemFactory = Callable[[dict[str, list[str]]], "Item"]
FileName = "Data.json"
CWD: Path = Path(__file__).resolve().parent
DataPath: Path = CWD / FileName
encoding = "utf-8"


def parse_date(date_str: str) -> date:
    """Parse a string in dd.mm.yyyy format into a date object with validation."""
    if not DATE_PATTERN.match(date_str):
        raise ValueError(f"{date_str!r} does not match the dd.mm.yyyy format")
    try:
        return datetime.strptime(date_str, "%d.%m.%Y").date()
    except ValueError as err:
        raise ValueError(f"{date_str!r} is not a valid calendar date") from err


def validate_Positive(number: float) -> None:
    if number <= 0:
        raise ValueError(f"Number must be greater than 0. Given: {number!r}")


def validate_DateOrder(create_dt: date, expire_dt: date) -> None:
    if create_dt > expire_dt:
        raise ValueError(
            f"Expire date ({expire_dt}) must be later than create date ({create_dt})"
        )


@dataclass
class Item(ABC):
    name: str
    price: float

    def __post_init__(self) -> None:
        validate_Positive(self.price)

    @abstractmethod
    def can_buy(self, money: float) -> bool: ...

    @abstractmethod
    def __str__(self) -> str: ...


@dataclass
class Product(Item):
    create_date: date
    expire_date: date

    def __post_init__(self) -> None:
        super().__post_init__()
        validate_DateOrder(self.create_date, self.expire_date)

    @classmethod
    def from_strings(
        cls, name: str, price: float, create_str: str, expire_str: str
    ) -> "Product":
        """Helper constructor: accepts date strings."""
        create_dt: date = parse_date(create_str)
        expire_dt: date = parse_date(expire_str)

        return cls(name=name, price=price, create_date=create_dt, expire_date=expire_dt)

    def can_buy(self, money: float) -> bool:
        return money >= self.price

    def __str__(self) -> str:
        return f"""
Продукт: {self.name!r}
Цена: {self.price:.2f}$
Дата изготовления: {self.create_date}
Годен до: {self.expire_date}
            """.strip()


@dataclass
class Supply(Item):
    create_date: date
    expire_date: date
    amount: int

    def __post_init__(self) -> None:
        super().__post_init__()
        validate_DateOrder(self.create_date, self.expire_date)
        validate_Positive(self.amount)

    @classmethod
    def from_strings(
        cls,
        name: str,
        price: float,
        amount: int,
        create_str: str,
        expire_str: str,
    ) -> "Supply":
        create_dt: date = parse_date(create_str)
        expire_dt: date = parse_date(expire_str)

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
        return f"""
Поставка: {self.name!r}
Количество продукта: {self.amount}
Стоимость: {self.cost:.2f}$
Дата изготовления: {self.create_date}
Годна до: {self.expire_date}
    """.strip()


@dataclass
class Phone(Item):
    def can_buy(self, money: float) -> bool:
        return money >= self.price

    def __str__(self) -> str:
        return f"""
Телефон: {self.name}
Цена: {self.price}$
    """.strip()


def main() -> None:
    data: dict[str, list[str]] = json.loads(DataPath.read_text(encoding=encoding))
    ItemsFactories: dict[int, ItemFactory] = {
        1: lambda data: Product.from_strings(
            name=r.choice(data["Product"]),
            price=r.randint(100, 500),
            create_str=r.choice(data["Date"][:29]),
            expire_str=r.choice(data["Date"][29:]),
        ),
        2: lambda data: Supply.from_strings(
            name=r.choice(data["Product"]),
            price=r.randint(100, 300),
            create_str=r.choice(data["Date"][:29]),
            expire_str=r.choice(data["Date"][29:]),
            amount=r.randint(1, 10),
        ),
        3: lambda data: Phone(
            name=r.choice(data["PhoneModel"]),
            price=r.randint(100, 500),
        ),
    }
    ItemsAmount: int = r.randint(5, 20)
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
