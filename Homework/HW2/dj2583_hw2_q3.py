import math
def factors(n):
    second_half = []
    for i in range(1, int(math.sqrt(n)) +1):
        val  = n / i
        if n % i == 0:

            if val != i:
                second_half.append(val)
            yield i

    for num in reversed(second_half):
        yield int(num)
