import main


def is_palindrome(input_str):
    deque = main.Deque()
    for i in range(len(input_str)):
        deque.addTail(input_str[i])

    while deque.size() > 1:
        if deque.removeTail() != deque.removeFront():
            return False
    return True
