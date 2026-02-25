import math as m
import random as r
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any, Callable, TypeAlias

import numpy as np
from numpy.typing import NDArray

# ========================= ТИПИЗАЦИЯ =========================
Vector3D: TypeAlias = NDArray[np.float64]  # Вектор в 3D: (x, y, z)
ShapeFactory: TypeAlias = Callable[
    [], "Shape"
]  # Алиас фабрики: функция без аргументов, возвращающая Shape

# ========================= ВАЛИДАЦИЯ =========================


def Validate_Vector(Vector: Vector3D) -> None:
    """
    Проверка вектора на ненулевую длину.

    Математика:
    - длина (норма) вектора |v| = sqrt(x^2 + y^2 + z^2)
    - если длина = 0, то вектор вырожденный (нельзя строить ребро/направление)

    Здесь:
    - считаем длину через np.linalg.norm(Vector)
    - округляем для красоты в сообщении об ошибке
    """
    Length: np.floating[Any] = round(np.linalg.norm(Vector), 4)
    if Length == 0:
        raise ValueError(
            f"Vector {{{Vector[0]}, {Vector[1]}, {Vector[2]}}} "
            f"is zero (length={Length:.4f})!"
        )


def Validate_Parallelepiped(
    Vector_A: Vector3D, Vector_B: Vector3D, Vector_C: Vector3D
) -> None:
    """
    Проверка, можно ли из трёх векторов A, B, C построить параллелепипед.

    Математика:
    - Строим матрицу из векторов:
        | A_x  A_y  A_z |
        | B_x  B_y  B_z |
        | C_x  C_y  C_z |
    - det(Matrix) = скалярное тройное произведение A · (B × C)
    - |det| = объём параллелепипеда
    - Если det ≈ 0 → объём ≈ 0 → векторы компланарны (лежат в одной плоскости)
      → нормального параллелепипеда не существует.
    """
    Matrix: NDArray[np.float64] = np.vstack([Vector_A, Vector_B, Vector_C])
    det: float = np.linalg.det(Matrix)
    if abs(det) < 1e-10:
        raise ValueError(
            "Parallelepiped cannot be formed:\n"
            f"  A = [{Vector_A[0]:.3f}, {Vector_A[1]:.3f}, {Vector_A[2]:.3f}]\n"
            f"  B = [{Vector_B[0]:.3f}, {Vector_B[1]:.3f}, {Vector_B[2]:.3f}]\n"
            f"  C = [{Vector_C[0]:.3f}, {Vector_C[1]:.3f}, {Vector_C[2]:.3f}]\n"
            f"(det = {det:.3e} ≈ 0 — vectors are coplanar)"
        )


def Validate_Radius(value) -> None:
    """
    Проверка корректности радиуса для сферы.

    Условия:
    - radius должен быть числом (int или float)
    - radius > 0
    """
    if not (isinstance(value, float | int)):
        raise ValueError(f"Radius must be a number! Given:{type(value)}")
    if value <= 0:
        raise ValueError(f"Radius must be greater than 0! Given:{value}")


# ========================= АБСТРАКТНАЯ ФИГУРА =========================


@dataclass
class Shape(ABC):
    """
    Абстрактный базовый класс для 3D-фигур.

    Любая фигура должна уметь:
    - считать площадь поверхности (SurfaceArea)
    - считать объём (Volume)
    - возвращать строковое представление (__str__)
    """

    @property
    @abstractmethod
    def SurfaceArea(self) -> float: ...

    @property
    @abstractmethod
    def Volume(self) -> float: ...

    @abstractmethod
    def __str__(self) -> str: ...


# ========================= ПАРАЛЛЕЛЕПИПЕД =========================


