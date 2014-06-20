
def rec_three(n):
    product = 3 * n
    print "The multiple of {} is {}".format(n, product)
    if n < 100:
        rec_three(n + 1)


def multiples(n):
    if n == 0:
        return 0
    else:
        print n
        return n + multiples(n - 1)
