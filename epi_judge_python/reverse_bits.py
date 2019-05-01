from test_framework import generic_test


def reverse_bits(x):

    result = 0
    for _ in range(4):
        result <<= 1
        result |= x & 1
        x >>= 1
    return result


print(reverse_bits(11))
