from test_framework import generic_test


def parity(x):

    # Brute Force: time complexity O(n)
    # result = 0
    # while x:
    #     result ^= x & 1
    #     x >>= 1
    # return result

    # Improvement 1: time complexity O(k)
    result = 0
    while x:
        result ^= 1
        x &= x - 1
    return result

    # Improvement 2: time complexity O(n/L)
    # MASK_SIZE = 16
    # BIT_MASK = 0xFFFF
    # return (PRECOMPUTED_PARITY[x >> (3 * MASK_SIZE)] ^
    #         PRECOMPUTED_PARITY[(x >> (2 * MASK_SIZE)) & BIT_MASK] ^
    #         PRECOMPUTED_PARITY[(x >> MASK_SIZE)
    #                            & BIT_MASK] ^ PRECOMPUTED_PARITY[x & BIT_MASK])

    # Improvement 3: time complexity O(log n)
    # x ^= x >> 32
    # x ^= x >> 16
    # x ^= x >> 8
    # x ^= x >> 4
    # x ^= x >> 2
    # x ^= x >> 1
    # return x & 0x1


if __name__ == '__main__':
    exit(generic_test.generic_test_main("parity.py", 'parity.tsv', parity))
