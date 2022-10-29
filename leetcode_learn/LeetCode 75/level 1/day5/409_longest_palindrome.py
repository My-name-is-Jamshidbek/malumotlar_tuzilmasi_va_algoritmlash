class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = {}
        for i in s:
            if i in l:l[i]+=1
            else:l[i]=1
        n = 0
        t = True
        for i in l:
            if l[i]%2 != 0 and t:
                n += l[i]
                t = False
            else:n += int(l[i]//2)*2
        return n
a = Solution()
print(a.longestPalindrome( "aa"))