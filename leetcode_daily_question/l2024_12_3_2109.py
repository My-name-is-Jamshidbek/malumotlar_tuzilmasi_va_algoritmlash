from typing import List


class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        return ''.join(s[start:end] + ' ' for start, end in zip([0] + spaces, spaces + [len(s)]))[:-1]

solution = Solution()
print(solution.addSpaces("LeetcodeHelpsMeLearn",[8,13,15]))
