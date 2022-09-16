def oxford_comma(items):
    if len(items) > 1:
        items[-1] = "and " + items[-1]

    if len(items) > 2:
        return ', '.join(items)
    else:
        return ' '.join(items)

