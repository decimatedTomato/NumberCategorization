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
    seq, looping_section_index = aliquot_sequence(n)
    
    # For regular terminating numbers
    if looping_section_index == None: return None
    
    # For aspiring numbers
    if looping_section_index > 0: return "Aspiring number"

    # For numbers that are part of a loop
    loop_length = len(seq) - looping_section_index
    if loop_length == 1: return "Perfect number"
    elif loop_length == 2: return f"Amicable number ({n}, {seq[-1]})"
    elif loop_length >= 3: return f"Sociable number ({seq})" #TODO test

def aliquot_sequence(n: int) -> tuple[list[int], int | None]:
    """Returns the sequence from n to 0 or until a number reappears, also returns the index of the looping section"""
    seq = [n]
    while n != 0:
        n = _next_aliquot(n)

        # Case in which n has already occured
        if n in seq:
            return seq, seq.index(n)
        # Case in which n is new
        seq.append(n)
    return seq, None

def max_aliquot_length(start: int, end: int, step: int = 1) -> tuple[int, list[int]]:
    """Returns the longest aliquot sequence length and starting values form within the range including start and excluding end using the given step"""
    max_idx_list = []
    max_len = 0
    for i in range(start, end, step):
        i_length = len(aliquot_sequence(i)[0])
        if i_length == max_len:
            max_idx_list.append(i)
        if i_length > max_len:
            max_len = i_length
            max_idx_list = [i]
    return max_len, max_idx_list

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
        aliquot_table[n] = next_aliquot
    return next_aliquot