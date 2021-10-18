import main


def evaluate_expression(expression):
    allowed_operators = ['+', '*', '=']

    source_stack = main.Stack()
    expression_parts = expression.split(' ')
    for i in range(len(expression_parts)-1, -1, -1):
        try:
            expression_number = int(expression_parts[i])
            source_stack.push(expression_number)
        except ValueError:
            if expression_parts[i] in allowed_operators:
                source_stack.push(expression_parts[i])
            else:
                raise ValueError('Not allowed operator')

    compute_stack = main.Stack()
    while source_stack.size():
        operand_or_operator = source_stack.pop()

        if operand_or_operator in ['+', '*'] and compute_stack.size() == 2:
            operand_one = compute_stack.pop()
            operand_two = compute_stack.pop()

            if operand_or_operator == '+':
                computed_operands = operand_one + operand_two
            if operand_or_operator == '*':
                computed_operands = operand_one * operand_two

            compute_stack.push(computed_operands)
            continue

        if isinstance(operand_or_operator, int) and compute_stack.size() < 2:
            compute_stack.push(operand_or_operator)
            continue

        if operand_or_operator == '=' and compute_stack.size() == 1 and source_stack.size() == 0:
            return compute_stack.pop()

        raise RuntimeError('Incorrect order of operator or operand')

    if compute_stack.size():
        raise RuntimeError('Not enough operators or operands')
