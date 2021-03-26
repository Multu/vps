def split_to_words(s):
    words = []

    word = []
    for i in range(len(s)):
        if s[i] == ' ':
            if len(word) > 0:
                words.append(''.join(word))
                word = []
        else:
            word.append(s[i])

    if len(word) > 0:
        words.append(''.join(word))

    return words


def append_word(line, word):
    for i in range(len(word)):
        line.append(word[i])
    return line


def split_to_aligment_lines(len_alignment, s):
    words = split_to_words(s)

    lines = []

    line = []

    for i in range(len(words)):
        word = words[i]

        reserved_line_len = len(line)
        # Reserve place for space symbol between words.
        if reserved_line_len:
            reserved_line_len += 1

        if len(word) > len_alignment:
            if reserved_line_len:
                lines.append(''.join(line))
                line = []

            for j in range(len(word)):
                line.append(word[j])
                if len(line) == len_alignment:
                    lines.append(''.join(line))
                    line = []
        else:
            if reserved_line_len + len(word) > len_alignment:
                lines.append(''.join(line))
                line = append_word([], word)
            else:
                if reserved_line_len:
                    line.append(' ')
                line = append_word(line, word)

    if len(line):
        lines.append(''.join(line))

    return lines


def WordSearch(len_alignment, s, subs):
    if len_alignment <= 0:
        return []

    lines = split_to_aligment_lines(len_alignment, s)

    search_seq = []
    for i in range(len(lines)):
        str_exists = 0
        line_words = split_to_words(lines[i])
        for j in range(len(line_words)):
            if line_words[j] == subs:
                str_exists = 1
        search_seq.append(str_exists)

    return search_seq

