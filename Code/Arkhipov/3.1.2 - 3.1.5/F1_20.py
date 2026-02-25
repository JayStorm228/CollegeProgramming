from math import factorial, prod
from typing import TypeVar

import numpy as np

TNum = TypeVar("TNum", int, float)
primes_100 = (
    2,
    3,
    5,
    7,
    11,
    13,
    17,
    19,
    23,
    29,
    31,
    37,
    41,
    43,
    47,
    53,
    59,
    61,
    67,
    71,
    73,
    79,
    83,
    89,
    97,
)


def filter_not_equal(List: list[TNum], znach: int | float) -> list[TNum]:  # Ex 1
    """Переписывает в новый список элементы, не равные заданному значению.

    Параметры
    ----------
    List : list[int | float]
        Исходный список чисел.
    znach : int | float
        Значение, элементы, равные которому, нужно исключить.

    Возврат
    -------
    list[int | float]
        Новый список, содержащий только элементы, не равные ``znach``.
    """
    return [w for w in List if w != znach]


def fill_list_with_value(znach: TNum) -> list[TNum]:  # Ex 2
    """Создаёт список заданной длины, заполненный указанным значением.

    Длина списка вводится пользователем c клавиатуры.

    Параметры
    ----------
    znach : float | int
        Значение, которым заполняется список.

    Возврат
    -------
    list[int | float]
        Список длины, заданной пользователем, заполненный значением ``znach``.
    """
    Len = int(input("Введите количество значений: "))
    return [znach for _ in range(Len)]


def count_greater_than(List: list[TNum], znach: TNum) -> int:  # Ex 3
    """Подсчитывает количество элементов списка, превышающих заданное значение.

    Параметры
    ----------
    List : list[int | float]
        Исходный список чисел.
    znach : float | int
        Пороговое значение для сравнения элементов.

    Возврат
    -------
    int
        Количество элементов списка, строго больших ``znach``.
    """
    return len([w for w in List if w > znach])


def sum_less_than(List: list[TNum], znach: TNum) -> float:  # Ex 4
    """Вычисляет сумму элементов списка, меньших заданного значения.

    Параметры
    ----------
    List : list[int | float]
        Исходный список чисел.
    znach : int | float
        Пороговое значение для сравнения элементов.

    Возврат
    -------
    float
        Сумма всех элементов списка, строго меньших ``znach``.
    """
    return sum(w for w in List if w < znach)


def product_of_list(List: list[TNum]) -> float:  # Ex 5
    """Вычисляет произведение всех элементов списка.

    Параметры
    ----------
    List : list[int | float]
        Исходный список чисел.

    Возврат
    -------
    float | int
        Произведение всех элементов списка ``List``.
    """
    return prod(List)


def count_greater_elements(Matrix: np.ndarray, znach: TNum) -> int:  # Ex 6
    """Подсчитывает количество элементов массива, превышающих заданное значение.

    Параметры
    ----------
    Matrix : numpy.ndarray
        Исходный числовой массив произвольной размерности.
    znach : int | float
        Пороговое значение для сравнения элементов.

    Возврат
    -------
    int
        Количество элементов массива, строго больших ``znach``.
    """
    return len(Matrix[Matrix > znach])


def remove_by_position(List: list[TNum], index: int) -> list[TNum]:  # Ex 7
    """Удаляет элемент списка по его номеру (нумерация с 1).

    Параметры
    ----------
    List : list[int | float]
        Исходный список чисел, который будет изменён.
    index : int
        Порядковый номер удаляемого элемента (начиная с 1).

    Возврат
    -------
    list[int | float]
        Изменённый список после удаления элемента.

    Исключения
    ----------
    IndexError
        Выбрасывается, если элемента с указанным номером не существует.
    """
    if index > len(List) or index < 1:
        raise IndexError("Указанного номера нет в списке!")
    List.pop(index - 1)
    return List


