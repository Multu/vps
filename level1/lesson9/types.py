# получение целочисленного результата от деления
def first_digit(n):
    while n >= 10:
        n = n // 10
    return n


# объявление переменной `line_length` типом float (ранее была типом int),
# чтобы избежать неявного преобразования типа при последующих арифметических операциях
line_length = 0.
for i in range(N - 1):
    point1 = get_point_coords(i)
    point2 = get_point_coords(i + 1)

    point_distance = ((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2) ** 0.5
    line_length += point_distance


# явное преобразование логического значения в строковый символ `1` или `0`
keys = [False, True, False]
keys_symbols = []
for i in range(len(keys)):
    keys_symbols.append(str(int(keys[i])))


# использование констант вместо магических строк
COMMAND_ADD = '1'
COMMAND_DELETE = '2'
COMMAND_GET = '3'
COMMAND_UNDO = '4'
COMMAND_REDO = '5'


# использование логических переменных в сложных условиях
ready_for_destroy = new_tree[i_up][j] < 3
branch_exists = 0 <= i_up <= H - 1
if branch_exists and ready_for_destroy:
    new_tree[i_up][j] = 0


# проверка при делении на знаменатель со значением 0
if total_votes > 0:
    vote_percent = round(votes_sum / total_votes * 100, 3)


# указание явно кодировки чтения файла
with open(filename, "rt", encoding="utf-8") as f:
    content = f.read()


# проверка на тип данных и при необходимости явное преобразование типа
if type(receipt_amount) is not Decimal:
    receipt_amount = Decimal(receipt_amount)


# округление счета на оплату в большую сторону вместо ближайшено четного по умолчанию
from decimal import Decimal, ROUND_HALF_UP

def round_up(value, precision = 0):
    rounded_value = Decimal(str(value))\
        .quantize(Decimal('1.' + precision * '0'), ROUND_HALF_UP)

    if type(value) is float:
        return float(rounded_value)
    if type(value) is int:
        return int(rounded_value)
    if type(value) is str:
        return str(rounded_value)

    return rounded_value


# пример на сравнение на равенство вещественных чисел
0.1 * 3 == 0.15 + 0.15 # вернет False


# пример сложения и вычитания слишком разных по величине чисел
5000000.1 + 0.0000000001 # результат 5000000.1, не тот, который мы ожидаем


