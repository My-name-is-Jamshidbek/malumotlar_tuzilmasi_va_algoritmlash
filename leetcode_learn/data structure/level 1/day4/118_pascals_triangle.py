class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        rm = [[1],[1,1]]
        if numRows==1:return [[1]]
        for i in range(1,numRows-1):
            r = []
            r.append(1)
            for i1 in range(i):
                r.append(rm[i][i1]+rm[i][i1+1])
            r.append(1)
            rm.append(r)
        return rm

a = Solution()
print(a.generate(1))