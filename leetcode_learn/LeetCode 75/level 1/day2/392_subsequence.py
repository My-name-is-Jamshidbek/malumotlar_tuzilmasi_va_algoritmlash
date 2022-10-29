class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ind1 = 0
        l = len(s)
        if l == 0:return True
        for i in t:
            if i == s[ind1]:
                ind1+=1
                if l == ind1:return True
        return False
a = Solution()
print(a.isSubsequence(s = "b", t = "abc"))