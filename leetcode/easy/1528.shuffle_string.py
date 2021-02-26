"""
Given a string s and an integer array indices of the same length.
The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.
Return the shuffled string.

Input: s = "codeleet", indices = [4,5,6,7,0,2,1,3]
Output: "leetcode"
Explanation: As shown, "codeleet" becomes "leetcode" after shuffling.
"""


class Solution:
    def restoreString(self, s, indices):
        characters = {}
        for i, character in enumerate(s):
            characters[indices[i]] = character

        return "".join(dict(sorted(characters.items(), key=lambda x: x[0])).values())


if __name__ == '__main__':
    assert Solution().restoreString(s="codeleet", indices=[4, 5, 6, 7, 0, 2, 1, 3]) == "leetcode"
    assert Solution().restoreString(s="abc", indices=[0, 1, 2]) == "abc"
    assert Solution().restoreString(s="aiohn", indices=[3, 1, 4, 2, 0]) == "nihao"
    assert Solution().restoreString(s="aaiougrt", indices=[4, 0, 2, 6, 7, 3, 1, 5]) == "arigatou"
    assert Solution().restoreString(s="art", indices=[1, 0, 2]) == "rat"
