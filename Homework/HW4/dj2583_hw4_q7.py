def split_by_sign(lst, low, high):
    if low >= high:
        return
    if lst[low] < 0:
        split_by_sign(lst, low + 1, high)
    else:
        lst[low], lst[high] = lst[high], lst[low]
        split_by_sign(lst, low, high - 1)

