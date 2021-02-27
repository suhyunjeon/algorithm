"""
Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.

Example 1:

Input: "Hello"
Output: "hello"
"""


class Solution:
    def toLowerCase(self, str):
        result = ""
        for s in str:
            result += chr(ord(s) + 32) if 65 <= ord(s) <= 90 else s

        return result


if __name__ == '__main__':
    assert Solution().toLowerCase("Hello") == "hello"
    assert Solution().toLowerCase("here") == "here"
    assert Solution().toLowerCase("LOVELY") == "lovely"


