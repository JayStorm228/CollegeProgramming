from random import randint

import F1_20 as F

N = 50
A: list[int] = [randint(0, 10) for _ in range(N)]
Value = 3
Count: int = F.count_greater_than(A, Value)
print(f"{N=}, {A=}\n Count > {Value} = {Count}")
