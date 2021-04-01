def BigMinus(s1, s2):

    # Create lists of digits for both digital strings.
    # If the original strings are of different lengths,
    # then align the digits to the right and pad the left with zeros.
    long1 = len(s1)
    long2 = len(s2)

    if long1 > long2:
        max_long = long1
    else:
        max_long = long2

    list1 = []
    list2 = []
    sub_lists = []

    for i in range(max_long):
        list1.append(0)
        list2.append(0)
        sub_lists.append(0)

    for i in range(long1 - 1, -1, -1):
        list1[i + max_long - long1] = int(s1[i])
    for i in range(long2 - 1, -1, -1):
        list2[i + max_long - long2] = int(s2[i])

    # The `list1` should contain digits of a larger number.
    # Otherwise, swap the content of the `list1` and `list2`
    for i in range(max_long):
        if list1[i] == list2[i]:
            continue

        if list1[i] > list2[i]:
            break
        else:
            list1, list2 = list2, list1
            break

    # Calculation of the subtraction between `list1` and `list2`
    for i in range(max_long - 1, -1, -1):
        sub_digits = list1[i] - list2[i]
        if sub_digits < 0:
            sub_digits += 10
            list1[i - 1] -= 1
        sub_lists[i] = sub_digits

    # Remove first zero digits
    while sub_lists[0] == 0:
        sub_lists.pop(0)
        if len(sub_lists) == 0:
            break

    # Convert result to string type
    for i in range(len(sub_lists)):
        sub_lists[i] = str(sub_lists[i])

    sub_str = ''.join(sub_lists)
    if len(sub_str) == 0:
        sub_str = '0'

    return sub_str
