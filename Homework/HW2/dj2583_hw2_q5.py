def split_parity(lst):
    even =0
    odd = len(lst) -1
    while even < odd:
        if lst[even] % 2 == 0 and lst[odd] % 2 != 0:
            lst[even], lst[odd] = lst[odd], lst[even]
            even += 1
            odd -= 1
        elif lst[even] % 2 == 0:
            odd -= 1

        elif lst[odd] % 2 != 0:
            even += 1
        else:
            odd -= 1
            even += 1
    return lst

