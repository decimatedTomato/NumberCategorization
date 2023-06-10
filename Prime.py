# Prime number check
"""
Sources:
I have none
"""

import math
from enum import Enum
from collections import defaultdict

class Priminess(Enum):
    PRIME_HIGHLY_COMPOSITE = -2
    HIGHLY_COMPOSITE = -1
    ZERO = 0
    COMPOSITE = 0
    PRIME = 1
    SEMPIPRIME = 2

primes = [Priminess.ZERO, Priminess.HIGHLY_COMPOSITE, Priminess.PRIME_HIGHLY_COMPOSITE]
most_factors = 1 # the greatest number of factors so far (used to find highly composite numbers) actually 1 less than real number because factor of 1 is not counted

def priminess(n: int) -> Priminess:
    if len(primes) < n + 1:
        _expand_prime_list(n)
    return primes[n]

def _expand_prime_list(end: int) -> None:
    global most_factors
    for i in range(len(primes), end + 1):
        factors = _prime_factorize(i)
        
        if len(factors) > most_factors:
            if len(factors) == 1 and next(iter(factors.values())) == 1:
                primes.append(Priminess.PRIME_HIGHLY_COMPOSITE)
            else:
                primes.append(Priminess.HIGHLY_COMPOSITE)
            most_factors = len(factors)
        elif len(factors) == 1 and next(iter(factors.values())) == 1:
            primes.append(Priminess.PRIME)
        elif len(factors) == 2:
            primes.append(Priminess.SEMPIPRIME)
        else:
            primes.append(Priminess.COMPOSITE)

def _prime_factorize(n: int) -> dict[int, int]:
    factorization = defaultdict(int)
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factorization[i] += 1
    if n > 1:
        factorization[n] += 1
    return factorization

