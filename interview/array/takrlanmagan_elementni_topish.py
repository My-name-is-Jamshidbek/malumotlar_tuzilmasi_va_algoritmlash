# Single Number
"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.
"""


class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        if len(nums) == 1:return nums[0]
        nums.sort()
        if nums[0]!=nums[1]:return nums[0]
        for i in range(2,len(nums)-1,2):
                if nums[i] != nums[i+1]:return nums[i]
        return nums[-1]
a = Solution()
print(a.singleNumber([-336,513,-560,-481,-174,101,-997,40,-527,-784,-283,-336,513,-560,-481,-174,101,-997,40,-527,-784,-283,354]))