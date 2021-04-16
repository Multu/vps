def fill_matrix(h, w, s):
    m = []

    char_index = 0
    for i in range(h):
        row = []
        for j in range(w):
            row.append(s[char_index])
            char_index += 1
        m.append(row)

        # Space delimiter
        char_index += 1

    return m

def crop_matrix(source, x, y, h, w):
    cropped = []

    for i in range(x, x+ h):
        row = []
        for j in range(y, y + w):
            row.append(source[i][j])
        cropped.append(row)

    return cropped


def is_equal_matrix(h, w, m1, m2):
    for i in range(h):
        for j in range(w):
            if m1[i][j] != m2[i][j]:
                return False

    return True


def TankRush(h1, w1, s1, h2, w2, s2):
    m1 = fill_matrix(h1, w1, s1)
    m2 = fill_matrix(h2, w2, s2)

    if h2 * w2 == 0:
        return True

    first_tank_el = m2[0][0]

    for i in range(0, h1 - h2 + 1):
        for j in range(0, w1 - w2 + 1):
            if first_tank_el == m1[i][j]:
                cropped_matrix = crop_matrix(m1, i, j, h2, w2)
                if is_equal_matrix(h2, w2, cropped_matrix, m2):
                    return True

    return False