@dataclass
class Parallelepiped(Shape):
    """
    Параллелепипед, заданный тремя векторами A, B, C,
    исходящими из одной вершины.

    Здесь:
    - Vector_A, Vector_B, Vector_C — рёбра, задающие всю фигуру.
    """

    Vector_A: Vector3D
    Vector_B: Vector3D
    Vector_C: Vector3D

    def __post_init__(self) -> None:
        """
        Валидация после создания объекта.

        Проверяем:
        - каждый вектор ненулевой
        - тройка векторов не компланарна (det != 0)
        """
        Validate_Vector(self.Vector_A)
        Validate_Vector(self.Vector_B)
        Validate_Vector(self.Vector_C)
        Validate_Parallelepiped(self.Vector_A, self.Vector_B, self.Vector_C)

    @property
    def SurfaceArea(self) -> float:
        """
        Площадь поверхности параллелепипеда.

        Математика:
        - площадь грани, натянутой на векторы A и B:
            S_AB = ||A × B||
          (норма векторного произведения = площадь параллелограмма)
        - всего 3 пары граней:
            S = 2 * (||A×B|| + ||A×C|| + ||B×C||)
        """

        # np.linalg.norm() - длина вектора
        # np.cross()       - векторное произведение

        AB = float(np.linalg.norm(np.cross(self.Vector_A, self.Vector_B)))
        BC = float(np.linalg.norm(np.cross(self.Vector_B, self.Vector_C)))
        AC = float(np.linalg.norm(np.cross(self.Vector_A, self.Vector_C)))
        return 2 * (AB + BC + AC)

    @property
    def Volume(self) -> float:
        """
        Объём параллелепипеда.

        Математика:
        - объём = |det(A, B, C)| = |A · (B × C)|
        - det считаем через np.linalg.det по матрице из векторов A, B, C.
        """
        Matrix: NDArray[np.float64] = np.vstack(
            [self.Vector_A, self.Vector_B, self.Vector_C]
        )
        return abs(np.linalg.det(Matrix))

    def __str__(self) -> str:
        return (
            "Параллелепипед:\n"
            f"  A = [{self.Vector_A[0]:.2f}, {self.Vector_A[1]:.2f}, {self.Vector_A[2]:.2f}]\n"
            f"  B = [{self.Vector_B[0]:.2f}, {self.Vector_B[1]:.2f}, {self.Vector_B[2]:.2f}]\n"
            f"  C = [{self.Vector_C[0]:.2f}, {self.Vector_C[1]:.2f}, {self.Vector_C[2]:.2f}]\n"
            f"  Площадь поверхности: {self.SurfaceArea:.2f}\n"
            f"  Объём: {self.Volume:.2f}"
        )


# ========================= СФЕРА =========================


@dataclass
class Sphere(Shape):
    """
    Сфера (шар) с заданным радиусом.

    Все точки поверхности на расстоянии Radius от центра.
    """

    Radius: float

    @property
    def SurfaceArea(self) -> float:
        """
        Площадь поверхности сферы.

        Формула:
            S = 4 * π * R^2
        """
        return round(m.pi * 4 * self.Radius**2, 4)

    @property
    def Volume(self) -> float:
        """
        Объём шара.

        Формула:
            V = 4/3 * π * R^3
        """
        return round(m.pi * (4 / 3) * self.Radius**3, 4)

    def __post_init__(self) -> None:
        """
        Проверяем корректность радиуса (число > 0).
        """
        Validate_Radius(self.Radius)

    def __str__(self) -> str:
        return (
            "Сфера:\n"
            f"  Радиус: {self.Radius:.2f}\n"
            f"  Площадь поверхности: {self.SurfaceArea:.2f}\n"
            f"  Объём: {self.Volume:.2f}"
        )


# ========================= ПОЛИГОН (основание пирамиды) =========================


@dataclass
class Polygon:
    """
    Многоугольник в 3D, заданный вершинами.

    vertices: массив формы (N, 3),
        где N — число вершин,
        каждая строка — координаты вершины (x, y, z).

    Требования:
    - N >= 3
    - все точки лежат в одной плоскости (копланарны)
    """

    vertices: NDArray[np.float64]  # Координаты вершин 3D

    def _Check_Coplanar(self) -> None:
        """
        Проверка, что все вершины лежат в одной плоскости.

        Математика:
        - Берём первые 3 точки A, B, C — они задают плоскость.
        - Нормаль к плоскости: n = (B - A) × (C - A).
        - Для каждой следующей вершины P:
            вектор AP = P - A
            скалярное произведение <AP, n> пропорционально расстоянию до плоскости.
        - Если |<AP, n>| > eps → точка не в плоскости.
        """
        # Берём первые 3 точки → плоскость
        A, B, C = self.vertices[:3]
        normal: NDArray[np.float64] = np.cross(B - A, C - A)  # Нормаль плоскости

        # Проверяем остальные точки
        for i in range(3, len(self.vertices)):
            vec = self.vertices[i] - A
            if (
                abs(np.dot(vec, normal)) > 1e-6
            ):  # «расстояние» до плоскости (с точностью eps)
                raise ValueError(f"Вершина {i} не в плоскости!")

    def _Validate_Shape(self) -> None:
        """
        Базовые проверки формы массива вершин.
        """
        if self.vertices.ndim != 2 or self.vertices.shape[1] != 3:
            raise ValueError("vertices: (N, 3) — N≥3 вершин в 3D!")
        if self.vertices.shape[0] < 3:
            raise ValueError("Полигон: минимум 3 вершины!")

    @property
    def Area(self) -> float:
        """
        Площадь многоугольника в 3D.

        Идея:
        - многоугольник разбивается на треугольники, и их площади суммируются.
        - используем формулу через векторное произведение:
            площадь треугольника = 0.5 * || (P_i - P_{i-1}) × (P_{i+1} - P_{i-1}) ||
        - идём по всем вершинам i, суммируем площади соответствующих треугольников.
        """
        S = 0.0
        n: int = len(self.vertices)
        for i in range(n):
            prev: NDArray[np.float64] = self.vertices[(i - 1) % n]
            curr: NDArray[np.float64] = self.vertices[i]
            next_: NDArray[np.float64] = self.vertices[(i + 1) % n]
            S += 0.5 * np.linalg.norm(np.cross(curr - prev, next_ - prev))
        return float(S)

    @property
    def perimeter(self) -> float:
        """
        Периметр многоугольника.

        Математика:
        - сумма длин всех рёбер.
        - ребро = расстояние между соседними вершинами.
        """
        diffs: NDArray[np.float64] = np.diff(
            self.vertices, axis=0, append=self.vertices[0:1]
        )
        return np.sum(np.linalg.norm(diffs, axis=1))

    def __post_init__(self) -> None:
        """
        Валидация полигона:
        - правильная форма массива
        - все точки копланарны.
        """
        self._Validate_Shape()
        self._Check_Coplanar()

    def __str__(self) -> str:
        return (
            f"    Полигон ({len(self.vertices)} вершин):\n"
            f"      Площадь: {self.Area:.2f}\n"
            f"      Периметр: {self.perimeter:.2f}\n"
            f"      Вершины: {self.vertices.shape[0]}×3"
        )


