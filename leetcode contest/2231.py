class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        l = []
        for i in range(len(str(number))):
            if number[i] == digit:
                l.append(int(number[:i]+number[i+1:]))
        return max(l)


a = Solution()
print(a.removeDigit(number = "551", digit = "5"))