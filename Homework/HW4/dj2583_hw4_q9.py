def permutations(lst, low, high):
    result = []
    if low == high:
        return [[lst[low]]]
    for i in range(low, high + 1):
        lst[low], lst[i] = lst[i], lst[low]
        rem_elements = permutations(lst, low + 1, high)
        for perm in rem_elements:
            result.append([lst[low]] + perm)

        lst[low], lst[i] = lst[i], lst[low]

    return result
