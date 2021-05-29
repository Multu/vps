def Football(f, n):
    f_sort = list(f)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if f_sort[j] < f_sort[i]:
                f_sort[j], f_sort[i] = f_sort[i], f_sort[j]

    diff_positions = []
    for i in range(n):
        if f[i] != f_sort[i]:
            diff_positions.append(i)
    diff_positions_count = len(diff_positions)

    # Input list was already sorted.
    if diff_positions_count == 0:
        return False
    # Swap two random elements
    elif diff_positions_count == 2:
        return True
    # Reverse chain of elements
    else:
        first_chain_index = diff_positions[0]
        last_chain_index = diff_positions[-1]

        for i in range(first_chain_index, last_chain_index + 1):
            if f_sort[i] != f[diff_positions_count - i]:
                return False
        else:
            return True
