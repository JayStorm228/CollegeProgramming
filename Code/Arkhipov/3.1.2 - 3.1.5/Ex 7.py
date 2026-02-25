from random import randint

import F1_20 as F

N = 10
A: list[int] = [randint(0, 10) for _ in range(N)]
Position = 3
print(f"{N=}, {A=}, {Position=}")
F.remove_by_position(A, Position)
print(f"Modified A = {A}")
