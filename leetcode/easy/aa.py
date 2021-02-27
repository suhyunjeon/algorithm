"""
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.
Return the merged string.
"""
from itertools import zip_longest


class Solution:
    def mergeAlternately(self, word1, word2):
        result = [w1 + w2 for w1, w2 in zip_longest(word1, word2, fillvalue="")]

        return "".join(result)


if __name__ == '__main__':
    assert Solution().mergeAlternately(word1="abc", word2="pqr") == "apbqcr"
    assert Solution().mergeAlternately(word1="ab", word2="pqrs") == "apbqrs"
    assert Solution().mergeAlternately(word1="abcd", word2="pq") == "apbqcd"
