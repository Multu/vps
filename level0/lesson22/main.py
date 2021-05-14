def is_equal_elements(input_list):
    if len(input_list) == 0:
        return True

    first_element = input_list[0]
    for i in range(1, len(input_list)):
        if first_element != input_list[i]:
            return False

    return True


def group

def SherlockValidString(input_str):
    if len(input_str) < 2:
        return False

    # Create list with pairs of [char => count of its meeting] in string.
    chars_dict = []
    for i in range(len(input_str)):
        char = input_str[i]
        for j in range(len(chars_dict)):
            if chars_dict[j][0] == char:
                chars_dict[j][1] += 1
                break
        else:
            chars_dict.append([char, 1])

    # List with only count of each char appears in string
    chars_meeting_count = []
    for i in range(len(chars_dict)):
        chars_meeting_count.append(chars_dict[i][1])

    print(chars_meeting_count)

    # Fill list with pairs of count of same chars -> count of it this combinations.
    combination_dict = []
    for i in range(len(chars_meeting_count)):
        count_chars = chars_meeting_count[i]
        for j in range(len(combination_dict)):
            if combination_dict[j][0] == count_chars:
                combination_dict[j][1] += 1
                break
        else:
            combination_dict.append([count_chars, 1])

    combination_meeting = []
    for i in range(len(combination_dict)):
        combination_meeting.append(combination_dict[i][0])

    print(chars_meeting_count)
    print(combination_dict)
    print(combination_meeting)

    # If occurs only one combination, then input string is valid.
    #
    # If occurs two combination, then possible to get a valid string.
    #
    # If occurs more than two combinations, then impossible to get
    # valid string with one attempt to delete a character.
    if len(combination_dict) == 1:
        is_valid_str = True
    elif len(combination_dict) == 2:
        is_valid_str = False
        for i in range(len(combination_dict)):
            if combination_dict[i][1] == 1:
                combination_meeting_copy = list(combination_meeting)
                combination_meeting_copy[i] -= 1
                if combination_meeting_copy[i] == 0:
                    combination_meeting_copy.pop(i)

                is_equal_copy = is_equal_elements(combination_meeting_copy)
                if is_equal_copy:
                    is_valid_str = True
                    break
    else:
        is_valid_str = False

    print(is_valid_str)

    return is_valid_str


SherlockValidString('xyzaa')
