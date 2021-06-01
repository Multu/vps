def Keymaker(k):
    keys = []

    for i in range(k):
        keys.append(False)

    for i in range(k):
        for j in range(i, k, i + 1):
            keys[j] = not keys[j]
        keys[i] = str(int(keys[i]))

    return ''.join(keys)
