def remove_all(lst, value):
    first= 0
    second= 0
    while second <= len(lst)-1:
        if lst[second] != value:
            lst[first], lst[second] = lst[second], lst[first]
            first+=1

        second += 1
    while len(lst) > first:
        lst.pop()

    return lst




