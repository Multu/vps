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
        if len(combinations) > 1:
            combinations.pop(0)
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


def generate_brackets(terms):
    brackets = []

    for i in range(len(terms)):
        brackets_item = []

        term = terms[i]
        for j in range(len(term)):
            for k in range(term[j]):
                brackets_item.append('(')
            for k in range(term[j]):
                brackets_item.append(')')
        brackets.append(''.join(brackets_item))

    return brackets


def BalancedParentheses(n):
    brackets = []

    for i in range(n, 0, -1):
        terms = generate_terms(i, [])
        terms_brackets = generate_brackets(terms)
        for j in range(len(terms_brackets)):
            outer_brackets = n - i
            bracket = '(' * outer_brackets + terms_brackets[j] + ')' * outer_brackets
            brackets.append(bracket)

    return ' '.join(brackets)
