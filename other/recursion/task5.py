def even_values(source):
    if len(source) > 0:
        even_items = even_values(source[1:])
        if source[0] % 2 == 0:
            even_items.insert(0, source[0])
        return even_items

    return []


def print_even_values(source):
    if len(source) > 0:
        if source[0] % 2 == 0:
            print(str(source[0]))
        return print_even_values(source[1:])

    return None

