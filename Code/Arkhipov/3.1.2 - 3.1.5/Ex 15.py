from random import randint

import F1_20 as F

n: int = randint(1, 10)
m: int = randint(1, 5)
C: float = F.binomial_coefficient(n, m)
print(f"{n=},{m=}, C(n, m) = {C}")
