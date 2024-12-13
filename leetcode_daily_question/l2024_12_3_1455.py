from typing import List


class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        j = 0
        for i in sentence.split(" "):
            j+=1
            if i.startswith(searchWord):
                return j
        return -1
solution = Solution()
print(solution.isPrefixOfWord("this problem is an easy problem", "pro"))
