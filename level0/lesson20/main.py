COMMAND_ADD = '1'
COMMAND_DELETE = '2'
COMMAND_GET = '3'
COMMAND_UNDO = '4'
COMMAND_REDO = '5'

pointer_filename = 'pointer'
history_filename = 'history'


def current_state():
    pointer = 0
    undo_state = ''

    try:
        f = open(pointer_filename, 'r')
        pointer = int(f.readline().strip('\n'))
        undo_state = f.readline().strip('\n')
    except IOError:
        f = open(pointer_filename, 'w')
        f.write(str(pointer))
        f.write(undo_state)
    finally:
        f.close()

    return [pointer, undo_state]


def save_state(pointer, is_undo=False):
    f = open(pointer_filename, 'w')
    f.write(str(pointer) + '\n')
    if is_undo:
        f.write('undo\n')
    else:
        f.write('')
    f.close()
    return pointer


def get_string(pointer):
    cur_str = ''

    try:
        f = open(history_filename, 'r')
        cur_str = f.readlines()[pointer].strip('\n')
    except IOError:
        f = open(history_filename, 'w')
        f.write(cur_str)
        f.write('\n')
    finally:
        f.close()

    return cur_str


def clear_history():
    f = open(history_filename, 'w')
    f.close()


def add_string(new_str):
    f = open(history_filename, 'a')
    f.write(new_str)
    f.write('\n')
    f.close()


def edit_string(line, new_str):
    f = open(history_filename, 'r')
    lines = f.readlines()
    f.close()

    lines[line] = new_str + '\n'
    f = open(history_filename, 'w')
    f.writelines(lines)
    f.close()


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
    cur_state = current_state()
    pointer = cur_state[0]
    undo_state = cur_state[1]

    cur_str = get_string(pointer)

    if len(part_str):
        new_str = cur_str + part_str

        if undo_state:
            new_pointer = 1

            clear_history()
            add_string(cur_str)
            add_string(new_str)
        else:
            new_pointer = pointer + 1
            add_string(new_str)

        save_state(new_pointer)
    else:
        new_str = cur_str

    return new_str


def delete(n):
    cur_state = current_state()
    pointer = cur_state[0]
    undo_state = cur_state[1]
    cur_str = get_string(pointer)

    if n > 0 and len(cur_str) > 0:
        new_str_chars = []
        for i in range(len(cur_str) - n):
            new_str_chars.append(cur_str[i])
        new_str = ''.join(new_str_chars)

        if undo_state:
            new_pointer = 1

            clear_history()
            add_string(cur_str)
            add_string(new_str)
        else:
            new_pointer = pointer + 1
            add_string(new_str)

        save_state(new_pointer)
    else:
        new_str = cur_str

    return new_str


def get_char(n):
    cur_state = current_state()
    pointer = cur_state[0]
    cur_str = get_string(pointer)
    try:
        pos_char = cur_str[n]
    except Exception:
        pos_char = ''

    edit_string(pointer, pos_char)

    return pos_char


def undo():
    cur_state = current_state()
    pointer = cur_state[0]
    cur_str = get_string(pointer)

    if pointer > 0:
        pointer -= 1

    save_state(pointer, is_undo=True)
    new_str = get_string(pointer)

    return new_str


def redo():
    cur_state = current_state()
    pointer = cur_state[0]
    cur_str = get_string(pointer)

    with open(history_filename, 'r') as f:
        count_lines = len(f.readlines())

    if pointer < count_lines - 1:
        pointer += 1

    save_state(pointer)
    new_str = get_string(pointer)

    return new_str


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
        try:
            pos = int(param)
            pos_char = get_char(pos)
        except Exception:
            pos_char = ''

        return pos_char

    if n == COMMAND_UNDO:
        new_str = undo()
        return new_str

    if n == COMMAND_REDO:
        new_str = redo()
        return new_str
