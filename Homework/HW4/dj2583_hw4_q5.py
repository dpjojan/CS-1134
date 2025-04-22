#a
def count_lowercase(s,low,high):

    if low == high:
        if s[low].islower():
            return 1
        return 0
    else:
        count = count_lowercase(s,low+1,high)
        if s[low].islower():
            return count + 1
        return count
#b
def is_number_of_lowercase_even(s,low,high):
    if low == high:
        return not s[low].islower()
    else:
        count = is_number_of_lowercase_even(s,low+1,high)
        if s[low].islower():
            return not count
        return count

