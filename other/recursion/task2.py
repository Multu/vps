def sum_digits(n):
    if n // 10 == 0:
        return n % 10

    return (n % 10) + sum_digits(n // 10)
