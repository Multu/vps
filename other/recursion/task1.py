def exponentiation(n, m):
    if m == 0:
        return 1

    return n * exponentiation(n, m - 1)
