class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        nm = []
        n = 0
        for i in nums:
            n+=i
            nm.append(n)
        return nm