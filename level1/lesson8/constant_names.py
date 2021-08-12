# вынесено в константу значение десятичной системы счисления
NUMBER_BASE = 10

def first_digit(n):
    while n >= NUMBER_BASE:
        n = n // NUMBER_BASE
    return n


# вынесена в константу точность округления дробного числа
DECIMAL_PRECISION = 5

line_length = round(math.sqrt(2), DECIMAL_PRECISION)


# вынесен в константу уровень расхода тонера на нестандартные символы
DEFAULT_TONER_CONSUMPTION = 23

def char_weight(char):
    for i in range(len(ancii_toner)):
        if ancii_toner[i][0] == char:
            return ancii_toner[i][1]

    return DEFAULT_TONER_CONSUMPTION


# вынесен в константу процент голосов, которые приводят к абсолютной победе
VOTE_MAJOR_THRESHOLD = 50

if winner_percent > VOTE_MAJOR_THRESHOLD:
    vote_result = f'majority winner {winner_index + 1}'


# вынесены в константы значения параметров для резайса изображения
IMAGE_RESIZED_WIDTH = 320
IMAGE_RESIZED_HEIGHT = 200

image_resized = asset_image(path, width=IMAGE_RESIZED_WIDTH, height=IMAGE_RESIZED_HEIGHT)


# замена константой максимально возможного размера превью описания статьи
DESCRIPTION_PREVIEW_MAX_LENGTH = 120

description_preview = get_preview(description, max_length=DESCRIPTION_PREVIEW_MAX_LENGTH)


# в константы вынесены идентификаторы страны и языка
COUNTRY_RUSSIA = 1
LANGUAGE_RUSSIA = 1

topics = anketa.get_topics(country=COUNTRY_RUSSIA, lang=LANGUAGE_RUSSIA)


# вынесен в константу путь к конфигурационному файлу
CONFIG_PATH = APPLICATION_PATH + 'config/application.ini'


# вынесено в константу значение таймаута на API запрос
API_REQUEST_TIMEOUT = 30


# замена имени константы
TEN_MINUTE = 10 * 60 # было
PARSING_DELAY = 10 * 60 # стало


# константа для идентификатора комиссии
TAX_FEE_TYPE = 5


# константа для идентификатора тарифного плана
PACKAGE_FAMILY_PREMIUM = 76