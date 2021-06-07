def even_index_values(source):
    if len(source) > 1:
        even_index_items = even_index_values(source[2:])
        even_index_items.insert(0, source[0])
        return even_index_items
    elif len(source) == 1:
        return [source[0]]

    return []


def print_even_index_values(source):
    if len(source) > 1:
        print(str(source[0]))
        print_even_index_values(source[2:])
    elif len(source) == 1:
        print(str(source[0]))
