import json
import random as r
import re
from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Callable

Date_Pattern: re.Pattern[str] = re.compile(
    r"^(0[1-9]|[12]\d|3[01])\.(0[1-9]|1[0-2])\.(19|20)\d{2}$"
)  # дд.мм.гггг

FileName = "Data.json"
CWD: Path = Path(__file__).resolve().parent
DataPath: Path = CWD / FileName
encoding = "utf-8"


def validate_date(date_str: str) -> bool:
    if not Date_Pattern.match(date_str):
        return False
    try:
        datetime.strptime(date_str, "%d.%m.%Y")
        return True
    except ValueError:
        return False


@dataclass(frozen=True)
class Phone(ABC):
    Name: str
    Address: str
    PhoneNumber: str

    @abstractmethod
    def __str__(self) -> str: ...
    @abstractmethod
    def matches_Name(self, name) -> bool: ...


@dataclass(frozen=True)
class PersonalPhone(Phone):
    def __str__(self) -> str:
        return f"""
Last Name: {self.Name}
Address: {self.Address}
Phone Number: {self.PhoneNumber}
""".strip()

    def matches_Name(self, name) -> bool:
        return self.Name == name


@dataclass(frozen=True)
class OfficePhone(Phone):
    Contact: str

    def __str__(self) -> str:
        return f"""
Office "{self.Name}"
Located at {self.Address}
Phone Number: {self.PhoneNumber}
Manager: {self.Contact}
""".strip()

    def matches_Name(self, name) -> bool:
        return self.Contact == name


@dataclass(frozen=True)
class FriendPhone(Phone):
    DateOfBirth: str

    def __post_init__(self) -> None:
        if not validate_date(self.DateOfBirth):
            raise ValueError(
                f"Date of Birth must be a correct date type. Given: {self.DateOfBirth}"
            )

    def __str__(self) -> str:
        return f"""
Last Name: {self.Name}
Date of birth: {self.DateOfBirth}
Address: {self.Address}
Phone Number: {self.PhoneNumber}
""".strip()

    def matches_Name(self, name) -> bool:
        return self.Name == name


def main() -> None:
    data: dict[str, list[str]] = json.loads(DataPath.read_text(encoding=encoding))
    PhoneFactories: dict[int, Callable[[dict[str, list[str]]], Phone]] = {
        1: lambda data: PersonalPhone(
            Name=r.choice(data["LastName"]),
            Address=r.choice(data["Address"]),
            PhoneNumber=r.choice(data["PhoneNumber"]),
        ),
        2: lambda data: OfficePhone(
            Name=r.choice(data["Office"]),
            Address=r.choice(data["Address"]),
            PhoneNumber=r.choice(data["PhoneNumber"]),
            Contact=r.choice(data["LastName"]),
        ),
        3: lambda data: FriendPhone(
            Name=r.choice(data["LastName"]),
            Address=r.choice(data["Address"]),
            PhoneNumber=r.choice(data["PhoneNumber"]),
            DateOfBirth=r.choice(data["Date"]),
        ),
    }
    PhonesAmount: int = r.randint(1, 10)
    PhonesList: list[Phone] = [
        PhoneFactories[r.randint(1, len(PhoneFactories))](data)
        for _ in range(PhonesAmount)
    ]
    SearchedName: str = r.choice(data["LastName"])
    print(f"Searching for {SearchedName}")
    output: list[Phone] = [
        phone for phone in PhonesList if phone.matches_Name(SearchedName)
    ]
    print(f"Found: {len(output)}")
    if output:
        for w in output:
            print(w, end="\n\n")


if __name__ == "__main__":
    main()
