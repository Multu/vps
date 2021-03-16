def factorial(n):
    fact = 1
    for i in range(n):
        fact *= i + 1
    return fact


def first_digit(n):
    while n >= 10:
        n = n // 10
    return n


def squirrel(n):
    fact = factorial(n)
    emeralds_count = first_digit(fact)
    return emeralds_count
