class Solution:
    def isValid(self, s: str) -> bool:
        for i in range(1,len(s),2):
            if (s[i] == '}') and (s[i] != '{'):return False
            elif (s[i] == ')') and (s[i] != '('):return False
            elif (s[i] == ']') and (s[i] != '['):return False
        return True
a = Solution()
print(a.isValid("(]"))