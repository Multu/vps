def shift_line_matrix(matrix, t):
    m = len(matrix)
    t = t % m

    shifted_matrix = list(matrix)
    for i in range(m):
        new_pos = i + t
        if new_pos > m - 1:
            new_pos = new_pos - m
        shifted_matrix[new_pos] = matrix[i]

    return shifted_matrix


def border_coords_list(m, n, border_number):
    coords = []

    for i in range(border_number, n - border_number):
        coords.append([border_number, i])
    for i in range(border_number + 1, m - border_number):
        coords.append([i, n - border_number - 1])
    for i in range(n - border_number - 2, border_number - 1, -1):
        coords.append([m - border_number - 1, i])
    for i in range(m - border_number - 2, border_number, -1):
        coords.append([i, border_number])

    return coords


def get_matrix_elements(matrix, coords):
    line_matrix = []

    for i in range(len(coords)):
        coords_pair = coords[i]
        line_matrix.append(matrix[coords_pair[0]][coords_pair[1]])

    return line_matrix


def update_matrix_elements(matrix, coords, shifted_line_matrix):
    for i in range(len(coords)):
        coords_pair = coords[i]
        matrix[coords_pair[0]][coords_pair[1]] = shifted_line_matrix[i]

    return


def MatrixTurn(Matrix, M, N, T):
    matrix = []

    # Convert list of strings to two-dimensional matrix of chars.
    for i in range(M):
        row = []
        for j in range(N):
            row.append(Matrix[i][j])
        matrix.append(row)

    # Calculate count of layers for transform cycle.
    min_side = M
    if N < min_side:
        min_side = N
    layers_count = min_side // 2

    # Shift each border layer of source two-dimensional matrix.
    for k in range(layers_count):
        border_coords = border_coords_list(M, N, k)
        border_line = get_matrix_elements(matrix, border_coords)
        shifted_border_line = shift_line_matrix(border_line, T)
        update_matrix_elements(matrix, border_coords, shifted_border_line)

    # Update source list of strings.
    for i in range(M):
        line_str_chars = []
        for j in range(N):
            line_str_chars.append(matrix[i][j])
        Matrix[i] = ''.join(line_str_chars)

    return
