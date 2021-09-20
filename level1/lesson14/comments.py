'''
    Задание 3.1. Примеры полезных комментариев.
'''

# Пояснение структуры переданного в фукцию параметра.
def odometer(oksana):
    '''
    :param oksana: odd elements of list contains speed, even elements - time.
    '''

    km = 0
    total_time = 0

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


# Случай, когда строка комментария помогает понять
# смысл блока кода и пропустить его чтение.
def BigMinus(s1, s2):

    # Create lists of digits for both digital strings.
    # If the original strings are of different lengths,
    # then align the digits to the right and pad the left with zeros.
    long1 = len(s1)
    long2 = len(s2)

    if long1 > long2:
        max_long = long1
    else:
        max_long = long2

    list1 = []
    list2 = []
    sub_lists = []

    for i in range(max_long):
        list1.append(0)
        list2.append(0)
        sub_lists.append(0)

    for i in range(long1 - 1, -1, -1):
        list1[i + max_long - long1] = int(s1[i])
    for i in range(long2 - 1, -1, -1):
        list2[i + max_long - long2] = int(s2[i])

    # The `list1` should contain digits of a larger number.
    # Otherwise, swap the content of the `list1` and `list2`
    for i in range(max_long):
        if list1[i] == list2[i]:
            continue

        if list1[i] > list2[i]:
            break
        else:
            list1, list2 = list2, list1
            break

    # Calculation of the subtraction between `list1` and `list2`
    for i in range(max_long - 1, -1, -1):
        sub_digits = list1[i] - list2[i]
        if sub_digits < 0:
            sub_digits += 10
            list1[i - 1] -= 1
        sub_lists[i] = sub_digits

    # Remove first zero digits
    while sub_lists[0] == 0:
        sub_lists.pop(0)
        if len(sub_lists) == 0:
            break

    # Convert result to string type
    for i in range(len(sub_lists)):
        sub_lists[i] = str(sub_lists[i])

    sub_str = ''.join(sub_lists)
    if len(sub_str) == 0:
        sub_str = '0'

    return sub_str


'''
    Задание 3.2 Примеры плохих комментариев.
'''

# Бессмысленный комментарий. И так понятно,
# что возвращается значение по умолчанию.
def char_weight(char):
    for i in range(len(ancii_toner)):
        if ancii_toner[i][0] == char:
            return ancii_toner[i][1]

    # Default value.
    return 23


# Пример лишних комментариев, без которых можно обойтись, улучшив код.
def MadMax(n, tele):

    # Sort left side elements by asc.
    for i in range(n // 2):
        pass

    # Sort middle and right side elements by desc.
    for i in range(n // 2, n - 1):
        pass

    return tele

# Улучшенный псевдокод без комментариев.
def MadMax(n, tele):
    middle_index = n // 2
    head_sorted = custom_sort(tele[:middle_index], 'asc')
    tail_sorted = custom_sort(tele[middle_index:], 'desc')
    tele_sorded = head_sorted + tail_sorted
    return tele_sorded


# Пример бесполезных комментариев, которые можно удалить,
# присвоив более осмысленные названия переменным.
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

        pass

    return total_time


# Пример лишнего комментария. Без него и так понятно, что делает код.
def encrypt(s):
    pass

    # Fill chars matrix.
    while len(no_space_list) < rows * cols:
        no_space_list.append('')

    pass

    return encrypted
