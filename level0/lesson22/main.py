def is_equal_elements(input_list):
    if len(input_list) == 0:
        return True

    first_element = input_list[0]
    for i in range(1, len(input_list)):
        if first_element != input_list[i]:
            return False

    return True


def group_by_unique_element(source):
    """Create list with pairs of [element => count of its meeting] in `source`."""
    input_list = list(source)

    grouped_list = []
    for i in range(len(input_list)):
        elem = input_list[i]
        for j in range(len(grouped_list)):
            if grouped_list[j][0] == elem:
                grouped_list[j][1] += 1
                break
        else:
            grouped_list.append([elem, 1])

    return grouped_list


def SherlockValidString(input_str):
    if len(input_str) < 2:
        return False

    chars_grouped = group_by_unique_element(input_str)
    chars_count = []
    for i in range(len(chars_grouped)):
        chars_count.append(chars_grouped[i][1])

    combinations_grouped = group_by_unique_element(chars_count)
    combinations_length = []
    for i in range(len(combinations_grouped)):
        combinations_length.append(combinations_grouped[i][0])

    # If occurs only one combination, then input string is valid.
    # If occurs two combination, then possible to get a valid string.
    # If occurs more than two combinations, then impossible to get
    # valid string with one attempt to delete a character.
    if len(combinations_grouped) == 1:
        is_valid_str = True
    elif len(combinations_grouped) == 2:
        is_valid_str = False

        for i in range(len(combinations_grouped)):
            combination = combinations_grouped[i]
            if combination[1] == 1:
                if combination[0] == 1:
                    is_valid_str = True
                    break
                else:
                    comb_length_copy = list(combinations_length)
                    comb_length_copy[i] -= 1

                    if is_equal_elements(comb_length_copy):
                        is_valid_str = True
                        break
    else:
        is_valid_str = False

    return is_valid_str
