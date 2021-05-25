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
        #if len(combinations) > 1:
        #    combinations.pop(0)
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
    print(terms)
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


def list_to_brackets(term):
    brackets = []

    for i in range(len(term)):
        brackets_item = []
        for k in range(term[i]):
            brackets_item.append('(')
        for k in range(term[i]):
            brackets_item.append(')')
    brackets.append(''.join(brackets_item))
    return brackets


def digit_to_brackets(digit):
    brackets = []

    for k in range(digit):
        brackets.append('(')
    for k in range(digit):
        brackets.append(')')

    return ''.join(brackets)


def all_brackets_combination(n, brackets, outer_br):

    for i in range(n, 0, -1):
        terms = generate_terms(i, [])
        terms_brackets = generate_brackets(terms)
        for j in range(len(terms_brackets)):
            outer_brackets = n - i
            bracket = '(' * outer_brackets + terms_brackets[j] + ')' * outer_brackets
            brackets.append(bracket)

    return brackets

def BalancedParentheses(n):
    brackets = all_brackets_combination(n, [], 0)
    return ' '.join(brackets)


n = 3

def test(n, combinations, outer):
    print('def call', n, combinations)

    terms = generate_terms(n, [])


    if n == 1:
        return [1]
    else:

        terms = generate_terms(n, [])
        for i in range(len(terms)):
            term = terms[i]
            for j in range(len(term)):
                if term[j] > 1:
                    term[j] = test(term[j] - 1, combinations)

    return combinations

def test2(n):
    combination = []
    terms = generate_terms(n, [])
    for i in range(len(terms)):
        term = terms[i]
        combination.append(term)
        brackets_combinations = list_to_brackets(term)
        #combination.append(brackets_combinations)
        for j in range(len(term)):
            if term[j] > 1:

                start_line = ''
                for m in range(0, j):
                    start_line += digit_to_brackets(term[m])

                end_line = ''
                for m in range(j, len(term)):
                    end_line += digit_to_brackets(term[m])

                comb_rec = test2(term[j] - 1)
                for k in range(len(comb_rec)):
                    term2 = list(term)
                    term2[j] = comb_rec[k]
                   # print(comb_rec[k])
                    combination.append(term2)
                    #combination.append(start_line + '(' + list_to_brackets(comb_rec[k][0]) + ')' + end_line)


    return combination

res = test2(5)
print(res, len(res))