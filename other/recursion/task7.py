def unique(source):
    unique_list = []
    for i in range(len(source)):
        for j in range(len(unique_list)):
            if source[i] == unique_list[j]:
                break
        else:
            unique_list.append(source[i])
    return unique_list


def second_maximum(source):
    if len(source) > 2:
        head = source[:3]
        tail = source[3:]

        # First element of `unique_head` store max value, next one - second max value.
        # The values must be different.
        unique_head = unique(head)
        unique_head.sort(reverse=True)
        if len(unique_head) > 2:
            unique_head = unique_head[:2]

        return second_maximum(unique_head + tail)

    elif len(source) == 2:
        unique_source = unique(source)
        unique_source.sort(reverse=True)
        try:
            return unique_source[1]
        except Exception:
            pass
