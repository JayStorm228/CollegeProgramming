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
FileName = "Data.json"
CWD: Path = Path(__file__).resolve().parent
DataPath: Path = CWD / FileName
encoding = "utf-8"


# Для валидации данных
def Validate_Price(value) -> None:
    if not (isinstance(value, int | float) and value > 0):
        raise ValueError(
            f"Price must be a positive float or int value! Given: {value!r} of type {type(value)}"
        )


def Validate_Date(obj: object, name: str = "value") -> None:
    if not isinstance(obj, date):
        raise TypeError(f"{name.capitalize()} must be a date object, got {type(obj)!r}")


def Validate_DateOrder(install_date: date, expire_date: date) -> None:
    if install_date >= expire_date:
        raise ValueError(
            f"Install date must be earlier than Expire date! "
            f"Given: Install date: {install_date}, Expire Date: {expire_date}"
        )


def parse_date(date_str: str) -> date:
    """Parse a string in dd.mm.yyyy format into a date object with validation."""
    if not DATE_PATTERN.match(date_str):
        raise ValueError(f"{date_str!r} does not match the dd.mm.yyyy format")
    try:
        return datetime.strptime(date_str, "%d.%m.%Y").date()
    except ValueError as err:
        raise ValueError(f"{date_str!r} is not a valid calendar date") from err


@dataclass
class Software(ABC):
    Title: str
    Manufacturer: str

    @abstractmethod
    def __str__(self) -> str: ...
    @abstractmethod
    def match_InstallDate(self, date: date | str) -> bool: ...


@dataclass
class OpenSourceSoftware(Software):
    def __str__(self) -> str:
        return f"""
Software:
    Type: OpenSource
    Title: {self.Title!r}
    Made by {self.Manufacturer}
        """.strip()

    def match_InstallDate(self, date) -> bool:
        return True


@dataclass
class CommercialSoftware(Software):
    Price: float | int
    InstallDate: date
    ExpireDate: date

    def __post_init__(self) -> None:
        Validate_Price(self.Price)
        Validate_Date(self.InstallDate, name="Install Date")
        Validate_Date(self.ExpireDate, name="Expire Date")
        Validate_DateOrder(self.InstallDate, self.ExpireDate)

    def match_InstallDate(self, date: date | str) -> bool:
        date = parse_date(date) if isinstance(date, str) else date
        return self.ExpireDate >= date

    def __str__(self) -> str:
        return f"""
Software:
    Type: Commercial
    Title: {self.Title!r}
    Made by: {self.Manufacturer}
    Installed on {self.InstallDate}
    Valid through {self.ExpireDate}
""".strip()

    @classmethod
    def Date_str(
        cls,
        Title: str,
        Manufacturer: str,
        Price: float | int,
        InstallDate_str: str,
        ExpireDate_str: str,
    ) -> "CommercialSoftware":
        return cls(
            Title=Title,
            Manufacturer=Manufacturer,
            Price=Price,
            InstallDate=parse_date(InstallDate_str),
            ExpireDate=parse_date(ExpireDate_str),
        )


@dataclass
class FreemiumSoftware(Software):
    InstallDate: date
    TrialExpireDate: date

    def __post_init__(self):
        Validate_Date(self.InstallDate, name="Install Date")
        Validate_Date(self.TrialExpireDate, name="Trial Expire Date")
        Validate_DateOrder(self.InstallDate, self.TrialExpireDate)

    def __str__(self) -> str:
        return f"""
Software:
    Type: Trial
    Title: {self.Title!r}
    Made by: {self.Manufacturer}
    Installed on {self.InstallDate}
    Trial valid through {self.TrialExpireDate}
""".strip()

    def match_InstallDate(self, date: date | str) -> bool:
        date = parse_date(date) if isinstance(date, str) else date
        return self.TrialExpireDate >= date

    @classmethod
    def Date_str(
        cls,
        Title: str,
        Manufacturer: str,
        InstallDate_str: str,
        TrialExpireDate_str: str,
    ) -> "FreemiumSoftware":
        return cls(
            Title=Title,
            Manufacturer=Manufacturer,
            InstallDate=parse_date(InstallDate_str),
            TrialExpireDate=parse_date(TrialExpireDate_str),
        )


def main() -> None:
    data: dict[str, list[str]] = json.loads(DataPath.read_text(encoding=encoding))
    SoftwareFactories: dict[int, Callable[[dict[str, list[str]]], Software]] = {
        1: lambda data: CommercialSoftware.Date_str(
            Title=r.choice(data["SoftwareTitle"]),
            Manufacturer=r.choice(data["SoftwareManufacturer"]),
            Price=round(r.uniform(500, 1000), 2),
            InstallDate_str=r.choice(data["Date"][:50]),
            ExpireDate_str=r.choice(data["Date"][51:]),
        ),
        2: lambda data: OpenSourceSoftware(
            Title=r.choice(data["SoftwareTitle"]),
            Manufacturer=r.choice(data["Manufacturer"]),
        ),
        3: lambda data: FreemiumSoftware.Date_str(
            Title=r.choice(data["SoftwareTitle"]),
            Manufacturer=r.choice(data["SoftwareManufacturer"]),
            InstallDate_str=r.choice(data["Date"][:50]),
            TrialExpireDate_str=r.choice(data["Date"][51:]),
        ),
    }
    SoftwareAmount: int = r.randint(5, 20)
    print(f"Initializing {SoftwareAmount} Softwares of {len(SoftwareFactories)} types")
    SoftwareList: list[Software] = [
        SoftwareFactories[r.randint(1, len(SoftwareFactories))](data)
        for _ in range(SoftwareAmount)
    ]
    SearchedInstallDate: str = r.choice(data["Date"][30:])
    print(f"Searching for Software available for use on {SearchedInstallDate}")
    output: list[Software] = [
        software
        for software in SoftwareList
        if software.match_InstallDate(SearchedInstallDate)
    ]
    print(f"Found: {len(output)}")
    if output:
        for w in output:
            print(w, end="\n\n")


if __name__ == "__main__":
    main()
