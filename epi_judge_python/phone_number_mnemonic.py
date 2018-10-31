import itertools

from test_framework import generic_test, test_utils

MAPPING = ('0', '1', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ')


def phone_mnemonic(phone_number):
    def phone_mnemonic_helper(digit):
        if digit == len(phone_number):
            mnemonics.append(''.join(partial_mnemonic))
        else:
            for c in MAPPING[int(phone_number[digit])]:
                partial_mnemonic[digit] = c
                phone_mnemonic_helper(digit + 1)

    mnemonics, partial_mnemonic = [], [0] * len(phone_number)
    phone_mnemonic_helper(0)
    return mnemonics


# Pythonic Solution 1
def phone_mnemonic_pythonic(phone_number):
    return [
        ''.join(mnemonic) for mnemonic in
        itertools.product(*(MAPPING[int(digit)] for digit in phone_number))
    ]


# Pythonic Solution 2
def phone_mnemonic_pythonic_another(phone_number):
    TABLE = {
        '0': '0',
        '1': '1',
        '2': 'ABC',
        '3': 'DEF',
        '4': 'GHI',
        '5': 'JKL',
        '6': 'MNO',
        '7': 'PQRS',
        '8': 'TUV',
        '9': 'WXYZ'
    }
    return [
        a + b for a in TABLE.get(phone_number[:1], '')
        for b in phone_mnemonic_pythonic_another(phone_number[1:]) or ['']
    ]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "phone_number_mnemonic.py",
            'phone_number_mnemonic.tsv',
            phone_mnemonic,
            comparator=test_utils.unordered_compare))
