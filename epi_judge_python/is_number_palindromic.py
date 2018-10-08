from test_framework import generic_test
import math


def is_palindrome_number(x):
    if x <= 0:
        return x == 0

    num_digits = math.floor(math.log10(x)) + 1
    msd_mask = 10**(num_digits - 1)
    for i in range(num_digits // 2):
        if x // msd_mask != x % 10:
            return False
        else:
            x %= msd_mask
            x //= 10
            msd_mask //= 100
    return True

    # Alternative implementation using reverse() function from 4.8
    # def reverse(x):
    #     result, x_remaining = 0, abs(x)
    #     while x_remaining:
    #         result = result * 10 + x_remaining % 10
    #         x_remaining //= 10
    #     return -result if x < 0 else result
    #
    # if x != reverse(x):
    #     return False
    # else:
    #     return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_number_palindromic.py",
                                       "is_number_palindromic.tsv",
                                       is_palindrome_number))
