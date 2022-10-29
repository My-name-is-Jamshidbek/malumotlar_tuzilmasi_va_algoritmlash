class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows<2:return s
        l,i1,n3,n,n1 = [],True,0,numRows,len(s)
        while n3<=n1:
            if i1:
                l.append(list(s[n3:n]))
                n3=n
                n+=numRows-2
                i1 = False
            else:
                li = ['']
                li += s[n3:n]
                li.append('')
                while len(li)!=numRows:                li.append('')
                l.append(li[::-1])
                n3 = n
                n += numRows
                i1 = True

        del n, n3, i1
        s = ''
        for i in range(numRows):
            for i1 in l:
                try:s += i1[i]
                except:pass
        return s

a = Solution()
print(a.convert(s = "ABCDE", numRows = 4))
