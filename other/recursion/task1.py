def exponentiation(n, m):
    if m == 0:
        return 1
    else:
        return n * exponentiation(n, m - 1)
