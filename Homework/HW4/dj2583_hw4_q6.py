def appearances(s,low,high):
    new_dict = {}
    if low == high:
        new_dict[s[low]] = 1
        return new_dict
    else:
        char_count = appearances(s,low+1,high)
        if s[low] in char_count:
            char_count[s[low]] +=1
        else:
            char_count[s[low]] = 1
        return char_count
