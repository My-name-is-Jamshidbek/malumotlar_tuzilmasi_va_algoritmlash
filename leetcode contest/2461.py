class Solution:
    def maximumSubarraySum(self, nums: list[int], k: int) -> int:
        i,l,m = 0,len(nums)-k+1,0
        while(i<l):
            if sum(nums[i:i+k])>m and len(nums[i:i+k])==len(set(nums[i:i+k])):m=sum(nums[i:i+k])
            i+=1
        return m
