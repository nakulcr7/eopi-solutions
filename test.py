def parity(num):
    result = 0
    while num is not 0:
        result ^= (num & 1)
        num >>= 1
    print result


print parity(3)
