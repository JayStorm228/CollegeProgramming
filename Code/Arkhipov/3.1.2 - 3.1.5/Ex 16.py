from random import randint

import F1_20 as F
from numpy import int64
from numpy.typing import NDArray

Rows: int = randint(1, 10)
Cols: int = randint(1, 10)
A: NDArray[int64] = F.np.random.randint(1, 10, (Rows, Cols))
print(f"{Rows=}, {Cols=}\n{A=}")
DeleteRow: int = randint(1, Rows)
B: NDArray[int64] = F.delete_row_2d(A, DeleteRow)
print(f"{DeleteRow=}\n{B=}")
