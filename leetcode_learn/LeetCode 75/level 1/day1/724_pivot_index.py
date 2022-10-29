class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        t = True
        n1,n2 = 0,sum(nums)
        for i in range(len(nums)):
            if n1 == n2-nums[i]:return i
            n1+=nums[i]
            n2-=nums[i]
        return -1