def list_min(lst,low,high):
    if low == high:
        return lst[low]
    else:
        min_val = list_min(lst,low+1 ,high)
        return min(lst[low], min_val)