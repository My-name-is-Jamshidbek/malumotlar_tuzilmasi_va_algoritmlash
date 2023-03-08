class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:return 0
        a, b, c = 0, 1, 1
        for i in range(n-2):
            a, b, c = b, c, (a + b + c)
        return c

# a = Solution()
# for i in range(100):
#     print(a.tribonacci(i))
