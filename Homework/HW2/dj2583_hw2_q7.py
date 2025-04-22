def findChange(lst01):
    first = 0
    last = len(lst01)-1
    while first <= last:
        mid = (first+last)//2
        if lst01[mid] == 1:
            last = mid-1
        else:
            first = mid+ 1
    return first



