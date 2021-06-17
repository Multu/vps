def generate_brackets(max_count, open_count=0, close_count=0, cur_brackets='', combinations=[]):
    if max_count == len(cur_brackets):
        combinations.append(cur_brackets)
        return

    if open_count < max_count / 2:
        generate_brackets(max_count, open_count + 1, close_count, cur_brackets + '(', combinations)

    if open_count > close_count:
        generate_brackets(max_count, open_count, close_count + 1, cur_brackets + ')', combinations)

    return combinations


def BalancedParentheses(n):
    combinations = generate_brackets(n * 2)
    return ' '.join(combinations)
