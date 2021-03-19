def SynchronizingTables(N, ids, salary):

    # Sort salary list by asc.
    for i in range(N - 1):
        for j in range(i + 1, N):
            if salary[j] < salary[i]:
                salary[i], salary[j] = salary[j], salary[i]

    shift_number = 0
    max_shift_index = 0

    for i in range(N):
        # Calculate count of ids elements,
        # that values are less then current value.
        asc_number = 0
        for j in range(N):
            if ids[j] < ids[i]:
                asc_number += 1

        # Put to the `i` position the element with `asc_number` index.
        # If replacement is needed, then shift the rest of
        # the elements to `shift_number` positions to the right.
        needle_pos = asc_number + shift_number

        print(i, needle_pos, salary)

        if needle_pos != i:
            for j in range(needle_pos, i, -1):
                salary[j], salary[j - 1] = salary[j - 1], salary[j]
            shift_number += 1

        print(salary)

    return salary

test = SynchronizingTables(3, [3, 1024], [20000, 100000, 90000])
print(test)
