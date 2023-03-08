"""
947. Most Stones Removed with Same Row or Column
Medium

3253

542

Add to List

Share
On a 2D plane, we place n stones at some integer coordinate points. Each coordinate point may have at most one stone.

A stone can be removed if it shares either the same row or the same column as another stone that has not been removed.

Given an array stones of length n where stones[i] = [xi, yi] represents the location of the ith stone, return the largest possible number of stones that can be removed.
"""


class Solution:
    def removeStones(self, stones: list[list[int]]) -> int:
        stones = [stones[:,0].argsort()]
        ls = len(stones)-1
        ou = 0
        i = -1
        while i<ls:
            i+=1
            i1 = i
            t = True
            while i1<ls and t:
                i1+=1
                if stones[i][0] == stones[i1][0] or stones[i][1] == stones[i1][1]:
                    ou+=1
                    # t = False
        return ou
a = Solution()
print(a.removeStones([[0,0]]))