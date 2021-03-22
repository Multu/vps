def SynchronizingTables(N, ids, salary):

    # Sort salary list by asc.
    sorted_salary = list(salary)
    for i in range(N - 1):
        for j in range(i + 1, N):
            if sorted_salary[j] < sorted_salary[i]:
                sorted_salary[i], sorted_salary[j] = sorted_salary[j], sorted_salary[i]

    replaced_salary = list(salary)

    for i in range(N):
        # Calculate count of ids elements,
        # that values are less then current value.
        asc_number = 0
        for j in range(N):
            if ids[j] < ids[i]:
                asc_number += 1

        replaced_salary[i] = sorted_salary[asc_number]

    return replaced_salary
