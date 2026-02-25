from random import randint

import F1_20 as F

N = 10
A: list[int] = [randint(0, 10) for _ in range(N)]
Value = 100
Index = 1
print(f"{N=}, {A=}")
F.insert_at_position(A, Value, Index)
print(f"Value to insert: {Value}, position(from 1): {Index}\nNew A: {A}")
