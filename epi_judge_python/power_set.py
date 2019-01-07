import math

from test_framework import generic_test, test_utils


# Non-recursive implementation using bit arrays
def generate_power_set(S):
    power_set = []
    for int_for_subset in range(1 << len(S)):
        bit_array = int_for_subset
        subset = []
        while bit_array:
            subset.append(int(math.log2(bit_array & ~(bit_array - 1))))
            bit_array &= bit_array - 1
        power_set.append(subset)
    return power_set


# Recursive implementation
# def generate_power_set(input_set):
#     def directed_power_set(to_be_selected, selected_so_far):
#         if to_be_selected == len(input_set):
#             power_set.append(list(selected_so_far))
#             return
#
#         directed_power_set(to_be_selected + 1, selected_so_far)
#         directed_power_set(to_be_selected + 1,
#                            selected_so_far + [input_set[to_be_selected]])
#
#     power_set = []
#     directed_power_set(0, [])
#     return power_set


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("power_set.py", 'power_set.tsv',
                                       generate_power_set,
                                       test_utils.unordered_compare))
