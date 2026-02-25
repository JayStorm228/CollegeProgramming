from random import randint

import F1_20 as F
from numpy import int64
from numpy.typing import NDArray

Rows: int = randint(1, 10)
Cols: int = randint(1, 10)
Matrix1: NDArray[int64] = F.np.random.randint(1, 10, (Rows, Cols))
Matrix2: NDArray[int64] = F.np.random.randint(1, 10, (Rows, Cols))
Result: NDArray[int64] = F.elementwise_multiply_2d(Matrix1, Matrix2)
print(
    f"{Rows=}, {Cols=}\nMatrix 1 = \n{Matrix1}\n\nMatrix2 = \n{Matrix2}\n\nResult = \n{Result}"
)
