"""
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
Return the running sum of nums.

Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4]
"""


class Solution:
    def runningSum(self, nums):
        result = []
        for i, _ in enumerate(nums):
            run_nums = nums[0:i + 1]
            result.append(sum(run_nums))

        return result


if __name__ == '__main__':
    assert Solution().runningSum([1, 2, 3, 4]) == [1, 3, 6, 10]
    assert Solution().runningSum([1, 1, 1, 1, 1]) == [1, 2, 3, 4, 5]
