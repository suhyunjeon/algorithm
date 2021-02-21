"""
Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].
Return the answer in an array.

Input: nums = [8,1,2,2,3]
Output: [4,0,1,1,3]
Explanation:
For nums[0]=8 there exist four smaller numbers than it (1, 2, 2 and 3).
For nums[1]=1 does not exist any smaller number than it.
For nums[2]=2 there exist one smaller number than it (1).
For nums[3]=2 there exist one smaller number than it (1).
For nums[4]=3 there exist three smaller numbers than it (1, 2 and 2).

"""

class Solution:
    def smallerNumbersThanCurrent(self, nums):
        result = []
        for num1 in nums:
            result.append(len([num2 for num2 in nums if num1 > num2]))

        return result


if __name__ == '__main__':
    assert Solution().smallerNumbersThanCurrent([8, 1, 2, 2, 3]) == [4, 0, 1, 1, 3]
    assert Solution().smallerNumbersThanCurrent([6, 5, 4, 8]) == [2, 1, 0, 3]
    assert Solution().smallerNumbersThanCurrent([7, 7, 7, 7]) == [0, 0, 0, 0]
