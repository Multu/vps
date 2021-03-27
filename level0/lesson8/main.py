def SumOfThe(n, data):
    for i in range(n):
        sum_res = data[i]

        sum_other = 0
        for j in range(n):
            if i != j:
                sum_other += data[j]

        if sum_res == sum_other:
            return sum_res

    return 0
