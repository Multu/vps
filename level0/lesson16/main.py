def MaximumDiscount(n, price):
    # Sort price by desc.
    for i in range(n - 1):
        max_price = price[i]
        for j in range(i + 1, n):
            if price[j] > max_price:
                max_price = price[j]
                price[i], price[j] = price[j], price[i]

    # Every third item on a discount.
    max_discount = 0
    for i in range(2, n, 3):
        if price[i] > 0:
            max_discount += price[i]

    return max_discount

