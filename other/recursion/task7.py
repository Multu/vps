def unique(source):
    unique_list = []
    for i in range(len(source)):
        for j in range(len(unique_list)):
            if source[i] == unique_list[j]:
                break
        else:
            unique_list.append(source[i])
    return unique_list


def pop_min_value(source):
    min_value_index = 0

    for i in range(1, len(source)):
        if source[i] < source[min_value_index]:
            min_value_index = i

    return source.pop(min_value_index)


def second_maximum(source):
    if len(source) > 2:
        head = source[:3]
        tail = source[3:]

        # First element of `unique_head` store max value, next one - second max value.
        # The values must be different.
        unique_head = unique(head)
        if len(unique_head) > 2:
            _ = pop_min_value(unique_head)

        return second_maximum(unique_head + tail)

    elif len(source) == 2:
        unique_source = unique(source)
        if len(unique_source) == 2:
            min_value = pop_min_value(unique_source)
            return min_value
