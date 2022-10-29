# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        low = 0
        high = n
        while low <= high:
            mid = (high + low) // 2
            b = isBadVersion(mid)
            b1 = isBadVersion(mid-1)
            if b and (b1==False):return mid
            elif b:
                high = mid - 1
            else:
                low = mid + 1
        return -1
