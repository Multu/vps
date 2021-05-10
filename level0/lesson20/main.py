COMMAND_ADD = '1'
COMMAND_DELETE = '2'
COMMAND_GET = '3'
COMMAND_UNDO = '4'
COMMAND_REDO = '5'

history = ['']
pointer = 0
undo_state = False


def current_string():
    return history[pointer]


def parse_command(command):
    n_chars = []
    param_chars = []

    separator_appeared = False
    for i in range(len(command)):
        if separator_appeared:
            param_chars.append(command[i])
        elif command[i] == ' ':
            separator_appeared = True
            continue
        else:
            n_chars.append(command[i])

    n = ''.join(n_chars)
    param = ''.join(param_chars)

    return [n, param]


def add(part_str):
    global history, pointer, undo_state

    cur_str = current_string()

    if len(part_str):
        new_str = cur_str + part_str

        if undo_state:
            history = [cur_str, new_str]
            pointer = 1
        else:
            history.append(new_str)
            pointer += 1

        undo_state = False
        cur_str = current_string()

    return cur_str


def delete(n):
    global history, pointer, undo_state

    cur_str = current_string()

    if n > 0 and len(cur_str) > 0:
        new_str_chars = []
        for i in range(len(cur_str) - n):
            new_str_chars.append(cur_str[i])
        new_str = ''.join(new_str_chars)

        if undo_state:
            history = [cur_str, new_str]
            pointer = 1
        else:
            history.append(new_str)
            pointer += 1

        undo_state = False
        cur_str = current_string()

    return cur_str


def get_char(n):
    global history, pointer

    cur_str = current_string()
    try:
        pos = int(n)
        if pos >= 0:
            pos_char = cur_str[pos]
        else:
            pos_char = ''
    except Exception:
        pos_char = ''

    history[pointer] = pos_char
    return pos_char


def undo():
    global history, pointer, undo_state

    if pointer > 0:
        pointer -= 1
        undo_state = True

    cur_str = current_string()
    return cur_str


def redo():
    global history, pointer, undo_state

    if pointer < len(history) - 1:
        pointer += 1

    cur_str = current_string()
    return cur_str


def BastShoe(command):
    parsed_command = parse_command(command)
    n = parsed_command[0]
    param = parsed_command[1]

    if n == COMMAND_ADD:
        new_str = add(param)
        return new_str

    if n == COMMAND_DELETE:
        try:
            del_count = int(param)
        except Exception:
            del_count = 0

        new_str = delete(del_count)
        return new_str

    if n == COMMAND_GET:
        pos_char = get_char(param)
        return pos_char

    if n == COMMAND_UNDO:
        new_str = undo()
        return new_str

    if n == COMMAND_REDO:
        new_str = redo()
        return new_str

    cur_str = current_string()
    return cur_str
