"""
Given an integer number n, return the difference between the product of its digits and the sum of its digits.

Example 1:

Input: n = 234
Output: 15
Explanation:
Product of digits = 2 * 3 * 4 = 24
Sum of digits = 2 + 3 + 4 = 9
Result = 24 - 9 = 15
"""
import functools
import operator


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        numbers = list(map(int, str(n)))
        product = functools.reduce(operator.mul, numbers)

        return product - sum(numbers)


if __name__ == '__main__':
    assert Solution().subtractProductAndSum(234) == 15
    assert Solution().subtractProductAndSum(4421) == 21
