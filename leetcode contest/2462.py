class Solution:
    def totalCost(self, costs: list[int], k: int, candidates: int) -> int:
        l = len(costs)
        x = 0
        while (candidates>0):
            if l<=k*2:
                costs.sort()
                x+=sum(costs[:candidates])
                candidates=0
            else:
                pass
        return x
a = Solution()
print(a.totalCost(costs = [1,2,4,1], k = 3, candidates = 3))