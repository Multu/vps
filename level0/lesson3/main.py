def generate_conquer_area(N, M):
    conquest_area = []
    for i in range(N):
        row = []
        for j in range(M):
            row.append(0)
        conquest_area.append(row)
    return conquest_area


def is_conquered(area):
    for i in range(len(area)):
        row = area[i]
        for j in range(len(row)):
            if area[i][j] == 0:
                return False
    return True


def new_conquer_day(area):
    n = len(area)
    m = len(area[0])

    conquest_area = generate_conquer_area(n, m)

    for i in range(n):
        for j in range(m):
            if area[i][j] == 1:
                conquest_area[i][j] = 1

                if i - 1 >= 0:
                    conquest_area[i - 1][j] = 1
                if i + 1 < n:
                    conquest_area[i + 1][j] = 1

                if j - 1 >= 0:
                    conquest_area[i][j - 1] = 1
                if j + 1 < m:
                    conquest_area[i][j + 1] = 1

    return conquest_area


def ConquestCampaign(n, m, l, battalion):

    conquest_area = generate_conquer_area(n, m)

    # Set battalion points
    for i in range(l):
        x = battalion[i * 2] - 1
        y = battalion[i * 2 + 1] - 1

        if 0 <= x < n and 0 <= y < m:
            conquest_area[x][y] = 1

    days = 1
    while is_conquered(conquest_area) is False:
        conquest_area = new_conquer_day(conquest_area)
        days += 1

    return days
