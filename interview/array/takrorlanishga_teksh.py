# Contains Duplicate
"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
"""
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        if len(nums)==len(set(nums)):return False
        else:return True
a = Solution()
print(a.containsDuplicate(nums = [1,1,1,3,3,4,3,2,4,2]))