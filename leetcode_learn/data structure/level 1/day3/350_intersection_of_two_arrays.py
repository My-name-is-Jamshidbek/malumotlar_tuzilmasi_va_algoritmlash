class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        rn = []

        for i in nums1:
            if i in nums2:rn.append(nums2.pop(nums2.index(i)))
        return rn
a = Solution()
print(a.intersect([4,9,5], nums2 = [9,4,9,8,4]))