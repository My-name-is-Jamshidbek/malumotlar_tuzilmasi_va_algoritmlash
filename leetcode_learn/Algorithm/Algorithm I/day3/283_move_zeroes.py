class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = 0
        while i<n:
            if nums[i]==0:
                nums.append(nums.pop(i))
                n-=1
            else:i+=1

nums = [0,1,0,3,12]
a = Solution()
a.moveZeroes(nums=nums)
print(nums)