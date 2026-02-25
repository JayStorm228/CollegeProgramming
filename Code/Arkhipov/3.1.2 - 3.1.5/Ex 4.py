from random import randint

import F1_20 as F

N = 50
A: list[int] = [randint(0, 10) for _ in range(N)]
Value = 5
Sum: float = F.sum_less_than(A, Value)
print(f"{N=}, {A=}\nSum values < {Value} = {Sum}")
