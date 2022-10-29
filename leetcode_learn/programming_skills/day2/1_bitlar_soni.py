class Solution:
    def hammingWeight(self, n: int) -> int:
        m = bin(n)[2:]
        b=0
        for i in str(m):
            if i=='1':b+=1
        return b

a = Solution()
print(a.hammingWeight(11))
