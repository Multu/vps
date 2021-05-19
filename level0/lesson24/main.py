def MatrixTurn(Matrix, M, N, T):
    matrix = []

    for i in range(M):
        row = []
        for j in range(N):
            row.append(Matrix[i][j])
        matrix.append(row)

    min_side = M
    if N < min_side:
        min_side = N
    layers_count = min_side // 2

    for i in range(T):
        for j in range(layers_count):



1 1 1 1
2 2 2 2
3 3 3 3
4 4 4 4
5 5 5 5
6 6 6 6