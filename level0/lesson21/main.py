def BiggerGreater(input_str):
    if len(input_str) < 2:
        return ''

    output_chars = []
    for i in range(len(input_str)):
        output_chars.append(input_str[i])

    threshold_pos = -1
    for i in range(len(output_chars) - 1, 0, -1):
        for j in range(i - 1, -1, -1):
            if output_chars[i] > output_chars[j]:
                output_chars[i], output_chars[j] = output_chars[j], output_chars[i]
                threshold_pos = j
                break

        if threshold_pos >= 0:
            break
    else:
        return ''

    for i in range(threshold_pos + 1, len(output_chars) - 1):
        for j in range(i + 1, len(output_chars)):
            if output_chars[j] < output_chars[i]:
                output_chars[i], output_chars[j] = output_chars[j], output_chars[i]

    output_str = ''.join(output_chars)
    return output_str
