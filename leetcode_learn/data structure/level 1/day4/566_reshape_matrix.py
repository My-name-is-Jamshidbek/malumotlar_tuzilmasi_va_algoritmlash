class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        try:
            lm = len(mat)
            ln = len(mat[0])
            j = lm * ln
            if lm == r and ln * lm == c:
                return mat
            else:
                l1 = []
                for i in mat: l1 += i
                l2 = []
                b = 0
                o = c
                for i in range(r):
                    l2.append(l1[b:o])
                    b = o
                    o += c
            lm = len(l2)
            ln = len(l2[-1])
            j1 = lm * ln
            if j1 != j: return mat
            return l2
        except:
            return mat
