def MadMax(n, tele):

    # Sort left side elements by asc.
    for i in range(n // 2):
        min_index = i
        min_value = tele[i]

        for j in range(i + 1, n):
            if tele[j] < min_value:
                min_index = j
                min_value = tele[j]

        tele[i], tele[min_index] = tele[min_index], tele[i]

    # Sort middle and right side elements by desc.
    for i in range(n // 2, n - 1):
        max_index = i
        max_value = tele[i]

        for j in range(i + 1, n):
            if tele[j] > max_value:
                max_index = j
                max_value = tele[j]

        tele[i], tele[max_index] = tele[max_index], tele[i]

    return tele
