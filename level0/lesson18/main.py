def shift_group(source_list, indexes_list):
    # Find minimum value among the shifted elements.
    min_shifted_value = source_list[indexes_list[0]]
    for i in range(1, len(indexes_list)):
        if source_list[indexes_list[i]] < min_shifted_value:
            min_shifted_value = source_list[indexes_list[i]]

    # Shift elements until the minimum value will be on the left position.
    while source_list[indexes_list[0]] != min_shifted_value:
        left_element = source_list[indexes_list[0]]
        for i in range(1, len(indexes_list)):
            source_list[indexes_list[i - 1]] = source_list[indexes_list[i]]
        source_list[indexes_list[-1]] = left_element

    return source_list


def MisterRobot(n, data):
    input_data = list(data)
    shift_count = 3

    for i in range(n - shift_count + 1):
        target_value = i + 1

        while input_data[i] != target_value:
            # Find index of target element.
            target_index = -1
            for j in range(i + 1, n):
                if input_data[j] == target_value:
                    target_index = j
                    break
            else:
                return False

            # Select a list of elements to future shifts.
            shift_index = []
            # First, add to list target element and previous `shift_count - 1` items.
            for shift_i in range(shift_count):
                shift_index.append(target_index - shift_count + shift_i + 1)

            # Check, that the list does not include elements previously processed.
            additional_shift = i - shift_index[0]
            if additional_shift > 0:
                for shift_i in range(shift_count):
                    shift_index[shift_i] += additional_shift

            input_data = shift_group(input_data, shift_index)

    # Last `shift_count` elements of input list must be equal to its `index  + 1`
    for i in range(1, shift_count):
        if input_data[n - i] != n - i + 1:
            return False

    return True

