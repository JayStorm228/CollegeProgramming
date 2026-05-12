import json
import random as r
from abc import ABC, abstractmethod
from dataclasses import dataclass
from pathlib import Path
from typing import Callable, TypeAlias

FileName = "Data.json"
CWD: Path = Path(__file__).resolve().parent
DataPath: Path = CWD / FileName
encoding = "utf-8"

EditionFactory: TypeAlias = Callable[[dict[str, list[str]]], "Edition"]


@dataclass
class Edition(ABC):
    Title: str
    AuthorSurname: str

    @abstractmethod
    def __str__(self) -> str: ...
    @abstractmethod
    def match_surname(self, surname: str) -> bool: ...


@dataclass
class Book(Edition):
    ReleaseYear: str
    Publisher: str

    def __str__(self) -> str:
        return f"Книга: '{self.Title}' ({self.AuthorSurname}, {self.ReleaseYear}, {self.Publisher})"

    def match_surname(self, surname: str) -> bool:
        return self.AuthorSurname == surname


@dataclass
class Article(Edition):
    Magazine: str
    MagazineID: str
    ReleaseYear: str

    def __str__(self) -> str:
        return f"Статья: '{self.Title}' ({self.AuthorSurname}, Журнал: {self.Magazine}(№{self.MagazineID}, год издания: {self.ReleaseYear})"

    def match_surname(self, surname: str) -> bool:
        return self.AuthorSurname == surname


@dataclass
class Website(Edition):
    URL: str
    Annotation: str

<<<<<<< HEAD:Code/Arkhipov/OOP/Ex 2.py
    def match_surname(self, surname: str) -> bool:
=======
    def match_surname(self, surname:str) -> bool:
>>>>>>> e0ee5b8 (4.1.2 - 4.1.4 and small overall changes):Code/Arkhipov/4.1.2 - 4.1.4/Ex 2.py
        return self.AuthorSurname == surname

    def __str__(self) -> str:
        return f"Электронный ресурс: '{self.Title}'(Автор: {self.AuthorSurname}). \n {self.Annotation} "


def main() -> None:
    data: dict[str, list[str]] = json.loads(DataPath.read_text(encoding=encoding))
    EditionFactories: dict[int, EditionFactory] = {
        1: lambda data: Book(
            Title=r.choice(data["Titles"]),
            AuthorSurname=r.choice(data["LastName"]),
            ReleaseYear=r.choice(data["Years"]),
            Publisher=r.choice(data["Publishers"]),
        ),
        2: lambda data: Article(
            Title=r.choice(data["Titles"]),
            AuthorSurname=r.choice(data["LastName"]),
            Magazine=r.choice(data["Magazines"]),
            MagazineID=r.choice(data["MagazineIDs"]),
            ReleaseYear=r.choice(data["Years"]),
        ),
        3: lambda data: Website(
            Title=r.choice(data["Titles"]),
            AuthorSurname=r.choice(data["LastName"]),
            URL=r.choice(data["URLs"]),
            Annotation=r.choice(data["Annotations"]),
        ),
    }
    EditionsAmount: int = r.randint(1, 10)
    EditionsList: list[Edition] = [
        EditionFactories[r.randint(1, len(EditionFactories))](data)
        for _ in range(EditionsAmount)
    ]
    print(f"Initializing {EditionsAmount} editions of {len(EditionFactories)}")
    SearchedSurname: str = r.choice(data["LastName"])
    print(f"Searching for {SearchedSurname}")
    output: list[Edition] = [
        edition for edition in EditionsList if edition.match_surname(SearchedSurname)
    ]
    print(f"Found: {len(output)}")
    if output:
        for w in output:
            print(w, end="\n\n")


if __name__ == "__main__":
    main()
