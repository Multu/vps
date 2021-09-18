# До рефакторинга. Перебор элементов списка по индексу.
digits_list = [1, 0, 5, 6, 7]
for i in range(len(digits_list)):
    if digits_list[i] != 0:
        pass

# После рефакторинга. Перебор элементов последовательно с помощью конструкции for.
digits_list = [1, 0, 5, 6, 7]
for digit in digits_list:
    if digit != 0:
        pass


# До рефакторинга. Таблица кодов представлена в виде списка.
keyboard = [[6, 1, 9],
            [5, 2, 8],
            [4, 3, 7]]

# После рефакторинга. Таблица кодов представлена в виде кортежа и стала иммутабельной.
keyboard = ((6, 1, 9),
            (5, 2, 8),
            (4, 3, 7))


# До рефакторинга. Расход тонера указан в виде многомерного списка.
ancii_toner = [
    ['g', 30], ['m', 22], ['s', 21], ['y', 24],
]

def char_weight(char):
    for i in range(len(ancii_toner)):
        if ancii_toner[i][0] == char:
            return ancii_toner[i][1]

    # Default value.
    return 23

# После рефакторинга. Расход тонера указан в виде словаря.
ancii_toner = {
    'g': 30, 'm': 22, 's': 21, 'y': 24
}

def char_weight(char):
    return dict(ancii_toner, 23)


# До рефакторинга. Список гостей хранится в виде списка.
def is_invited(guests, guest):
    for i in range(len(guests)):
        if guests[i] == guest:
            return True

    return False

# После рефакторинга. Список гостей хранится в виде множества.
def is_invited(guests, guest):
    guests_set = set(guests)
    return guest in guests_set


# До рефакторинга. Обход многомерного списка.
lines = get_lines()
for i in range(len(lines)):
    line_words = lines[i]
    for j in range(len(line_words)):
        pass

# До рефакторинга. Обход многомерного списка c помощью конструкции for.
lines = get_lines()
for line_words in lines:
    for word in line_words:
        pass
