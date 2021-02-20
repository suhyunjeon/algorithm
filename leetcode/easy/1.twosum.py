"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
"""


class Solution:
    def twoSum(self, nums, target):
        nums_length = len(nums)
        for i in range(nums_length):
            remain = target - nums.pop(0)
            if remain in nums:
                return [i, nums.index(remain) + i + 1]


if __name__ == '__main__':
    assert Solution().twoSum(nums=[2, 7, 11, 15], target=9) == [0, 1]
    assert Solution().twoSum(nums=[11, 15, 2, 7], target=9) == [2, 3]
