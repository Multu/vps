def LineAnalysis(line):
    separator_char = '*'

    if len(line) == 0:
        return False

    if line[0] == line[len(line) - 1] == separator_char:
        pass
    else:
        return False

    # Collect all templates between separator char.
    templates_list = []
    template_item_chars = []
    for i in range(1, len(line) - 1):
        if line[i] == separator_char:
            templates_list.append(''.join(template_item_chars))
            template_item_chars = []
        else:
            template_item_chars.append(line[i])
    templates_list.append(''.join(template_item_chars))

    # Check if all templates are equals.
    for i in range(len(templates_list) - 1):
        if templates_list[i] != templates_list[i + 1]:
            return False

    return True
