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


def decrypt(s):
    # Separate string by words.
    words_list = []

    word = []
    for i in range(len(s)):
        if s[i] == ' ':
            if len(word):
                words_list.append(word)
                word = []
        else:
            word.append(s[i])

    if len(word):
        words_list.append(word)


    # Aligns the size of words by padding them with blank characters.
    max_word_size = 0
    for i in range(len(words_list)):
        word_len = len(words_list[i])
        if word_len > max_word_size:
            max_word_size = word_len

    for i in range(len(words_list)):
        while len(words_list[i]) < max_word_size:
            words_list[i].append('')

    # Generate decoded string.
    decoded_list = []

    for i in range(max_word_size):
        for j in range(len(words_list)):
            decoded_list.append(words_list[j][i])

    decoded_str = ''.join(decoded_list)

    return decoded_str


def TheRabbitsFoot(s, encode):
    if encode:
        res = encrypt(s)
    else:
        res = decrypt(s)

    return res

