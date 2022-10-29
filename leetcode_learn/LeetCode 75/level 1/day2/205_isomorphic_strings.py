class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):return False
        str1,str2=[],[]
        for i,j in zip(s,t):
            if i in str1:
                i1 = str1.index(i)
                if str2[i1] != j:return False
            else:
                if j in str2:return False
            str1.append(i)
            str2.append(j)
        return True

a = Solution()
print(a.isIsomorphic(s = "egg", t = "add"))