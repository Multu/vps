"""
    Ниже собраны примеры плохих комментариев.
    В реальном коде их можно либо просто удалить либо заменить "говорящим" кодом.
"""


# Неочевидный комментарий. Не понятно с каким блоком кода он связан.

# Remove first zero digits.

# Some another code here.
pass

# Commented above block.
while sub_lists[0] == 0:
    sub_lists.pop(0)
    if len(sub_lists) == 0:
        break


# Бормотание. Комментарий не выразительный, написан на скорую руку.

# Dog actions
class Dog:
    def say(self):
        pass

    def walk(self):
        pass


# Недостоверынй комментарий.

# Find odd digits.
even_digits = []
for i in range(len(digits)):
    if digits[i] % 2 == 0:
        even_digits.add(digits[i])


# Шум. Утверждает очевидное.

# Calculate total price amount.
total_price = price + fees


# Позиционные маркеры.

# ///////////////////////
# Pretty format of receipt.
total_price = f"Total price: {total_price:.2f}"
# ///////////////////////


# Комментарии за закрывающей фигурной скобкой.

for i in range(100):
    pass
    for j in range(100):
        pass
        for k in range(100):
            pass
    # End internal cycle.


# Избыточные комментарии.

# Calculate the length of a circular arc.
# Formula: 2 * pi * r, where pi is constant and equal 3.14.
l = 2 * pi * r


# Слишком много информации.

# Team Lead advised using a Canny detector.
# I will bring this code up for discussion later.
edge = canny(img, 0, 50)


# "Обязательные комментарии". Глупо комментировать каждый метод/переменную

# Dog class
class Dog:
    # Generate dog's bark.
    def say(self):
        pass

    # Dog walking mode.
    def walk(self):
        pass


# Закомментированный код.

# square = 2 * a + 2 * a
square = a * 4


# Не используйте комментарии там, где можно использовать функцию или переменную
def get_prime(n):
    for i in range(2, n):

        # Check if i is prime. If can be replaced in separate function.
        for j in range(2, i):
            if i % j == 0:
                continue

        return i

    return n
