def init_tree(H, W, tree):
    digital_tree = []

    for i in range(H):
        tree_row = []
        for j in range(W):
            if tree[i][j] == '.':
                tree_row.append(0)
            elif tree[i][j] == '+':
                tree_row.append(1)
            else:
                tree_row.append(0)
        digital_tree.append(tree_row)

    return digital_tree


def show_tree(H, W, digital_tree):
    tree = []

    for i in range(H):
        tree_row_chars = []
        for j in range(W):
            if digital_tree[i][j] == 0:
                tree_row_chars.append('.')
            else:
                tree_row_chars.append('+')
        tree.append(''.join(tree_row_chars))

    return tree


def grow_tree(H, W, tree):
    new_tree = list(tree)

    for i in range(H):
        for j in range(W):
            new_tree[i][j] += 1

    return new_tree


def destroy_tree(H, W, tree):
    new_tree = list(tree)

    for i in range(H):
        for j in range(W):
            if new_tree[i][j] >= 3:
                i_up = i - 1
                if 0 <= i_up <= H - 1 and new_tree[i_up][j] < 3:
                    new_tree[i_up][j] = 0

                i_down = i + 1
                if 0 <= i_down <= H - 1 and new_tree[i_down][j] < 3:
                    new_tree[i_down][j] = 0

                j_left = j - 1
                if 0 <= j_left <= W - 1 and new_tree[i][j_left] < 3:
                    new_tree[i][j_left] = 0

                j_rigth = j + 1
                if 0 <= j_rigth <= W - 1 and new_tree[i][j_rigth] < 3:
                    new_tree[i][j_rigth] = 0

    for i in range(H):
        for j in range(W):
            if new_tree[i][j] >= 3:
                new_tree[i][j] = 0

    return new_tree


def TreeOfLife(H, W, N, tree):
    digital_tree = init_tree(H, W, tree)

    for i in range(N):
        if i % 2 == 0:
            digital_tree = grow_tree(H, W, digital_tree)
        else:
            digital_tree = grow_tree(H, W, digital_tree)
            digital_tree = destroy_tree(H, W, digital_tree)

    str_tree = show_tree(H, W, digital_tree)
    return str_tree
