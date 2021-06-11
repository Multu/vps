def unique(source):
    unique_list = []
    for i in range(len(source)):
        for j in range(len(unique_list)):
            if source[i] == unique_list[j]:
                break
        else:
            unique_list.append(source[i])
    return unique_list


def sort_desc(source):
    for i in range(len(source) - 1):
        for j in range(i + 1, len(source)):
            if source[j] > source[i]:
                source[i], source[j] = source[j], source[i]


def second_maximum(source):
    if len(source) > 2:
        head = source[:3]
        tail = source[3:]

        # First element of `unique_head` store max value, next one - second max value.
        # The values must be different.
        unique_head = unique(head)
        sort_desc(unique_head)
        if len(unique_head) > 2:
            unique_head = unique_head[:2]

        return second_maximum(unique_head + tail)

    elif len(source) == 2:
        unique_source = unique(source)
        sort_desc(unique_source)
        if len(unique_source) == 2:
            return unique_source[1]
