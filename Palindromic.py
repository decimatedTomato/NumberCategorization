# Palindromic numbers

def palindromic(n: int) -> bool:
    return str(n) == str(n)[::-1]