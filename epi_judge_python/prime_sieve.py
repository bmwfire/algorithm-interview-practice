from test_framework import generic_test


# Given n, return all primes up to and including n.
def generate_primes(n):
    primes = []
    is_prime = [False, False] + [True] * (n - 1)
    for p in range(2, n + 1):
        if is_prime[p]:
            primes.append(p)
            for i in range(p, n + 1, p):
                is_prime[i] = False
    return primes

    # Approach 2
    # if n < 2:
    #     return []
    # size = (n - 3) // 2 + 1
    # primes = [2]
    # is_prime = [True] * size
    # for i in range(size):
    #     if is_prime[i]:
    #         p = i * 2 + 3
    #         primes.append(p)
    #         for j in range(2 * i**2 + 6 * i + 3, size, p):
    #             is_prime[j] = False
    # return primes


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("prime_sieve.py", "prime_sieve.tsv",
                                       generate_primes))
