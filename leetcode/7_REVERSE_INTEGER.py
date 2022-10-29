class Solution:
    def reverse(self, x: int) -> int:
        if -4294967296>x>4294967296:return 0
        if len(str(x))==1:return x
        manfiy = False
        if x<0:x,manfiy=(x*(-1)),True
        x = int(str(x)[::-1])
        if manfiy:x*=-1
        return x
