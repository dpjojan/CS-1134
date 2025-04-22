def squares(n):
    total = 0
    for i in range(1,n):
        total += i**2
    return total

sum([i **2 for i in range(1,n)])

def odd_squares(n):
    total = 0
    for i in range(1,n,2):
        total += i**2
    return total

sum([i **2 for i in range(1,n,2)])