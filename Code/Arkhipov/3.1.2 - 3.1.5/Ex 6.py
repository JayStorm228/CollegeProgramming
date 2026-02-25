from random import randint

import F1_20 as F
from numpy import int64
from numpy.typing import NDArray

Cols = 10  # Col
Rows = 10  # Row
A: NDArray[int64] = F.np.array(
    [[randint(0, 10) for _ in range(Cols)] for _ in range(Rows)]
)
Critical = 4
CountCritical: int = F.count_greater_elements(A, Critical)
print(f"A({Rows}x{Cols}):\n{A}\nCritical Value = {Critical}, found: {CountCritical}")
