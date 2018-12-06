import heapq

from test_framework import generic_test, test_utils


def k_largest_in_binary_heap(A, k):
    if k <= 0:
        return []

    candidates_max_heap = []
    candidates_max_heap.append((-A[0], 0))
    result = []

    for _ in range(k):
        candidate_idx = candidates_max_heap[0][1]
        result.append(-heapq.heappop(candidates_max_heap)[0])

        left_child_idx = 2 * candidate_idx + 1
        if left_child_idx < len(A):
            heapq.heappush(candidates_max_heap, (-A[left_child_idx], left_child_idx))

        right_child_idx = 2 * candidate_idx + 2
        if right_child_idx < len(A):
            heapq.heappush(candidates_max_heap, (-A[right_child_idx], right_child_idx))

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "k_largest_in_heap.py",
            "k_largest_in_heap.tsv",
            k_largest_in_binary_heap,
            comparator=test_utils.unordered_compare))
