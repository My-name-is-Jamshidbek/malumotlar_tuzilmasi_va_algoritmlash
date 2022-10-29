class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        p = {}
        for i in range(len(nums)):
            c = target - nums[i]
            if c in p:
                return [i, p[c]]
            p[nums[i]] = i