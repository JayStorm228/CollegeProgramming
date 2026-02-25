import random as r

import F1_20 as F

N = 50
Value = 1
A: list[int] = [r.randint(0, 10) for _ in range(N)]
B: list[int | float] = F.filter_not_equal(A, Value)
print(f"{A=}\n{B=}\n {Value=}")
