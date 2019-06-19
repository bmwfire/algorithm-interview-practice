import functools

from test_framework import generic_test


def ss_decode_col_id(col):
    return functools.reduce(lambda result, c: result * 26 + ord(c) - ord('A') + 1, col, 0)


    # # Non-functional programming solution
    # result = 0
    #
    # for c in col:
    #     result = result * 26 + ord(c) - ord('A') + 1
    #
    # return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("spreadsheet_encoding.py",
                                       'spreadsheet_encoding.tsv',
                                       ss_decode_col_id))
