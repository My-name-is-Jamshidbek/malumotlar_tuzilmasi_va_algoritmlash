class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        n = 0
        for i in nums:
            if len(str(i))%2==0:n+=1
        return n