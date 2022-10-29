class Solution:
    def maxArea(self, height: list[int]) -> int:
        max_h = 0
        l = len(height)
        for i in range(l):
            for i1 in range(i+1,l):
                n = min(height[i],height[i1])*(i1-i)
                if n>max_h:
                    max_h=n
        return max_h
a = Solution()
print(a.maxArea([1,1]))