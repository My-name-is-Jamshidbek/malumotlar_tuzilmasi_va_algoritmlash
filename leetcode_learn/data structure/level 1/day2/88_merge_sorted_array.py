class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[:] = sorted(nums1[:m]+nums2)
a = Solution()
nums1 = [1,2,3,0,0,0]
print(a.merge(nums1=nums1, m = 3, nums2 = [2,5,6], n = 3))
print(nums1)