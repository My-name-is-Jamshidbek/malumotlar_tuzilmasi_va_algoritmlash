# Number of Distinct Averages

class Solution:
    def distinctAverages(self, nums: list[int]) -> int:
        nums.sort()
        n, u = len(nums), set()

        for i in range(0, n // 2):
            u.add((nums[i] + nums[n - i - 1]) / 2)

        return len(u)
a = Solution()
print(a.distinctAverages([9,5,7,8,7,9,8,2,0,7]))
