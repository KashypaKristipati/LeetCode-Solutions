def reverseInteger(x):
    sign = -1 if x < 0 else 1
    x *= sign

    res = 0
    while x > 0:
        res = res * 10 + x % 10
        x //= 10

    return sign * res