"""
    Связывание во время написания кода.
"""

# Инициализация значений констант
COUNTRY_RUSSIA = 1
LANGUAGE_RUSSIA = 1

# Настройка файла конфигурации
config = {
    'passwords': {
        'users': {
            'provider': 'users',
            'table': 'password_resets',
            'expire': 60,
        }
    }
}


"""
    Связывание во время компиляции кода.
"""

# Инициализация переменной значением константы.
# Удобно использовать, если значение переменной
# может время от времени изменяться.
def open_serial(self):
    try:
        return serial.Serial(
            port=PORT,
            baudrate=BAUDRATE,
            bytesize=SERIAL_SEVENBITS,
            parity=SERIAL_PARITY_EVEN,
            stopbits=SERIAL_STOPBITS_ONE,
        )
    except Exception as e:
        pass


"""
    Связывание во время выполнения кода.
"""

# Установка значения по умолчанию для параметра функции
def str_to_lines(line, space_separator=False):
    lines = []
    # some code
    return lines

# Установка значения через методы.
# Удобно использовать в случаях, когда нужное значение
# становися известным только во время выполнения кода в результате
# проверки каких-либо условий или дополнительных расчетов.
signature = calculate_checksum(personal_data)


