from random import randint

import F1_20 as F

N = 10
A: list[int] = [randint(0, 100) for _ in range(N)]
Primes: list[int] = [w for w in A if F.is_prime_to_100(w)]
CountPrimes: int = len(Primes)
print(f"{N=}, {A=}\n{Primes=}, Number of primes: {CountPrimes}")
