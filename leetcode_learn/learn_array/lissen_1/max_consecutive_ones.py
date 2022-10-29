class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        m = 0
        n = 0
        for i in nums:
            if i==1:n+=1
            else:
                if n>m:m=n
                n=0
        if n > m: m = n
        return m