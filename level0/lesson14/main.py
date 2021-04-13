def Unmanned(L, N, track):
    total_time = L

    red_additional_time = 0

    for i in range(N):
        time_road = track[i][0]
        time_red = track[i][1]
        time_green = track[i][2]

        # Total waiting time on red before the current traffic light.
        actual_time_road = time_road + red_additional_time

        # Total burning time of red and green colors.
        time_lights_total = time_red + time_green

        if time_lights_total and L > time_road:
            actual_lights_moment = actual_time_road % time_lights_total
            if actual_lights_moment < time_red:
                wait_time = time_red - actual_lights_moment
                red_additional_time += wait_time

    total_time += red_additional_time

    return total_time
