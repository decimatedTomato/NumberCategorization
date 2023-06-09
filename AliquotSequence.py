# Aliquot sequence code
"""
Sources:
https://www.youtube.com/watch?v=Cw0IYZuo3HU&ab_channel=ComboClass
https://en.wikipedia.org/wiki/Aliquot_sequence
https://www.geeksforgeeks.org/aliquot-sequence/
"""

import math

aliquot_table: dict[int, int] = { 1: 0 }


def aliquot_property(n: int) -> str | None:
    """Possible values include None, perfect number, amicable numbers, sociable number, aspiring number"""
    return None

def aliquot_sequence(n: int) -> list[int]:
    seq = [n]
    while n != 0:
        n = _next_aliquot(n)
        if n in seq: return seq # clumsy solution
        seq.append(n)
    return seq


def _calculate_aliquot(n: int) -> int:
    next = -n
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            if n // i == i:
                next += i
            else:
                next += i
                next += n // i
    return next

def _next_aliquot(n: int) -> int:
    next_aliquot = aliquot_table.get(n)
    if next_aliquot == None:
        next_aliquot = _calculate_aliquot(n)
    return next_aliquot