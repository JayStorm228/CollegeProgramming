from random import randint

import F1_20 as F

N = 10
A: list[int] = [randint(1, 10) for _ in range(N)]
znach = 5
znach1 = 2
B: list[int] = F.replace_value_in_list(A, znach, znach1)
print(f"{N=}, {A=}, {znach=}, {znach1=}\nNew List = {B}")
