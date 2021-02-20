"""
Given a valid (IPv4) IP address, return a defanged version of that IP address.
A defanged IP address replaces every period "." with "[.]".

Example 1:
Input: address = "1.1.1.1"
Output: "1[.]1[.]1[.]1"
Example 2:

Input: address = "255.100.50.0"
Output: "255[.]100[.]50[.]0"
"""


class Solution:
    def defangIPaddr(self, address):
        return address.replace(".", "[.]")


if __name__ == '__main__':
    assert Solution().defangIPaddr("1.1.1.1") == "1[.]1[.]1[.]1"
    assert Solution().defangIPaddr("255.100.50.0") == "255[.]100[.]50[.]0"
