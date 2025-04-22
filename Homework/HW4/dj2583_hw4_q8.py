def flat_list(nested_lst, low, high):
    if low > high:
        return []
    if low == high:
        if isinstance(nested_lst[low], list):
            return flat_list(nested_lst[low], 0, len(nested_lst[low]) - 1)
        else:
            return [nested_lst[low]]
    else:
        result = flat_list(nested_lst, low + 1, high)
        if isinstance(nested_lst[low], list):
            return flat_list(nested_lst[low], 0, len(nested_lst[low]) - 1) + result
        else:
            return [nested_lst[low]] + result