def scale_array(Matrix: np.ndarray, chislo: TNum) -> np.ndarray:  # Ex 8
    """Умножает все элементы массива на заданное число.

    Параметры
    ----------
    Matrix : numpy.ndarray
        Исходный числовой массив.
    chislo : int | float
        Число, на которое умножаются все элементы массива.

    Возврат
    -------
    numpy.ndarray
        Новый массив, полученный поэлементным умножением на ``chislo``.
    """
    return Matrix * chislo


def replace_except_value(
    Matrix: np.ndarray, znach1: TNum, znach2: TNum
) -> np.ndarray:  # Ex 9
    """Заменяет все элементы массива, не равные заданному значению, другим значением.

    Параметры
    ----------
    Matrix : numpy.ndarray
        Исходный числовой массив, который будет изменён на месте.
    znach1 : int | float
        Значение, которое требуется сохранить.
    znach2 : int | float
        Значение, которым заменяются все элементы, отличные от ``znach1``.

    Возврат
    -------
    numpy.ndarray
        Тот же массив, в котором все элементы, не равные ``znach1``,
        заменены на ``znach2``.
    """
    Matrix[Matrix != znach1] = znach2
    return Matrix


def append_and_sort(List: list[TNum], znach: TNum) -> list[TNum]:  # Ex 10
    """Добавляет элемент в список и возвращает отсортированную версию списка.

    Параметры
    ----------
    List : list[int | float]
        Исходный список чисел.
    znach : int | float
        Значение, которое нужно добавить в список.

    Возврат
    -------
    list[int | float]
        Новый отсортированный список, содержащий все элементы ``List`` и ``znach``.
    """
    List.append(znach)
    return sorted(List)


def compare_products(List1: list[TNum], List2: list[TNum]) -> str:  # Ex 11
    """Сравнивает произведения элементов двух списков и возвращает строковое описание результата.

    Параметры
    ----------
    List1 : list[int]
        Первый список целых чисел.
    List2 : list[int]
        Второй список целых чисел.

    Возврат
    -------
    str
        Строка с результатом сравнения произведений списков.
    """
    if prod(List1) > prod(List2):
        return f"Product List1: {prod(List1)} > product List2: {prod(List2)}"
    elif prod(List1) < prod(List2):
        return f"Product List2: {prod(List2)} > product List1: {prod(List1)}"
    else:
        return f"Product List1 is equal to product List2: {prod(List1)}"


def count_max_elements(List: list[TNum]) -> int:  # Ex 12
    """Подсчитывает количество максимальных элементов в списке.

    Параметры
    ----------
    List1 : list[int | float]
        Исходный список чисел.

    Возврат
    -------
    int
        Количество элементов, равных максимальному значению в списке.
    """
    return List.count(max(List))


def insert_at_position(
    List: list[TNum], value: TNum, index: int
) -> list[TNum]:  # Ex 13
    """Вставляет элемент в список по указанному номеру (нумерация с 1).

    Параметры
    ----------
    List : list[int | float]
        Исходный список чисел, который будет изменён.
    value : int | float
        Значение, которое нужно вставить.
    index : int
        Порядковый номер позиции вставки (начиная с 1).

    Возврат
    -------
    list[int | float]
        Изменённый список после вставки элемента.

    Исключения
    ----------
    IndexError
        Выбрасывается, если указанного номера позиции нет в списке.
    """
    if index > len(List) or index < 1:
        raise IndexError("Указанного номера нет в списке!")
    List.insert(index - 1, value)
    return List


def get_list_max(List: list[TNum]) -> TNum:  # Ex 14
    """Находит максимальный элемент в списке.

    Параметры
    ----------
    List : list[int | float]
        Исходный список чисел.

    Возврат
    -------
    int | float
        Максимальное значение в списке.
    """
    return max(List)


def binomial_coefficient(n: int, m: int) -> float:  # Ex 15
    """Вычисляет биномиальный коэффициент C(n, m) = n! / (m! * (n-m)!).

    Параметры
    ----------
    n : int
        Общее количество элементов.
    m : int
        Количество элементов для выбора.

    Возврат
    -------
    float
        Значение биномиального коэффициента.
    """
    if m > n:
        raise ValueError(f"n must be bigger than m!\n n = {n}, m = {m}")
    return factorial(n) / (factorial(m) * factorial(n - m))


