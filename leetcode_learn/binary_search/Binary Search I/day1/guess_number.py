# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
def guess(num):pass

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        low = 0
        high = n
        while low <= high:
            mid = (high + low) // 2
            j = guess(mid)
            if j==1:
                low = mid + 1
            elif j==-1:
                high = mid - 1
            else:
                return mid
        return -1