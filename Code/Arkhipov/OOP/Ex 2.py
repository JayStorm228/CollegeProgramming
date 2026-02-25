import json
import random as r
from abc import ABC, abstractmethod
from dataclasses import dataclass
from pathlib import Path
from typing import Callable, List

FileName = "Data.json"
CWD: Path = Path(__file__).resolve().parent
DataPath: Path = CWD / FileName
encoding = "utf-8"


@dataclass
class Edition(ABC):
    Title: str = ""
    AuthorSurname: str = ""

    @abstractmethod
    def __str__(self) -> str: ...
    @abstractmethod
    def match_surname(self, surname) -> bool: ...


@dataclass
class Book(Edition):
    ReleaseYear: str = ""
    Publisher: str = ""

    def __str__(self) -> str:
        return f"Книга: '{self.Title}' ({self.AuthorSurname}, {self.ReleaseYear}, {self.Publisher})"

    def match_surname(self, surname) -> bool:
        return self.AuthorSurname == surname


@dataclass
class Article(Edition):
    Magazine: str = ""
    MagazineID: str = ""
    ReleaseYear: str = ""

    def __str__(self) -> str:
        return f"Статья: '{self.Title}' ({self.AuthorSurname}, Журнал: {self.Magazine}(№{self.MagazineID}, год издания: {self.ReleaseYear})"

    def match_surname(self, surname) -> bool:
        return self.AuthorSurname == surname


@dataclass
class Website(Edition):
    URL: str = ""
    Annotation: str = ""

    def match_surname(self, surname) -> bool:
        return self.AuthorSurname == surname

    def __str__(self) -> str:
        return f"Электронный ресурс: '{self.Title}'(Автор: {self.AuthorSurname}). \n {self.Annotation} "


def main() -> None:
    data: dict[str, list[str]] = json.loads(DataPath.read_text(encoding=encoding))
    EditionFactories: dict[int, Callable[[dict[str, list[str]]], Edition]] = {
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
    output: List[Edition] = [
        edition for edition in EditionsList if edition.match_surname(SearchedSurname)
    ]
    print(f"Found: {len(output)}")
    if output:
        for w in output:
            print(w, end="\n\n")


if __name__ == "__main__":
    main()
