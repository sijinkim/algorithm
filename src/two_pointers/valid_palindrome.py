"""
2024-03-08
125.Valid Palindrome (https://leetcode.com/problems/valid-palindrome/description/)
"""
from functools import reduce


def uppercase_filter(s: str) -> str:
    return s.lower()


def empty_filer(s: str) -> str:
    return s.replace(" ", "")


def non_alphanumeric_filer(s: str) -> str:
    alnum = ""
    for i in s:
        if not i.isalnum():
            continue

        alnum += i
    return alnum


FILTERS = [uppercase_filter, empty_filer, non_alphanumeric_filer]


class ValidPalindromeSolution:
    def is_palindrome(self, s: str) -> bool:
        """
        제약사항
            1 <= s.length <= 2 * 100_000
            s:uppercase letters, lowercase letters,
              alphanumeric characters(letters, numbers), non-alphanumeric characters(empty)
        """
        alnum_s = reduce(lambda s, func: func(s), FILTERS, s)

        start = 0
        end = len(alnum_s) - 1

        while start <= end:
            if not alnum_s[start] == alnum_s[end]:
                return False

            start += 1
            end -= 1

        return True
