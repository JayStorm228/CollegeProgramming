import json
import random as r
import re
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import date, datetime
from pathlib import Path
from typing import Callable

DATE_PATTERN: re.Pattern[str] = re.compile(
    r"^(0[1-9]|[12]\d|3[01])\.(0[1-9]|1[0-2])\.(19|20)\d{2}$"
)  # дд.мм.гггг

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


def Validate_Money(value) -> None:
    if not (isinstance(value, float) and value >= 0):
        raise ValueError(
            f"Money amount must be a positive float value! Given: {value!r} of type {type(value)!r}"
        )


def Validate_InterestRate(value):
    if not (isinstance(value, float) and (0 < value < 1)):
        raise ValueError(
            f"Interest Rate must be a positive float value in (1,0)! Given: {value!r} of type {type(value)!r}"
        )


def generate_AccountNumber() -> str:
    balance = "40702"
    currency = "840"
    unused = "0"
    branch: str = f"{r.randint(1000, 9999):04d}"
    serial: str = f"{r.randint(1000000, 9999999):07d}"
    return f"{balance}{currency}{unused}{branch}{serial}"


@dataclass
class Client(ABC):
    Name: str
    OpenDate: date

    @abstractmethod
    def __str__(self) -> str: ...
    @abstractmethod
    def match_OpenDate(self, date: date | str) -> bool: ...
    @classmethod
    def Str_OpenDate(cls, Name: str, OpenDate_str: str, **kwargs) -> "Client":
        OpenDate: date = parse_date(OpenDate_str)
        return cls(Name=Name, OpenDate=OpenDate, **kwargs)


@dataclass
class Depositor(Client):
    DepositAmount: float
    InterestRate: float

    def __post_init__(self) -> None:
        Validate_Money(self.DepositAmount)
        Validate_InterestRate(self.InterestRate)

    def __str__(self) -> str:
        return f"""
Depositor {self.Name!r}:
    Deposit was opened on {self.OpenDate}
    Deposit amount: {self.DepositAmount}$
    Interest rate: {self.InterestRate*100}%
""".strip()

    def match_OpenDate(self, date: date | str) -> bool:
        date = parse_date(date) if isinstance(date, str) else date
        return self.OpenDate == date


@dataclass
class Creditor(Client):
    CreditAmount: float
    InterestRate: float

    def __post_init__(self) -> None:
        Validate_Money(self.CreditAmount)
        Validate_InterestRate(self.InterestRate)

    def __str__(self) -> str:
        return f"""
Creditor {self.Name!r}:
    Credit was taken on {self.OpenDate}
    Credit amount: {self.CreditAmount}$
    Interest rate: {self.InterestRate*100}%
""".strip()

    def match_OpenDate(self, date: date | str) -> bool:
        date = parse_date(date) if isinstance(date, str) else date
        return self.OpenDate == date


@dataclass
class Organization(Client):
    _AccountNumber: str = field(init=False)
    Balance: float

    @property
    def AccountNumber(self) -> str:
        return self._AccountNumber

    def __post_init__(self) -> None:
        Validate_Money(self.Balance)
        self._AccountNumber = generate_AccountNumber()

    def __str__(self) -> str:
        return f"""
Organization: {self.Name!r}
    Account was registered on {self.OpenDate}
    Account Number: {self.AccountNumber}
    Current Balance: {self.Balance}
""".strip()

    def match_OpenDate(self, date: date | str) -> bool:
        date = parse_date(date) if isinstance(date, str) else date
        return self.OpenDate == date


def main() -> None:
    data: dict[str, list[str]] = json.loads(DataPath.read_text(encoding=encoding))
    ClientFactories: dict[int, Callable[[dict[str, list[str]]], Client]] = {
        1: lambda data: Depositor.Str_OpenDate(
            Name=r.choice(data["LastName"]),
            OpenDate_str=r.choice(data["Date"]),
            DepositAmount=r.randint(1000, 100000),
            InterestRate=round(r.uniform(0.01, 0.5), 2),
        ),
        2: lambda data: Creditor.Str_OpenDate(
            Name=r.choice(data["LastName"]),
            OpenDate_str=r.choice(data["Date"]),
            CreditAmount=r.randint(1000, 100000),
            InterestRate=round(r.uniform(0.01, 0.5), 2),
        ),
        3: lambda data: Organization.Str_OpenDate(
            Name=r.choice(data["Office"]),
            OpenDate_str=r.choice(data["Date"]),
            Balance=round(r.uniform(1000, 100000), 2),
        ),
    }
    ClientsAmount: int = r.randint(1, 10)
    print(f"Initializing {ClientsAmount} clients of {len(ClientFactories)} types")
    ClientList: list[Client] = [
        ClientFactories[r.randint(1, len(ClientFactories))](data)
        for _ in range(ClientsAmount)
    ]
    SearchedOpenDate: str = r.choice(data["Date"])
    print(f"Searching for Clients, registered on {SearchedOpenDate}")
    output: list[Client] = [
        client for client in ClientList if client.match_OpenDate(SearchedOpenDate)
    ]
    print(f"Found: {len(output)}")
    if output:
        for w in output:
            print(w, end="\n\n")


if __name__ == "__main__":
    main()
