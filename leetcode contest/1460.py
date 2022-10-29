class Solution:
    def applyOperations(self, nums: list[int]) -> list[int]:
        l,i,n = len(nums),1,0
        while (i<l)and(n<l):
            n+=1
            if nums[i-1]==0:
                nums.pop(i-1)
                nums.append(0)
                i-=1
            elif nums[i-1]==nums[i]:
                nums[i-1]=nums[i-1]+nums[i]
                nums.pop(i)
                nums.append(0)
            i+=1
        return nums


a = Solution()
print(a.applyOperations(nums = [847,847,0,0,0,399,416,416,879,879,206,206,206,272]))