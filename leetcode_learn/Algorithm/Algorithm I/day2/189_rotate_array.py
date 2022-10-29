class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums)<k: k=k%len(nums)
        if k==0:pass
        else:nums[:] = nums[-k:]+nums[:len(nums)-k]
a = Solution()
nums=[1,2,3,4,5,6,7,8,9,10]
print(a.rotate(nums = nums, k = 3))
print(nums)