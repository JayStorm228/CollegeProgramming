from random import randint

import F1_20 as F

N = 50
A: list[int] = [randint(0, 10) for _ in range(N)]
Product: float | int = F.product_of_list(A)
print(f"{N=}, {A=}\n{Product=}")
