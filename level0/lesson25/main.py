def max_value_in_range(value_list, from_pos, to_pos):
    max_value = value_list[from_pos]

    for i in range(to_pos + 1):
        if value_list[i] > max_value:
            max_value = value_list[i]

    return max_value


def transform(a):
    b = []

    for i in range(len(a)):
        for j in range(len(a) - i):
            k = i + j
            max_value = max_value_in_range(a, j, k)
            b.append(max_value)

    return b


def TransformTransform(a, n):
    s_a = transform(a)
    s_s_a = transform(s_a)

    key_value = 0
    for i in range(len(s_s_a)):
        key_value += s_s_a[i]

    is_even = key_value % 2 == 0
    return is_even

