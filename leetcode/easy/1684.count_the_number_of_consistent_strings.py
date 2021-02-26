"""
You are given a string allowed consisting of distinct characters and an array of strings words. A string is consistent if all characters in the string appear in the string allowed.
Return the number of consistent strings in the array words.

Input: allowed = "ab", words = ["ad","bd","aaab","baa","badab"]
Output: 2
Explanation: Strings "aaab" and "baa" are consistent since they only contain characters 'a' and 'b'.
"""


class Solution:
    def countConsistentStrings(self, allowed: str, words):
        return sum(all(w in allowed for w in word) for word in words)


if __name__ == '__main__':
    Solution().countConsistentStrings(allowed="ab", words=["ad", "bd", "aaab", "baa", "badab"]) == 2
    Solution().countConsistentStrings(allowed="abc", words=["a", "b", "c", "ab", "ac", "bc", "abc"]) == 7
    Solution().countConsistentStrings(allowed="cad", words=["cc", "acd", "b", "ba", "bac", "bad", "ac", "d"]) == 4
