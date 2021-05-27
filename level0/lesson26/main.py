def generate_brackets(max_count, open_count, close_count, cur_list, combinations):
    if max_count == len(cur_list):
        combinations.append(''.join(cur_list))
        return

    if open_count < max_count / 2:
        cur_copy = list(cur_list)
        cur_copy.append('(')
        generate_brackets(max_count, open_count + 1, close_count, cur_copy, combinations)

    if open_count > close_count:
        cur_copy = list(cur_list)
        cur_copy.append(')')
        generate_brackets(max_count, open_count, close_count + 1, cur_copy, combinations)

    return combinations

def BalancedParentheses(n):
    combinations = generate_brackets(n * 2, 0, 0, [], [])
    return ' '.join(combinations)
