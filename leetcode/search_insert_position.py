class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        t=0
        ind=0
        for i in nums:
            if i<=target:ind=t+1
            if i==target:return t
            t += 1
        return ind
a = Solution()
print(a.searchInsert([1,3,5,6],0))