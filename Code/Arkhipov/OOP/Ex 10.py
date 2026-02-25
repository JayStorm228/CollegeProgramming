import json
import random as r
import time as t
from abc import ABC, abstractmethod
from dataclasses import dataclass
from itertools import count
from pathlib import Path
from typing import Callable, TypeAlias

import numpy as np
from numpy import int64
from numpy.typing import NDArray

# Типизация
MapArray: TypeAlias = NDArray[int64]
MapSlice: TypeAlias = NDArray[np.int_]
Coordinate: TypeAlias = tuple[int, int]


# Данные генерации
FileName = "Data.json"
CWD: Path = Path(__file__).resolve().parent
DataPath: Path = CWD / FileName
encoding = "utf-8"
_id_gen = count(1)
_index_gen = count(0)


class LocationMap:
    def __init__(self, x: int, y: int) -> None:
        self.Size: tuple[int, int] = x, y
        self.Map: MapArray = np.zeros(self.Size, dtype=int64)
        self.PlacedObjects: dict[int, "Vehicle"] = {}
        self.AvailableCoordinates: list[tuple[int, int]] = []

    def PlaceObject(self, obj: "Vehicle") -> None:
        x, y = obj.Cords
        if not (0 <= x < self.Map.shape[0] and 0 <= y < self.Map.shape[1]):
            raise ValueError(f"Coordinates {obj.Cords} out of map bounds")

        ID: int = next(_id_gen)
        self.Map[obj.Cords] = ID  # ID объекта в базе
        self.PlacedObjects[ID] = obj  # Добавление в базу объектов на карте
        print(f"Placed {obj.Mark!r} at x={obj.Cords[0]}, y={obj.Cords[1]}")

    def SearchBy_Area(
        self, X_slice: Coordinate, Y_slice: Coordinate
    ) -> list["Vehicle"]:
        x1, x2 = X_slice
        y1, y2 = Y_slice

        if not (
            0 <= x1 <= x2 <= self.Map.shape[0] and 0 <= y1 <= y2 <= self.Map.shape[1]
        ):
            raise ValueError(
                f"""
Selected area out of bounds!
Map size: {self.Map.shape[0]}x{self.Map.shape[1]}
Given: x={X_slice}, y={Y_slice}
""".strip()
            )

        SearchedArea: MapSlice = self.Map[x1:x2, y1:y2]
        FoundVehicleIDs: list[int] = SearchedArea[SearchedArea != 0].tolist()
        return [self.PlacedObjects[ID] for ID in FoundVehicleIDs]

    def GenerateCoordinate(self, ObjectAmount: int, seed: int = 42) -> None:
        np.random.seed(seed)  # воспроизводимость

        rows, cols = self.Size
        # Все возможные координаты как плоский индекс
        possible_flat: NDArray[int64] = np.arange(rows * cols)

        # Выбираем N уникальных индексов
        unique_flat: NDArray[int64] = np.random.choice(
            possible_flat, size=ObjectAmount, replace=False
        )

        # Преобразуем в (x, y)
        # Формула: index = x * cols + y
        x: NDArray[int64] = unique_flat // cols
        y: NDArray[int64] = unique_flat % cols
        self.AvailableCoordinates = list(zip(x, y, strict=True))

    def __len__(self) -> int:
        return self.Size[0] * self.Size[1]

    def __str__(self):
        return f"\n{self.Map}\n"


@dataclass
class Vehicle(ABC):
    Mark: str
    Cords: Coordinate

    @abstractmethod
    def __str__(self) -> str: ...


@dataclass
class Airplane(Vehicle):
    MaxSpeed: float  # kmh
    Maxheight: float  # m
    PassengersAmount: int

    def __str__(self) -> str:
        return f"""
Transport: Airplane {self.Mark!r}
    Maximum speed: {self.MaxSpeed}kmh
    Max height: {self.Maxheight}m
    Can carry {self.PassengersAmount} person
    Located at x={self.Cords[0]}, y={self.Cords[1]}
""".strip()