# ========================= ПИРАМИДА =========================


@dataclass
class Pyramid(Shape):
    """
    Пирамида с произвольным многоугольником в основании.

    Base — Polygon (основание, N-угольник в одной плоскости).
    Apex — вершина пирамиды (точка в 3D).
    """

    Base: Polygon
    Apex: NDArray[np.float64]

    @property
    def Height(self) -> float:
        """
        Высота пирамиды — расстояние от вершины Apex до плоскости основания.

        Математика:
        - плоскость основания задаётся тремя точками A, B, C (первые вершины Base).
        - нормаль к плоскости: n = (B - A) × (C - A), затем нормируем её.
        - расстояние от точки P до плоскости:
            h = | (P - A) · n_нормированная |
        """
        A: NDArray[np.float64] = self.Base.vertices[0]
        B: NDArray[np.float64] = self.Base.vertices[1]
        C: NDArray[np.float64] = self.Base.vertices[2]
        normal: NDArray[np.floating[Any]] = np.cross(B - A, C - A)
        normal = normal / np.linalg.norm(normal)  # единичный вектор нормали

        # Вектор от точки на плоскости до вершины
        point_on_plane: NDArray[np.float64] = A
        apex_vec: NDArray[np.float64] = self.Apex - point_on_plane
        return abs(np.dot(apex_vec, normal))

    @property
    def Volume(self) -> float:
        """
        Объём пирамиды.

        Формула:
            V = 1/3 * S_основания * h
        где:
            S_основания = площадь многоугольника Base.Area
            h           = высота (Distance Apex → plane(Base))
        """
        return (1 / 3) * self.Base.Area * self.Height

    @property
    def SurfaceArea(self) -> float:
        """
        Полная площадь поверхности пирамиды.

        Состоит из:
        - площади основания
        - суммарной площади всех боковых треугольников.

        Математика:
        - каждый боковой треугольник задаётся вершиной Apex
          и двумя соседними вершинами основания B, C.
        - площадь треугольника:
            S = 0.5 * || (B - Apex) × (C - Apex) ||
        - суммируем по всем рёбрам основания.
        """
        S_base: float = self.Base.Area
        S_lateral = 0.0
        n: int = len(self.Base.vertices)
        for i in range(n):
            A = self.Apex
            B: NDArray[np.float64] = self.Base.vertices[i]
            C: NDArray[np.float64] = self.Base.vertices[(i + 1) % n]
            S_lateral += 0.5 * np.linalg.norm(np.cross(B - A, C - A))
        return float(S_base + S_lateral)

    def __str__(self) -> str:
        return (
            "Пирамида:\n"
            f"  Основание: \n{self.Base}\n"
            f"  Вершина: [{self.Apex[0]:.2f}, {self.Apex[1]:.2f}, {self.Apex[2]:.2f}]\n"
            f"  Высота: {self.Height:.2f}\n"
            f"  Площадь поверхности: {self.SurfaceArea:.2f}\n"
            f"  Объём: {self.Volume:.2f}"
        )


# ========================= ГЕНЕРАЦИЯ ФИГУР =========================


