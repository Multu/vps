def even_index_values(source):
    if len(source) > 0:
        even_index_items = even_index_values(source[2:])
        even_index_items.insert(0, source[0])
        return even_index_items

    return []


def print_even_index_values(source):
    if len(source) > 0:
        print(str(source[0]))
        return print_even_index_values(source[2:])

    return None

