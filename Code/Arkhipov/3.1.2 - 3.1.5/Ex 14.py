from random import randint

import F1_20 as F

N = 10
A: list[int] = [randint(0, 10) for _ in range(N)]
print(f"N = {N}, A = {A}")
MaxValue: int = F.get_list_max(A)
print(f"Max value of this list: {MaxValue}")
