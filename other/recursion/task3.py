def list_len(source_list):
    try:
        source_list.pop(0)
        return 1 + list_len(source_list)
    except IndexError:
        return 0
