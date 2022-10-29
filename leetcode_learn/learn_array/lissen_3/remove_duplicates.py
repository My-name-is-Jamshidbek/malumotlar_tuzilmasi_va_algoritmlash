class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        ind = 0
        while ind<l-1:
            if nums[ind] == nums[ind+1]:
                nums.pop(ind)
                l -= 1
            else:ind+=1