def delete_row_2d(matrix: np.ndarray, row: int) -> np.ndarray:  # Ex 16
    """Удаляет строку из двумерного массива по её порядковому номеру (нумерация с 1).

    Параметры
    ----------
    matrix : numpy.ndarray
        Исходный двумерный числовой массив.
    row : int
        Порядковый номер удаляемой строки (начиная с 1).

    Возврат
    -------
    numpy.ndarray
        Новый массив без указанной строки.

    Исключения
    ----------
    ValueError
        Выбрасывается, если передан массив, отличный от двумерного.
    IndexError
        Выбрасывается, если номер строки выходит за допустимые границы.
    """
    if matrix.ndim != 2:
        raise ValueError(f"Given array is not 2D:\n{matrix}\n")
    if row < 1 or row > matrix.shape[0]:
        raise IndexError(f"Index {row} out of range!")
    return np.delete(matrix, row - 1, axis=0)


def is_prime_to_100(Num: int) -> bool:  # Ex 17
    """Проверяет, является ли число простым в диапазоне до 100.

    Параметры
    ----------
    Num : int
        Проверяемое целое число.

    Возврат
    -------
    bool
        ``True``, если ``Num`` входит в список простых чисел до 100, иначе ``False``.

    Исключения
    ----------
    TypeError
        Выбрасывается, если ``Num`` не является целым числом.
    """
    if type(Num) is not int:
        raise TypeError(f"{Num} must be an integer!")
    return Num in primes_100


def array_max(Matrix: np.ndarray) -> TNum:  # Ex 18.1
    """Находит максимальный элемент в числовом массиве.

    Параметры
    ----------
    Matrix : numpy.ndarray
        Исходный числовой массив.

    Возврат
    -------
    int | float
        Максимальное значение элементов массива.
    """
    return Matrix.max()


def count_value_in_array(Matrix: np.ndarray, value: TNum) -> int:  # Ex 18.2
    """Подсчитывает количество вхождений заданного значения в массив.

    Параметры
    ----------
    Matrix : numpy.ndarray
        Исходный числовой массив.
    value : int | float
        Значение, количество вхождений которого требуется подсчитать.

    Возврат
    -------
    int
        Число элементов массива, равных ``value``.
    """
    return len(Matrix[Matrix == value])


def replace_value_in_list(
    List: list[TNum], znach: TNum, znach1: TNum
) -> list[TNum]:  # Ex 19
    """Заменяет элементы списка, не равные заданному значению, другим значением.

    Параметры
    ----------
    List : list[int | float]
        Исходный список чисел.
    znach : int | float
        Значение, которое требуется оставить.
    znach1 : int | float
        Значение, на которое заменяются все элементы, не равные ``znach``.

    Возврат
    -------
    list[int | float]
        Новый список, в котором все элементы, не равные ``znach``,
        заменены на ``znach1``.
    """
    return [znach1 if x != znach else znach for x in List]


def elementwise_multiply_2d(
    Matrix1: np.ndarray, Matrix2: np.ndarray
) -> np.ndarray:  # Ex 20
    """Выполняет поэлементное умножение двух согласованных двумерных массивов.

    Параметры
    ----------
    Matrix1 : numpy.ndarray
        Первый двумерный числовой массив.
    Matrix2 : numpy.ndarray
        Второй двумерный числовой массив той же формы.

    Возврат
    -------
    numpy.ndarray
        Новый массив, являющийся поэлементным произведением ``Matrix1`` и ``Matrix2``.

    Исключения
    ----------
    ValueError
        Выбрасывается, если хотя бы один из массивов не является двумерным
        или формы массивов не совпадают.
    """
    if Matrix1.ndim != 2 or Matrix2.ndim != 2:
        raise ValueError("Both matrix must be 2D")
    if Matrix1.shape != Matrix2.shape:
        raise ValueError(
            f"Shapes of given matrixes aren't equal!: \nMatrix1:\n{Matrix1}\n\nMatrix2:\n{Matrix2}"
        )
    return Matrix1 * Matrix2


if __name__ == "__main__":
    pass
