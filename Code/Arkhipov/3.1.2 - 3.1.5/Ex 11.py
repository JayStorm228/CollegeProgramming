from random import randint

import F1_20 as F

N = 10
A: list[int] = [randint(0, 10) for _ in range(N)]
M = 10
B: list[int] = [randint(0, 10) for _ in range(M)]
result: str = F.compare_products(A, B)
print(f"{N=}, {A=}\n{M=}, {B=}\n{result}")
