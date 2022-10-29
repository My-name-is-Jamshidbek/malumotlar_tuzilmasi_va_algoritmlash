class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.split()
        s1 = ''
        for i in s:s1+=i[::-1]
        return s1[:-1]