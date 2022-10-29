# class Solution:
#     def minCostClimbingStairs(self, cost: list[int]) -> int:
#         def f(narxlar, xarajat=0, ind=0, m_index=0):
#             if ind + 2 > m_index: return [xarajat]
#             n1 = f(narxlar=narxlar, xarajat=xarajat + narxlar[ind], m_index=m_index, ind=ind + 1)
#             n2 = f(narxlar=narxlar, xarajat=xarajat + narxlar[ind + 1], m_index=m_index, ind=ind + 2)
#             return min(n1, n2)
#         m = f(narxlar=cost,m_index=len(cost))
#         return m[0]
# a = Solution()
# print(a.minCostClimbingStairs(cost = [1,100,1,1,1,100,1,1,100,1]))
# # def f(narxlar,xarajat=0,ind=0,m_index=0):
# #     if ind+2>m_index:return [xarajat]
# #     n1 = f(narxlar=narxlar,xarajat=xarajat+narxlar[ind],m_index=m_index,ind=ind+1)
# #     n2 = f(narxlar=narxlar,xarajat=xarajat+narxlar[ind+1],m_index=m_index,ind=ind+2)
# #     return min(n1,n2)
# # print(f(narxlar=[1,100,1,1,1,100,1,1,100,1],m_index=10))

class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        jx = {-1:0} #jami xarajatlar
        ind = -1 #biz turgan joy
        l = len(cost)-1
        sakrashlar = 0
        while ind+2<l:
            if cost[ind+1]<cost[ind+2]:
                jx[sakrashlar] =  jx[sakrashlar-1]+cost[ind+1]
                sakrashlar+=1
                ind+=1
            else:
                jx[sakrashlar] = jx[sakrashlar - 1] + cost[ind + 2]
                sakrashlar += 1
                ind+=2
        print(jx)
        print(jx[sakrashlar-1])
a = Solution()
print(a.minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))



# class Solution:
#     def minCostClimbingStairs(self, cost: list[int]) -> int:
#         a=b=0
#         for c in cost:
#             print(c)
#             print(a,b)
#             a,b=b,min(a,b)+c
#             print(a,b)
#         return min(a,b)
