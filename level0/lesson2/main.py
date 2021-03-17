def odometer(oksana):
    km = 0
    total_time = 0

    # If length of `oksana` list is odd, then ignore last element.
    max_even_index = len(oksana)
    if max_even_index % 2 == 1:
        max_even_index -= 1

    for i in range(0, max_even_index, 2):
        speed = oksana[i]
        time = oksana[i + 1]

        if time > total_time and speed >= 0:
            path_time = time - total_time
            total_time = time
            km += speed * path_time

    return km
