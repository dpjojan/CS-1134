def fibs(n):
    value1 = 1
    yield value1

    value2 = 1
    yield value2

    for i in range(n-2):
        new_val = value1 + value2
        yield new_val
        value1 = value2
        value2 = new_val

