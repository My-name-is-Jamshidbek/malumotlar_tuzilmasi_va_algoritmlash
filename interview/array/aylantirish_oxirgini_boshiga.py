# Rotate Array
"""
Given an array, rotate the array to the right by k steps, where k is non-negative.
"""
class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for _ in range(k):nums.insert(0,nums.pop())
a = Solution()
# nums,k = [-1,-100,3,99],2
nums,k = [1,2,3,4,5,6,7],3
a.rotate(nums = nums, k = k)
print(nums)

# for i in range(k):
#     nums.insert(0, nums.pop())