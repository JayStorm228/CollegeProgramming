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


@dataclass
class Vehicle(ABC):
    mark: str
    ID: str
    speed: float
    carrying_capacity: float

    @property
    @abstractmethod
    def carrying(self) -> float: ...

    def __str__(self) -> str:
        return f"""
Vehicle:
    mark: {self.mark}, ID: {self.ID}
    max speed: {self.speed}
    max carrying: {self.carrying_capacity}kg
""".strip()

    @abstractmethod
    def match_carrying(self, carrying) -> bool: ...


class Auto(Vehicle):

    @property
    def carrying(self) -> float:
        return self.carrying_capacity

    def __str__(self) -> str:
        return super().__str__().replace("Vehicle", "Auto")

    def match_carrying(self, carrying) -> bool:
        return self.carrying >= carrying


@dataclass
class Motorcycle(Vehicle):
    has_sidecar: bool = False

    @property
    def carrying(self) -> float:
        return self.carrying_capacity if self.has_sidecar else 0.0

    def __str__(self) -> str:
        return (
            super()
            .__str__()
            .replace("Vehicle", "Motorcycle")
            .replace(f"{self.carrying_capacity}", f"{self.carrying}")
        )

    def match_carrying(self, carrying) -> bool:
        return self.carrying >= carrying


@dataclass
class Truck(Vehicle):
    has_cargo: bool = False

    @property
    def carrying(self) -> float:
        return (
            (self.carrying_capacity * 2) if self.has_cargo else self.carrying_capacity
        )

    def __str__(self) -> str:
        return (
            super()
            .__str__()
            .replace("Vehicle", "Truck")
            .replace(f"{self.carrying_capacity}", f"{self.carrying}")
        )

    def match_carrying(self, carrying) -> bool:
        return self.carrying >= carrying


def main() -> None:
    data: dict[str, list[str]] = json.loads(DataPath.read_text(encoding=encoding))
    VehiclesFactories: dict[int, Callable[[dict[str, list[str]]], Vehicle]] = {
        1: lambda data: Auto(
            mark=r.choice(data["Mark"]),
            ID=r.choice(data["CarNumber"]),
            speed=r.randint(100, 200),
            carrying_capacity=r.randint(100, 200),
        ),
        2: lambda data: Motorcycle(
            mark=r.choice(data["Mark"]),
            ID=r.choice(data["CarNumber"]),
            speed=r.randint(100, 200),
            carrying_capacity=r.randint(100, 200),
            has_sidecar=bool(r.randint(0, 1)),
        ),
        3: lambda data: Truck(
            mark=r.choice(data["Mark"]),
            ID=r.choice(data["CarNumber"]),
            speed=r.randint(100, 200),
            carrying_capacity=r.randint(100, 200),
            has_cargo=bool(r.randint(0, 1)),
        ),
    }
    VehiclesAmount: int = r.randint(1, 10)
    print(f"Initializing {VehiclesAmount} vehicles of {len(VehiclesFactories)} types")
    SearchedCarrying: int = r.randint(150, 200)
    print(f"Searching for {SearchedCarrying}kg capacity vehicles")
    VehicleList: list[Vehicle] = [
        VehiclesFactories[r.randint(1, len(VehiclesFactories))](data)
        for _ in range(VehiclesAmount)
    ]
    output: list[Vehicle] = [
        vehicle for vehicle in VehicleList if vehicle.match_carrying(SearchedCarrying)
    ]
    print(f"Found: {len(output)}")
    if output:
        for w in output:
            print(w, end="\n\n")


if __name__ == "__main__":
    main()
