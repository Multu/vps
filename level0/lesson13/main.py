def convert_to_decimal(number, base):
    decimal_value = 0

    multiplier = 0
    while number > 0:
        rest = number % 10
        decimal_value += (rest * (base ** multiplier))
        multiplier += 1
        number = number // 10

    return decimal_value


def UFO(n, data, octal):
    decimal_list = []

    if octal:
        base = 8
    else:
        base = 16

    for i in range(n):
        decimal_list.append(convert_to_decimal(data[i], base))

    return decimal_list