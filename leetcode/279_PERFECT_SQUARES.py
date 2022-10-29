from math import inf


class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0,1,2,3,1]
        if n<5:return dp[n]
        else:
            for i in range(5,n+1):
                _min = i-int(i**0.5)**2
                for i in range(int(i**0.5)):
                    pass
                dp.append(1+dp[m])
        return dp[-1]

a = Solution()
print(a.numSquares(13))











# class Solution:
#     def numSquares(self, n: int) -> int:
#         m = 0
#         s = n % 2
#         if n==2 or n==10:return 2
#         for i in range(n):
#             if (n**0.5)%1==0 and n%2==s:
#                 if m:
#                     print(n)
#                     return 1+self.numSquares(n=m)
#                 else:return 1
#             else:n,m=n-1,m+1
# a = Solution()
# print(a.numSquares(10))