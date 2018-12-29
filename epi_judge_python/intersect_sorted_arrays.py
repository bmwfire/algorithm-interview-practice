import bisect

from test_framework import generic_test


def intersect_two_sorted_arrays(A, B):
    i, j, intersection_A_B = 0, 0, []
    while i < len(A) and j < len(B):
        if A[i] == B[j]:
            if i == 0 or A[i] != A[i - 1]:
                intersection_A_B.append(A[i])
            i, j = i + 1, j + 1
        elif A[i] < B[j]:
            i += 1
        else:
            j += 1
    return intersection_A_B

    # non-optimal solution using binary search
    # solution yields time complexity of O(m log n) vs above O(m + n)
    # def is_present(k):
    #     i = bisect.bisect_left(B, k)
    #     return i < len(B) and B[i] == k
    #
    # return [a for i, a in enumerate(A)
    #         if (i == 0 or a != A[i - 1]) and is_present(a)]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("intersect_sorted_arrays.py",
                                       'intersect_sorted_arrays.tsv',
                                       intersect_two_sorted_arrays))
