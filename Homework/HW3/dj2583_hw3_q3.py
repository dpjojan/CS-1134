#A
def find_duplicates(lst):
    initial = 0
    second = 1
    new_lst = []

    while second < len(lst):
        if lst[initial] == lst[second]:  #O(1)
            new_lst.append(lst[initial]) #O(1)
            initial += 1
            second = initial + 1
        elif second == len(lst) - 1:
            initial += 1
            second = initial + 1
        else:
            second += 1
    return new_lst

#B
#O(n^2)