@dataclass
class Ship(Vehicle):
    MaxSpeed: float  # kmh
    PassengersAmount: int
    Port: str

    def __str__(self) -> str:
        return f"""
Transport: Ship {self.Mark!r}
    Maximum speed: {self.MaxSpeed}
    Can carry {self.PassengersAmount} person
    Located at x={self.Cords[0]}, y={self.Cords[1]}
""".strip()


@dataclass
class Auto(Vehicle):
    LicensePlate: str
    ReleaseYear: str

    def __str__(self) -> str:
        return f"""
Transport: Auto {self.Mark!r}
    License Plate: {self.LicensePlate}
    Released in {self.ReleaseYear}
    Located at x={self.Cords[0]}, y={self.Cords[1]}
""".strip()


def main() -> None:
    # Конфигурация запуска
    WaitDelay = 0.7
    MapSize: dict[str, int] = {"x": r.randint(10, 15), "y": r.randint(10, 15)}
    data: dict[str, list[str]] = json.loads(DataPath.read_text(encoding=encoding))
    VehicleFactories: dict[int, Callable[[dict[str, list[str]]], Vehicle]] = {
        1: lambda data: Airplane(
            Mark=r.choice(data["Airplane"]),
            Cords=Map.AvailableCoordinates[next(_index_gen)],
            MaxSpeed=r.randint(800, 950),
            Maxheight=r.randint(10000, 15000),
            PassengersAmount=r.randint(100, 400),
        ),
        2: lambda data: Ship(
            Mark=r.choice(data["Ship"]),
            Cords=Map.AvailableCoordinates[next(_index_gen)],
            MaxSpeed=r.randint(35, 45),
            PassengersAmount=r.randint(500, 5000),
            Port=r.choice(data["Port"]),
        ),
        3: lambda data: Auto(
            Mark=r.choice(data["Mark"]),
            Cords=Map.AvailableCoordinates[next(_index_gen)],
            LicensePlate=r.choice(data["CarNumber"]),
            ReleaseYear=r.choice(data["Years"]),
        ),
    }
    SearchedArea: dict[str, Coordinate] = {
        "x": (
            r.randint(0, MapSize["x"] // 2),
            r.randint(MapSize["x"] // 2, MapSize["x"]),
        ),
        "y": (
            r.randint(0, MapSize["y"] // 2),
            r.randint(MapSize["y"] // 2, MapSize["y"]),
        ),
    }

    # Инициализация
    print(f'Initializing map of {MapSize["x"]}x{MapSize["y"]}')
    Map = LocationMap(MapSize["x"], MapSize["y"])
    VehicleAmount: int = r.randint(1, len(Map))
    Map.GenerateCoordinate(VehicleAmount)
    t.sleep(WaitDelay)

    print(f"Initializing {VehicleAmount} vehicles of {len(VehicleFactories)} types")
    VehicleList: list[Vehicle] = [
        VehicleFactories[r.randint(1, len(VehicleFactories))](data)
        for _ in range(VehicleAmount)
    ]
    t.sleep(WaitDelay)

    print("Placing vehicles on map...")
    for vehicle in VehicleList:
        Map.PlaceObject(vehicle)
        t.sleep(WaitDelay)

    print(Map)

    print(
        f'Searching for vehicles in coordinates {SearchedArea["x"]} on x and {SearchedArea["y"]} on y'
    )
    output: list[Vehicle] = Map.SearchBy_Area(SearchedArea["x"], SearchedArea["y"])
    t.sleep(WaitDelay * 2)

    if output:
        print(f"Found: {len(output)}")
        for vehicle in output:
            print(vehicle, end="\n\n")
            t.sleep(WaitDelay)
    else:
        print("No vehicles in searched area!")

    input("Press any button to exit")


if __name__ == "__main__":
    main()
