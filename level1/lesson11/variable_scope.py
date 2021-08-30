# Код до режакторига.

def encrypt(s):
    # Remove space symbols.
    no_space_list = []
    for i in range(len(s)):
        if s[i] != ' ':
            no_space_list.append(s[i])
    no_space = ''.join(no_space_list)

    # Calculate thresholds.
    # If square value if an integer value, then low and high thresholds must be the same.
    # If value is fractional, then high value must be greater then low value.
    no_space_len = len(no_space)
    low_thr = int(no_space_len ** 0.5)

    if low_thr ** 2 == no_space_len:
        high_thr = low_thr
    else:
        high_thr = low_thr + 1

    # Definition matrix size.
    rows = low_thr
    cols = high_thr
    if rows * cols < no_space_len:
        rows += 1

    # Fill chars matrix.
    while len(no_space_list) < rows * cols:
        no_space_list.append('')

    matrix = []
    for i in range(rows):
        row_value = []
        for j in range(cols):
            row_value.append(no_space_list[i * cols + j])
        matrix.append(row_value)

    # Generate encoded string.
    encoded_words = []
    for i in range(cols):
        encoded_word = []
        for j in range(rows):
            if matrix[j][i] != '':
                encoded_word.append(matrix[j][i])
        encoded_words.append(''.join(encoded_word))

    encoded_str = ' '.join(encoded_words)

    return encoded_str


# Этот же код после рефакторинга.
# Связанные команды сгруппированы в отдельные функции.
# Переменные локализованы на уровне отдельных небольших функций.

def extract_no_space_chars(s):
    no_space_chars = []
    for i in range(len(s)):
        if s[i] != ' ':
            no_space_chars.append(s[i])
    return no_space_chars


def calculate_encrypt_matrix_dimension(chars_count):
    rows = int(chars_count ** 0.5)
    if rows ** 2 == chars_count:
        cols = rows
    else:
        cols = rows + 1

    if rows * cols < chars_count:
        rows += 1

    return [rows, cols]


def create_encrypt_matrix(rows, cols, source):
    source_aligned = list(source)
    while len(source_aligned) < rows * cols:
        source_aligned.append('')

    matrix = []
    for i in range(rows):
        row_value = []
        for j in range(cols):
            row_value.append(source_aligned[i * cols + j])
        matrix.append(row_value)

    return matrix


def get_encoded_words(encrypt_matrix):
    encoded_words = []

    rows = len(encrypt_matrix)
    cols = len(encrypt_matrix[0])

    for i in range(cols):
        encoded_word = []
        for j in range(rows):
            if encrypt_matrix[j][i] != '':
                encoded_word.append(encrypt_matrix[j][i])
        encoded_words.append(''.join(encoded_word))

    return encoded_words


def encrypt(s):
    no_space_chars = extract_no_space_chars(s)
    matrix_dimension = calculate_encrypt_matrix_dimension(len(no_space_chars))
    matrix = create_encrypt_matrix(matrix_dimension[0], matrix_dimension[1], no_space_chars)
    encoded_words = get_encoded_words(matrix)
    encoded_str = ' '.join(encoded_words)
    return encoded_str