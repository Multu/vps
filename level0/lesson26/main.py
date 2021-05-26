def sum_list(source_list):
    res = 0
    for i in range(len(source_list)):
        res += source_list[i]
    return res


def generate_terms(total_sum, combinations):
    if len(combinations) == 0:
        combinations.append([total_sum])

    stop_combination = [1] * total_sum

    if combinations[-1] == stop_combination:
        return list(combinations)
    else:
        previous_combination = combinations[-1]
        current_combination = list(previous_combination)

        for i in range(len(current_combination) - 1, -1, -1):
            if current_combination[i] == 1:
                current_combination.pop()
            else:
                current_combination[-1] -= 1
                break

        current_sum = sum_list(current_combination)
        current_combination.append(total_sum - current_sum)
        combinations.append(current_combination)

        return generate_terms(total_sum, combinations)


def digit_to_brackets(digit):
    brackets = []

    for k in range(digit):
        brackets.append('(')
    for k in range(digit):
        brackets.append(')')

    return ''.join(brackets)


def all_combinations(n):
    combinations = []
    terms = generate_terms(n, [])
    for i in range(len(terms)):
        term = terms[i]
        combinations.append(term)
        for j in range(len(term)):
            if term[j] > 1:
                inner_combinations = all_combinations(term[j] - 1)
                for k in range(len(inner_combinations)):
                    inner_term = list(term)
                    inner_term[j] = inner_combinations[k]
                    combinations.append(inner_term)

    return combinations


def combinations_to_brackets(combinations_list):
    brackets_list = []

    for i in range(len(combinations_list)):
        combination = combinations_list[i]
        brackets_line = ''

        for j in range(len(combination)):
            combination_element = combination[j]
            if isinstance(combination_element, int):
                brackets_line += digit_to_brackets(combination_element)
            else:
                inner_combinations = combinations_to_brackets([combination_element])
                if len(inner_combinations):
                    brackets_line += '('
                    for k in range(len(inner_combinations)):
                        brackets_line += inner_combinations[k]
                    brackets_line += ')'

        brackets_list.append(brackets_line)

    return brackets_list


def unique_list(source_list):
    unique_elements = []
    for i in range(len(source_list)):
        for j in range(len(unique_elements)):
            if source_list[i] == unique_elements[j]:
                break
        else:
            unique_elements.append(source_list[i])

    return unique_elements


def BalancedParentheses(n):
    combinations = all_combinations(n)
    brackets = combinations_to_brackets(combinations)
    unique_brackets = unique_list(brackets)
    return ' '.join(unique_brackets)
