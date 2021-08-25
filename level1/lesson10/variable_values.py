# инициализация используемых переменных непосредственно перед циклом
km = 0
total_time = 0

for i in range(0, max_even_index, 2):
    speed = oksana[i]
    time = oksana[i + 1]

    if time > total_time and speed >= 0:
        path_time = time - total_time
        total_time = time
        km += speed * path_time


# инициализация используемых переменных непосредственно перед циклом
toner_sum = 0
for i in range(len(line)):
    toner_sum += char_weight(line[i])


# завершение работы с переменной
    templates_list = []
    template_item_chars = []
    for i in range(1, len(line) - 1):
        if line[i] == separator_char:
            templates_list.append(''.join(template_item_chars))
            template_item_chars = []
        else:
            template_item_chars.append(line[i])

    templates_list.append(''.join(template_item_chars))
    template_item_chars = [] # сброс текущего значения


# инициализация переменных при объявлении
decimal_value = 0
multiplier = 0


# объявление переменной непосредственно перед обращением к ней
diff_positions_count = len(diff_positions)

if diff_positions_count == 0:
    return False
elif diff_positions_count == 2:
    return True
else:
    pass


# завершение работы с переменной
s_a = transform(a)
s_s_a = transform(s_a)

key_value = 0
for i in range(len(s_s_a)):
    key_value += s_s_a[i]

s_a = []
s_s_a = []


# завершение работы с переменной
chars_grouped = group_by_unique_element(input_str)
chars_count = []
for i in range(len(chars_grouped)):
    chars_count.append(chars_grouped[i][1])
chars_grouped = []


# использование счетчика цикла только внутри цикла
last_shifted_index = 0
for shift_i in range(shift_count):
    shift_index.append(target_index - shift_count + shift_i + 1)
    last_shifted_index = shift_i


# инварианты в коде
def avg(ranks):
    assert len(ranks) != 0
    return round(sum(ranks)/len(ranks), 2)


# инварианты в коде
def divide(x, y):
    assert y != 0 , 'Нельзя делить на 0'
    return round(x/y, 2)


# явное объявление переменных
# использую языки с динамической типизацией (PHP, Python, Javascript)


# объявление переменной как константы
JANUARY_DAYS = 31 # работает на уровне соглашения


# инициализация всех без исключения полей класса в его конструкторе
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.color = 'green'
        self.border_weight = 3


# работа со счетчиком в цикле while
def first_digit(n):
    while n >= 10:
        n = n // 10
    return n


# инварианты в коде
def WordSearch(len_alignment, s, subs):
    assert len_alignment > 0
    pass
