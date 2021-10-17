import main


def is_brackets_in_balance(brackets):
    stack = main.Stack()

    for i in range(len(brackets)):
        if brackets[i] == '(':
            stack.push(brackets[i])
        if brackets[i] == ')':
            if stack.size() > 0:
                stack.pop()
            else:
                return False

    return stack.size() == 0
