def split_sale(sale):
    title_chars = []
    count_chars = []

    delimiter_appeared = False
    for i in range(len(sale)):
        if sale[i] == ' ':
            delimiter_appeared = True
            continue

        if delimiter_appeared:
            count_chars.append(sale[i])
        else:
            title_chars.append(sale[i])

    title = ''.join(title_chars)
    count = int(''.join(count_chars))

    return [title, count]

def ShopOLAP(n, items):
    # Grouping of goods by name.
    # Result present as two-dimensional list [[good-name, total-sales]].
    items_grouped = []
    for i in range(n):
        item_parts = split_sale(items[i])
        for j in range(len(items_grouped)):
            if items_grouped[j][0] == item_parts[0]:
                items_grouped[j][1] += item_parts[1]
                break
        else:
            items_grouped.append(item_parts)

    # Sort goods.
    for i in range(len(items_grouped) - 1):
        title1 = items_grouped[i][0]
        count1 = items_grouped[i][1]

        for j in range(i + 1, len(items_grouped)):
            title2 = items_grouped[j][0]
            count2 = items_grouped[j][1]

            if count2 > count1:
                items_grouped[i], items_grouped[j] = items_grouped[j], items_grouped[i]
            elif count2 == count1:
                if title2 < title1:
                    items_grouped[i], items_grouped[j] = items_grouped[j], items_grouped[i]

    # Prepare resulting list
    result = []
    for i in range(len(items_grouped)):
        title = items_grouped[i][0]
        count = items_grouped[i][1]
        result.append(title + ' ' + str(count))

    return result








