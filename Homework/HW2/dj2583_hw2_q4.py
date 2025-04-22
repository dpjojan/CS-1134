import math
def e_approx(n):
    total = 1
    numerator = 1
    for i in range(1,n+1):
        numerator /= i
        total += numerator
    return total


def main():
    for n in range(15):
        curr_approx = e_approx(n)
        approx_str = "{:.15f}".format(curr_approx)
        print("n =", n, "Approximation:", approx_str)
if __name__ == '__main__':
    main()