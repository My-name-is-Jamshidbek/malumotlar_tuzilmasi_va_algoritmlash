class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        len1 = len(s)
        maximum = ''
        lm = 0
        for len2 in range(len1):
            text = ''
            rtext = ''
            lt = 0
            for len3 in range(len2,len1):
                lt += 1
                text+=s[len3]
                rtext=s[len3]+rtext
                lt+=1
                if (text == rtext) and (lm < lt):
                    maximum=text
                    lm = lt
        return maximum


s = Solution()
a = s.lengthOfLongestSubstring("cbbd")
print(a)