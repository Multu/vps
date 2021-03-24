def get_point_coords(keyboard, digit):
    for i in range(len(keyboard)):
        for j in range(len(keyboard[i])):
            if keyboard[i][j] == digit:
                return [i, j]

    return False

def PatternUnlock(N, hits):
    keyboard = [[6, 1, 9],
                [5, 2, 8],
                [4, 3, 7]]

    line_length = 0
    for i in range(N - 1):
        point1 = get_point_coords(keyboard, hits[i])
        point2 = get_point_coords(keyboard, hits[i + 1])

        if point1 and point2:
            point_distance = ((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2) ** 0.5
            line_length += point_distance

    code_digits = []
    code_string = str(int(round(line_length, 5) * 100000))
    for i in range(len(code_string)):
        if code_string[i] != '0':
            code_digits.append(code_string[i])

    code = ''.join(code_digits)
    return code