def main() -> None:

    def generate_Parallelepiped() -> Parallelepiped:
        """
        Генерация случайного параллелепипеда.

        - случайно генерируем три вектора A, B, C
        - пытаемся создать Parallelepiped
        - если вектора выродились (det≈0 или длина 0), ловим ValueError
          и пробуем ещё раз.
        """
        shape = None
        while shape is None:
            try:
                shape = Parallelepiped(
                    Vector_A=np.random.uniform(1, 10, 3).round(4),
                    Vector_B=np.random.uniform(1, 10, 3).round(4),
                    Vector_C=np.random.uniform(1, 10, 3).round(4),
                )
            except ValueError:
                shape = None
        return shape

    def random_plane_basis() -> tuple[Vector3D, Vector3D, Vector3D]:
        """
        Генерация случайной плоскости в 3D в виде базиса (O, u, v).

        - Dot (O): случайная точка на плоскости.
        - u: единичный вектор в плоскости.
        - v: второй единичный вектор в той же плоскости, ортогональный u.

        Математика:
        - сначала берём случайный вектор a и нормируем → u
        - затем берём b и вычитаем проекцию на u:
            b_⊥ = b - (b·u) * u
          чтобы получить направление, перпендикулярное u.
        - нормируем b_⊥ → v.
        """
        # Случайная точка на плоскости
        Dot: NDArray[np.float64] = np.random.uniform(1, 10, 3)

        # Случайный ненулевой вектор → нормируем → u
        a: NDArray[np.float64] = np.random.uniform(-1, 1, 3)
        a /= np.linalg.norm(a)

        # Второй вектор, не параллельный a, ортогонализуем относительно a → v
        b: NDArray[np.float64] = np.random.uniform(-1, 1, 3)
        b = b - np.dot(b, a) * a
        b /= np.linalg.norm(b)

        return Dot, a, b

    def generate_coplanar_polygon_vertices(N: int) -> NDArray[np.float64]:
        """
        Генерация N вершин многоугольника, лежащих в одной плоскости.

        Идея:
        - выбираем плоскость (Dot, u, v) через random_plane_basis()
        - в координатах этой плоскости задаём точки по окружности с
          небольшими вариациями радиуса:
            (s, t) = (r*cos(angle), r*sin(angle))
        - переводим их в 3D:
            P = Dot + s*u + t*v
        """
        Dot, u, v = random_plane_basis()

        angles: NDArray[np.float64] = np.linspace(0, 2 * np.pi, N, endpoint=False)
        radii: NDArray[np.float64] = np.random.uniform(
            1, 3, N
        )  # случайный радиус для «неровности» многоугольника

        vertices = []
        for angle, radius in zip(angles, radii, strict=True):
            s = radius * np.cos(angle)
            t = radius * np.sin(angle)
            P = Dot + s * u + t * v  # точка в 3D в выбранной плоскости
            vertices.append(P)

        return np.array(vertices).round(4)

    def generate_Polygon() -> Polygon:
        """
        Генерация случайного копланарного многоугольника.

        - случайно выбираем N вершин (3..10)
        - строим N копланарных точек через generate_coplanar_polygon_vertices
        - создаём Polygon; если по какой-то причине валидация не прошла,
          пробуем ещё раз.
        """
        while True:
            N: int = r.randint(3, 10)
            vertices: NDArray[np.float64] = generate_coplanar_polygon_vertices(N)
            try:
                return Polygon(vertices)
            except ValueError:
                # Сработает только если что-то ещё не понравилось _Validate_Shape()
                continue

    def generate_Pyramid() -> Pyramid:
        """
        Генерация случайной пирамиды:
        - случайное основание (копланарный N-угольник)
        - случайное положение вершины Apex.
        """
        shape = None
        while shape is None:
            try:
                shape = Pyramid(
                    Base=generate_Polygon(),
                    Apex=np.random.uniform(1, 10, 3).round(4),
                )
            except ValueError:
                shape = None
        return shape

    def generate_Sphere() -> Sphere:
        """
        Генерация случайной сферы с радиусом в диапазоне [1, 10].
        """
        shape = None
        while shape is None:
            try:
                shape = Sphere(Radius=round(r.uniform(1, 10), 4))
            except ValueError:
                shape = None
        return shape

    # Словарь фабрик фигур: по ключу (типу) выбираем генератор конкретной фигуры
    ShapeFactories: dict[int, ShapeFactory] = {
        1: generate_Parallelepiped,
        2: generate_Sphere,
        3: generate_Pyramid,
    }

    # Случайное количество фигур
    ShapesAmount: int = r.randint(1, 10)

    # Генерируем список случайных фигур
    ShapesList: list[Shape] = [
        ShapeFactories[r.randint(1, len(ShapeFactories))]() for _ in range(ShapesAmount)
    ]

    # Печатаем все с их параметрами
    for shape in ShapesList:
        print(shape, end="\n\n")


if __name__ == "__main__":
    main()
