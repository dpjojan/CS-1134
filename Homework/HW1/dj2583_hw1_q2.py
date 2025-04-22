def shift(lst,k,direction = None):
    for i in range(k):
        if direction is None or direction == 'left':
            end_val = lst.pop(0)
            lst.append(end_val)
        else:
            end_val = lst.pop()
            lst.insert(0,end_val)

    return lst


